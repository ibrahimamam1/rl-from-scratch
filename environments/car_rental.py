import numpy as np
import math 

class CarRentalEnv:
    def __init__(self):
        self.n_cars = [10, 10]  #initially 10 cars at each location
        self.actions = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] #can move 0-5 cars overnight. sign indicated direction of moving
        self.rent_lambda1 = 3
        self.rent_lambda2 = 4
        self.return_lambda1 = 3
        self.return_lambda1 = 2
    
    def _get_state(self):
        return self.n_cars

    def _get_actions(self):
        return self.actions 

    def _get_transition_probability(self, state, action, next_state): # assuming cars are only rented and never returned 
        n1 = abs(state[0] - next_state[0]) #how many cars were rented at location 1
        p1 =  ((self.rent_lambda1**n1) / math.factorial(n1)) * math.exp(-self.rent_lambda1)

        n2 = abs(state[1] - next_state[1]) #how many cars were rented at location 2
        p2 =  ((self.rent_lambda2**n2) / math.factorial(n2)) * math.exp(-self.rent_lambda2)

        return p1*p2 

    def reset(self):
        self.n_cars = [10,10]

    def step(self, action):
        pass 
    
    @property
    def n_states(self):
        return 
    
    @property
    def n_actions(self):
        return 11
