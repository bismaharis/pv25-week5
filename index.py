import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence
from F1D022055_ui import Ui_Form  # Your generated UI file from .ui

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.pushButton_save.clicked.connect(self.save_data)
        self.ui.pushButton_clear.clicked.connect(self.clear_form)

        # Shortcut to close app with 'Q'
        shortcut_quit = QShortcut(QKeySequence('Q'), self)
        shortcut_quit.activated.connect(self.close)

    def save_data(self):
        name = self.ui.lineEdit_name.text()
        email = self.ui.lineEdit_email.text()
        age = self.ui.lineEdit_age.text()
        phone = self.ui.lineEdit_phone.text()
        address = self.ui.textEdit_address.toPlainText()
        gender = self.ui.comboBox_gender.currentText()
        education = self.ui.comboBox_education.currentText()

        # Validations
        if not name:
            self.show_message("Name is required.")
            return
        if not email or "@" not in email:
            self.show_message("Please enter a valid email.")
            return
        if not age.isdigit() or int(age) < 0:
            self.show_message("Age must be a positive number.")
            return
        if not phone or len(phone.strip()) < 15:
            self.show_message("Please enter a valid phone number.")
            return
        if not address.strip():
            self.show_message("Address is required.")
            return
        if gender == "Select":
            self.show_message("Please select a gender.")
            return
        if education == "Select":
            self.show_message("Please select your education.")
            return

        # If all valid
        self.show_message("Data saved successfully!", QMessageBox.Information)

        # Clear fields after successful submission
        self.clear_form()

    def clear_form(self):
        self.ui.lineEdit_name.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_age.clear()
        self.ui.lineEdit_phone.clear()
        self.ui.textEdit_address.clear()
        self.ui.comboBox_gender.setCurrentIndex(0)
        self.ui.comboBox_education.setCurrentIndex(0)

    def show_message(self, message, icon=QMessageBox.Warning):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(message)
        msg.setWindowTitle("Form Status")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
