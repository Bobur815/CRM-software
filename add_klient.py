from moduls import *

class AddKlient(QDialog):
    def __init__(self,mainWindow):
        super().__init__()

        self.setWindowTitle("Klient qo'shish")
        self.setWindowIcon(QIcon("rasmlar/add_klient.webp"))
        self.setFixedSize(600,250)
        self.setModal(True) 
        
        main_layout = QFormLayout(self)
        self.mainWindow = mainWindow

        klient = QLabel("Klientni nomi:",self)
        self.klient_edit = QLineEdit(self)

        qarz = QLabel("Qarzdorlik:    ",self)
        self.qarz_edit = QLineEdit(self)

        button_layout = QHBoxLayout()
        ok_button = QPushButton("OK", self)
        cancel_button = QPushButton("Cancel", self)

        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        button_layout.setSpacing(20)

        main_layout.addRow(klient,self.klient_edit)
        main_layout.addRow(qarz,self.qarz_edit)
        main_layout.addRow(button_layout)
        main_layout.setSpacing(25)

        self.greenBorder = "2px solid #28a745"

        self.set_style(klient)
        self.set_style(qarz)
        self.set_style_edit(self.klient_edit,self.greenBorder)
        self.set_style_edit(self.qarz_edit,self.greenBorder)
        self.set_button_style(ok_button)
        self.set_button_style(cancel_button)

        ok_button.clicked.connect(self.on_ok)
        cancel_button.clicked.connect(self.close)

        self.setLayout(main_layout)

    def on_ok(self):
        
        msg = QMessageBox(self)
        nomi = self.klient_edit.text()
        qarz = self.qarz_edit.text()

        if not nomi:
            msg.warning(self,"Error","Klient nomi bo'sh")
            self.set_style_edit(self.klient_edit,"2px solid red")
            return
        else: self.set_style_edit(self.klient_edit,self.greenBorder)

        if not qarz:
            msg.warning(self,"Error","Qarzdorlikni kiriting")
            self.set_style_edit(self.qarz_edit,"2px solid red")
            return
        
        
        self.set_style_edit(self.qarz_edit,self.greenBorder)
        conn = get_cursor()
        conn.autocommit = True

        with conn.cursor() as cursor:
           cursor.execute("INSERT INTO klientlar (nomi,qarzdorlik) VALUES (%s,%s)",(nomi,qarz)) 
           conn.commit()
        msg.information(self,"Muvaffaqiyatli","Klient muvaffaqiyatli qo'shildi")
        self.mainWindow.load_data()
        self.close()

    def set_button_style(self, button):
        button.setStyleSheet("""
        QPushButton {
            color: white; /* White text */
            background-color: #28a745; /* Green background */
            border: none;
            border-radius: 10px;
            font-size: 18px;
            padding: 10px 20px;
        }
        QPushButton:hover {
            background-color: #45d38a; /* Lighter green hover */
        }
        QPushButton:pressed {
            background-color: #1e7e34; /* Darker green on press */
        }
        """)


    def set_style(self, label):
        label.setStyleSheet("""
        QLabel {
            color: #28a745; /* Green text color for contrast */
            background-color: white;
            border: 2px solid #28a745;
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
                outline: none; /* Remove default outline */
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