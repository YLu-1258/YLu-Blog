---
toc: true
title: MCQ Reflections
layout: base
description: Providing an overview of the problems that I answered incorrectly on the Collegeboard MCQ.
categories: [markdown, APCSP, Tri2]
tags: [markdown, APCSP, Tri2]
---

# Quiz Overview
Overall I scored a 48/50 on this MCQ, which isn't a bad score. However, there are definitely still more places where I can improve and reinforce my knowledge for the class.

![]({{site.baseurl}}/images/Total_Score.png " ")

## Question 30
![]({{site.baseurl}}/images/30.png " ")

On this problem, I incorrectly responded with B and D, when the actual correct answer was B and C. The main issue with me answering this problem wrong was not because of my knowledge, but simply because I was too careless in answering the last few questions. Option D is wrong because although it starts out with the right center coordinates, it starts with an initial radius of 3, but quickly decrements it to 2 for the first circle, which would ultimately scale down the true sizes of the circles. A better option would be choice C, which uses almost the same sequencing, but prints out the circle first before decrementing, which would result in the right response

## Question 33
![]({{site.baseurl}}/images/33.png " ")

On this problem, I failed to recognize that the possible input to the program could be negative. By excluding negative values, I made the erroneous assumption that the given inputs will always be positive numbers, hence always greater than -1, and overwriting the intial value. However, if all inputs were negative values smaller than -1, the first program would return the wrong value as -1 would be greater than all other inpout values, and thus never updated. Thus in this scenario, the program will output -1, the initial condition, instead of the true maximum. I was correct to assume that the other algorithm would work well.