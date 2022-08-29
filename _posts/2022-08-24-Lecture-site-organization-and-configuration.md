---
toc: true
layout: post
description: APCSP Lecture 2
categories: [markdown, APCSP]
title: 08/24/2022 Lecture
author: Alex Lu
show_tags: true
comments: true
---
## Lecture - 08/24/2022

### Using documents as blog posts
To import past assignemnts and documents from document-based editors such as word and google docs, we can import such files as `.docx` documents and place them under the `_word` subdirectory in our blog. 

NOTE: Doing so **does not** keep the formatting of the document, any font colors, size, styling is not preserved, additionall work with CSS is required for original effects.

### Blog Front-Matter
Each markdown or jupyter post contains a set configurations at the head of the file known as **Front-Matter**
Front-matter settings are seperated into two main groups, **keys**, and **values**.
> **keys**: The name of the configuration or setting we wish to edit
> **value**: The value or data we grant to a specific configuration

**IMPORTANT**: It is crucial to always pair a key with a value, a blank value on the key overwrites the default value, making the key take on a null value and breaking the front-matter
To define front matter in *markdown*, use the following format
<code style="display: block; white-space: pre-wrap;">   ---
    toc: true
    layout: post
    description: APCSP Lecture 2
    categories: [markdown, notes]
    title: 08/24/2022 Lecture
    author: Alex Lu
    show_tags: true
    hide: true
    comments: true
    ...
    ---
</code> 

To define front-matter in *computational notebooks*, use the following format
<code style="display: block; white-space: pre-wrap;">   # Jupyter Notebook Demonstration
    > My first Jupyter notebook on my blog!
    - toc: true
    - title: First Jupyter Notebook
    - author: Alex Lu
    - badges: true
    - comments: true
    - categories: [jupyter]
</code>

**NOTE:** A title and and description must be specified with the # and > characters respectively, furthermore, each front-matter key and value should be prefixed with a hyphen (-) similar to a markdown list.

### Adding pages on the navbar
If we ever find the need to add a special page on the top of our site in the navbar, simply move the post into the `_pages` directory, and change the front matter key `layout` from `post` to `page`

**NOTE:** setting a table of contents in the front-matter does not work for a page, further tinkering with html is required.

### _config.yml
Most of the blog's default keys and values are defined within the `_config.yml` configuration file in the base directory of the blog.
The values under `_config.yml` are in the standard `key: value` syntax prevalent in most `.yml` files.
NOTABLE KEYS:

| Key | function |
| - | - |
| title | Title of site in upper left hand corner |
| baseurl | The url path to the blog |
| show_description | Display brief description of blog post uner blog lists |
| show_image | Display image on post card |
