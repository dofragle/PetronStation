class Application:
    def __init__(self, volumeOfGasoline, brandOfGasoline, totalTime, dayOfWeek):
        self.volumeOfGasoline = volumeOfGasoline
        self.brandOfGasoline = brandOfGasoline
        self.dayOfWeek = dayOfWeek
        self.timeUntilTheEnd = totalTime

    def getTimeUntilTheEnd(self):
        return self.timeUntilTheEnd

    def getTimeUntilTheEnd(self, timeUntilTheEnd):
        self.timeUntilTheEnd = timeUntilTheEnd

    def getVolumeOfGasoline(self):
        return self.volumeOfGasoline

    def getDayOfWeek(self):
        return self.dayOfWeek

    def getBrandOfGasoline(self):
        return self.brandOfGasoline
