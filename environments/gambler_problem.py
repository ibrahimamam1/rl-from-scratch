from environments.base_env import ModelBasedEnv

class GamblerProblem(ModelBasedEnv):
    def __init__(self, p_heads):
        self.p = p_heads #probability of the coin beeing heads 
    @property
    def n_states(self):
        return 101 #gamble can have 0$-100$
    
    @property
    def n_actions(self):
        return 50 #gambler can stake 1$-50$
    
    def get_transition_model(self, state, action, next_state):
        if state == 0 or state == 100:
            if next_state == state:
                return 1.0, 0.0
            return 0.0, 0.0

        max_bet = min(state, 100 - state)
        if action < 1 or action > max_bet:
            return 0.0, 0.0

        #Lost the bet
        if next_state == state - action:
            return 1 - self.p, 0.0

        # Won the bet
        if next_state == state + action:
            # Reward is 1.0 if the win takes the gambler to exactly $100
            if next_state == 100:
                return self.p, 1.0
            else:
                return self.p, 0.0

        # Impossible to reach next state given current state and action 
        return 0.0, 0.0
