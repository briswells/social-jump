// Handle the users input
var controller = new Controller();

// Handles the window/camera
var display = new Display();//add vars probs based on user window

//Game logic
var game = new Game();

//will setup web sockets and handle all the interations with the server
var server = new Server();

//engine, were all 3 above classes get combined
var engine = new Engine();
