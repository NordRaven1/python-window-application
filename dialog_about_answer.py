from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class AnswerDialog(QDialog):

    def __init__(self, answer):
        super().__init__()

        self.setWindowTitle("Результат ответа")
        layout = QVBoxLayout()
        self.res = answer

        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)

        self.notification = QLabel()
        if self.res:
            self.notification.setText("Ответ правильный, вы молодец!")
        else:
            self.notification.setText("Ответ неправильный, но не унывайте!")
        layout.addWidget(self.notification)
        layout.addWidget(button_box)
        self.setLayout(layout)
