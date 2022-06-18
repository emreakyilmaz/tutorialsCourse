class Gridworld:
    def __init__(self):
        rewards = {(0,3): 1,
                   (1,3): -1}

        actions = {(0,0): ('D', 'R'),
                   (0,1): ('L', 'R'),
                   (0,2): ('L', 'D', 'R'),
                   (1,0): ('U', 'D'),
                   (1,2): ('U', 'D', 'R'),
                   (2,0): ('U', 'R'),
                   (2,1): ('L', 'R'),
                   (2,2): ('L', 'U', 'R'),
                   (2,3): ('L', 'U')}

        curr_loc_x = 0
        curr_loc_y = 0

    def current_state(self) -> tuple:
        return (self.curr_loc_y,
                self.curr_loc_x)

    def move(self, action:str) -> int:
        reward = 0

        if action == 'D':
            self.curr_loc_y += 1
        elif action == 'U':
            self.curr_loc_y -= 1
        elif action == 'L':
            self.curr_loc_x -= 1
        elif action == 'R':
            self.curr_loc_x += 1


        if self.curr_loc_y == 0 and self.curr_loc_x == 3:
            reward = 1
        elif self.curr_loc_y == 1 and self.curr_loc_x == 3:
            reward = -1
        else:
            reward = 0

        return reward

    def game_over(self) -> bool:
        if self.curr_loc_y == 0 and self.curr_loc_x == 3:
            return True
        elif self.curr_loc_y == 1 and self.curr_loc_x == 3:
            return True
        else:
            return False

