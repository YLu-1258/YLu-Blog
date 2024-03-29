---
toc: true
title: Collegeboard Grading part 1
layout: base
description: Grading the collegeboard create performance tasks
categories: [markdown, APCSP, Tri2]
tags: [markdown, APCSP, Tri2]
---

## Cross-grading of submission 1  
The theme of this submission was to create a program that returns the type of a triangle based on it's side lengths, as well as the various trigonometric ratios of the triangle's 3 angles.

### Analysis:  
<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>0/1</td>
    <td>The video response does a good job of showing the input, functionality, and output of the program, and while the written response explains the functionality of the program (What the program does), it does not explina the purpose of the program (Why the progra was created or the problem it intends to solve)</td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response  does include the usage of a list, it's name, and the purpose it serves, but the list used ultimately does not serve to reduce complexity or serve the functionality of the program. The programmer could've just returned literal strings rather than individual list indicies and such.</td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>0/1</td>
    <td>While the program does include the usage of a list, it does not make sense to store all possible outputs of a program in such a structure. It would be much more simpler had the individual return statements been stored as simple strings and such, making it easier for debugging</td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The student has created a function that takes in 3 parameters, that returns the overall ratio of the triangle's sides, which is eventually stored within a varaible for future use and printing. This function is shown to be functioning based on the data inputted in the video.</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a for-loop to iterate over a range of integers, while selecting specific values from a premade list to output triangle types in the code. The code also follows a clear sequence, where each line is dependent on data or manipulation made in previous lines.</td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different input sets, one of integers and one of floats. The written response then goes over the conditional in the <mark>ratioCalculate</mark> function, which analyzes the the numbers to see if any are factors of others. Finally, the code returns the correct expected outputs, even having the floats converted into an integer ratio.</td>
  </tr>
</table>




## Cross-grading of submission 2
The theme of this submission was to create a program that can simulate conway's game of life, using the scratch block coding language to achieve their goal.

### Analysis:  

<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>1/1</td>
    <td>The video response does a good job of showing the input, functionality, and output of the program, which was the user inputed set of pixels, and a set of conditionals to execute the necessary operations, and a final replacement of the previous board as the output of the program. Moreover the function and purpose was clearly stated in the written response, which was to create a program to simulate conway's game of life for the user's entertainment</td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response  does include the usage of a list, it's name, and the purpose it serves. The list is in the form of a grid, and from the looks of it, a two dimentional one given the x and y coordinate inputs used to access each individual element. The written response also shows how the grid is later used in the `cellCheck` function in order to execute the rules of the game of life. Moreover, it seems the list itself is named as `currentGrid` and consists of boolean values of 1 (clicked) and 0 (not clicked)</td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response gives a detailed yet concise explaination as to why the lists used were optimal and even necessary for program function. This is because since Conway's game of life is a very graphical game, it requires some form or method to be able to store the status of each individual cell in order to run the simulation. In this case, using a list consolidates all the required data of the cells in a single variable name, rather than using thousands of individual variables or some other complex data structures to accomplish (like a graph or something similar)</td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse very clearly indicates a function that takes in 2 lists as input and updates the current list with the predicted output in order to display the output that the user expects to see. This function is later called within the `Newgen` function satisfying the requirements for this row.</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a for-loop to iterate over the range of their gird, while smaking specific selections with their nested if and else conditionals. By doing so, the program could then correctly identify which list to copy to which list, making the overal program functional yet efficient.</td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different input sets, one of the beginning inputted grid frame and the currently displayed frame, and the other of the current grid and the next grid. This is clear demonstration of good testing as both inputs give the proper desired results, as the first test represents the beginning of the game as the board is generated and passed along to the current grid, while the second function shows the progression of the game from one frame to the next.</td>
  </tr>
</table>
