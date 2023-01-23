---
toc: true
title: Collegeboard Grading part 1
layout: default
description: Grading the collegeboard create performance tasks
categories: [markdown, APCSP, Tri2]
tags: [markdown, APCSP, Tri2]
---

## Cross-grading of submission 1  
The theme of this submission was to create a program that displays a set of animals an then prompts the user to remember all animals in a memory gussing game.

### Analysis:  

<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
    <th>Notes/Discrepancies</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>0/1</td>
    <td>The video response does a good job of showing the input, functionality, and output of the program, which displayed a set of animals for the user to remember and eventually input back into the system to test for correctness. However, only the function of the program was stated in the written response, and the purpose of the program was neglected.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response  does include the usage of a list, it's name, and the purpose it serves. The list is in the form of an array that stores the pictures of each individual animal. Moreover, the type of data was clearly stated and the name of the array <code>animalImages</code> was clearly specified.</td>
    <td>This project scored a 0 according to collegeboard scoring guidelines because the submissions failed to include an instance where the list was used in the code to fulfill the program purpose.</td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>0/1</td>
    <td>Although the response explains why a list specifically would serve to manage complexity and imrpove program quality, it does indicate that additional vairables would be used in place of a list, however, it does not show a segment of code that demonstrates how the list was used to manage complexity. </td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse indicates a function that takes in an user quess as input and verifies it with the prior <code>animalList</code> list. This function is also shown to be called within a for-loop that will continuosly check the user's knowledge.</td>
    <td>The collegeboard grader said that the written response did not serve to explain how the particular procedure helped to contribute to the overall functionality of the program</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a for-loop to implement iteration and sequencing. Moreover, the algorithm also uses an if statement to implement selection in the code to determine if the player should gain a point or not.</td>
    <td>The student did not earn the point for this row because they did not explain in detail enough on how the algorithm itself worked so that someone else may recreate it.</td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different guesses, one that's correct, and another one that was false. Moreover, the response clearly details why each response gave their resutls and also properly identified each respective result of the program.</td>
    <td></td>
  </tr>
</table>

## Cross-grading of submission 2
The theme of this submission was to create a program that intakes certain words and ideas inputted by the user and then reassembles such words to eventually peice together a poem

### Analysis:  

<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
    <th>Notes/Discrepancies</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>1/1</td>
    <td>The video response does a good job of showing the input, functionality, and output of the program, created a poem based on a set of words inputted by the user. Moreover, the overall purpose and function of the program was also clearly stated within the written response, aiming to stimulate the creative sides of people by offering a program that can assemble poems for them.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response does include the usage of a list, it's name, and the purpose it serves. The list is in the form of an array that stores the inputs of words from the user, including words descritive of trees, oceans, and the sky. Moreover, the type of data was clearly stated and the name of the array <code>nounList</code> was clearly specified. Additionally, the program also does a good job of utilizing this word list to eventually select words to use in the poem.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response does an excellent job at stating how the usage of the list serves to reduce complexity. The student responds that without the usage of a list, they would likely have to resort to the use of individual variables to store user input, which would not only be cumbersome and produce clutter, but would also be difficult to implement a radomized selection with. </td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse demonstrates excellent usage of a function <code>createPoems</code> in order to generate a string containing all poems demanded by the user. Moreover this function is later used in the program to directly generate a string for printing out the poems. This function also consists of 3 list arguments and 1 boolean (integer) argument to dictate the words to use for generation, and whether or not to include articles in the poem. The students also a does a good job to describe how the algorithm works, and the steps that can be taken to reproduce it</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a while-loop to implement iteration. Sequencing could also be observed in the function as the coutner variable is set before the loop, to generate the correct amount of poems. Moreover, the algorithm also uses an if statement to implement selection in the code to determine if the poem should contain articles or not.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different inputs, one desiring articles in the poem, and another one that does not. Moreover, the response clearly details why each response gave their resutls and also properly identified each respective result of the program. Finally, the student also explicitly cited the line numbers within the code to give a detailed overview of how the program executes.</td>
    <td></td>
  </tr>
</table>

## Cross-grading of submission 3
The theme of this submission was to create a program that intakes a state inputed by the user and outputs certain information concerning that state

### Analysis:  

<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
    <th>Notes/Discrepancies</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>1/1</td>
    <td>The video response does a good job of showing the input, functionality, and output of the program, which had the user input a state and then select different pieces of information to display on the screen. Moreover, the written response also clear documented the purpose (function) of the program was to provide the user with information on a us state, and that the actual purpose was to help with memorization and to learn new things.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>0/1</td>
    <td>The program and response does include the usage of a list, it's name (<code>statelist</code>), and the purpose it serves. However, it does not show how the data is stored within the list. As such, it does not earn the point for this row of the rubric.
    <td>Moreover, the description in the written response for the list was also inaccurate as the list statelist only represents the name of the states.</td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response does an good job at stating how the usage of the list serves to reduce complexity. The student responds that without the usage of a list, they would likely have to code each peice of data independently from each other, resulting in greater code complexity. </td>
    <td>Collegeboard says that the written response does not go a good job of explaining in detail on how the operation would be more complex to store.</td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>0/1</td>
    <td>Although the written reponse demonstrates the usage of a function <code>updatescreen</code> in order to assign an index to each state. This function does not contain any parameters that are passed to it. Thus the program does not earn the point in this row.</td>
    <td>Collegeboard decided that the written response also inaccurately described the main function of the procedure</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>0/1</td>
    <td>The algorithm indicates the proper use of many if statements to implement sequencing and selection. However, the program does not indicate the use of any form of a loop or anything similar to denote a use of iteration in the program.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response shows the results and scenario of the both proceudres to identify that their program works as expected according to the set purpose and function</td>
    <td>The written reponse does not properly show different parameters that are plugged into the procedures. Additionally, it does not describe the result in detail, instead, it only gives a breif overview of what happens on screen instead.</td>
  </tr>
</table>

## Cross-grading of submission 4
The theme of this submission was to create a program that simulates a fishing game to reduce boredom

### Analysis:  

<table>
  <tr>
    <th>Row</th>
    <th>Score</th>
    <th>Explaintation</th>
    <th>Notes/Discrepancies</th>
  </tr>
  <tr>
    <td><strong>Program Function and Purpose</strong></td>
    <td>1/1</td>
    <td>The video response does a good job of showing the input and output of the program, which was to use certain keyboard keys such as a and d to move the boat, and eventually add to a total count of fish if the hook comes into contact with a fish. THe function and purpose were also stated explicity, with the purpose being to reduce boredom, and the function being to simulate a fishing game.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response does include the usage of a list, it's name (<code>fishtypes</code>), and the purpose it serves. The list is in the form of an array that stores the total amount of fish caught by the user. Later, the list is also shown to be used to output the total number of fish of each type caught.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response does an good job at stating how the usage of the list serves to reduce complexity. The student responds that without the usage of a list, they would likely have to resort to the use of individual variables to store each fish and the number of that fish caught, which would not only be cumbersome and produce clutter, but would also be hard to add new fish types in the future. The student also address and refutes the possibility of using individual variables for each type of fish and it's total.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse demonstrates usage of a function <code>clone movement</code> in order to determine the spawning of the fishes including their location, distance, and final position. This function consists of 5 arguments serving to define the range and speed of the fish. The student also explains how this specific helps the functionality of the program as a whole, as it serves to randomly spawn fishes with different attributes to increase the difficulty of the game.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a loop to implement iteration to move the fish clone until it eithe reaches the end of the screen, or is touched by the hook. Sequencing could also be observed in the function as it creates a clone of a fish first before executing the loop and it's following logic. Moreover, the algorithm also uses an if statement to implement selection in the code to determine whether of not if the clone is touching the edge of the screen.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different inputs, one where the clone is touching the right edge of the screen, and another one where it doesn't. Moreover, the response clearly details the results of each procedure. The end results of the program are also the expected results.</td>
    <td>According to collegeboard, this student did not earn the point for this row because they only tested for the alternate code segments, rather than actual arguments, parameters, and inputs into the function itself.</td>
  </tr>
</table>