from PySide6.QtWidgets import QApplication, QStyleFactory
import test_window
import greeting_window
import results_window

info = []              # Массив из массивов информации о вопросе - номер, текст вопроса, ответы, правильный ответ
personal_results = []  # Массив из массивов информации об участнике и его результатов по каждому тесту
given_answers = []     # Массив из номеров ответов теста, которые пользователь уже отвечал
users_passwords = {}   # Словарь соответствия участвовавших ранее пользователей и их паролей
tests_numbers = {}     # Словарь соответствия тестов и их номеров
users = [""]           # Массив из имен участвовавших ранее пользователей для авторизации
tests = [""]           # Массив из названий тестов для их выбора в викторине
Aanswers = 0           # Переменная для количества вопросов, на которые ответ был дан
Ranswers = 0           # Переменная для количества вопросов, на которые ответ был дан правильно
Wanswers = 0           # Переменная для количества вопросов, на которые ответ был дан неправильно
Username = ""          # Переменная для имени участника
Flag = True            # bool переменная для того, чтобы знать, нужно создавать окно тестирования или нет
Window_number = 0      # Переменная, чтобы знать на каком сейчас вопросе участник
Test_number = 0        # Переменная, чтобы знать какой по номеру тест выбрал участник
app = QApplication([])
QApplication.setStyle(QStyleFactory.create("Fusion"))

with open("style.qss", "r") as f:
    style = f.read()
    app.setStyleSheet(style)

with open('users.txt', 'r', encoding="utf8") as f:
    users_strings = f.readlines()
    for names in users_strings:
        names = names.strip()
        name, password = names.split(";")
        users_passwords[name] = password
        users.append(name)
with open('tests.txt', 'r', encoding="utf8") as f:
    tests_strings = f.readlines()
    for test_text in tests_strings:
        test_text = test_text.strip()
        num, test = test_text.split(';')
        tests_numbers[test] = num
        tests.append(test)


def createTestWindow(element):
    global Flag
    Flag = False
    window = test_window.Window(info[element][0], info[element][1], info[element][2], info[element][3],
                                info[element][4], info[element][5], info[element][6], Username, Aanswers,
                                Ranswers, Wanswers)
    window.show()
    app.exec()


def createGreetingWindow():
    window = greeting_window.Window()
    window.show()
    app.exec()


def createResultsWindow():
    window = results_window.Window()
    window.show()
    app.exec()


def test_choice(file):
    path = '' + file + ".txt"
    test_info = open(path, 'r', encoding="utf8")
    for i in range(10):
        string = test_info.readline()
        string = string.strip()
        info.append(string.split(";"))


def write_result(name_of_user):
    file = open('results.txt', 'r', encoding="utf8")
    replaced_content = ''
    for result in file:
        result = result.strip()
        if name_of_user in result:
            for i in range(len(personal_results)):
                if personal_results[i][0] == name_of_user:
                    personal_results[i][Test_number] = str(Ranswers)
                    new_line = ';'.join(personal_results[i])
                    break
        else:
            new_line = result
        replaced_content = replaced_content + new_line + "\n"
    file.close()
    write_file = open('results.txt', 'w', encoding="utf8")
    write_file.write(replaced_content)
    write_file.close()


def find_result(name1):
    isFind = False
    for i in range(len(personal_results)):
        if personal_results[i][0] == name1 and personal_results[i][Test_number] == "?":
            isFind = True
            break
    return isFind


def find_result_arr(name2):
    for i in range(len(personal_results)):
        if personal_results[i][0] == name2:
            return personal_results[i]


def get_result():
    personal_results.clear()
    pathto = 'results.txt'
    results_info = open(pathto, 'r', encoding="utf8")
    for res in results_info:
        res = res.strip()
        personal_results.append(res.split(";"))
