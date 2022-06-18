from Gridworld import Gridworld

def print_values(V, g):
  for i in range(g.rows):
    print("---------------------------")
    for j in range(g.cols):
      v = V.get((i,j), 0)
      if v >= 0:
        print(" %.2f|" % v, end="")
      else:
        print("%.2f|" % v, end="") # -ve sign takes up an extra space
    print("")

def print_policy(P, g):
  for i in range(g.rows):
    print("---------------------------")
    for j in range(g.cols):
      a = P.get((i,j), ' ')
      print("  %s  |" % a, end="")
    print("")

if  __name__ == '__main__':
    transition_probs = {}
    rewards = {}

    grid = Gridworld()
    for i in range(grid.rows):
        for j in range(grid.cols):
            s = (i,j)
            if not grid.game_over():
                for a in grid.actions:
                    s2 = grid.get_next_state(s, a)
                    transition_probs[(s,a,s2)] = 1
                    if s2 in grid.rewards:
                        rewards[s,a,s2] = grid.rewards[s2]

    ### fixed policy ###
    policy = {
        (2, 0): 'U',
        (1, 0): 'U',
        (0, 0): 'R',
        (0, 1): 'R',
        (0, 2): 'R',
        (1, 2): 'U',
        (2, 1): 'R',
        (2, 2): 'U',
        (2, 3): 'L',
    }

    print_policy(policy, grid)