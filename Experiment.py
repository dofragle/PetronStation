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
        self.listOfApplications = []
        self.petrolStation = None
        self.lostApplications = []
        self.serviceTime = 20
        self.basicServiceTime = 1
        self.timeNewApplication = 0
        self.haveSafeTimeNewApplication = False
        self.dayInWeek = 7
        cnt = 0
        for i in range(len(brandOfGasoline)):
            for j in range(numberOfFillingMachinesForBrandOfGasoline[i]):
                self.brandOfGasoline.append(brandOfGasoline[i])
                self.basePriceForBrandOfGasoline.append(basePriceForBrandOfGasoline[i])
                cnt += 1
        self.timeIntervalBetweenApplications = timeIntervalBetweenApplications
        self.amountOfFuelForOneCar = amountOfFuelForOneCar
        self.petrolStation = PetrolStation(N, self.brandOfGasoline)

    def CreateNewApplication(self):
        volumeOfGasoline = random.randint(self.amountOfFuelForOneCar[0], self.amountOfFuelForOneCar[1])
        brandOfGasoline = random.choice(self.brandOfGasoline)
        totalServiceTime = self.basicServiceTime + volumeOfGasoline * self.serviceTime / 60 + 1
        return Application(volumeOfGasoline, brandOfGasoline, totalServiceTime, self.currentTime[0])

    def GetListOfApplicationsSize(self):
        if self.listOfApplications is not None:
            return self.listOfApplications.count
        else:
            return 0
        
    def FindPriceByBrandOfGasoline(self, brandOfGasoline):
        for i in range(len(self.brandOfGasoline)):
            if self.brandOfGasoline[i] == brandOfGasoline:
                return self.basePriceForBrandOfGasoline[i]
        return 0        
    
    def totalEarnings(self):
        sum = 0
        for application in range(self.listOfApplications):
            if application.getTimeUntilTheEnd() == 0:
                sum += self.FindPriceByBrandOfGasoline(application.GetBrandOfGasoline()) * application.GetVolumeOfGasoline() * (100 + self.tradeMargin) / 100
        return sum
    
    def EarningsByDay(self, listOfApplications):
        earningsByDay = []*(self.dayInWeek+1)
        for application in range(listOfApplications):
            if application.getTimeUntilTheEnd() == 0:
                earningsByDay[application.GetDayOfWeek() - 1] += self.FindPriceByBrandOfGasoline(application.GetBrandOfGasoline()) * application.GetVolumeOfGasoline() * (100 + self.tradeMargin) / 100
        avg = 0
        for i in self.dayInWeek:
            if earningsByDay[i] == 0:
                earningsByDay[self.dayInWeek] = 0 if i == 0 else avg / i
                return earningsByDay
            avg += earningsByDay[i]
        earningsByDay[self.dayInWeek] = avg / self.dayInWeek
        return earningsByDay
    
    def HaveEarning(self):
        return self.EarningsByDay(self.listOfApplications)
    
    def LostEarning(self):
        return self.EarningsByDay(self.lostApplications)
    
    def GetBrandOfGasoline(self):
        return self.brandOfGasoline

    def GetBrandOfGasolineByOne(self):
        return self.brandOfGasolineByOne

    def GetK(self):
        return self.K

    def IsWeekend(self):
        if self.currentTime[0] == 6 or self.currentTime[0] == 7:
            return 1
        return 0

    def IsTheTimeBetween16And22(self):
        if self.currentTime[1] >= 16 or self.currentTime[1] < 22:
            return 1
        return 0

    def GenerateTimeIntervalForNewApplication(self):
        forMarkupPercentage = 3
        forWeekend = 7
        forTheTimeBetween16And22 = 3
        avg = (self.timeIntervalBetweenApplications[0] + self.timeIntervalBetweenApplications[1]) / 2.0
        avg_in_minutes = 1.0 / avg
        fluxDensity = 100 - forMarkupPercentage * self.tradeMargin + forWeekend * self.IsWeekend() + forTheTimeBetween16And22 * self.IsTheTimeBetween16And22()
        avg_in_minutes = avg_in_minutes * fluxDensity / 100.0
        new_avg = 1.0 / avg_in_minutes
        return [round((int) (new_avg - avg)), (int) (new_avg + avg)]

    def UpdateTimeForApplication(self, timeNewApplication):
        for i in self.listOfApplications.len:
            self.listOfApplications[i].timeUntilTheEnd = max(self.listOfApplications.get(i).timeUntilTheEnd - timeNewApplication, 0)

    def UpdateGlobalTime(self, step):
        self.currentTime[2] += step
        if self.currentTime[2] >= 60:
            self.currentTime[2] -= 60
            self.currentTime[1] += 1
            if self.currentTime[1] >= 24:
                self.currentTime[1] -= 24
                self.currentTime[0] += 1

    def NewSimulationStep(self):
        currentTimeInStep = 0
        timeInterval = self.GenerateTimeIntervalForNewApplication()
        while True:
            if not self.haveSafeTimeNewApplication:
                timeNewApplication = timeInterval[0] + (int) (random() * (timeInterval[1] - timeInterval[0]))
            self.haveSafeTimeNewApplication = False
            currentTimeInStep += timeNewApplication
            if currentTimeInStep > self.simulationStep:
                break
            self.UpdateTimeForApplication(timeNewApplication)
            self.petrolStation.DeleteTheEnd()

            newApplication = self.CreateNewApplication()
            if self.petrolStation.ServiceNewApplication(newApplication):
                self.listOfApplications.add(newApplication)
            else:
                newApplication.setTimeUntilTheEnd(0)
                self.lostApplications.add(newApplication)
        self.UpdateTimeForApplication(timeNewApplication - (currentTimeInStep - self.simulationStep))
        self.petrolStation.DeleteTheEnd()
        self.haveSafeTimeNewApplication = True
        timeNewApplication = currentTimeInStep - self.simulationStep
        self.UpdateGlobalTime(self.simulationStep)

    def FinishSimulation(self):
        while True:
            timeInterval = self.GenerateTimeIntervalForNewApplication()
            if not self.haveSafeTimeNewApplication:
                timeNewApplication = timeInterval[0] + (int) (random() * (timeInterval[1] - timeInterval[0]))
            self.haveSafeTimeNewApplication = False
            self.UpdateGlobalTime(timeNewApplication)
            if self.currentTime[0] > self.dayInWeek:
                break

            self.UpdateTimeForApplication(timeNewApplication)
            self.petrolStation.DeleteTheEnd()
            newApplication = self.CreateNewApplication()
            if self.petrolStation.ServiceNewApplication(newApplication):
                self.listOfApplications.add(newApplication)
            else:
                newApplication.setTimeUntilTheEnd(0)
                self.lostApplications.add(newApplication)
        for application in range(self.listOfApplications):
            application.setTimeUntilTheEnd(0)

    def GetCurrentTime(self):
        return self.currentTime

    def GetSizeLostApplications(self):
        return self.lostApplications.size()

    def ApplicationByDay(self, listOfApplications):
        applicationByDay = []*(self.dayInWeek + 1)
        for application in range(listOfApplications):
            if application.getTimeUntilTheEnd() == 0:
                applicationByDay[application.GetDayOfWeek() - 1] += 1
        avg = 0
        for i in self.dayInWeek:
            if applicationByDay[i] == 0:
                applicationByDay[self.dayInWeek] =0 if i == 0 else avg / i
                return applicationByDay
            avg += applicationByDay[i]
        applicationByDay[self.dayInWeek] = avg / self.dayInWeek
        return applicationByDay

    def GetIndexBrandOfGasoline(self, brandOfGasoline):
        for i in self.brandOfGasolineByOne.length:
            if brandOfGasoline == self.brandOfGasolineByOne[i]:
                return i
        return -1

    def VolumeGasolineByDay(self, listOfApplications):
        volumeGasolineByDay = []
        for application in listOfApplications:
            if application.getTimeUntilTheEnd() == 0:
                volumeGasolineByDay[self.GetIndexBrandOfGasoline(application.brandOfGasoline)][application.GetDayOfWeek() - 1] += application.GetVolumeOfGasoline()
        for i in self.brandOfGasolineByOne.length:
            avg = 0
            j = 0
            for j in self.dayInWeek:
                if volumeGasolineByDay[i][j] == 0:
                    break
                avg += volumeGasolineByDay[i][j]
            volumeGasolineByDay[i][self.dayInWeek] = 0 if j == 0 else avg / j
        return volumeGasolineByDay

    def HaveVolumeGasolineByDay(self):
        return self.VolumeGasolineByDay(self.listOfApplications)

    def ServiceApplicationByDay(self):
        return self.ApplicationByDay(self.listOfApplications)

    def LostApplicationByDay(self):
        return self.ApplicationByDay(self.lostApplications)

    def GetTradeMargin(self):
        return self.tradeMargin

    def GetN(self):
        return self.N

    def SetSimulationStep(self, simulationStep):
        self.simulationStep = simulationStep

    def GetPetrolStation(self):
        return self.petrolStation