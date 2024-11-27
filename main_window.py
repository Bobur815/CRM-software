from moduls import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yangi Asr Market")
        self.setWindowIcon(QIcon("rasmlar/y.png"))
        self.showMaximized()

        main_layout = QVBoxLayout()

        # Add "Qo'shish" button
        qoshish_btn = QPushButton(" Mahsulot qo'shish", self)
        qoshish_btn.setIcon(QIcon("rasmlar/14025467.png"))
        self.set_style(qoshish_btn)

        self.main_table = QTableWidget(self)
        self.main_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.main_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.set_table_style(self.main_table)
        self.load_data()

        main_layout.addWidget(qoshish_btn)
        main_layout.addWidget(self.main_table)

        qoshish_btn.clicked.connect(self.add_page)

        self.setLayout(main_layout)

    def add_page(self):
        from addPage import AddWindow

        self.addOyna = AddWindow(self)
        self.addOyna.show()


    def load_data(self):
        self.main_table.clear()

        conn = get_cursor()

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    m.id,
                    m.nomi, 
                    k.nomi AS klient_nomi, 
                    m.soni, 
                    m.tan_narxi, 
                    m.tan_jami, 
                    m.sotilish_narxi, 
                    m.foiz, 
                    m.sotilish_jami 
                FROM mahsulotlar m
                LEFT JOIN klientlar k ON m.klient_nomi = k.id;
            """)
            products = cursor.fetchall()
            self.main_table.setRowCount(len(products))
            self.main_table.setColumnCount(11)
            self.main_table.setHorizontalHeaderLabels(["id","Mahsulot nomi","Klient","Soni","Tannarxi","Tannarx jami","Sotilish narxi","Foyda %","Sotilish Jami","Edit","Del"])

            self.main_table.hideColumn(0)
            self.main_table.setColumnWidth(1,420)
            self.main_table.setColumnWidth(2,420)
            self.main_table.setColumnWidth(3,100)
            self.main_table.setColumnWidth(4,170)
            self.main_table.setColumnWidth(5,170)
            self.main_table.setColumnWidth(6,170)
            self.main_table.setColumnWidth(7,100)
            self.main_table.setColumnWidth(8,170)
            self.main_table.setColumnWidth(9,65)
            self.main_table.setColumnWidth(10,50)
            self.main_table.horizontalHeader().setStretchLastSection(True)

            for row, data in enumerate(products):
                for column, item in enumerate(data):
                    self.main_table.setItem(row,column,QTableWidgetItem(str(item)))


                # Elementni tahrirlash uchun buttonlar
                edit_button = QPushButton(self)
                edit_button.setFixedSize(50,25)
                edit_button.setIcon(QIcon("rasmlar/edit_icon.png"))
                self.main_table.setCellWidget(row,9,edit_button)

                edit_button.clicked.connect(lambda _, i=row: self.edit_item(i))

                # Element o'chirish uchun buttonlar
                del_button = QPushButton()
                del_button.setFixedSize(50,25)
                del_button.setIcon(QIcon("rasmlar/delete.png"))
                self.main_table.setCellWidget(row, 10, del_button)
                

                del_button.clicked.connect(lambda _, id=row: self.del_button_click(id))

    def edit_item(self,row_id):
        len = self.main_table.columnCount()-2
        old_texts = []

        for n in range(len):
            old_texts.append(self.main_table.item(row_id,n).text())
        print(old_texts)
            
        from editPage import EditWindow

        self.oyna = EditWindow(self,old_texts)
        self.oyna.show()

    def del_button_click(self,row_id):
        mahsulot_id = self.main_table.item(row_id,0).text()

        reply = QMessageBox.question(
            self,
            "O'chirishni tasdiqlash",
            "Rostan o'chirib tashlamoqchimisiz?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            dbc = get_cursor()
            dbc.autocommit(True)
            db_cursor = dbc.cursor()
            try:
                db_cursor.execute("DELETE FROM mahsulotlar WHERE id = %s;", (mahsulot_id,))
            finally:
                db_cursor.close()
                dbc.close()
            self.load_data()
            QMessageBox.information(self,"O'chirildi","Ma'lumotlar o'chirildi") 
        


    def set_table_style(self, table):

        table.setStyleSheet("""
            QTableWidget {
                border: 2px solid #3E8E41; /* Slightly darker border for definition */
                background-color: #ffffff; /* Bright white background */
                gridline-color: #ddd; /* Soft gridlines */
                selection-background-color: #66BB6A; /* Vibrant green for selection */
                selection-color: #ffffff; /* White text for contrast on selection */
                font-size: 18px;
                font-family: Arial, sans-serif;
                color: #333; /* Dark gray text for readability */
                alternate-background-color: #F9FBE7; /* Soft pale yellow for alternate rows */
            }
            QTableWidget::item {
                padding: 10px;
                border: none; /* Remove borders for a clean look */
                border-radius: 5px;
                
            }
            QTableWidget::item:hover {
                background-color: #E8F5E9; /* Light green hover effect */
            }
            QHeaderView::section {
                background-color: #388E3C; /* Deep green for headers */
                color: #ffffff; /* White text */
                font-size: 18px; /* Larger text for headers */
                font-weight: bold;
                padding: 10px;
                border: none;
                text-align: center; /* Center-align header text */
            }
            QTableWidget::item:selected {
                background-color: #388E3C; /* Match header green for selection */
                color: white;
            }
            QTableCornerButton::section {
                background-color: #388E3C; /* Match header style for corner button */
            }
        """)

        # Enable alternating row colors
        table.setAlternatingRowColors(True)

        # Adjust horizontal and vertical header styles
        horizontal_header = table.horizontalHeader()
        vertical_header = table.verticalHeader()
        horizontal_header.setDefaultAlignment(Qt.AlignCenter)



    def set_style(self, button):

        button.setStyleSheet("""
        QPushButton {
            color: #28a745; /* Green text for contrast */
            background-color: white;
            border: 2px solid #28a745; /* Add a green border for definition */
            border-radius: 10px;
            font-size: 26px;
            padding: 10px 20px;
        }
        QPushButton:hover {
            background-color: #f0f0f0; /* Light gray hover effect */
        }
        QPushButton:pressed {
            background-color: #dcdcdc; /* Darker gray for pressed state */
        }
        """)

        # Apply a drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.gray)  # Softer shadow for light background
        button.setGraphicsEffect(shadow)


if __name__ == "__main__":
    app = QApplication([])

    oyna = MainWindow()
    oyna.show()

    sys.exit(app.exec_())
