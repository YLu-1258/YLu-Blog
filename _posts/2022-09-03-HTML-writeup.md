---
toc: true
layout: post
description: HTML write up on changing Jekyll theme 
categories: [markdown, APCSP]
title: HTML writeup
author: Alex Lu
show_tags: true
comments: true
---

# Changing theme to Jekyll Midnight
The overall theme of the blog could be changed under the `_config.yml` file in the home directory of the blog. One can either edit the `theme` key pair value, or the `remote_theme` keypair value. However, the latter option must have the value `jekyll-remote-theme` defined under the `plugins key`. I decided to use the midnight theme becuase it looks cool as heck.

However, the first major problem I ran into was a porblem with my jekyll build, looking closer at the error message, I realized that there was a "Download Error", presumably some problems occured while trying to install the new midnight theme. 

![]({{site.baseurl}}/images/Jekyll_midnight_error.png "https://github.com/YLu-1258/YLu-Blog/")

However, after doing some more research, I realized that the version of the theme must be specified with the `@` at the end of the value, I initially didn't supply this value, and thus received the error. After specifying the latest version, The Jekyll build passed, and my blog looked like this:

Top half of blog:
![]({{site.baseurl}}/images/Midnight_theme.png "https://github.com/YLu-1258/YLu-Blog/")

Bottom half of blog:
![]({{site.baseurl}}/images/Jekyll_midnight_bot_theme.png "https://github.com/YLu-1258/YLu-Blog/")

One immediate problems I noticed was that the chagne in theme completely removed parts of my blog's navigation bar, as the tags and lecutre notes tab were no longer present at the top. This finding shows that other Jekyll themes are not fully compatible with the fastpages backend, and that the `minima` theme is prefered for compatibility.