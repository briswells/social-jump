//This will draw the levels and animate the charactors movements based on whats return from the controller class
var can = document.getElementById('game');

var ctx = can.getContext('2d');

can.width = 800;
can.height = 400;

var background = new Image();
var runnerSprite = new Image();
var yPos = 272;
var xPos = 70;
background.src = "background.jpg";
runnerSprite.src = "runnerSmall.png";

window.onload = function() {
    // the initial image height
    var backgroundY = 0;
    var backgroundX = 0;
    var tick = 0;
    // the scroll speed
    // an important thing to ensure here is that can.width
    // is divisible by scrollSpeed
    var scrollSpeed = 8;

    // this is the primary animation loop that is called 60 times
    // per second
    function loop()
    {

        ctx.drawImage(background, backgroundX + can.width, backgroundY);
        ctx.drawImage(background, backgroundX, backgroundY);
        runner(tick, xPos, yPos);
        // draw image 1

        // draw image 2


        // update image width
        backgroundX -= scrollSpeed;
        tick += 1;
        // reseting the images when the first image entirely exits the screen
        if (backgroundX == -800)
            backgroundX =  0;

        if(tick == 16){
          tick = 0;
        }

        // this function creates a 60fps animation by scheduling a
        // loop function call before the
        // next redraw every time it is called
        window.requestAnimationFrame(loop);
    }

    // this initiates the animation by calling the loop function
    // for the first time
    loop();


}

function runner(tick, xPos, yPos){
      var width = runnerSprite.width/4;
      var height = runnerSprite.height/4;
      var sy = Math.floor(tick/4)*height;
      var sx = Math.floor(tick/4)*width;
      ctx.drawImage(runnerSprite, sx, sy, width, height, xPos, yPos, width, height);
    }
