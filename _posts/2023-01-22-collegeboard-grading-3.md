---
toc: true
title: Collegeboard Grading part 3
layout: base
description: Grading the collegeboard create performance tasks
categories: [markdown, APCSP, Tri2]
tags: [markdown, APCSP, Tri2]
---

## Cross-grading of submission 1  
The theme of this submission was to create a program simulates a rock-paper-sicsors game .

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
    <td>The video response does a good job of showing the input, functionality, and output of the program, which prompted the user for either rock, scissors, or paper. However, only the purpose of the program was stated in the written response, and the function of the program was neglected.</td>
    <td>Apparently, the response was detailed enough to include both the function and the purpose.</td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>0/1</td>
    <td>The program and response  does include the usage of a list, it's name (<code>RPS</code>), and the purpose it serves (seving as random set of input for the computer), but the does not show how the data within the list is being used in the program.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>0/1</td>
    <td>Although the response explains why a list is used within the program, it does not indicate why the usage of the list would serve to reduce overall complexity in the program. Instead the response only gives a brief overview of what can be used in place of a list, and not how that particular replacement is not as optimal as the current usage of a list.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse indicates a function that takes in an user input and compares it with a computer move thorugh the <code>rpsGame</code> function. This function serves to output different results based on the computer and user inputs..</td>
    <td>The collegeboard grader said that the written response did not serve to explain how the particular procedure helped to contribute to the overall functionality of the program,m and was way too vague in stating how it allowed for the program to execute smoothly.</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a recursive function call to implement iteration and a logical sequence of code to demontrate sequencing. Moreover, the algorithm also uses a if statements to implement selection in the code to determine if the player won against the computer or not.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different guesses, one comparing the user's guess of rock with the computer's guess of paper, and another one that was the opposite of the former inputs. Moreover, the response clearly details why each response gave their resutls and also properly identified each respective result of the program.</td>
    <td></td>
  </tr>
</table>

## Cross-grading of submission 2
The theme of this submission was to create a program that challenges the user to a 5-word hangman game to help them recognize new words and to expand their vocabulary

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
    <td>The video response does a good job of showing the input, functionality, and output of the program, challenging the user to a game of hangman by selecting a word and taking in user inputs to judge whether or not a correct guess was found. Moreover, the overall purpose and function of the program was also clearly stated within the written response, aiming to improve people's ability tp recognize new words and to expand their vocabulary.</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response does include the usage of a list, it's name, and the purpose it serves. The list is in the form of an array that stores the individual letters of a word (<code>letOfGuessWord</code>), which allows for the program to perform future comparisons. Moreover, the written response also very clearly shows the list being used in the program to fullfil it's purpose in successful program execution</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response does an excellent job at stating how the usage of the list serves to reduce complexity. The student responds that without the usage of a list, they would likely have to resort to the use of individual variables to store each individual letter, which would not only be cumbersome and produce clutter, but would also be annoying to implement an iterative method to check if there was a match. </td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse demonstrates excellent usage of a function <code>guessWords</code> in order to compare the user inputted word against the randomly selected word by the program itself. This function also consists of 1 string argument to represent the user's letter guess at the hidden word, and checks each index of the word list to find a match for the letter. The students also a does a good job to describe how the algorithm works, and the steps that can be taken to reproduce it</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a for-loop to implement iteration, in order to properly check over each letter in the hidden word. Sequencing could also be observed in the functio, and selection is also implemented to check whether or not if there was a match in the letter and the word, and if the total number of lives is greater than 0. If the total number of lives was found to be equal to 0, the game will end and a losing screen will be displayed</td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different inputs, one containing the number "1" that is not in the test string "hello", and another containing the letter "h" that is found in "hello". Moreover, the response clearly details why each response gave their resutls and also properly identified each respective result of the program. Finally, the student also explicitly cited the line numbers within the code to give a detailed overview of how the program executes.</td>
    <td></td>
  </tr>
</table>

## Cross-grading of submission 3
The theme of this submission was to create a program that intakes a state inputed by the user and outputs certain information concerning that state.

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

## Cross-grading of submission 4:
The theme of this submission was to create a program that simulates a fishing game to reduce boredom.

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