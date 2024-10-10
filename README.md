<h1>Tic-Tac-Toe</h1>

This is a text-based Tic-Tac-Toe game implemented in Python. The game allows two players to take turns inputting their moves until there is a winner or the game ends in a draw.

<h2>Prerequisites:</h2>

  - Python 3.6 or higher installed on your system.

<h2>Running the application:</h2>

1- Clone this repository or download the project files.

2- Run the Python script:

  Launch the application by running the following command in your terminal or command prompt:

    python main.py

3- After lauching the app, do the following:

  - After launching, instructions on how to play will be displayed.
    
  - Players take turns marking a spot on the 3x3 grid by entering the position in the format `XY`, where `X` is the row number and `Y` is the column number (both starting from 0).
    - Example: `00` marks to top left spot; `11` marks the center spot.
      
  - The game continues until a player wins by getting three in a row, or the game ends in a draw.

<h2>Code Structure:</h2>

  - `Main Game Loop`: The game runs in a while loop that continues until there is a win or a draw.
    
  - `play()` Function: Handles player input, marking the board with X or O based on the current player's turn. It also validates the input to ensure the move is legal.
    
  - `victory_check()` Function: Checks the current state of the board to determine if a player has won the game by completing a row, column, or diagonal.
    
  - `is_draw()` Function: Detects if the game is a draw by checking if all spots on the board are filled without a winner.
    
  - `tic_tac_print()` Function: Prints the current state of the game board after each turn.

<h2>Example Game Flow:</h2>

   1- The game begins with an empty board.
  
   2- Player 1 (X) selects a position by entering a two-digit number like 00 to mark the top-left spot.
  
   3- The board is updated and displayed.
  
   4- Player 2 (O) then selects a position to mark their symbol.
  
   5- The game checks for a win or a draw after each move.
  
   6- The game continues until either a player wins or there’s a draw.

<h2>License</h2>

This project is open-source and available under the MIT License.

<h2>Contact</h2>

If you have any questions, feel free to reach out to me at yagopais@id.uff.br.
