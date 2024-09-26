# adventureGame
CS120 Adventure Game 

Define main():
	Run getGame()
	currentNode = "start"
	Run playNode(game, currentNode)
Define getGame():
	No parameters needed
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
      }
	Return game

Define playNode():
	Parameters-game and currentNode
	Extract description, menu1, node1, menu2, node2 from game
	Print menu:
		Description
		1 menu1
		2 menu2
	Get userChoice input
	If userChoice is 1
		newNode gets node1
	If userChoice is 2
		newNode gets node2
	Else:
		print("Choose 1 or 2, you bovine.")
	

