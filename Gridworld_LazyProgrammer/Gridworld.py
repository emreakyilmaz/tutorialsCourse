class Grid: # Environment
  def __init__(self, rows, cols, start):
    self.rows = rows
    self.cols = cols
    self.i = start[0]
    self.j = start[1]

  def set(self, rewards, actions):
    # rewards should be a dict of: (i, j): r (row, col): reward
    # actions should be a dict of: (i, j): A (row, col): list of possible actions
    self.rewards = rewards
    self.actions = actions

  def set_state(self, s):
    self.i = s[0]
    self.j = s[1]

  def current_state(self):
    return (self.i, self.j)

  def is_terminal(self, s):
    return s not in self.actions

  def get_next_state(self, s, a):
    # this answers: where would I end up if I perform action 'a' in state 's'?
    i, j = s[0], s[1]

    # if this action moves you somewhere else, then it will be in this dictionary
    if a in self.actions[(i, j)]:
      if a == 'U':
        i -= 1
      elif a == 'D':
        i += 1
      elif a == 'R':
        j += 1
      elif a == 'L':
        j -= 1
    return i, j

  def move(self, action):
    # check if legal move first
    if action in self.actions[(self.i, self.j)]:
      if action == 'U':
        self.i -= 1
      elif action == 'D':
        self.i += 1
      elif action == 'R':
        self.j += 1
      elif action == 'L':
        self.j -= 1
    # return a reward (if any)
    return self.rewards.get((self.i, self.j), 0)

  def undo_move(self, action):
    # these are the opposite of what U/D/L/R should normally do
    if action == 'U':
      self.i += 1
    elif action == 'D':
      self.i -= 1
    elif action == 'R':
      self.j -= 1
    elif action == 'L':
      self.j += 1
    # raise an exception if we arrive somewhere we shouldn't be
    # should never happen
    assert(self.current_state() in self.all_states())

  def game_over(self):
    # returns true if game is over, else false
    # true if we are in a state where no actions are possible
    return (self.i, self.j) not in self.actions

  def all_states(self):
    # possibly buggy but simple way to get all states
    # either a position that has possible next actions
    # or a position that yields a reward
    return set(self.actions.keys()) | set(self.rewards.keys())

'''class Gridworld:
    def __init__(self):
        self.rewards = {(0,3): 1,
                   (1,3): -1}

        self.actions = {(0,0): ('D', 'R'),
                   (0,1): ('L', 'R'),
                   (0,2): ('L', 'D', 'R'),
                   (1,0): ('U', 'D'),
                   (1,2): ('U', 'D', 'R'),
                   (2,0): ('U', 'R'),
                   (2,1): ('L', 'R'),
                   (2,2): ('L', 'U', 'R'),
                   (2,3): ('L', 'U')}

        self.curr_loc_x = 0
        self.curr_loc_y = 0

        self.rows = 3
        self.cols = 4

    def current_state(self) -> tuple:
        return (self.curr_loc_y,
                self.curr_loc_x)

    def move(self, action:str) -> int:
        reward = 0

        if action in self.actions[(self.curr_loc_y,self.curr_loc_x)]:
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

    def get_next_state(self, s, a):
        i, j = s[0], s[1]
        if a in self.actions[(self.curr_loc_y, self.curr_loc_x)]:
            if a == 'D':
                self.curr_loc_y += 1
            elif a == 'U':
                self.curr_loc_y -= 1
            elif a == 'L':
                self.curr_loc_x -= 1
            elif a == 'R':
                self.curr_loc_x += 1

        return i, j

    def game_over(self) -> bool:
        if self.curr_loc_y == 0 and self.curr_loc_x == 3:
            return True
        elif self.curr_loc_y == 1 and self.curr_loc_x == 3:
            return True
        else:
            return False

    def all_states(self):
        return set(self.actions.keys()) | set(self.rewards.keys())'''
