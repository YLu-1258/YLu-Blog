---
toc: true
title: Computing Bias
layout: post
description: Providing an overview of the effects and implications of computing bias and crowdsourcing data.
categories: [markdown, APCSP, Tri2]
tags: [markdown, APCSP, Tri2]
---

## Big Idea 5.5 Legal and Ethical Concerns

### Types of Licences
There are two main types of Licenses that one can choose to use:
1. **Open Source Licences**: Allow for other people to view, access, and download the source code for a program. permissions may vary amongst some licenses but overalll idea would be the same. Some Open source licenses allow for closed source distribution, others do not.
2. **Closed Source Licences**: Does not allow for other people to access a project or program's source code. Typically the marketer of such a program will release a closed version to the public, and keep the source code for their own development.

### Examples of Licenses
1. Creative Commons Zero v1.0 Universal: Grants most unrestricted usage and rights, for the public domain and the author waives all copyrights to the product.
2. Open Source MIT License: Allows other consumers to freely use the code produced and also release closed source versions. However, in these products, people commonly would be required by the License to give credit to the original author.
3. Open Source GPL License: Allows for viewing and access and most other rights to a project, with the exception of releasing or distributing a closed sourced version of it

### Personal Summary:
- As an individual, I believe that protecting a user's intellectual rights to something that they've made is highly important in ensuring that the right people receive credit for their works. Thus, licenses are really important tools to outline the rights of the creator, as well as the rights of the user to use and access code made by someone else.
- Because of our projected-based learning curriculum, I feel like students should be able to make their projects open-sourced so that other students can view and see what particular edits or changes may be added to address a specfic issue. Moreover, these licenses should also restrict the usage rights of other students, such that they can still view the source code, but not copy it directly and release it for their own work.
- Because many large companies distribute their products amongst a userbase, it is important to create a license to outline the consumer rights of their product, such that they can stil protect their patent rights and earn money.

### Team Selection:
As a team, we decided to pick the GNU GPLv3 License for our project. This is because the license not only allows other students to access our project if they need help, but it also prevents them from directly copying or stealing the code for themselves. We determined that this would thus be the best license type to use for such a school based project.

## Big Idea 5.6 Legal and Ethical Concerns
### Describe PII you have seen on project in CompSci Principles.
Some notable Personal Identifiable Information that I've seen in the class are forms gathering data about name and email. Typically, such information isn't too sensitive, as there can be many people with the same name, and the email address is meant to be shared publically for communication. However, there are more sensitive forms of data stored, such as address and date of birth on some other projects.

### What are your feelings about PII and your personal exposure?
I believe that PII's are an important aspect of our internet activities. Most of our web services rely on such PII's for providing us with the best quality and experience. However, we should also be careful with what we do with PII on the internet. Because some of these data can be identifiable and are highly private to an individual, it would be problematic if such details leaked out into the hands of an attacker.

### Describe good and bad passwords? What is another step that is used to assist in authentication.
A good password typically has met certain criterias that make it harder to brute force, such as a set minimum password length (typically 15), a mix of numbers and letters, mixed-cases for alphabetical characters, as well as other special symbols. A bad password would be one that is easily brute-forced or dictionary cracked, because of how commonly used it is or because of the lack of rules imposed on it. There are other certain methdos to help with autneitcation, one being encryption, which could help us to mask and store passwords safely, and the other can be 2FA (Two Factor Authentication), which would require users to verify using another device before granting access.

### Try to describe Symmetric and Asymmetric encryption.
In Symmetric encryption, only one secret key is used to encryot and decrypt encrypted content. However, asymmetric encryption may utilize a pair of related keys, known as public and private keys, in order to     encrypt and decrypt a given piece of information. Thus by virtue, asymmetric encryptio is commonly more secure than symmetric encryption.

### Provide an example of encryption we used in AWS deployment.
An example of an encruption that we used in AWS deployment is SSL encryption, which uses a mix of both symmetric and asymmetric encryption methods. We have also previously generated RSA keys too for our SSH deployment keys when we set up the project.

### Describe a phishing scheme you have learned about the hard way. Describe some other phishing techniques.
While I personally haven't been phished or scammed before on the internet, there are a multitude of other methods that people may use to phish others. For instance, a common way of phishing is to send an email disguised to look like an official email from a company, asking for money or a fee for a service or other business related task. For such instances, the emails are typically misspelled, carrying many other mistkaes within it's subject and body that could be noticed amongst closer inspection. These emails often link to other sites and such that can eventually track and store user inputted data such as paswords and card info, to ultimately scam the user. 