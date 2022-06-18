from Gridworld import Gridworld

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

    print(transition_probs)
