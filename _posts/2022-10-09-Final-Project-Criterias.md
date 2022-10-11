---
toc: false
layout: post
description: The 6 collegeboard criterias and our project
categories: [markdown, APCSP, week 7]
title: 6 Collegeboard Criterias
author: Alex Lu
show_tags: true
comments: true
---
## Collegeboard's 6 Criterias
What are we aiming to accomplish?

### Program Purpose & Function

- An online single-player minesweeper game that can be played anywhere, anytime  
- Users could choose to store data such as high scores (minimum number of moves or time) if they wish.

### Data Abstraction
- Using the `sqlite3` library on python to store user names and each user's corresponding information, such as high-score
- Using python lists to store the state of the game, what nodes or cells are revealed, flagged, hidden, etc.
- Creating a main class for the game and then establishing a constructor that initializes other object attributes for the main game to access or manipulate.

### Managing Complexity
- Maintaining user data in a organized manner with software like databases (SQL).
- Using loops to reduce repetitive code / allow for a dynamic number of times for the execution of our code.

### Procedural Abstraction
- Establishing a set of enumerated types to link certain values with constants. 
    - Used to established the different states of a node or the particular status of that cell.
- Using a main class to cover the Minesweeper Game:
    - The class will contain a constructor, attributes, and methods to ensure smooth gameplay.
    - This will simplify the programming process too as each individual method under the class will "inherit" the attributes of the class. This expands the scope of our functions sort of "links" them together. (Methods work in harmony with each other)
- Creating templates for SQL queries, JSON queries, and also html pages to reduce the amount of manual programing required

### Algorithm Implementation
- Maintain a clear-board at the begining of the game. On the first input (click) from the user, start randomly generating `N=(M//3)` number of mines, where M is the total number of mines. 
    - Use the `random` module to generate a set of integers within the bounds of the array, generate two integers from each mine to indicate the row or coloumn coordinate. Finally, add both generated values into a tuple which will then be appended to a list containing all of the mine coordinates.
    - AS OF **10/10** Consider using the `RapidAPI minesweeper API` to generate a board. (However this limits our flexibility as the first mine clicked might be an actual mine, leading to an inevitable loss).
- Use an overall gameloop that checks the status of the game on each "turn of the game" (iteration of the game).
    - If `gameOver == true`, signify that the game is over
        - Use control flow statements such as if-else-elif to determine wether or not a user has clicked on a mine. If yes, set `gameOver` to `true`, if not, continue with the current iteration of the loop. 
        - Based on the current state of the board, if there are no mines left, return a win screen. If there are mines left, assume that the player clicked on a mine and return a lose screen.
- Within each iteration, prompt the user to input a coordinate point (When testing, use terminal input with standard `(x,y)` input, for the final product, clicking each cell should return a coordinate automatically to the python backend).
    - **Hard part is detecting a nearby "safe grid" for each mine clicked, while subsequently revealing all the mines in the safe grid**
    - We have decided to use a **recursive** approach to resolve this problem. The recursive approach will store a list of safe mines. It will first append the mine clicked by the user (assuming that the mine passes the safe check). Following this, the algorithm will then check the `(r+1,c), (r+1,c-1), (r+1,c+1), (r,c-1), (r,c+1), (r-1,c), (r-1,c-1), and (r-1,c+1)` coordinates to determine wether or not surrouding cells are safe or not. Recursively execute the same process for each the 8 mines adjacent to the initial cell and stop until an "edge-mine" is reached.
- Communiate user input and program output via JSON queries between the python backend and the HTML/CSS/JS frontend.

### Testing Code
- For testing our code, we will primarily experiment with our code either in linux for python programs, or in the browser for frontend testing.
- We will make use of `print()` and `Console.log()` statements to help with debugging.
- Certain events in python could be made easier if we used `try/except` exceptions to catch errors.