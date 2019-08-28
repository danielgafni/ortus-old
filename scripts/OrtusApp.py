from PyQt5 import QtWidgets
from local import manage
from OrtusUi import Ui_Ortus
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.core = manage.Core()
        self.ui = Ui_Ortus()
        self.ui.setupUi(self)
        self.ui.button_login.clicked.connect(self.login)
        self.ui.button_generate_password.clicked.connect(self.generate_password)
        self.ui.button_register.clicked.connect(self.register)
        self.ui.actionExit.triggered.connect(sys.exit)

    def login(self):
        self.core.login(self.ui.line_username.text(),
                        self.ui.line_password.text())
        self.log()
        self.update_logged_state()

    def register(self):
        self.core.register_user_temporary(self.ui.line_username.text(),
                                          self.ui.line_password.text())
        self.log()
        self.update_logged_state()

    def remove_current_user(self):
        self.core.remove_current_user()
        self.log()
        self.update_logged_state()

    def generate_password(self):
        password = self.core.add_password(self.ui.line_keyword.text())
        self.ui.line_output_password.setText(password)
        if self.core.logged:
            self.core.save_passwords()
        self.log()

    def logout(self):
        self.core.logout()
        self.core.logged = False
        self.ui.text_passwords.setText('')
        self.ui.line_keyword.setText('')
        self.ui.line_output_password.setText('')
        self.log()
        self.update_logged_state()

    def log(self):
        if self.core.logged:
            passwords_message = ''
            for key in self.core.passwords.keys():
                passwords_message += f'Password for {key}:    {self.core.passwords[key]}\n'

        else:
            passwords_message = ''
        self.ui.text_passwords.setText(passwords_message)
        self.ui.text_log.setText(self.core.logmessage)

    def update_logged_state(self):
        if self.core.logged:
            self.ui.button_login.clicked.disconnect()
            self.ui.button_register.clicked.disconnect()
            self.ui.label_log.setText(f'User: {self.core.user.username}\nOutput log')
            self.ui.button_login.setText('Log Out')
            self.ui.button_register.setText('Delete user')
            self.ui.button_login.clicked.connect(self.logout)
            self.ui.button_register.clicked.connect(self.remove_current_user)
        else:
            self.ui.button_login.clicked.disconnect()
            self.ui.button_register.clicked.disconnect()
            self.ui.label_log.setText(f'Output log')
            self.ui.button_login.setText('Log In')
            self.ui.button_register.setText('Register')
            self.ui.button_login.clicked.connect(self.login)
            self.ui.button_register.clicked.connect(self.register)
            self.ui.line_username.setText('')
            self.ui.line_password.setText('')


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
