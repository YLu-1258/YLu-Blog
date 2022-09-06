---
toc: true
layout: post
description: 2022-08-31 Lecture - What are HTML fragments and what do they do? 
categories: [markdown, APCSP, week 2]
title: HTML Fragments
author: Alex Lu
show_tags: true
comments: true
---

# HTML Fragments and Markdown
HTML fragments are just a part of the total HTML source on our site.

**Table Fragments**
Fastpages allows to build tables in HTML or Markdown. Everything on the site is built in HTML, the markdown is converted into individual HTML fragments which are assembled to form webpage. Tables that we create and use in markdown are also read, interpreted and turned into html tables. 

tl;dr EVERYTHING ON THE WEBPAGE IS IN HTML

**images**
"<img>" element in HTML
allows us to specify cetain image parameters, more flexible than markdown method.

**links**
"<a>" element with href in HTML

## Web Page Layout
Design themes and layouts of the page.

In the <code>_config.yml</code> page, The theme can be changed with the <code> remote_theme: </code>, which could change the coloration of the text

NOTE: **Fastpages only works with the Jekyll/minima theme, and not with any other theme**

Additional coloration and customization could be attained with the <code>sass</code> (sassy)