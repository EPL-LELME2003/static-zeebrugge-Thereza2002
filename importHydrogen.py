# Reza Javadian test 2

import pyomo.environ as pyo

# Create a Pyomo model
model = pyo.ConcreteModel()

# Define model parameters
maxVboat = 200000 # m^3

LHV_NH3 = 18.5 # MJ/kg
rho_NH3 = 600 # kg/m^3
loss_NH3 = 0.4 # %
H2_NH3 = 0.18 # t_H2/t_NH3

LHV_CH4 = 18.5 # MJ/kg
rho_CH4 = 600 # kg/m^3
loss_CH4 = 0.35 # %
H2_CH4 = 0.25 # t_H2/t_CH4
CO2_CH4_needs = 2.75 # t



# Define model variables
model.b_NH3 = pyo.Var(within = pyo.NonNegativeReals)
model.b_CH4 = pyo.Var(within = pyo.NonNegativeReals)

# Define the objective functions
##########################################
############ CODE TO ADD HERE ############
##########################################

# Define the constraints
##########################################
############ CODE TO ADD HERE ############
##########################################

# Specify the path towards your solver (gurobi) file
solver = pyo.SolverFactory('/Users/rezajavadian/Documents/gurobi')
sol = solver.solve(model)

# Print here the number of CH4 boats and NH3 boats
##########################################
############ CODE TO ADD HERE ############
##########################################