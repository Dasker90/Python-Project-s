#!pip install ortools
print("""
3a + 6b + 2c <= 50
4a-6b+8c <= 45
3a+1b-5c <= 37
max -> 3a+2b+2*c
""")
# Import linear solver lib
from ortools.linear_solver import pywraplp
# SCIP its the argument used for the toolbox OR Tools for solving mixed nonlinear problems.
solver = pywraplp.Solver.CreateSolver('SCIP')
# a,b,c are non-negative integer variables.
vara = solver.IntVar(0.0, solver.infinity(),'a')
varb = solver.IntVar(0.0, solver.infinity(),'b')
varc = solver.IntVar(0.0, solver.infinity(),'c')
# Constraints
# Equation 1
cons_in1 = solver.Constraint(-solver.infinity(), 50)
cons_in1.SetCoefficient(vara, 3)
cons_in1.SetCoefficient(varb, 6)
cons_in1.SetCoefficient(varc, 2)
# Equation 2
cons_in1 = solver.Constraint(-solver.infinity(), 45)
cons_in1.SetCoefficient(vara, 4)
cons_in1.SetCoefficient(varb, -6)
cons_in1.SetCoefficient(varc, 8)
# Equation 3
cons_in1 = solver.Constraint(-solver.infinity(), 37)
cons_in1.SetCoefficient(vara, 3)
cons_in1.SetCoefficient(varb, 6)
cons_in1.SetCoefficient(varc, 2)
#Objective function
obj_prog = solver.Objective()
obj_prog.SetCoefficient(vara, 3)
obj_prog.SetCoefficient(varb, 2)
obj_prog.SetCoefficient(varc, 2)

obj_prog.SetMaximization()
#printing segment of program
print('Max Value = %d' % solver.Objective().Value())
print()
for variable in [vara,varb,varc]:
    print('%s = %d' %(variable.name(), variable.solution_value()))






