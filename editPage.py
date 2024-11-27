from moduls import *

class EditWindow(QDialog):
    def __init__(self,mainWindow,old_texts):
        super().__init__()

        self.setWindowTitle("Mahsulotni o'zgartirish")
        self.setWindowIcon(QIcon("rasmlar/edit_icon.png"))
        self.setFixedSize(1000,800)
        self.setModal(True) 
        
        main_layout = QFormLayout()
        self.main_window = mainWindow
        self.old_texts = old_texts


        self.prevent_signal = False 

        # Labels set-up
        line = QLabel(self)
        line.setFixedSize(970,2)
        klient = QLabel("Klientni tanlang:",self)
        klient.setFixedHeight(50)
        self.mahsulot_nomi = QLabel("Mahsulot nomi:",self)
        self.mahsulot_nomi.setFixedSize(200,50)
        self.soni = QLabel("Soni:",self)
        self.soni.setFixedSize(200,50)
        self.tannarx = QLabel("Tannarxi:",self)
        self.tannarx.setFixedSize(200,50)
        self.tannarx_jami = QLabel("Tannarx jami:",self)
        self.tannarx_jami.setFixedSize(200,50)
        self.sotilish_narx = QLabel("Sotilish narxi:",self)
        self.sotilish_narx.setFixedSize(200,50)
        self.foiz = QLabel("Foyda %:",self)
        self.foiz.setFixedSize(200,50)
        self.sotilish_jami = QLabel("Jami:",self)
        self.sotilish_jami.setFixedSize(200,50)
        self.vaqt_label = QLabel("Sanani tanlang:",self)
        self.vaqt_label.setFixedSize(200,50)


        # Line edits set-up
        self.mahsulot_nomi_edit = QLineEdit(self)
        self.soni_edit = QLineEdit(self)
        self.tannarx_edit = QLineEdit(self)
        self.tannarx_jami_edit = QLineEdit(self)
        self.sotilish_narx_edit = QLineEdit(self)
        self.foiz_edit = QLineEdit(self)
        self.sotilish_jami_edit = QLineEdit(self)

        self.mahsulot_nomi_edit.setFixedHeight(50)
        self.soni_edit.setFixedHeight(50)
        self.tannarx_edit.setFixedHeight(50)
        self.tannarx_jami_edit.setFixedHeight(50)
        self.sotilish_narx_edit.setFixedHeight(50)
        self.foiz_edit.setFixedHeight(50)
        self.sotilish_jami_edit.setFixedHeight(50)

        self.date = QDateEdit(self)
        self.date.setCalendarPopup(True) 
        self.date.setDate(QDate.currentDate())
        self.date.lineEdit().setReadOnly(True)
        self.date.setFixedHeight(50)

        self.tannarx_jami_edit.setDisabled(True)
        self.sotilish_jami_edit.setDisabled(True)
        self.foiz_edit.setDisabled(True)


        self.klient_box = QComboBox(self)
        self.klient_box.setFixedHeight(50)
        self.checkbox_foiz = QCheckBox("Foizda hisoblash",self)
        self.set_style_checkbox(self.checkbox_foiz)

        self.load_data()

        klient_add = QPushButton("Qo'shish",self)
        icon = QIcon("rasmlar/add_klient.webp")
        klient_add.setIcon(QIcon(icon))
        klient_add.setIconSize(QSize(30,30))
        klient_add.setFixedSize(200,50)

        self.saqlash_btn = QPushButton(QIcon("rasmlar/saqlash.png")," Saqlash",self)
        self.saqlash_btn.setIconSize(QSize(30,30))
        tozalash = QPushButton(QIcon("rasmlar/Refresh_icon.svg.png")," Tozalash",self)
        tozalash.setIconSize(QSize(30,30))
        chiqish = QPushButton(QIcon("rasmlar/10910382.png")," Chiqish",self)
        chiqish.setIconSize(QSize(30,30))

        layout = QHBoxLayout()
        layout.addWidget(self.saqlash_btn)
        layout.addWidget(tozalash)
        layout.addWidget(chiqish)

        vert_layout = QVBoxLayout(self)

        main_layout.addRow(klient, self.klient_box)
        main_layout.addRow(klient_add)
        main_layout.addRow(line)
        main_layout.addRow(self.mahsulot_nomi,self.mahsulot_nomi_edit)
        main_layout.addRow(self.soni,self.soni_edit)
        main_layout.addRow(self.tannarx,self.tannarx_edit)
        main_layout.addRow(self.tannarx_jami,self.tannarx_jami_edit)
        main_layout.addRow(self.vaqt_label,self.date)
        main_layout.addRow(self.checkbox_foiz)
        main_layout.addRow(self.foiz,self.foiz_edit)
        main_layout.addRow(self.sotilish_narx,self.sotilish_narx_edit)
        main_layout.addRow(self.sotilish_jami,self.sotilish_jami_edit)

        vert_layout.addLayout(main_layout)
        vert_layout.addLayout(layout)
        vert_layout.setSpacing(15)

        # Label set style
        self.set_style_label(klient)
        self.set_style_label(line)
        self.set_style_label(self.mahsulot_nomi)
        self.set_style_label(self.soni)
        self.set_style_label(self.tannarx)
        self.set_style_label(self.tannarx_jami)
        self.set_style_label(self.sotilish_narx)
        self.set_style_label(self.foiz)
        self.set_style_label(self.sotilish_jami)
        self.set_style_label(self.vaqt_label)


        # Edit set style
        self.greenBorder = "2px solid #28a745"
        self.set_style_edit(self.mahsulot_nomi_edit,self.greenBorder)
        self.set_style_edit(self.soni_edit,self.greenBorder)
        self.set_style_edit(self.tannarx_edit,self.greenBorder)
        self.set_style_edit(self.tannarx_jami_edit,self.greenBorder)
        self.set_style_edit(self.sotilish_narx_edit,self.greenBorder)
        self.set_style_edit(self.foiz_edit,self.greenBorder)
        self.set_style_edit(self.sotilish_jami_edit,self.greenBorder)
        self.set_style_date(self.date)

        self.set_style_combo(self.klient_box)

        # Buttons set style
        self.set_style_button(klient_add)
        self.set_style_button(self.saqlash_btn)
        self.set_style_button(tozalash)
        self.set_style_button(chiqish)
        

        klient_add.clicked.connect(self.add_klient)
        tozalash.clicked.connect(self.tozalash)
        chiqish.clicked.connect(self.chiqish)
        self.saqlash_btn.clicked.connect(self.check)


        self.tannarx_edit.textChanged.connect(self.check_tannarx)
        self.soni_edit.textChanged.connect(self.check_soni)
        self.checkbox_foiz.stateChanged.connect(self.handle_checkbox_change)
        self.sotilish_narx_edit.textChanged.connect(self.foiz_jami_hisobla)
        self.foiz_edit.textChanged.connect(self.sotilish_jami_hisobla)

        self.setLayout(vert_layout)

    def set_style_date(self, date_edit):

        date_edit.setStyleSheet("""
        QDateEdit {
            color: #28a745; /* Green text for input */
            background-color: white; /* White background */
            border: 2px solid #28a745; /* Green border */
            border-radius: 10px; /* Rounded corners */
            font-size: 20px; /* Adjust font size */
            padding: 5px 15px; /* Padding for better appearance */
        }
        QDateEdit:hover {
            background-color: #f0f0f0; /* Light gray hover effect */
        }
        QDateEdit:focus {
            border: 2px solid #45d38a; /* Highlight border when focused */
            outline: none; /* Remove default outline */
        }
        QDateEdit::drop-down {
            border: none; /* Remove default border for drop-down button */
            background: transparent;
            subcontrol-position: right center; /* Move drop-down button to the left */
            width: 35px; /* Width for the drop-down area */
            padding-left: 5px;
        }
        QDateEdit::down-arrow {
            image: url(rasmlar/46-512.webp); /* Custom arrow image */
            width: 30px;
            height: 30px;
        }
        QDateEdit::up-button, QDateEdit::down-button {
            subcontrol-origin: padding;
            subcontrol-position: right; /* Place drop-down arrow to the right */
        }
        """)
        
        # Apply a drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.gray)  # Softer shadow for light background
        date_edit.setGraphicsEffect(shadow)

    def sotilish_jami_hisobla(self):
        if self.prevent_signal:  # Exit if signals are disabled
            return

        if not self.foiz_edit.text():
            self.sotilish_narx_edit.clear()
            self.sotilish_jami_edit.clear()
            return

        value = self.foiz_edit.text()

        if not value.replace('.', '', 1).isdigit() or value.count('.') > 1:
            self.set_style_edit(self.foiz_edit, "2px solid red")
            return

        self.set_style_edit(self.foiz_edit, self.greenBorder)
        self.set_style_edit(self.sotilish_narx_edit, self.greenBorder)

        foiz = float(self.foiz_edit.text())
        tannarx = int(self.tannarx_edit.text())
        if foiz != 0:
            result = tannarx + (tannarx / (100 / foiz))
        soni = int(self.soni_edit.text())

        self.prevent_signal = True  # Prevent signal triggering
        self.sotilish_narx_edit.setText(str(int(result)))
        self.sotilish_jami_edit.setText(str(int(soni * result)))
        self.prevent_signal = False  # Re-enable signal triggering

    def foiz_jami_hisobla(self):
        if self.prevent_signal:  # Exit if signals are disabled
            return

        if not self.sotilish_narx_edit.text():
            self.foiz_edit.clear()
            self.sotilish_jami_edit.clear()
            return

        value = self.sotilish_narx_edit.text()

        if not value.replace('.', '', 1).isdigit() or value.count('.') > 1:
            self.set_style_edit(self.sotilish_narx_edit, "2px solid red")
            return

        self.set_style_edit(self.sotilish_narx_edit, self.greenBorder)
        self.set_style_edit(self.foiz_edit, self.greenBorder)

        sot_narx = int(self.sotilish_narx_edit.text())
        tannarx = int(self.tannarx_edit.text())
        result = ((sot_narx - tannarx) / tannarx) * 100
        soni = int(self.soni_edit.text())

        self.prevent_signal = True  # Prevent signal triggering
        self.sotilish_jami_edit.setText(str(int(soni * sot_narx)))
        self.foiz_edit.setText(str(int(result)))
        self.prevent_signal = False  # Re-enable signal triggering

    def handle_checkbox_change(self, state):
        self.foiz_edit.clear()
        self.sotilish_narx_edit.clear()

        if state == Qt.Checked:
            self.prevent_signal = True  # Prevent signal handling during changes
            self.sotilish_narx_edit.setDisabled(True)
            self.foiz_edit.setDisabled(False)
            self.prevent_signal = False
        else:
            self.prevent_signal = True  # Prevent signal handling during changes
            self.sotilish_narx_edit.setDisabled(False)
            self.foiz_edit.setDisabled(True)
            self.prevent_signal = False
    
    def check_soni(self):
        if not self.soni_edit.text():
            self.set_style_edit(self.soni_edit,"2px solid red")
            self.soni_edit.setFocus()
            return
        
        if  not self.soni_edit.text().isdigit():
            self.set_style_edit(self.soni_edit,"2px solid red")
            self.soni_edit.setFocus()
            return
        self.set_style_edit(self.soni_edit,self.greenBorder)

        if self.soni_edit.text():
            self.tannarx_edit.setDisabled(False)
        else:
            self.tannarx_edit.setDisabled(True) 
        if self.tannarx_edit.text():
            self.tannarx_jami_edit.setText(str(int(self.soni_edit.text())*int(self.tannarx_edit.text())))

    def check_tannarx(self):

        if not self.tannarx_edit.text():
            self.set_style_edit(self.tannarx_edit,"2px solid red")
            self.tannarx_edit.setFocus()
            return
        
        if  not self.tannarx_edit.text().isdigit():
            self.set_style_edit(self.tannarx_edit,"2px solid red")
            self.tannarx_edit.setFocus()
            return
        self.set_style_edit(self.tannarx_edit,self.greenBorder)

        
        soni = int(self.soni_edit.text())
        tannarx = int(self.tannarx_edit.text())
        self.tannarx_jami_hisobla(soni,tannarx)

    def check(self):

        msg = QMessageBox(self)
        if not self.mahsulot_nomi_edit.text():
            self.set_style_edit(self.mahsulot_nomi_edit,"2px solid red")
            msg.warning(self,"Error","Mahsulot nomi bo'sh")
            self.mahsulot_nomi_edit.setFocus()
            return
        self.set_style_edit(self.mahsulot_nomi_edit,self.greenBorder)

        if not self.soni_edit.text():
            self.set_style_edit(self.soni_edit,"2px solid red")
            msg.warning(self,"Error","Mahsulot sonini kiriting")
            self.soni_edit.setFocus()
            return
        
        if  not self.soni_edit.text().isdigit():
            self.set_style_edit(self.soni_edit,"2px solid red")
            msg.warning(self,"Error","Mahsulot soniga raqam kiriting")
            self.soni_edit.setFocus()
            return
        self.set_style_edit(self.soni_edit,self.greenBorder)

        if not self.tannarx_edit.text():
            self.set_style_edit(self.tannarx_edit,"2px solid red")
            msg.warning(self,"Error","Mahsulot tannarxini kiriting")
            self.tannarx_edit.setFocus()
            return
        
        if  not self.tannarx_edit.text().isdigit():
            self.set_style_edit(self.tannarx_edit,"2px solid red")
            msg.warning(self,"Error","Mahsulot tannarxiga raqam kiriting")
            self.tannarx_edit.setFocus()
            return
        self.set_style_edit(self.tannarx_edit,self.greenBorder)
        
        if not self.foiz_edit.text():
            self.set_style_edit(self.foiz_edit,"2px solid red")
            msg.warning(self,"Error","Foyda foizini kiriting")
            self.foiz_edit.setFocus()
            return
        
        if  not self.foiz_edit.text().isdigit():
            self.set_style_edit(self.foiz_edit,"2px solid red")
            msg.warning(self,"Error","Foiz uchun raqam kiriting")
            self.foiz_edit.setFocus()
            return
        self.set_style_edit(self.foiz_edit,self.greenBorder)
        
        if not self.sotilish_narx_edit.text():
            self.set_style_edit(self.sotilish_narx_edit,"2px solid red")
            msg.warning(self,"Error","Sotilish narxini kiriting")
            self.sotilish_narx_edit.setFocus()
            return
        
        if  not self.sotilish_narx_edit.text().isdigit():
            self.set_style_edit(self.sotilish_narx_edit,"2px solid red")
            msg.warning(self,"Error","Sotilish narx uchun raqam kiriting")
            self.sotilish_narx_edit.setFocus()
            return
        self.set_style_edit(self.sotilish_narx_edit,self.greenBorder)

        self.save_data()

    def save_data(self):
        conn = get_cursor()
        conn.autocommit =True
        nomi = self.mahsulot_nomi_edit.text()
        klient = self.klient_box.currentText()
        mahsulot_id = self.old_texts[0]

        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM klientlar WHERE nomi=%s;",(klient,))
            klient_id = cursor.fetchone()
            conn.commit()

        soni = int(self.soni_edit.text())
        tannarx = int(self.tannarx_edit.text())
        tan_jami = self.tannarx_jami_edit.text()
        sot_narx = int(self.sotilish_narx_edit.text())
        foiz = float(self.foiz_edit.text())
        sot_jami = int(self.sotilish_jami_edit.text())
        date = self.date.date().toString("yyyy-MM-dd")

        with conn.cursor() as cursor:
            cursor.execute("""
                    UPDATE mahsulotlar 
                    SET nomi = %s, klient_nomi = %s, soni = %s, tan_narxi = %s, 
                        tan_jami = %s, sotilish_narxi = %s, foiz = %s, sotilish_jami = %s, kelgan_vaqti = %s
                    WHERE id = %s
                """, (nomi, klient_id, soni, tannarx, tan_jami, sot_narx, foiz, sot_jami, date, mahsulot_id))

            conn.commit()
        
        msg = QMessageBox(self)
        msg.information(self,"Muvaffaqiyat","Mahsulot muvaffaqiyatli o'zgartirildi!")
        self.main_window.load_data()
        self.close()
        
    def tannarx_jami_hisobla(self,soni,tannarx):
        self.tannarx_jami_edit.setText(str(soni * tannarx))

    def chiqish (self):
        self.close()

    def tozalash(self):
        self.mahsulot_nomi_edit.clear()
        self.soni_edit.clear()
        self.tannarx_edit.clear()
        self.foiz_edit.clear()
        self.sotilish_narx_edit.clear()

    def load_data(self):
        self.klient_box.clear()
        conn = get_cursor()
        conn.autocommit = True
        self.klientlar_ls = []

        with conn.cursor() as cursor:
           cursor.execute("SELECT * FROM klientlar") 
           temp = cursor.fetchall()
           conn.commit()

        for i in temp:
            self.klientlar_ls.append(i[1])
        
        self.klient_box.addItems(self.klientlar_ls)

        self.klient_box.setCurrentText(self.old_texts[2])
        self.mahsulot_nomi_edit.setText(self.old_texts[1])
        self.soni_edit.setText(self.old_texts[3])
        self.tannarx_edit.setText(self.old_texts[4])
        self.tannarx_jami_edit.setText(self.old_texts[5])
        self.foiz_edit.setText(self.old_texts[7])
        self.sotilish_narx_edit.setText(self.old_texts[6])
        self.sotilish_jami_edit.setText(self.old_texts[8])
        

    def add_klient(self):
        from add_klient import AddKlient
        self.add = AddKlient(self)
        self.add.show()

    def set_style_edit(self, line_edit, borderColor):

        line_edit.setStyleSheet(f"""
            QLineEdit {{
                color: #28a745; /* Green text for input text */
                background-color: white; /* White background */
                border: {borderColor};
                border-radius: 10px; /* Rounded corners */
                font-size: 20px; /* Adjust font size */
                padding: 10px; /* Add padding for better appearance */
            }}
            QLineEdit:hover {{
                background-color: #f0f0f0; /* Light gray hover effect */
            }}
            QLineEdit:focus {{
                border: {borderColor}; 
                outline: none; 
            }}
            QLineEdit:disabled {{
                background-color: #e0e0e0; /* Gray background for disabled state */
                color: #a0a0a0; /* Gray text for disabled state */
            }}
        """)

        # Apply a drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.gray)  # Softer shadow for light background
        line_edit.setGraphicsEffect(shadow)
    
    def set_style_button(self, button):
        button.setStyleSheet("""
        QPushButton {
            color: white; /* White text for contrast */
            background-color: #28a745; /* Green background */
            border: 2px solid #28a745; /* Green border for consistency */
            border-radius: 10px;
            font-size: 22px;
            padding: 10px 20px;
        }
        QPushButton:hover {
            background-color: #218838; /* Slightly darker green on hover */
        }
        QPushButton:pressed {
            background-color: #1e7e34; /* Even darker green for pressed state */
        }
        
        """)

        # Apply a drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.gray)  # Softer shadow for light background
        button.setGraphicsEffect(shadow)
    
    def set_style_checkbox(self, checkbox):
        checkbox.setStyleSheet("""
        QCheckBox {
            color: #28a745; /* Green text color */
            font-size: 20px; /* Font size for text */
            padding: 10px; /* Padding for better appearance */
        }
        
        """)

        # Apply a drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.gray)  # Softer shadow for light background
        checkbox.setGraphicsEffect(shadow)


    def set_style_label(self, label):
        label.setStyleSheet("""
        QLabel {
            color: #28a745; /* Green text color for contrast */
            background-color: white;
            border: 2px solid #28a745; /* Add a green border for definition */
            border-radius: 10px;
            font-size: 20px;
            padding: 10px 20px; /* Add padding for a button-like appearance */
            text-align: center; /* Ensure text is centered */
        }
        """)
        
        # Apply a drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.gray)  # Softer shadow for light background
        label.setGraphicsEffect(shadow)

    def set_style_combo(self, combobox):
        combobox.setStyleSheet("""
        QComboBox {
            color: #28a745; /* Green text for contrast */
            background-color: white;
            border: 2px solid #28a745; /* Add a green border for definition */
            border-radius: 10px;
            font-size: 22px;
            padding: 5px 15px;
        }
        QComboBox:hover {
            background-color: #f0f0f0; /* Light gray hover effect */
        }
        QComboBox:pressed, QComboBox:editable:hover {
            background-color: #dcdcdc; /* Darker gray for pressed state */
        }
        QComboBox:focus {
            outline: 2px solid #45d38a; /* Focus indicator */
        }
        QComboBox::drop-down {
            border: none; /* Remove default border for drop-down button */
            background: transparent;
            subcontrol-position: right center; /* Move drop-down button to the left */
            width: 35px; /* Width for the drop-down area */
            padding-left: 5px; /* Add space between the arrow and the border */
        }
        QComboBox::down-arrow {
            image: url(rasmlar/46-512.webp);
            width: 30px;
            height: 30px;
        }
        """)

        # Apply a drop shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.gray)  # Softer shadow for light background
        combobox.setGraphicsEffect(shadow)

