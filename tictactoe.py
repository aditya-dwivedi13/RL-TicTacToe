import numpy as np

class Board:
  def __init__(self):
    self.state = np.zeros((3,3)).astype(int)

  def display(self):
    board = "\n".join(" ".join(row.astype(str)) for row in self.state)
    board = board.replace("0","_")
    board = board.replace("-1","X")
    board = board.replace("1","O")
    print(board)

  def reset(self):
    self.state = np.zeros((3,3)).astype(int)

  def getstate(self):
  	return self.state
  
class Player:
  def __init__(self,type):
    if type == "o" :
      self.value = 1
    elif type=='x':
      self.value = -1

class Game:
  def __init__(self) -> None:
    self.board = Board()
    self.player1 = Player("o")
    self.player2 = Player("x")

  def move(self,player,block,simulate=False):
    block = block-0.001
    x = int(block//3)
    y = round(block%3) - 1
    position = (x,y)
    if simulate:
    	board = Board()
    	board.state = self.board.state.copy()
    else:
    	board = self.board
    if board.state[position] != 0:
      print("Invalid move")
      if simulate:
      	return None
      return "continue"
    else:
      board.state[position] = player.value
      if simulate:
      	return board
      return "play"
  	
  def checkwin(self):
    # checking row wise
    for row in self.board.state:
      if np.sum(row) == 3:
        return 1
      elif np.sum(row) == -3:
        return 2
    # checking column wise
    for col in self.board.state.T:
      if np.sum(col) == 3:
        return 1
      elif np.sum(col) == -3:
        return 2
    # checking the diagonals
    if np.sum(np.diag(self.board.state)) == 3 or np.sum(np.diag(np.fliplr(self.board.state))) == 3:
      return 1
    elif np.sum(np.diag(self.board.state)) == -3 or np.sum(np.diag(np.fliplr(self.board.state))) == -3:
      return 2
    return 0

  def checkdraw(self):
    if np.sum(self.board.state!=0)==9:
      return True
    return False

  def play(self):
    self.board.display()
    turn = 1
    while True:
      if turn==2:
        player = self.player2
      else:
        player = self.player1
      block = int(input(f"Player {turn}: Enter block number: "))
      cmd = self.move(player,block)
      if cmd == "play":
        self.board.display()
        turn = 3-turn
      else:
        continue

      r = self.checkwin()
      if r==0:
        if self.checkdraw():
          print("Draw")
          break
      else:
        print(f"Player{r} Won!!")
        break
if __name__ == "__main__":
  game = Game()
  game.play()