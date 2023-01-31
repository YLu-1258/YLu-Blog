---
toc: true
title: Individual project Overview
layout: default
description: Providing an overview of the aspects and purpose of my part of the group's CPT plan
categories: [markdown, APCSP, Tri2]
tags: [markdown, APCSP, Tri2]
---

## The Goal:

The end goal of the collegeboard create performance tasks is to challenge students to write a program and expertly explain a wide range aspects convered by the program in complexity management, purpose and functionality, and algorithm implementation. Due to this, we have begun a team project in hopes of practicing such skills. I personally work on one small program of our entire project, but within this sub program still contains all of the required collegeboard aspects.

## The Idea:

For our poject, we are aiming to create a student toolkit website that allows them to compare grades, schedules, and plan their academic activities throughout the day. Although the project seems simple on the surface, there are a lot of intricacies that one might have to consider when approaching such a task. For instance, a crucial part of the project would be managing the overall complexity of the data and the method though which it is stored. For persistent data, we will be using a SQLite3 database to keep track of the user data in the backend, while temporary computational data could be stored in arrays and other abstract data structures (heap, queue, stacks, trees, etc.) for better access and efficiency. There is also the case of computing algorithms that we need to consider, which would be apparent with a larger userbase. We might need to branch out from the naive method and look for certain algorithmic advantages that are present within certain design models but not within others.

## My portion:
My portion of the project is a GPA comparison app. Named "MyGPA", the program serves to reduce the difficulty of calculating one's GPA, as well as providing them with the necessary tools to compute their admissions GPAs for other schools. Another purpose of the program is also to provide an ability for students to compare their Overall GPAs with other students at their schools, through taking the average GPA value of their classes and grade respectively. Such a program would greatly increase the average student's awareness of their academic strength.

## My Write up:
In my write-up, I will first reivew the program's purpose, function and inputs, which is help students gauge their academic prowess, while also serving to help them calcualte their GPA through their inputted grades and such. I will additionally go over the form of data abstraction that I used in the program which would likely be an array or dictionary converted from database schema. I will then explain how such a model serves to reduce overall data complexity within my program. Needless to say, I will also consider the algorithmic implementation of my program and how I could potentially speed up the calculation process for average GPAs, especially when there are millions of potential students and users. To achieve this approach, I might use a dynammic programming model to store past results and upate them accordingly. Finally, I will also be able to test out my program outputs by entering different sets of data, which could be to calculate different types of GPAs and etc.

In the video, I'll be clear to show how the inputs and outputs to my program work together, and how the student is able to compare their GPA to others around them.