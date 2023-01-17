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
    <td>The video response does a good job of showing the input, functionality, and output of the program, created a poem based on a set of words inputted by the user. Moreover, the overall purpose and function of the program was also clearly stated within the written response, aiming to stimulate the creative sides of peopel by offering a program that can assemble poems for them.</td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response does include the usage of a list, it's name, and the purpose it serves. The list is in the form of an array that stores the inputs of words from the user, including words descritive of trees, oceans, and the sky. Moreover, the type of data was clearly stated and the name of the array <code>nounList</code> was clearly specified.</td>. Additionally, the program also does a good job of utilizing this word list to eventually select words to use in the poem.
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response does an excellent job at stating how the usage of the list serves to reduce complexity. The student responds that without the usage of a list, they would likely have to resort to the use of individual variables to store user input, which would not only be cumbersome and produce clutter, but would also be difficult to implement a radomized selection with. </td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse demonstrates excellent usage of a function <code>createPoems</code> in order to generate a string containing all poems demanded by the user. Moreover this function is later used in the program to directly generate a string for printing out the poems. This function also consists of 3 list arguments and 1 boolean (integer) argument to dictate the words to use for generation, and whether or not to include articles in the poem. The students also a does a good job to describe how the algorithm works, and the steps that can be taken to reproduce it</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a while-loop to implement iteration. Sequencing could also be observed in the function as the coutner variable is set before the loop, to generate the correct amount of poems. Moreover, the algorithm also uses an if statement to implement selection in the code to determine if the poem should contain articles or not.</td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different inputs, one desiring articles in the poem, and another one that does not. Moreover, the response clearly details why each response gave their resutls and also properly identified each respective result of the program. Finally, the student also explicitly cited the line numbers within the code to give a detailed overview of how the program executes.</td>
  </tr>
</table>

## Cross-grading of submission 3
The theme of this submission was to create a program that intakes two marvel characters and assign certain attributes to them for the program to ultimately determine which character would win

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
    <td>The video response does a good job of showing the input, functionality, and output of the program, which displayed a pair of marvel characters to test for their respective power levels. However, only the function of the program was stated in the written response, and the purpose of the program was neglected.</td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response does include the usage of a list, it's name (<code>firstCharacterList</code>), and the purpose it serves. The list is in the form of an array that stores the attribute values of each character and the url of that character. Moreover, the list was shown to be accessed by another function within the program, to ultimately calcuate that character's average attribute values.
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response does an good job at stating how the usage of the list serves to reduce complexity. The student responds that without the usage of a list, they would likely have to resort to the use of individual variables to store each attribute value, which would not only be cumbersome and produce clutter, but would also be hard to view as the code would contain multiple refrences to many variables, while with a list approach, the program can simply iterate over that list.. </td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse demonstrates excellent usage of a function <code>findWinner</code> in order to determine the overall winner of the comparison game, and to change the displayed info on the screen. This function consists of 2 list arguments to dictate the statistics and attributes of each marvle character. The students also a does a good job to describe how the algorithm works, and the steps that can be taken to reproduce it, going over the various cycles completed by the loops and the selections made by the if-else statements.</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a for-loop to implement iteration. Sequencing could also be observed in the function as the average attributes of both characters are calculated before the final comparison between the two. Moreover, the algorithm also uses an if statement to implement selection in the code to determine the final winner of the match. Additionally, the program also contains an edge case where the average attribute values of both characters were equal, displaying a tied screen instead.</td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different inputs, one comparing two inequal characters, and another one that comapres two similar ones. Moreover, the response clearly details why each response gave their resutls and also properly identified each respective result of the program. The student also makes various references to the <code>findWinner()</code> function to state how the if-else statements helps to determine the outcome of the program.</td>
  </tr>
</table>

## Cross-grading of submission 4
The theme of this submission was to create a program that simulates a wordle-esque game by having the user try to guess a word based on how close the spelling is

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
    <td>The video response does a good job of showing the input, functionality, and output of the program, which was to test the critical thinking skills of the player and to ultimately determine if the user-guessed words were correct or not</td>
  </tr>
  <tr>
    <td><strong>Data Abstraction</strong></td>
    <td>1/1</td>
    <td>The program and response does include the usage of a list, it's name (<code>guessess</code>), and the purpose it serves. The list is in the form of an array that stores the user's guesses of each of their tries. Additionally, it should be noted that the list only has the maximum length of 6 to represent the 6 tries that the user has to input their data.</td>
    <td>Collegeboard states that only the length of the array is being accessed, and not each individual element within the list, thus not meeting all of the requirements in this row</td>
  </tr>
  <tr>
    <td><strong>Managing Complexity</strong></td>
    <td>1/1</td>
    <td>The written response does an good job at stating how the usage of the list serves to reduce complexity. The student responds that without the usage of a list, they would likely have to resort to the use of individual variables to store each attribute value, which would not only be cumbersome and produce clutter, but would also be hard to calculate the overall number of guess that the program already had. However, the student failed to consider the implmentation of a counter variable to address this issue.</td>
    <td>Collegeboard stated the same reasoning as I did, that the student can just use a counter to keep track of the number of guesses, but instead gave this row a 0/1</td>
  </tr>
  <tr>
    <td><strong>Procedural Abstraction</strong></td>
    <td>1/1</td>
    <td>The written reponse demonstrates usage of a function <code>isitcorrect</code> in order to determine whether or not the user inputted choice was a correct one. This function consists of 1 argument <code>checkanswer</code> to dicate the answer that needs verification. The student also explains how this specific helps the functionality of the program as a whole, as it reduces the action of checking an answer down to a single procedure that can be called many times over.</td>
  </tr>
  <tr>
    <td><strong>Algorithm Implementation</strong></td>
    <td>1/1</td>
    <td>The algorithm indicates the proper use of a loop to implement iteration to check the status of each letter in the player's guess. Sequencing could also be observed in the function as it implements a counter variable to keep track of the current letter to check before iteration. Moreover, the algorithm also uses an if statement to implement selection in the code to determine the end output of the letter, either correct, not in the right place, or not in the word. Additionally, the program also determines when the win/loss screen shows up.</td>
  </tr>
  <tr>
    <td><strong>Testing</strong></td>
    <td>1/1</td>
    <td>The written response clearly shows the inputting of two different inputs, one comparing a letter in the right locations, and another one that comapres an existing letter in the wrong location. Moreover, the response clearly details why each response gave their resutls and also properly identified each respective result of the program. The end results of the program are also the expected results</td>
    <td>According to collegeboard, this student did not earn the point for this row because they only tested for the conditions that would control their program, rather than actual arguments and inputs into the function itself.</td>
  </tr>
</table>