import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from Experiment import Experiment
from ExperimentField import ExperimentField


class ExperimentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Входные данные для эксперимента')

        layout = QVBoxLayout()

        # Шаг моделирования
        self.label1 = QLabel("Шаг моделирования (выберите шаг от 10 до 60 минут):")
        self.text_edit1 = QLineEdit()
        self.text_edit1.setFixedWidth(250)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.label1, alignment=Qt.AlignLeft)
        hbox1.addWidget(self.text_edit1, alignment=Qt.AlignRight)
        layout.addLayout(hbox1)

        # Максимально возможная длина очереди возле разливочного автомата N
        self.label2 = QLabel("Максимально возможная длина очереди возле разливочного автомата N (от 5 до 9):")
        self.text_edit2 = QLineEdit()
        self.text_edit2.setFixedWidth(250)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.label2, alignment=Qt.AlignLeft)
        hbox2.addWidget(self.text_edit2, alignment=Qt.AlignRight)
        layout.addLayout(hbox2)

        # Торговая наценка
        self.label3 = QLabel("Торговая наценка (от 5 до 15 %):")
        self.text_edit3 = QLineEdit()
        self.text_edit3.setFixedWidth(250)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.label3, alignment=Qt.AlignLeft)
        hbox3.addWidget(self.text_edit3, alignment=Qt.AlignRight)
        layout.addLayout(hbox3)

        # Марки топлива на бензозаправочной станции
        self.label4 = QLabel("Марки топлива на бензозаправочной станции:")
        self.text_edit4 = QLineEdit()
        self.text_edit4.setFixedWidth(250)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.label4, alignment=Qt.AlignLeft)
        hbox4.addWidget(self.text_edit4, alignment=Qt.AlignRight)
        layout.addLayout(hbox4)

        # Базовая цена на бензин каждой марки
        self.label5 = QLabel("Базовая цена на бензин каждой марки (y.e.):")
        self.text_edit5 = QLineEdit()
        self.text_edit5.setFixedWidth(250)
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.label5, alignment=Qt.AlignLeft)
        hbox5.addWidget(self.text_edit5, alignment=Qt.AlignRight)
        layout.addLayout(hbox5)

        # Количество разливочных автоматов под каждую марку
        self.label6 = QLabel("Количество разливочных автоматов под каждую марку (общее число от 3 до 7):")
        self.text_edit6 = QLineEdit()
        self.text_edit6.setFixedWidth(250)
        hbox6 = QHBoxLayout()
        hbox6.addWidget(self.label6, alignment=Qt.AlignLeft)
        hbox6.addWidget(self.text_edit6, alignment=Qt.AlignRight)
        layout.addLayout(hbox6)

        # Временной промежуток между последовательным поступлением заявок
        self.label7 = QLabel("Временной промежуток между последовательным поступлением заявок (от 0 до 20 секунд):")
        self.text_edit7 = QLineEdit()
        self.text_edit7.setFixedWidth(250)
        hbox7 = QHBoxLayout()
        hbox7.addWidget(self.label7, alignment=Qt.AlignLeft)
        hbox7.addWidget(self.text_edit7, alignment=Qt.AlignRight)
        layout.addLayout(hbox7)

        # Объема требуемого топлива в каждой заявке
        self.label8 = QLabel("Объема требуемого топлива в каждой заявке (от 10 до 50 литров):")
        self.text_edit8 = QLineEdit()
        self.text_edit8.setFixedWidth(250)
        hbox8 = QHBoxLayout()
        hbox8.addWidget(self.label8, alignment=Qt.AlignLeft)
        hbox8.addWidget(self.text_edit8, alignment=Qt.AlignRight)
        layout.addLayout(hbox8)

        start_button = QPushButton('Начать моделирование эксперимента')
        start_button.clicked.connect(self.start_experiment)
        exit_button: QPushButton = QPushButton('Выход')
        exit_button.clicked.connect(self.close)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(start_button)
        buttons_layout.addWidget(exit_button)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

        self.fill_text_edits()

    def fill_text_edits(self):
        # Список всех текстовых полей
        self.text_edit1.setText('10')
        self.text_edit2.setText('5')
        self.text_edit3.setText('5')
        self.text_edit4.setText('92, 95, 97, 98, 100')
        self.text_edit5.setText('10, 11, 12, 13, 14')
        self.text_edit6.setText('2, 2, 1, 1, 1')
        self.text_edit7.setText('1-20')
        self.text_edit8.setText('10-50')

    def start_experiment(self):
        currentData = Experiment(int(self.text_edit1.text()), int(self.text_edit2.text()), int(self.text_edit3.text()),
                                     len(list(map(int, self.text_edit6.text().split(",")))), list(map(int, self.text_edit4.text().split(","))),
                                     list(map(int, self.text_edit5.text().split(","))),list(map(int, self.text_edit6.text().split(","))),
                                     list(map(int, self.text_edit7.text().split("-"))),list(map(int, self.text_edit8.text().split("-"))))
        # Открытие окна эксперимента
        self.experiment_field = ExperimentField("Experiment Field", currentData)
        self.experiment_field.show()
        self.close()  # Закрываем текущее окно

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExperimentWindow()
    window.show()
    sys.exit(app.exec_())
