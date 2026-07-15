# environments/base_env.py
from abc import ABC, abstractmethod

class BaseEnv(ABC):
    """Base class for all RL environments"""
   
    @property
    @abstractmethod
    def n_states(self):
        """Total number of states"""
        pass
    
    @property
    @abstractmethod
    def n_actions(self):
        """Total number of actions"""
        pass

class ModelBasedEnv(BaseEnv):
    @abstractmethod
    def get_transition_model(self, state, action, next_state):
        """ takes s, a, s' and returns p(s,a,s') and r(s,a)"""
        pass 

class ModelFreeEnv(BaseEnv):
    @abstractmethod
    def reset(self):
        """Reset environment to initial state"""
        pass
    
    @abstractmethod
    def step(self, action):
        """Take action, return (next_state, reward, done, info)"""
        pass
