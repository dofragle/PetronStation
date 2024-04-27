import random
from PetrolStation import PetrolStation
from Application import Application

class Experiment:
    def __init__(self, simulationStep, N, tradeMargin, K,
                 brandOfGasoline, basePriceForBrandOfGasoline,
                 numberOfFillingMachinesForBrandOfGasoline, timeIntervalBetweenApplications,
                 amountOfFuelForOneCar):
        self.currentTime = [1, 0, 0]
        self.simulationStep = simulationStep
        self.N = N
        self.K = K
        self.tradeMargin = tradeMargin
        self.brandOfGasoline = []
        self.brandOfGasolineByOne = brandOfGasoline
        self.basePriceForBrandOfGasoline = []
        self.timeIntervalBetweenApplications = timeIntervalBetweenApplications
        self.amountOfFuelForOneCar = amountOfFuelForOneCar
        self.listOfApplications = []
        self.petrolStation = None
        self.lostApplications = []
        self.serviceTime = 20
        self.basicServiceTime = 1
        self.timeNewApplication = 0
        self.haveSafeTimeNewApplication = False
        self.dayInWeek = 7
        self.petrolStation = PetrolStation(N, self.brandOfGasoline)
        cnt = 0
        for i in range(len(brandOfGasoline)):
            for j in range(numberOfFillingMachinesForBrandOfGasoline[i]):
                self.brandOfGasoline.append(brandOfGasoline[i])
                self.basePriceForBrandOfGasoline.append(basePriceForBrandOfGasoline[i])
                cnt += 1

    def CreateNewApplication(self):
        volumeOfGasoline = random.randint(self.amountOfFuelForOneCar[0], self.amountOfFuelForOneCar[1])
        brandOfGasoline = random.choice(self.brandOfGasoline)
        totalServiceTime = self.basicServiceTime + volumeOfGasoline * self.serviceTime / 60 + 1
        return Application(volumeOfGasoline, brandOfGasoline, totalServiceTime, self.currentTime[0])
