1 # pylint: disable=no-member

import gurobipy as gp
import numpy as np
import math
class Model():
    def __init__(self, nums_sys, nums_equip, nums_crews, 
                 dep, coordinates, sys_cps, cap, repair_time, Time):
        self.nums_sys = nums_sys
        self.nums_equip = nums_equip
        self.nums_crews = nums_crews
        self.dep = dep
        self.coordinates = coordinates
        self.sys_cps = sys_cps
        self.cap = cap
        self.repair_time = repair_time
        self.Time = Time
        self.m = gp.Model()

    def get_traveltime(self):
        traveltime = np.zeros((self.nums_equip+self.nums_crews, 
                               self.nums_equip+self.nums_crews))
        for i in range(self.nums_crews+self.nums_equip):
            for j in range(self.nums_crews+self.nums_equip):
                traveltime[i][j] = traveltime[j][i]= math.sqrt(math.pow(self.coordinates[i][0]-self.coordinates[j][0], 2) 
                                                             + math.pow(self.coordinates[i][1]-self.coordinates[j][1], 2))

        return traveltime
  
    def set_variables(self):
        self.y = self.m.addVars((self.nums_equip, self.nums_crews), vtype=gp.GRB.BINARY, name="y")
        self.y_prime = self.m.addVars((self.nums_equip, self.nums_crews), vtype=gp.GRB.BINARY, name="y_prime")
        self.y_prime2 = self.m.addVars((self.nums_equip, self.nums_crews), vtype=gp.GRB.BINARY, name="y_prime2")
        self.z = self.m.addVars((self.nums_equip, self.nums_equip), vtype=gp.GRB.BINARY, name="z")
        self.x = self.m.addVars( self.nums_equip, vtype=gp.GRB.BINARY, name="x")
        self.o = self.m.addVars( self.nums_sys, vtype=gp.GRB.BINARY, namse="o")


    def set_objective(self) -> None:
        traveltime = self.get_traveltime()
        exprtotal = self.m.LinExpr()
        for s in range(self.nums_sys):
            exprtau = self.m.LinExpr()
            exprtraveltime = self.m.LinExpr()
            
            for i in self.sys_cps[s]:
                exprtau.addTerms(self.repair_time[i])
                for j in self.sys_cps[s]:
                    exprtraveltime.addTerms(traveltime[i][j], self.z[i][j])
            exprtotal.add(self.Time - (exprtau + exprtraveltime), self.cap[s])
        self.m.setObjective(exprtotal, gp.GRB.MAXIMIZE)

    def set_constraints(self):
        self.m.addConstrs(self.y.sum(i, '*') == self.x[i] for i in range(self.nums_equip))

        self.m.addConstrs(self.y_prime[i][p] <= self.y[i][p] for i in range(self.nums_equip) 
                                                             for p in range(self.nums_crews))
        self.m.addConstrs(self.y_prime.sum('*', p) == 1 for p in range(self.nums_crews))

        self.m.addConstrs(self.y_prime2[i][p] <= self.y[i][p] for i in range(self.nums_equip) 
                                                             for p in range(self.nums_crews))
        self.m.addConstrs(self.y_prime2.sum('*', p) == 1 for p in range(self.nums_crews))
