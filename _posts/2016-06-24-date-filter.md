---
layout: post
title:  "A decent attempt at a date filter"
date:   2016-06-24 09:11:27
category: "kitchen drawer"
---
Back when I was at GDS, I worked on a thing that is small but, I don't know, almost perfect&#8253;
It's an input for dates that people can use to filter search results. It's used on a bit of GOV.UK architecture called "Finders". Finders are the technology behind pages like [Competitions and Markets Authority cases](https://gov.uk/cma-cases) or [Air Accident Investigation Branch reports](https://gov.uk/aaib-reports). They're the place you go to look for technical reports about ongoing investigations happening in bits of government. The users of this tool are mostly professionals who need to find and follow these reports. The users have a reasonable degree of technical confidence. I only mention that because the research here is with these users and their needs, so if you're looking at supporting users less familiar with computers then you might be better off doing something else.

I was looking for it the other day; the interesting technical and design bits are all over the place so I thought I'd write it up here.

## Research
We shipped the first version of the date input in public beta and then iterated on it with lab based user research and by examining the logs of search queries.

The first version of this date input was pretty sketchy. It used ruby's Date.parse function and some regex to work around a 'feature' whereby 11/11/90 is parsed as 2090. This worked OKish but it didn't accept dates like "July" or "2010".

Research uncovered a second problem too. We had some help text under the input: 'for example 21/11/2014'. But this text didn't really align with how people wanted to search for dates. In research users revealed that they'd prefer much fuzzier matching like "June" or "06/2010" but thought that the date input wouldn't accept that date because of that label. When we looked at the logs, it confirmed that the majority of people were putting in dates according to the label text suggestion.

You can see the raw data over on the [GDS design hackpad](https://designpatterns.hackpad.com/Dates-vpx6XlVjIbE#:h=Date-patterns-from-users).

## Fixing it
The first thing to do was open up the date label to imply a broader range of date formats. We went with "For example 2008 or 21/11/2014". This isn't perfect but an improvement.

The second thing was to write some code. This is the other thing I feel good about. Using the raw logs and some regex, we were able to construct a test suite for all the dates we would accept. Here's the [Pull request](https://github.com/alphagov/finder-frontend/pull/122) that fixes that all up.

In the end we swapped out reliance on Ruby's Date parsing and used a gem called Chronic instead. The app now accepts any date and passes it to the Chronic gem. Chronic is great but we did have to work around the following problems:

1. Interpreted '2008' to be 20:08 hrs.
2. Barfed on strings like "20 11 16" and 20.11.16
3. Barfed on strings like "20112016". This is probably the right call for chronic, which has to be general purpose. For our use though, we were able to make some more useful assumptions with these kinds of inputs. Once the date has been parsed we return the full unambiguous date to the screen so if users get this wrong they can see.

## And so
This one of the things GDS does extremely well. User research, design and code working together to create something boring but very well formed. They also publish everything with varying levels of certainty and formality on their [hackpad](https://designpatterns.hackpad.com) or in their [service manual](https://www.gov.uk/service-manual).
