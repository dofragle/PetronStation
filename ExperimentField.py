from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox, QSizePolicy
from Experiment import Experiment
class ExperimentField(QMainWindow):
    def __init__(self, name, experiment):
        super().__init__()
        self.setWindowTitle(name)
        self.width = 1200
        self.height = 1000
        self.experiment = experiment
        self.brand_of_gasoline = experiment.brandOfGasoline
        self.brand_of_gasoline_by_one = experiment.brandOfGasolineByOne

        self.setGeometry(100, 100, self.width, self.height)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout(self.central_widget)

        self.menu_layout = QVBoxLayout()
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.menu_layout)

        self.simulation_step_list = QComboBox()
        self.simulation_step_list.addItems(["10", "20", "30", "40", "50", "60"])
        self.simulation_step_list.setCurrentIndex(0)
        self.simulation_step_list.currentIndexChanged.connect(self.onSimulationStepChanged)
        self.menu_layout.addWidget(self.simulation_step_list)

        button_labels = ["Шаг моделирования", "Статистика", "Начать моделирование заново", "Завершить эксперимент",
                         "Выход"]
        self.buttons = []
        for label in button_labels:
            button = QPushButton(label)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.buttons.append(button)
            self.menu_layout.addWidget(button)
            if label == "Статистика":
                button.clicked.connect(self.onStatisticsClicked)
            elif label == "Завершить эксперимент":
                button.clicked.connect(self.onFinishExperimentClicked)
            elif label == "Выход":
                button.clicked.connect(self.close)
            elif label == "Шаг моделирования":
                button.clicked.connect(self.onSimulationStepClicked)

        self.petrol_station_queue_field = PetrolStationQueueField(self.experiment)
        self.layout.addWidget(self.petrol_station_queue_field)

    def onSimulationStepChanged(self, index):
        simulation_step = int(self.simulation_step_list.currentText())
        self.experiment.SetSimulationStep(simulation_step)

    def onSimulationStepClicked(self):
        if self.statistic_dialog:
            self.statistic_dialog.close()
            self.statistic_dialog = None

        self.experiment.NewSimulationStep()
        cur_time = self.experiment.GetCurrentTime()
        if cur_time[0] == 8:
            finish_dialog = QMessageBox()
            finish_dialog.setWindowTitle("Завершение эксперимента")
            finish_dialog.setText("Эксперимент завершен.")
            finish_dialog.exec_()
            self.close()

    def onStatisticsClicked(self):
        if self.statistic_dialog:
            self.statistic_dialog.close()
            self.statistic_dialog = None
        self.statistic_dialog = StatisticDialog(self.experiment, self.brand_of_gasoline_by_one, self)
        self.statistic_dialog.show()

    def onFinishExperimentClicked(self):
        if self.statistic_dialog:
            self.statistic_dialog.close()
            self.statistic_dialog = None
        self.experiment.FinishSimulation()
        self.statistic_dialog = StatisticDialog(self.experiment, self.brand_of_gasoline_by_one, self, True)
        self.statistic_dialog.show()

class PetrolStationQueueField(QWidget):
    def __init__(self, experiment):
        super().__init__()
        self.experiment = experiment


