import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import matplotlib.pyplot as plt
import numpy as np
from environments.gambler_problem import GamblerProblem
from algorithms.value_iteration import value_iteration

env = GamblerProblem(p_heads=0.25)

policy = np.ones(env.n_states, dtype=int)
policy[0] = 0  # Terminal state
policy[100] = 0 # Terminal state

V, policy = value_iteration(env, policy, gamma=1.0, theta=0.0001)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Plot 1: Value Estimates
ax1.plot(range(env.n_states), V, color='blue')
ax1.set_xlabel("Capital")
ax1.set_ylabel("Value Estimates")
ax1.set_title("Value Function (p_h = 0.4)")

# Plot 2: Final Policy
# A bar chart with width=1.0 looks best for discrete actions
ax2.bar(range(env.n_states), policy, color='gray', width=1.0)
ax2.set_xlabel("Capital")
ax2.set_ylabel("Final Policy (Stake)")
ax2.set_title("Policy (p_h = 0.4)")

plt.tight_layout()
plt.show()
