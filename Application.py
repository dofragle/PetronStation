class Application:
    def __init__(self, volumeOfGasoline, brandOfGasoline, totalTime, dayOfWeek):
        self.volumeOfGasoline = volumeOfGasoline
        self.brandOfGasoline = brandOfGasoline
        self.dayOfWeek = dayOfWeek
        self.timeUntilTheEnd = totalTime

    def get_time_until_the_end(self):
        return self.timeUntilTheEnd

    def set_time_until_the_end(self, timeUntilTheEnd):
        self.timeUntilTheEnd = timeUntilTheEnd

    def get_volume_of_gasoline(self):
        return self.volumeOfGasoline

    def get_day_of_week(self):
        return self.dayOfWeek

    def get_brand_of_gasoline(self):
        return self.brandOfGasoline
