---
layout: post
title:  "Six months at GDS"
date:   2014-08-07 12:29:21
category: "kitchen drawer"
---
I've been at the Government Digital Service for over six months now, I was thinking about all the stuff I've learnt in that time. It's a lot! I was also reading the week-notes I took when I first joined. I don't think I ever planned to make these public, but they feel so weird and far away from me now I feel OK sharing them. Here's the first paragraph I wrote about the first day of work:

> On Monday I thought I might cry. I felt really completely overwhelmed in a way I don't think I've ever felt before. There are so many people at GDS and they were all talking about things I didn't understand. [...] When I got home from work I cried for about an hour and then [my boyfriend] rescued me.

Not the most auspicious start. Next:

> I tried to set up my computer and read the vast amount of Civil Service crap that people kept emailing me. A particular highlight was: "All desktop backgrounds should be approved by your line manager".

By Tuesday I had figured some stuff out:

> I realised I was going to have to get over my fear of the kitchen, which is about 5 times too small for the office and proved as a major source of anxiety for me on the first day as I felt like I was in constantly getting in somebodies way as I tried to get to the fridge / sink / water cooler.

I was afraid of the *kitchen*? Seriously? I don't even remember that. By Thursday, things are looking up:

> Thursday was also cool because I got to sit next to Edds who is excellent and has the weirdest laugh ever.

It's funny to read all that stuff I wrote in Week 1. How quickly you forget what it's like to be new. On to Week 2:

> This week was better than last, I really didn't want to go to work on Sunday night, I had a full on impostor syndrome melt-down which [my boyfriend] helped me out with but it was a bit wimpy and sad.

By week three things have settled down and I'd started getting those weird insights that new people give you about yourself

> Elliot has pointed out a few times that I am very dead-pan. Which I knew but it's funny when new people tell you things about yourself isn't it?

At this point the week-notes stop. Things felt generally less traumatic by week three, my memories of them are permeated by a lot less dread, anyway. All that feels very far away now, I've settled in and it's easy to forget how tough being new is.

## So, after six months, what have I learnt?

Gosh! So many things. Allow me to list four of them:

1. __*Feature branches are cool but you gotta think from the pull request backwards*__.
  Coming from a company of four developers, there wasn't really any process for getting code deployed. You wrote it, you committed it to master, you deployed it. Well, GDS has about 50 developers working across a huge codebase of apps talking to other apps, it's massive. You can't just make a code change and punt it out there, it has to be reviewed. When you're writing code that's going to go through a code review you do well to plan it from the pull request backwards. Use lots of commits. Guide people through your thought process with the code changes. Obviously your commit messages are going to describe what you did and why. Why is really important. [The Alphagov repo has a pretty sensible set of guidelines](https://github.com/alphagov/styleguides/blob/master/git.md)
2. __*Coding in the open is terrifying, but great*__.  
If you have even a modest amount of self doubt, the prospect of all of your work being completely public should terrify you to begin with. It terrified me. I fretted endlessly over it. Overthinking every single decision I made in code. Six months on, I'm better at this, I put stuff in pull requests that I know isn't perfect, because nothing is perfect. Really what you're aiming for is some collective level of OK-ness. Someone told me "think of the pull request comments as a to-do list" rather than a list of every single thing you cocked up, with which to flagellate yourself. This helps me now, but it took a long time to sink in. As a result, if I'm giving feedback on a pull request, I always go find the person first and check how they'd best like the feedback, sometimes I'll offer to pair with them on it, or email them feedback privately. I think it's polite to give people options.
3.  __*It's brilliant having permission to support everyone*__.  
When your user population is an entire country, you have to think of everyone. This is a brilliant challenge for a front-end dev to have, and it's great to have permission take it on. In the private sector sometimes you have to be pragmatic about the time you give to supporting legacy browsers/users with diverse needs. Maybe you have a small homogeneous user group and a lot of pressure on your time, so supporting the users you have becomes priority number 1. At GDS we have a massive userbase which is as diverse at the UK is, and we don't want any user to be left behind.
4. __*User researchers are the best!*__  
Here's another thing I'd never come across before GDS, user research. Like, proper, record them using your stuff, ask them questions, study the results, user research. Again, coming from a company of less than 20 people, we didn't really have the time or the inclination to do user research, but I can't imagine GDS without it. It is baked into everything here and it makes the things we are building so much better.


Those are the four main things. It's amazing how much hanging out with a bunch of really smart helpful people can help you improve. I'm looking forward to learning a tonne more in the next six months (and beyond). As they say at GDS, Onwards!
