---
toc: true
layout: post
description: APCSP Lecture 3
categories: [markdown, APCSP, week 1]
title: Intro to Python Lecture
author: Alex Lu
show_tags: true
comments: true
---

## Lecture - 08/25/2022

To build up a relationshhip with my partner, I should comment in his <a href="https://chewyboba10.github.io/sushi-burrito/"><mark>blog</mark></a> and also open up review tickets to communicate with him

When working with others, always **pull** before you make any additions, this ensures that we are on the latest version and that there are no difference conflicts.

There are multiple "**shells**" installed on a linux machine, such as **bash**, **dash** and **zsh**. The commands that we enter into terminal are like a pseudo-language. We can create bash scripts to automate actions in terminal for us.

### Bash - Analyzing part 1
```bash
cd $project #cd means "Change Directory", $project is a variable named project
ls          # lists directory
ls -a       # lists directory with hidden files
ls -al      # lists directory with hidden files in long format
```

By using bash we can easily create scripts that automate terminal operations for us.

### The Cloud
The cloud contains all git repositories. Individual computers can clone repositories from the cloud and down to our own SSD. This creates a *link* between our local repository and the remote repository.

A **pull action** will pull any new updates made to the repository down to our local repository and update it with the latest changes.

A **push action** will push any new updates from our local repository up to our remote directory in the cloud and contribute to the git repository.