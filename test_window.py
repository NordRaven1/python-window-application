from PySide6.QtWidgets import QLabel, QWidget, QPushButton, QGridLayout, QCheckBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from dialog_about_answer import AnswerDialog
import data


class Window(QWidget):

    def __init__(self, number, question, a1, a2, a3, a4, rightanswer, username, allA, rightA, wrongA):
        super().__init__()

        self.setWindowTitle("Тестирование")
        self.setFixedWidth(1000)
        self.setFixedHeight(350)

        self.user = username
        self.question_text = question
        self.question_number = number
        self.text_a = a1
        self.text_b = a2
        self.text_c = a3
        self.text_d = a4
        self.right_answer = rightanswer
        self.all_answers_text = allA
        self.right_answers_text = rightA
        self.wrong_answers_text = wrongA

        self.participant = QLabel(self.user)

        self.question = QLabel(f"{self.question_number}. {self.question_text}")
        self.answer_A = QCheckBox(f"а)  {self.text_a}")
        self.answer_B = QCheckBox(f"б)  {self.text_b}")
        self.answer_C = QCheckBox(f"в)  {self.text_c}")
        self.answer_D = QCheckBox(f"г)  {self.text_d}")

        if self.question_number in data.given_answers:
            self.answer_A.setEnabled(False)
            self.answer_B.setEnabled(False)
            self.answer_C.setEnabled(False)
            self.answer_D.setEnabled(False)

        self.all_answers = QLabel(f"Всего ответов: {self.all_answers_text}/10")
        self.right_answers = QLabel(f"Правильных: {self.right_answers_text}/10")
        self.wrong_answers = QLabel(f"Ошибочных: {self.wrong_answers_text}/10")

        self.next_question = QPushButton()
        self.previous_question = QPushButton()
        self.exit = QPushButton()

        mainLayout = QGridLayout()

        self.answer_A.clicked.connect(self.AnswersState)
        self.answer_B.clicked.connect(self.AnswersState)
        self.answer_C.clicked.connect(self.AnswersState)
        self.answer_D.clicked.connect(self.AnswersState)
        self.next_question.pressed.connect(self.nextQuestion)
        self.previous_question.pressed.connect(self.previousQuestion)
        self.exit.pressed.connect(self.exitButton)

        self.next_question.setIcon(QIcon('rightarrowbutton.png'))
        self.previous_question.setIcon(QIcon('leftarrowbutton.png'))
        self.exit.setIcon(QIcon('exitbutton.png'))
        self.next_question.setIconSize(QSize(35, 35))
        self.previous_question.setIconSize(QSize(35, 35))
        self.exit.setIconSize(QSize(35, 35))

        mainLayout.addWidget(self.participant, 0, 0)
        mainLayout.addWidget(self.question, 2, 1, 2, 5)
        mainLayout.addWidget(self.answer_A, 4, 0)
        mainLayout.addWidget(self.next_question, 5, 8)
        mainLayout.addWidget(self.answer_B, 5, 0)
        mainLayout.addWidget(self.previous_question, 6, 8)
        mainLayout.addWidget(self.answer_C, 6, 0)
        mainLayout.addWidget(self.exit, 7, 8)
        mainLayout.addWidget(self.answer_D, 7, 0)
        mainLayout.addWidget(self.all_answers, 11, 0, 11, 2)
        mainLayout.addWidget(self.right_answers, 11, 3, 11, 4)
        mainLayout.addWidget(self.wrong_answers, 11, 5, 11, 6)
        self.setLayout(mainLayout)

    def checkingAnswer(self, user_answer):
        data.given_answers.append(self.question_number)
        if user_answer == self.right_answer:
            dlg = AnswerDialog(True)
            if dlg.exec():
                data.Aanswers += 1
                data.Ranswers += 1
                self.all_answers_text += 1
                self.right_answers_text += 1
                self.all_answers.setText(f"Всего ответов: {self.all_answers_text}/10")
                self.right_answers.setText(f"Правильных: {self.right_answers_text}/10")
                self.answer_A.setEnabled(False)
                self.answer_B.setEnabled(False)
                self.answer_C.setEnabled(False)
                self.answer_D.setEnabled(False)
                if self.all_answers_text == 10:
                    self.close()
        else:
            dlg = AnswerDialog(False)
            if dlg.exec():
                data.Aanswers += 1
                data.Wanswers += 1
                self.all_answers_text += 1
                self.wrong_answers_text += 1
                self.all_answers.setText(f"Всего ответов: {self.all_answers_text}/10")
                self.wrong_answers.setText(f"Ошибочных: {self.wrong_answers_text}/10")
                self.answer_A.setEnabled(False)
                self.answer_B.setEnabled(False)
                self.answer_C.setEnabled(False)
                self.answer_D.setEnabled(False)
                if self.all_answers_text == 10:
                    self.close()

    def AnswersState(self):
        if self.answer_A.isChecked():
            self.checkingAnswer(self.text_a)
        elif self.answer_B.isChecked():
            self.checkingAnswer(self.text_b)
        elif self.answer_C.isChecked():
            self.checkingAnswer(self.text_c)
        elif self.answer_D.isChecked():
            self.checkingAnswer(self.text_d)

    def nextQuestion(self):
        if data.Window_number < 9:
            data.Window_number += 1
            data.Flag = True
            self.close()

    def previousQuestion(self):
        if data.Window_number > 0:
            data.Window_number -= 1
            data.Flag = True
            self.close()

    def exitButton(self):
        data.write_result(data.Username)
        exit()
