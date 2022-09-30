---
toc: true
layout: post
description: Project Purpose and Scrum Methodology
categories: [markdown, APCSP, week 5]
title: Project Purpoes and Scrum Methodology
author: Alex Lu
show_tags: true
comments: true
---

## The Idea

Our team wishes to build a minesweeper game with a python backend that could consistently communicate with our front-end website to bring a new degree of sophistication and aesthetic to this classic Game. This project would be split into two main portions each with it's own challenge. The first portion would be making the game engine in python, while the latter portion would be to design and create an aesthetically pleasing and functional frontend to display the Game Status

![]({{site.baseurl}}/images/minesweeper_diagram.png "Minesweeper design methodology and interactions")

## The Frontend
The frontend aspect of this project should preferably display a grid of the game and incorporate some aspect of user input. Preliminary testing and experimentation could be done through textbox inputs of coordinate values, while prospective functions could include individual buttons on the Grid itself to provide a GUI for the user to interact with. In both cases, the frontend should be able to communicate with the python backend through JSON data to send and receive data.  

More aspects about the Frontend aspects will be added with additional planning in the future.



## The Backend
Arguably the more challenging half of this project, the backend would primarily serve to be the game engine of the minesweeper game. Additionally, the backend would also control and organize the various pages and menus on the website. In this writeup, we will only be focusing on the main goals and challenges faced by the Backend team.

1. Using Object Oriented Programming to create individual objects for the game. Some aspects that could be represented by such objects would be the gameboard and also the individual cells and nodes present within the game board.
    1. Doing so would simplify the algorithmic aspect of the game, as the board itself could have methods and attributes to help control the game logic. 
    2. Morever, using an object to represent an individual cell in the board would provide greater functionalities than just using a single variable  
2. Use Enumerated types with the python `enum` module to create different values for the type and status of each node. Each of these types could then be bound to a constant value which could then be printed on the screen

3. Use Recursion to create an algorithm to recursively detect adjacent cells that are safe (AKA not mines). This algorithm would work in the following format
    1. Maintain a list of current cells already determined to be safe
    2. Verify if the four adjacent (up, down, left, right) cells next to the selected cell are safe or not, if safe, store the coordinate point in the list, if not, record the cell as a "border cell", terminate the recursive process, and run another helper function to determine the precise number of mines surrounding the cell
    3. Re-call the function for each of the surrounding adjacent cells to identify other consecutive cells who are safe.
    4. Return a list of the coordinates of a contiguous block of safe cells
    5. Mark the cells to be safe and calculate number of surrounding mines for border cells.

4. Verify the Game status, Game is won if:
    1. All mines are flagged
    2. All safe cells are cleared
    Game is lost if:
    1. A mine was dug by the user

5. Return the final result back to the front end. If a safe cell was dug, send out a JSON containing an array of the coordinates of the cell and it's safe neighbors. If a mine was dug, send a JSON containing a boolean value to signify the end of the game. 

## The Scrum Process

![]({{site.baseurl}}/images/scrum_methodology.png " ")
