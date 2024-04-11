from PySide6.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QLabel, QComboBox
from dialog_about_stats import StatsDialog
from dialog_about_ban import BanDialog
import data


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Авторизация")
        self.setFixedWidth(510)
        self.setFixedHeight(350)

        self.greeting = QLabel()
        self.personal_info = QLineEdit()
        self.personal_pass = QLineEdit()
        self.ok_button = QPushButton("Готово")
        self.stats_button = QPushButton("Статистика")
        self.i_am_already_user = QComboBox()
        self.test_combobox = QComboBox()
        mainLayout = QGridLayout()

        self.i_am_already_user.addItems(data.users)
        self.test_combobox.addItems(data.tests)
        self.greeting.setText("Добро пожаловать на викторину! Перед тем, как приступать к тесту, выберите тест "
                              "из списка и введите своё имя с паролем через ';'. Если вы уже участвовали, выберите "
                              "себя из списка пользователей и введите пароль. После этого нажмите кнопку 'Готово'."
                              "Вы также можете посмотреть свою статистику по всем тестам по кнопке 'Статистика'.")
        self.greeting.setWordWrap(True)

        self.ok_button.pressed.connect(self.Send_name)
        self.stats_button.pressed.connect(self.My_stats)
        self.i_am_already_user.currentTextChanged.connect(self.Write_text)
        self.test_combobox.currentTextChanged.connect(self.Which_number_of_test)

        mainLayout.addWidget(self.greeting, 0, 0, 1, 10)
        mainLayout.addWidget(self.i_am_already_user, 9, 0, 9, 3)
        mainLayout.addWidget(self.personal_info, 9, 4, 9, 6)
        mainLayout.addWidget(self.personal_pass, 10, 0, 10, 3)
        mainLayout.addWidget(self.test_combobox, 10, 4, 10, 6)
        mainLayout.addWidget(self.ok_button, 11, 1, 11, 7)
        mainLayout.addWidget(self.stats_button, 12, 1, 12, 7)
        self.setLayout(mainLayout)

    def Send_name(self):
        user = self.personal_info.text()
        already_user = self.i_am_already_user.currentText()
        password = self.personal_pass.text()
        if already_user == "":
            if user != "" and user != " " * len(user):
                if user.count(";") != 0:
                    if self.test_combobox.currentText() != "":
                        name, passw = user.split(';')
                        if name not in data.users:
                            data.Username = name
                            users_info = open('users.txt', 'a', encoding="utf8")
                            results_info = open('results.txt', 'a', encoding="utf8")
                            users_info.write(f"{user}\n")
                            results_info.write(name + ";?" * 2 + "\n")
                            data.test_choice(self.test_combobox.currentText())
                            self.close()
                        else:
                            dlg = BanDialog("Такой пользователь уже существует, попробуйте как-то "
                                            "изменить свой никнейм")
                            if dlg.exec():
                                return
                    else:
                        dlg = BanDialog("Вы не выбрали тест для викторины")
                        if dlg.exec():
                            return
                else:
                    dlg = BanDialog("Вы не ввели пароль после имени через ';'")
                    if dlg.exec():
                        return
            else:
                dlg = BanDialog("Вы ввели пустое пространство вместо никнейма")
                if dlg.exec():
                    return
        else:
            first_try = data.find_result(already_user)
            if password == data.users_passwords[already_user]:
                if self.test_combobox.currentText() != "":
                    if first_try:
                        data.Username = already_user
                        data.test_choice(self.test_combobox.currentText())
                        self.close()
                    else:
                        dlg = BanDialog("Вы уже проходили данный тест")
                        if dlg.exec():
                            return
                else:
                    dlg = BanDialog("Вы не выбрали тест для викторины")
                    if dlg.exec():
                        return
            else:
                dlg = BanDialog("Вы ввели неверный пароль")
                if dlg.exec():
                    return

    def Write_text(self):
        text = self.i_am_already_user.currentText()
        self.personal_info.setText(text)

    def Which_number_of_test(self):
        if self.test_combobox.currentText() != "":
            data.Test_number = int(data.tests_numbers[self.test_combobox.currentText()])

    def My_stats(self):
        user = self.i_am_already_user.currentText()
        password = self.personal_pass.text()
        if user in data.users and user != "":
            if password == data.users_passwords[user]:
                arr = data.find_result_arr(self.i_am_already_user.currentText())
                dlg = StatsDialog(arr)
                if dlg.exec():
                    return
