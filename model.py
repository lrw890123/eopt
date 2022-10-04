import gurobipy as gp
import numpy as np

class Model():
    def __init__(self, nums_sys, nums_equip, nums_crews, dep, coordinates, sys_cps, cap, repair_time):
        self.nums_sys = nums_sys
        self.nums_equip = nums_equip
        self.nums_crews = nums_crews
        self.dep = dep
        self.coordinates = coordinates
        self.sys_cps = sys_cps
        self.cap = cap
        self.repair_time = repair_time
        self.m = gp.Model()

    def set_objective(self):
        