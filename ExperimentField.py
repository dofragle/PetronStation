from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox, QSizePolicy
from Experiment import Experiment
class ExperimentField(QMainWindow):
    def __init__(self, name, experiment):
        super().__init__()
        self.setWindowTitle(name)
        self.width = 1200
        self.height = 1000
        self.menuPanelX = 0
        self.experiment = experiment
        self.curTime = [1, 0, 0]
        self.dayOfWeek = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
        self.labelDayOfWeek = QLabel(len(self.dayOfWeek) + 1)
        self.labelForStatisticWindow = [
            QLabel("Число обслуженных клиентов"),
            QLabel("Число потерянных клиентов"),
            QLabel("Общая прибыль"),
            QLabel("Общие потери")
        ]
        self.buttonLabels = [
            QLabel("Шаг моделирования"), 
            QLabel("Статистика"), 
            QLabel("Начать моделирование заново"), 
            QLabel("Завершить эксперимент"), 
            QLabel("Выход")
        ]
        self.simulationStep = ["10", "20", "30", "40", "50", "60"]
        self.brand_of_gasoline = experiment.brandOfGasoline
        self.brand_of_gasoline_by_one = experiment.brandOfGasolineByOne
        self.statisticDialog = QDialog()
        self.setGeometry(100, 100, self.width, self.height)
        self.simulationStepList = QComboBox()
        self.simulationStepList.addItems(self.simulationStep)
        self.simulationStepList.setCurrentIndex(0)
        self.simulationStepList.currentIndexChanged.connect(self.onSimulationStepChanged)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout(self.centralWidget)

        self.menuLayout = QVBoxLayout()
        self.menuLayout.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.menuLayout)
        self.menuLayout.addWidget(self.simulationStepList)
        self.buttons = []
        for label in self.buttonLabels:
            button = QPushButton(label)
            button.setSizePolicy(QSizePolicy.expandingDirections)
            self.buttons.append(button)
            self.menuLayout.addWidget(button)
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


