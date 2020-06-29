---
layout: post
title: "On Community"
date: 2020-06-28
categories:
    - Data Science Teaming
commentIssueId: 38
---
TLDR; I've been interacting with the open source community a bit recently and they're a great bunch of developers.

Do you remember when you learned how to ride a bicycle? You were probably fairly wobbly and fell over a number of times before you finally did it. But once you could ride 100 feet, you could ride for miles (or perhaps for you CS majors out there, it’s like induction - once you’ve proven your base case(s) and n+1, you can climb the ladder arbitrarily high). Back to the bike analogy, there was that remarkably satisfying feeling of *learning to do something new*! It’s important not to forget that childlike wonder as adults. This is how *learning* to interact with the open source community has felt.

As a newbie to data science and the development process for the better part of the past 5 years, I was always worried about asking trivial questions and I certainly had no idea how *I* could be of any help to the open source community or even my fellow data scientists. ..until recently.

If there’s one takeaway message from this post, it’s that the people you interact with on Github, Reddit, Stack Overflow, or any developer forum (e.g. PyTorch) are overwhelmingly kind and altruistic people who want to help. And you are closer than you think to contributing to that generous practice. This is not a humble brag. This is an observation I’ve made after humbly asking for help.

### Stack Overflow
I think every developer’s first interaction with the community is Stack Overflow (SO). I mean seriously, if you’re a developer, could you actually get through a day without looking at something on SO? Ok fine, maybe you’re a *really* good developer. How about a week? In any event, think about all the time and effort that people have put into thoughtfully answering basic questions for junior and senior developers. So if you get to the point where you can answer someone’s question on SO, pay it forward, *everyone* will appreciate it. <a href="https://stackoverflow.com/questions/55959570/how-to-properly-iterate-over-a-for-loop-using-dask/61242241#61242241" target="_blank">Here’s my first contribution.</a>

### Github
Git and Github are scary when you first start using them. Git is overwhelmingly complex (branches, merging, pulling, pushing, stashing, conflicts, and the list goes on) and then there are pull requests, code reviews, Github issues, and GitOps. I can see why people might take a long time to properly engage with this community. But in short, there will be a day sometime soon, when you are out on the bleeding edge of some new library and you hit an issue and you google around and nothing. Then you scratch your head and think, hm, is this *my* bug or is there an issue with the tool that I’m using, or is there some feature that I’d like to see, or is there an example that would make using this tool sooo much better? As time goes on, you get better and better at discovering where *you’ve* erred versus where the *tool* is erring.

When you discover what you think is an issue or a bug with the tool, find an existing Github issue  or raise a new issue and describe your experience. It’s as simple as that. If it’s an active project someone will be in touch and two wonderful things might happen. 1) You might inform them on how to continue improving the repository, and/or 2) you may soon become a happy consumer of a tool that does exactly what you need it to do.
Here are some of the issues and pull requests that I’ve raised or participated in:

#### Examples
- <a href="https://github.com/dask/dask-ml/issues/664" target="_blank">An issue that turned into the example below</a>
- <a href="https://github.com/dask/dask-examples/pull/149" target="_blank">Hyperparameter optimization example I'm working on</a>

#### Bugs
- <a href="https://github.com/pytorch/text/issues/835" target="_blank">Issue I discovered while working with `torchtext`</a>

#### Features
- <a href="https://github.com/skorch-dev/skorch/issues/605" target="_blank">Figuring out how `skorch` can work well for NLP modeling</a>
- <a href="https://github.com/GoogleCloudPlatform/python-docs-samples/issues/4046" target="_blank">Feature request for a Google Cloud tool</a>

#### Questions
- <a href="https://github.com/skorch-dev/skorch/issues/641" target="_blank">Asking how to score a `skorch` model in a customized way</a>
- <a href="https://github.com/GoogleCloudPlatform/cloud-builders/issues/697" target="_blank">FAIL 😂 - don’t worry, shit happens.</a> You can see that I asked the question in the wrong forum and the guy closed and locked the issue. Now, I would have *liked* to post my solution when I figured it out but I trust that his action was for the good of that community.

### Other forums
After SO and Github, you’re likely to particpate (either as a consumer or contributor) in other online communites like Reddit, Quora, or tool-specific forums (e.g. PyTorch). Again, I believe that *most* people in these communities are kind and mean well. It doesn’t mean you won’t get the occasional troll, but hey, sometimes that keeps things interesting! So perhaps you have a question that doesn’t really apply to SO or Github or you just read a rad new paper on arXiv and you’re wondering, well, where should I engage? And the answer is that it depends but also that it doesn’t really matter. Just put your stuff out there and people will point you in the right direction.

- <a href="https://www.reddit.com/r/MachineLearning/comments/hfulv7/d_what_are_your_thoughts_on_data_labeling/" target="_blank">First post on r/MachineLearning</a>
- <a href="https://discuss.pytorch.org/t/aligning-torchtext-vocab-index-to-loaded-embedding-pre-trained-weights/20878/8
" target="_blank">First posts on the PyTorch forums</a> 

As a newbie to data science for the better part of the past 5 years, I didn’t have a team of senior engineers to show me the way. And I’ll bet that’s the case for a lot of people reading this. You might be the go-to woman at your startup for all things data science and there may be very few people, if anyone, more experienced than you to help you figure things out. If you’re anything like me, you probably feel a bit (read a lot) of imposter syndrome as you’re learning how everything works.

And indeed, there is *a lot* to know. We have to learn the math behind the algorithms we work with (e.g. how backpropagation works), new techniques (e.g. causality), new APIs (e.g. insert fancy new deep learning library name here), and simply how to deliver a data science project with a *better* than 50% chance of success (e.g. putting a model into production).

Regardless of where you’re at on your journey as a data scientist or developer, just know that you have the community backing you up. And before you know it, *you* might be the person supporting a newcomer. 

The upshot of participating in all these communities is that you will learn rapidly and give back to the community that has given so much. Once you learn how to engage a little bit, you’ll experience an exponential ability to successfully participate. And that’s why this was like learning how to ride a bike, at least for me. Once you can ride 100 feet, you can ride 100 miles and you’ll feel a sense of satisfaction and wonder that *money cannot buy*.

What do you think? Leave a comment at the link below.