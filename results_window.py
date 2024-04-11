from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel
from dialog_about_stats import StatsDialog
import data


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Результаты")
        self.setFixedWidth(500)
        self.setFixedHeight(180)
        self.user = data.Username
        self.res = data.Ranswers

        self.congratulations = QLabel()
        self.close_button = QPushButton("Завершить")
        self.stats_button = QPushButton("Статистика")
        mainLayout = QGridLayout()

        self.congratulations.setText(f"Поздравляем вас, {self.user}, с окончанием теста. Ваш результат - {self.res}/10."
                                    f"Вы также можете посмотреть свою статистику по всем тестам по кнопке 'Статистика'")
        self.congratulations.setWordWrap(True)

        self.close_button.pressed.connect(self.Finish_test)
        self.stats_button.pressed.connect(self.My_stats)

        mainLayout.addWidget(self.congratulations,  0, 0, 1, 10)
        mainLayout.addWidget(self.stats_button, 3, 0, 3, 3)
        mainLayout.addWidget(self.close_button, 3, 5, 3, 6)
        self.setLayout(mainLayout)

    def My_stats(self):
        arr = data.find_result_arr(data.Username)
        dlg = StatsDialog(arr)
        if dlg.exec():
            return

    def Finish_test(self):
        self.close()
