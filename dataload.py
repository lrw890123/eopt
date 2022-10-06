import numpy as np
class Dataload:
    def __init__(self, route):
        self.route = route

    def get_size(self, file_name):
        size = []
        f = open(self.route + file_name, encoding='utf-8')
        while True:
            line = f.readline()
            if line:
                line=line.strip('\n')
                size.append(list(map(int, line.split(' '))))

            else:
                break
        f.close()
        systems_number, equipments_number, crews_number = size[0][0], size[0][1], size[0][2]
        crews_set = size[1]
        return systems_number, equipments_number, crews_number, crews_set

    def get_coordinates(self, file_name):
        coordinates = np.loadtxt(self.route + file_name)
        return coordinates

    def get_systemcomposition(self, file_name):
        system_composition = []
        f = open(self.route + file_name, encoding='utf-8')
        while True:
            line = f.readline()
            if line:
                line=line.strip('\n')
                system_composition.append(list(map(int, line.split(' '))))

            else:
                break
        f.close()
        return system_composition

    def get_capabilities(self, file_name):
        capabilities = np.loadtxt(self.route + file_name)
        return capabilities 

    def get_repairtime(self, file_name):
        repair_time = np.loadtxt(self.route + file_name, dtype=int)
        return repair_time

