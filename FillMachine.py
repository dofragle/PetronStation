class FillMachine:
    def __init__(self, brandOfGasoline):
        self.brandOfGasoline = brandOfGasoline
        self.listOfApplications = []

    def size_list_of_applications(self):
        return len(self.listOfApplications)

    def set_new_applications(self, application):
        self.listOfApplications.append(application)
