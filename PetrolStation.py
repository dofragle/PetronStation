from FillMachine import FillMachine


class PetrolStation:
    def __init__(self, N, brandOfGasoline):
        self.N = N
        self.listOfFillingMachines = []
        for brand in brandOfGasoline:
            self.listOfFillingMachines.append(FillMachine(brand))

    def service_new_application(self, application):
        for i in range(len(self.listOfFillingMachines)):
            if self.listOfFillingMachines[i].brandOfGasoline == application.brandOfGasoline:
                if (i != len(self.listOfFillingMachines) - 1 and
                        self.listOfFillingMachines[i].brandOfGasoline ==
                        self.listOfFillingMachines[i + 1].brandOfGasoline and
                        self.listOfFillingMachines[i].size_list_of_applications() >
                        self.listOfFillingMachines[i + 1].size_list_of_applications()):
                    continue
                new_queue_size = self.listOfFillingMachines[i].size_list_of_applications() + 1
                if new_queue_size <= self.N:
                    self.listOfFillingMachines[i].set_new_applications(application)
                    return True
        return False

    def delete_the_end(self):
        for machine in self.listOfFillingMachines:
            machine.list_of_applications = [app for app in machine.list_of_applications if app.time_until_the_end != 0]

    def get_size_queue_in_fill_machine(self):
        return [machine.size_list_of_applications() for machine in self.listOfFillingMachines]
