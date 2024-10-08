"""Marianne Adams
CS120 Adventure Game
A haunted house adventure games with multiple ways to live (or die)."""
def main():
    game = getGame()
    keepGoing = True
    currentNode = "start"
    while keepGoing == True:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playNode(game, currentNode)

def getGame():
    game = {
      "start": ["You are in a haunted house. A ghost approaches you.", "Run away from the ghost.", "run", "Talk to the ghost", "talk"], 
      "run": ["The ghost chases you. You approach a door and a hallway", "Open door", "open", "Run down hallway", "hallway"], 
      "talk": ["The ghost is mad that you had the audacity to talk to them. You die.", "Quit", "quit", "Start over", "start"], 
      "open": ["The door is locked. You have the tools to pick the lock. ", "Pick lock.", "pickLock", "Don't pick the lock.", "doorLock"], 
      "hallway": ["The hallway ends with a set of stairs or a secondary hallway", "Go up stairs", "stairs", "Go down second hallway", "hallway2"], 
      "pickLock": ["You picked the lock! There is a window. ", "Jump out the window. ", "window", "Close the door", "closeDoor"], 
      "doorLock": ["The ghost catches you. You die.", "Quit", "quit", "Start over", "start"], 
      "stairs": ["You are now in the attic. You find the ghost's body.", "Salt and burn the body", "salt", "Do nothing", "nothing"], 
      "hallway2": ["The hallway is a dead end.", "Quit", "quit", "Start over", "start"], 
      "salt": ["This didn't work. The ghost is angry. There is a dumbwaiter elevator.", "Go in the dumbwaiter elevator", "elevator", "Jump out the window", "window2"], 
      "window": ["You escaped. ", "Quit", "quit", "Start over.", "start"], 
      "elevator": ["You are now on the first floor.", "Escape through the front door", "frontDoor", "Taunt the ghost", "taunt"], 
      "window2": ["You fell onto a sharp rock. ", "Quit", "quit", "Start over", "start"], 
      "nothing": ["Why would you do that? The ghost kills you.", "Quit", "quit", "Start over", "start"], 
      "frontDoor": ["You escaped!", "Quit", "quit", "Start over", "start"], 
      "taunt": ["Why would you do that? The ghost kills you.", "Quit", "quit", "Start over", "start"], 
      "closeDoor": ["You forgot the ghost can walk through walls. You die.", "Quit", "quit", "Start over", "start"], 
 }
    return game

def playNode(game, nodeKey):
    currentNode = game[nodeKey]
    (description, menu1, node1, menu2, node2) = currentNode
    print (f"""{description}
    1: {menu1}
    2: {menu2}""")
    userChoice = input("1 or 2: ")
    userChoice = int(userChoice)
    if userChoice == 1:
        currentNode = node1
    if userChoice == 2:
        currentNode = node2
    return currentNode
main()