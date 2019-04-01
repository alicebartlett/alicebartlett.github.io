---
layout: post
title:  "Improving our career map for engineers (crosspost)"
date:   2019-04-01 20:40:00
categories: [work, crosspost]
---

_This is a cross post from the [Financial Times Product and Technology Medium](https://medium.com/ft-product-technology/improving-our-career-map-for-engineers-4210185c6246)._

On Monday 18th March we launched the alpha of our new career competencies framework for engineers at the Financial Times. In this blog post I’ll talk about what we did, what we learnt, and what we’re going to do next.

## Our career map for engineers needed an update

In late 2017 we started looking at our career map for engineers. At that time the career map was a spreadsheet with a list of skills against some levels. Because of how Google Sheets works, there were several different versions of these sheets. The one any given engineer was looking at depended on who they had asked when they were looking for them. Initially there was a single source of truth, but over time things got a little scattered and confused.

By 2017 the career maps were in need of an overhaul; they referred to roles that had been phased out and there were at least six competing versions, not including all of the copies individuals had made to track their own progression.

Our conversations with engineers also revealed that some of the competencies in the matrix were quite vague. When it came to working out how well an engineer was meeting a specific competency it was quite open to interpretation.

## What are career maps for?

There are three reasons career maps are useful.

One is to help engineers understand what is expected of them at each level, and to be able to track their progress against this map. They may want to add personal notes as they do things that demonstrate a competency. The map for them is a living document.

The second use case is for the promotions board. They need to be able to look at a career map and understand how well an engineer is meeting the competencies at the level they want to be promoted into. Where are their strengths and where do they need further support or opportunities to grow?

The final reason for a career map is as a recruitment tool. The abundance of engineering jobs in London mean great engineers can pick and choose between many excellent roles. Sharing our career maps can be very helpful for anyone trying to work out if the FT is for them.

These three use cases don’t coalesce into a single appropriate format. For hiring, we want a format optimised for reading. For engineers, we want something editable. For promotions we want something easy to review and compare.

## Revolution not evolution

Having talked about all this stuff, we ended up doing three things:

Rewriting all of our competencies and role definitions
Creating a new place for them to live, and some tooling to manage them
Creating a plan for roll out
This work happened over three away days, and with a lot of work in-between.

We rewrote all of our competencies and role definitions
The first thing we did was to rewrite all of the competencies. This was by far the least fun part of the work, but also the most important. There is no point in having a beautiful, scalable single source of truth for these if the underlying competencies were bad.

We looked at what some other companies were doing; [Monzo](https://monzo.com/blog/2018/06/25/monzos-transparent-engineering-progression-framework/) and [Rent The Runway](http://dresscode.renttherunway.com/blog/ladder) both have public frameworks. I had also done this exercise at the Government Digital Service so we had a look at theirs too.

## We divided the competencies into four areas:

- *Technical* — The level of mastery someone has over the technologies they’re working with.
- *Communication* — How effectively does this person work with others and communicate with them?
- *Delivery* — How good is this person at delivering the right things and working as part of a team to deliver shared team goals?
- *Leadership* — How good is this person at positively influencing those around them?

We felt that although the weight of these areas would change from a Junior to a Senior, there are still nascent leadership qualities in a Junior engineer that we wanted to highlight and nurture.

Once we had those sorted we did a post-it exercise where we wrote down competencies, stuck them up and discussed them. This process was very illuminating and we had many difficult discussions about what we expect of our engineers.

![A spirited discussion about career competencies — complete with Post-it notes](/assets/img/career-progression.jpeg.jpg)

For example, we had quite a long debate about whether it was important for a mid level engineer to be able to demonstrate that they could set up a continuous integration pipeline from scratch.

The two sides of the argument were that: continuous integration is an important aspect of our services and people should know how it works properly

On the other hand, setting it up from scratch is something that happens once in a project, and so is it realistic to require all mid level developers to have done it?

In the end we decided that the key thing for mid level engineers to be able to do was be able to use continuous integration pipelines, and be adaptable enough to learn new things (like setting one up from scratch) if they needed to do so.

We tried to phrase the competencies so that the requirement for evidence would be inherently met. So for example, instead of saying “Understands how to write tests” we said “Writes tests”. If you meet this competency then there will be some tests you’ve written to prove that.

It wasn’t possible to do this for all of the competencies. For example there is a competency in the leadership category that is “Acts with integrity, honesty and accountability”. These are the Financial Times’s core values, however evidence for this will probably be through testimony from colleagues, which is valuable, but subjective.

By the end of this process we had about eighty competencies across three seniority levels. The competencies were considered as a threshold for getting promoted into that level, so Junior to Mid, Mid to Senior One, Senior One to Senior Two.

We left off any competencies for being hired as a Junior Engineer because it’s the entry level position so we’re looking more at potential than a list of expectations. We also left off Senior Two to Principal. The Principal role at the FT is a “by appointment only” role, not something you can be promoted into by the promotions board. I think we should revisit both of these in due course.

## Our competencies live on GitHub now

Once we had a first pass of competencies, we started thinking about where they would live and in what format. We knew that we wanted a proper canonical source for them, and we wanted it to be a place where individual competencies could be discussed and changes could be tracked.

We decided the competencies should live on GitHub and be stored as YAML. This meant we could serve the competencies as an API, and then build things to meet the needs I outlined above. A Google Sheets integration for individual tracking and note making, a website for more leisurely reading and public recruitment, something more structured for the promotions board.

GitHub is the perfect place for these engineering competencies to live as there are some built in tools that we can use to manage them:

- GitHub Issues — which will allow us to openly discuss areas where these competencies need improvement
- GitHub Pull Requests — which will allow us to make changes to the competencies
- Git tags and releases to version changes so that anyone working with an older version of the competencies can see if they need to update
- Various markdown documents as guidelines for contributing
- A Jekyll instance that will run a live site, which exposes these competencies as a JSON API so people can build their own integrations

We’re going to roll this out between now and October
At the moment these competencies are in Alpha. We created them as a group of five engineers, but there are 231 people that report into the CTO at the Financial Times and this needs to work for most of them.

There is great variety in the things that an engineer at the FT might be working on. We have engineers working in Node.js, Java and Python, engineers working on infrastructure, engineers who work on greenfield projects, and those that work on much supporting and improving much older codebases.

We are also spread across three locales, London, Manila and Sofia. This framework was only developed by people in London.

So, to get to Beta, we’re going to run the competencies past a lot of people. We’ll ask them:

For your seniority, do these represent what you do?
- Is it easy to provide evidence for them?
- Are any of them too vague or too high level?
- Do any of them not apply to your role?
- We want to make sure we cover enough surface area and that the people we ask give it some proper thought, so we’ll be holding a series of hour long workshops with different groups. Of course, anybody that would like to raise issues in GitHub is also welcome to pitch in there.

Our date for launching the Beta is June. This gives us ample time to get feedback from the engineers across the FT. We will use the Beta for our September promotions board. This will be another big test for the framework. When people have to use it in anger, how will they feel about it? What will the big-wigs on the promotions board make of it?

After we have incorporated any changes from the September promotions board, we’ll launch V1.

Thanks to everyone that’s helped with this work so far. My working group pals: [Mark Barnes](https://twitter.com/barnes_tweets), [Rowan Manning](https://twitter.com/rowanmanning), [Laura Carvajal](https://twitter.com/lc512k), [Rhys Evans](https://twitter.com/wheresrhys) and Tom Kennedy. Also Jason Mackie, Lily Madar, Rob Godfrey, Tuf Gavaz, Sarah Wells, John Kundert, Karolina Gardocka, and David Edge.

If you’d like to see the Alpha, it’s on GitHub here: [https://github.com/financial-times/engineering-progression](https://github.com/financial-times/engineering-progression)

Or the website is here: [https://engineering-progression.ft.com](https://engineering-progression.ft.com)

I’ll be back with another update after we’ve launched the Beta in June.
