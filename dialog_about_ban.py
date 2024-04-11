from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class BanDialog(QDialog):

    def __init__(self, ban_info):
        super().__init__()

        self.setWindowTitle("Ошибка регистрации")
        layout = QVBoxLayout()

        self.my_stats = QLabel(ban_info)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)

        layout.addWidget(self.my_stats)
        layout.addWidget(button_box)
        self.setLayout(layout)
