---
toc: true
layout: post
description: The quiz I made on code.org app lab
categories: [markdown, APCSP, week 2]
title: Applab Quiz Write up
author: Alex Lu
show_tags: true
comments: true
---

## What is AppLab?

> App Lab is a programming environment where you can make simple apps. Design an app, code in JavaScript with either blocks or text, then share your app with Teacher or Student Peers. The big limitations of App Lab, that makes it simple, is that the HTML and CSS are not available to developer/student coder, thus it is not directly transportable to an independent Web server.

[Code.org](https://studio.code.org/users/sign_up) account created. To create a new project, click on the AppLab section on the main page.

The block code used in code.org AppLab is a simplified version of the JavaScript language. Click on the Show Text button to edit the code directly.

### Plan for the Quiz (Design)

✔️ Verify answer 

✔️ Inccorect Answer Screen

✔️ Counter to keep track of incorrect account

✔️ Variable to keep track of current problem

✔️ Free Response question prompts

Link to the [quiz](https://studio.code.org/projects/applab/oI46BLVP4jwiNm8q6-bFXH3GEBLM7W_65_0X7krViUo)

![]({{site.baseurl}}/images/app_lab_quiz.png "Picture of the quiz home")


### Successes
- Was able to create a quiz where one screen was able to dynamically able to backtrack to the previous answer.
- Free response input is now also supported by the quiz.
- Background counter helps to keep a track of the number of inccorect attempts made.
- Free response questions can accept multiple different forms of input.

### Discoveries / Challenges
- Realized that you can convert between Int and string types with the `toString()` function.
- Struggled to find a way to concatenate strings and integers but then found about about the `concat()` function.
- The score box seemed to reset, realized that I just made the text box too small :/