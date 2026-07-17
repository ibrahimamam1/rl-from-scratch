from environments.base_env import ModelBasedEnv

class CarRental(ModelBasedEnv):
    def __init__(self, p_heads):
        pass
    @property
    def n_states(self):
        return 21**2 #you can have 0-20 cars at each location
    @property
    def n_actions(self):
        return 11 #move -5,-4...,4,5 from A to B  
    def get_transition_model(self, state, action, next_state):
      #handle impossible states 
      #cars will exceed 20 after moving
      s = self.states[state]
      if s[0] + action > 20 or s[1] - action > 20:
          return 0,0
      #mving more cars than avalaible
      if s[0] - action < 0 or s[1] + action < 0:
          return 0,0

      reward = abs(action) * -2

