from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class StatsDialog(QDialog):

    def __init__(self, stats_arr):
        super().__init__()

        self.setWindowTitle("Статистика пользователя")
        layout = QVBoxLayout()

        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)

        self.my_stats = QLabel()
        name, res1, res2 = stats_arr[0], stats_arr[1], stats_arr[2]
        stats_line = f"{name}  Тест 1: {res1}/10  Тест 2: {res2}/10"
        self.my_stats.setText(stats_line)

        layout.addWidget(self.my_stats)
        layout.addWidget(button_box)
        self.setLayout(layout)
