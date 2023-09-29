// Define the game variables
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

// Define the game objects
var player = {
  x: 100,
  y: 100,
  speed: 5
};

var obstacles = [
  {
    x: 200,
    y: 200,
    type: "tree"
  },
  {
    x: 300,
    y: 300,
    type: "rock"
  },
  {
    x: 400,
    y: 400,
    type: "water"
  }
];

// Draw the game state
function draw() {
  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw the player
  ctx.fillStyle = "red";
  ctx.fillRect(player.x, player.y, 10, 10);

  // Draw the obstacles
  ctx.fillStyle = "green";
  for (var i = 0; i < obstacles.length; i++) {
    ctx.fillRect(obstacles[i].x, obstacles[i].y, 10, 10);
  }
}

// Update the game state
function update() {
  // Move the player
  player.x += player.speed;
  player.y += player.speed;

  // Check if the player is hitting an obstacle
  for (var i = 0; i < obstacles.length; i++) {
    if (player.x === obstacles[i].x && player.y === obstacles[i].y) {
      // If the player is hitting an obstacle, move them back to their previous position
      player.x -= player.speed;
      player.y -= player.speed;
    }
  }
}

// Game loop
function gameLoop() {
  // Update the game state
  update();

  // Draw the game state
  draw();

  // Request the next animation frame
  requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();


// Add keyboard controls
addEventListener("keydown", function(event) {
  switch (event.keyCode) {
    case 37: // Left arrow
      player.speed -= 1;
      break;
    case 38: // Up arrow
      player.speed -= 1;
      break;
    case 39: // Right arrow
      player.speed += 1;
      break;
    case 40: // Down arrow
      player.speed += 1;
      break;
  }
});
