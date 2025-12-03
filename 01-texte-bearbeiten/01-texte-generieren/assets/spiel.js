const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreElement = document.getElementById('score');
const highScoreElement = document.getElementById('highScore');
const gameOverElement = document.getElementById('gameOver');
const finalScoreElement = document.getElementById('finalScore');
const startBtn = document.getElementById('startBtn');

const gridSize = 20;
const tileCount = canvas.width / gridSize;

let snake = [{ x: 10, y: 10 }];
let food = { x: 15, y: 15 };
let dx = 0;
let dy = 0;
let score = 0;
let highScore = localStorage.getItem('snakeHighScore') || 0;
let gameLoop;
let gameStarted = false;
let gameSpeed = 100;

highScoreElement.textContent = highScore;

// Keyboard controls
document.addEventListener('keydown', changeDirection);

function changeDirection(event) {
  const LEFT_KEY = 37;
  const RIGHT_KEY = 39;
  const UP_KEY = 38;
  const DOWN_KEY = 40;

  if (!gameStarted) return;

  const keyPressed = event.keyCode;
  const goingUp = dy === -1;
  const goingDown = dy === 1;
  const goingRight = dx === 1;
  const goingLeft = dx === -1;

  if (keyPressed === LEFT_KEY && !goingRight) {
    dx = -1;
    dy = 0;
  }
  if (keyPressed === UP_KEY && !goingDown) {
    dx = 0;
    dy = -1;
  }
  if (keyPressed === RIGHT_KEY && !goingLeft) {
    dx = 1;
    dy = 0;
  }
  if (keyPressed === DOWN_KEY && !goingUp) {
    dx = 0;
    dy = 1;
  }
}

function startGame() {
  if (gameStarted) return;

  gameStarted = true;
  startBtn.textContent = 'Game Running...';
  startBtn.disabled = true;

  dx = 1;
  dy = 0;

  gameLoop = setInterval(update, gameSpeed);
}

function restartGame() {
  gameOverElement.classList.remove('show');
  snake = [{ x: 10, y: 10 }];
  food = generateFood();
  dx = 0;
  dy = 0;
  score = 0;
  gameStarted = false;
  scoreElement.textContent = score;
  startBtn.textContent = 'Start Game';
  startBtn.disabled = false;
  clearCanvas();
  drawSnake();
  drawFood();
}

function update() {
  if (checkCollision()) {
    endGame();
    return;
  }

  moveSnake();

  if (checkFoodCollision()) {
    score += 10;
    scoreElement.textContent = score;

    if (score > highScore) {
      highScore = score;
      highScoreElement.textContent = highScore;
      localStorage.setItem('snakeHighScore', highScore);
    }

    food = generateFood();

    // Increase speed slightly as score increases
    if (score % 50 === 0 && gameSpeed > 50) {
      gameSpeed -= 5;
      clearInterval(gameLoop);
      gameLoop = setInterval(update, gameSpeed);
    }
  } else {
    snake.pop();
  }

  clearCanvas();
  drawFood();
  drawSnake();
}

function moveSnake() {
  const head = { x: snake[0].x + dx, y: snake[0].y + dy };
  snake.unshift(head);
}

function checkCollision() {
  const head = snake[0];

  // Wall collision
  if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
    return true;
  }

  // Self collision
  for (let i = 1; i < snake.length; i++) {
    if (head.x === snake[i].x && head.y === snake[i].y) {
      return true;
    }
  }

  return false;
}

function checkFoodCollision() {
  return snake[0].x === food.x && snake[0].y === food.y;
}

function generateFood() {
  let newFood;
  while (true) {
    newFood = {
      x: Math.floor(Math.random() * tileCount),
      y: Math.floor(Math.random() * tileCount)
    };

    // Make sure food doesn't spawn on snake
    const onSnake = snake.some(segment =>
      segment.x === newFood.x && segment.y === newFood.y
    );

    if (!onSnake) break;
  }
  return newFood;
}

function clearCanvas() {
  ctx.fillStyle = '#1a1a2e';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function drawSnake() {
  snake.forEach((segment, index) => {
    // Gradient color for snake
    const gradient = ctx.createLinearGradient(
      segment.x * gridSize,
      segment.y * gridSize,
      segment.x * gridSize + gridSize,
      segment.y * gridSize + gridSize
    );

    if (index === 0) {
      gradient.addColorStop(0, '#4ade80');
      gradient.addColorStop(1, '#22c55e');
    } else {
      gradient.addColorStop(0, '#86efac');
      gradient.addColorStop(1, '#4ade80');
    }

    ctx.fillStyle = gradient;
    ctx.fillRect(
      segment.x * gridSize + 1,
      segment.y * gridSize + 1,
      gridSize - 2,
      gridSize - 2
    );

    // Draw eyes on head
    if (index === 0) {
      ctx.fillStyle = 'white';
      const eyeSize = 3;
      const eyeOffset = 5;

      if (dx === 1) { // Moving right
        ctx.fillRect(segment.x * gridSize + gridSize - eyeOffset, segment.y * gridSize + 5, eyeSize, eyeSize);
        ctx.fillRect(segment.x * gridSize + gridSize - eyeOffset, segment.y * gridSize + gridSize - 8, eyeSize, eyeSize);
      } else if (dx === -1) { // Moving left
        ctx.fillRect(segment.x * gridSize + 3, segment.y * gridSize + 5, eyeSize, eyeSize);
        ctx.fillRect(segment.x * gridSize + 3, segment.y * gridSize + gridSize - 8, eyeSize, eyeSize);
      } else if (dy === -1) { // Moving up
        ctx.fillRect(segment.x * gridSize + 5, segment.y * gridSize + 3, eyeSize, eyeSize);
        ctx.fillRect(segment.x * gridSize + gridSize - 8, segment.y * gridSize + 3, eyeSize, eyeSize);
      } else if (dy === 1) { // Moving down
        ctx.fillRect(segment.x * gridSize + 5, segment.y * gridSize + gridSize - eyeOffset, eyeSize, eyeSize);
        ctx.fillRect(segment.x * gridSize + gridSize - 8, segment.y * gridSize + gridSize - eyeOffset, eyeSize, eyeSize);
      }
    }
  });
}

function drawFood() {
  // Draw apple
  const gradient = ctx.createRadialGradient(
    food.x * gridSize + gridSize / 2,
    food.y * gridSize + gridSize / 2,
    0,
    food.x * gridSize + gridSize / 2,
    food.y * gridSize + gridSize / 2,
    gridSize / 2
  );
  gradient.addColorStop(0, '#ff6b6b');
  gradient.addColorStop(1, '#ee5a6f');

  ctx.fillStyle = gradient;
  ctx.beginPath();
  ctx.arc(
    food.x * gridSize + gridSize / 2,
    food.y * gridSize + gridSize / 2,
    gridSize / 2 - 2,
    0,
    2 * Math.PI
  );
  ctx.fill();

  // Draw leaf
  ctx.fillStyle = '#4ade80';
  ctx.beginPath();
  ctx.arc(
    food.x * gridSize + gridSize / 2 + 3,
    food.y * gridSize + 3,
    3,
    0,
    2 * Math.PI
  );
  ctx.fill();
}

function endGame() {
  clearInterval(gameLoop);
  gameStarted = false;
  finalScoreElement.textContent = score;
  gameOverElement.classList.add('show');
}

// Initial draw
clearCanvas();
drawSnake();
drawFood();