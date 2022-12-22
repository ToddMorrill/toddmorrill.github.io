---
title: "MS in Computer Science at Columbia: Semester One, Fall 2022"
date: 2022-12-21
categories:
    - school
tags:
    - research
header:
    teaser: /assets/images/mscs_semesters/romanesco_broccoli_fractal.png
excerpt: TLDR; I finished the first semester (fall '22) of my MSCS program at Columbia.
---
TLDR; I finished the first semester (fall '22) of my MSCS program at Columbia.

<figure class="align-center">
  <img src="/assets/images/mscs_semesters/romanesco_broccoli_fractal.png" alt="romanesco broccoli fractal">
  <figcaption>Romanesco broccoli fractally goodness.</figcaption>
</figure>

It has been absolutely incredible to be a part of the computer science community at Columbia and I'm writing this to: 1) share this experience for any future Columbia CS students considering what classes to take and 2) capture the memories.

# Summary
- took 3 classes: Unsupervised Machine Learning, Distributed Systems Fundamentals, and Probabilistic Graphical Models
- began working with Professor Kathleen McKeown as an NLP researcher on a DARPA project
- learned how to write the curly braces used in set notation (e.g. $\\{ x \| x < 42, x \in \mathbb{R}\\}$) 🙃.

# Coursework
In general, I think you'll find your plate is pretty full with 3 classes. You'll probably have a little time to spare for research or other projects. With 4 classes, I suspect you'll be slightly over capacity and compromising the learning experience somewhere.

## Unsupervised Machine Learning (COMS 4774)
Unsupervised Machine Learning (UML) was taught by <a href="https://www.cs.columbia.edu/~verma/index.html" target="_blank">Nakul Verma</a>. The course covers clustering procedures (e.g. $k$-centers, spectral clustering, etc.), linear dimensionality reduction (e.g. PCA, Johnson-Lindenstrauss Lemma), non-linear dimensionality reduction (e.g. IsoMap, tSNE, etc.), density estimation (e.g. Gaussian mixture models, etc.), topological data analysis, text embeddings, and hyperbolic embeddings. There is far too much material to cover in a semester so Prof. Verma tends to go deep on a few of these topics rather than giving a cursory overview of all of them. Prof. Verma's problem sets are notoriously difficult. There is a problem set 0 to earn your way into the class and then 4 demanding problem sets. There is also a semester project, where you'll be expected to work on a problem related to unsupervised learning. On the problem sets, you'll be required to prove that certain classes of problems are NP-hard and apply the Johnson-Lindenstrauss (JL) Lemma to dimensionality reduction. The JL lemma essentially shows that randomly generated matrices, where the entries are sampled from a normal distribution, approximately preserve interpoint distances in low dimensions. In other words, you can approximately preserve the high dimensional distance (e.g. $L_2$) between pairs of points in low dimensional space (i.e. approximately an isometric embedding). This is a pretty surprising result! This class will require a fair amount of work and it best suited for those with a background in ML and the usual culprits: linear algebra, probability, and calculus. You will also have a leg up if you've taken real analysis. My sense is that an A is very common in this class but you'll have to put in a lot of hours on the problem sets and final project to get it.

<figure class="align-center">
  <img src="/assets/images/mscs_semesters/spectral_spring.png" alt="spectral clustering">
  <figcaption>Spectral clustering of butterfly species data, where colors correspond to cluster assignments.</figcaption>
</figure>

## Distributed Systems Fundamentals (COMS 4113)
Distributed Systems Fundamentals was taught by <a href="https://roxanageambasu.github.io/" target="_blank">Roxana Geambasu</a>. The course covers some of the big ideas related to distributed systems such as sharding, replication, consensus protocols (e.g. Paxos), atomic commitment protocols (e.g. 2-Phase Commit), logical clocks, database transactions, and a number of real-word systems such as Google's Spanner, Kubernetes, and cluster schedulers such as YARN and Mesos. Much of the learning takes place through 5 programming assignments in Golang that are HARD. You'll work toward implementing Paxos for a sharded and replicated distributed key-value store and will encounter the difficulties of concurrent programming along the way. There is also a final exam at the end of the semester. Depending on your background, be prepared to put in ~20 hours (or more) per week to earn an A.
My personal reflections on the course are as follows. I implemented Paxos! Wow. That was hard but also really cool. I also spent some time thinking about high-level (e.g. Python) vs. low-level languages (e.g. Go, C++, etc.) and my conclusion is that you gain so much by programming in a high level language. In A LOT of scenarios, you gain a huge amount of productivity and a much lower cognitive load, which probably outweighs any performance optimizations or type checking "safety" you get with low-level languages. I think the reason the for greater cognitive load while coding in lower-level languages is that it's harder to test your code interactively. You definitely don't have Jupyter notebook for Golang. Oftentimes in Python, I'll set breakpoints after writing some functionality and run the code up to that breakpoint and inspect the state of the variables to confirm it's behaving as expected. In contrast, in a compiled language you wind up either: 1) writing a bunch of unit tests while you're developing your code (which is what you should be doing anyway but sometimes breaks your flow), or 2) writing your whole program without testing at all. In Python, you can almost think in code, watch your ideas come to life in real-time, and get nearly instant feedback about what's working or not. I think this is why Python is the second-best language for nearly everything (which is a good thing), and also why Python is being used for some serious systems, like <a href="https://instagram-engineering.com/static-analysis-at-scale-an-instagram-story-8f498ab71a0c" taget="_blank">Instagram</a>. Some of Go's "features," like not allowing unused variables actually make you feel bad as you're coding (check out screenshot) because you constantly feel like there are errors in your code, when in fact it's really just the linter.

<figure class="align-center">
  <img src="/assets/images/mscs_semesters/go_linter.png" alt="go linting error">
  <figcaption>Go's linting errors for unused variables make you feel bad while you're coding - see the red underlines.</figcaption>
</figure>

## Probabilistic Graphical Models (AKA Probabilistic Machine Learning, STCS 6701)
Probabilistic Machine Learning is taught by the legendary <a href="http://www.cs.columbia.edu/~blei/" target="_blank">David Blei</a>. This course covers machine learning from a probabilistic perspective, which focuses on quantifying the uncertainty of a model's predictions and discovering latent structure in data. For example, Bayesian linear regression provides a distribution of possible values for a given input as opposed to only a point estimate, which can be used to quantify a model's uncertainty.

<figure class="align-center">
  <img src="/assets/images/mscs_semesters/regression_uncertainty.png" alt="regression uncertainty">
  <figcaption>Figure illustrating the quantification of uncertainty for regression estimates (PRML, Bishop, page 29).</figcaption>
</figure>

As an example of discovering latent structure, the Gaussian mixture model is a clustering model that discovers the means of the clustering components as well as cluster assignments of data points, which can be modeled as latent variables. The Bayesian approach to machine learning modeling often necessitates approximate posterior inference procedures due to intractable integrals and sums so a large portion of the class was devoted to inference procedures including Gibbs sampling and variational inference. The assignments for this class consist of weekly reader reports, where you read a paper and write a brief summary of what your read, 3 homework assignments, and a final report. This class assumes you have had at least some exposure to probabilistic modeling. Experience with a probabilistic programming package like Pyro, PyMC3, or STAN would be a huge plus. I found the manipulations of some of the probabilistic expressions to be a little tricky and intend to continue reading Christopher Bishop's classic 2006 textbook *Pattern Recognition and Machine Learning*. For example, I found implementing the ELBO for coordinate ascent variational inference (CAVI) for the Gaussian mixture model to be pretty tricky because it requires proficiency in manipulating not only probability expressions in the abstract but also their functional forms, and then implementing the result in Python. The final project makes up 60% of the grade and is held to a high bar so my sense is that you'll get an A if you submit essentially publishable work. Note this class is advertised as a PhD level class.

## Modern Analysis I (AKA Real Analysis, MATH 4061)
This iteration of the course was taught by Florian Johne. I audited Real Analysis and I made it through about a third of the course before I had to divert my attention full-time back to my other classes. This is a demanding, fast-paced course that covers the construction of the Real numbers, topology of metrics spaces, sequences and series, continuity, differentiation, integration, and sequences and series of functions. So that's my project for winter break - finishing up this material because as I mentioned above, having some familiarity with analysis really does help as you push into topics like metric learning, topological data analysis, or measure theory, which is useful to understanding the underpinnings of probability theory.

## Columbia Community
Working in Prof. Kathy McKeown's NLP research lab has been a really special opportunity. We're working on a DARPA project called <a href="https://www.darpa.mil/news-events/2021-05-03a" target="_blank">Computation Cultural Understanding</a>. The objective of the project is to develop systems that can inform an operator (e.g. a diplomat, military commander, etc.) on how successful their cross-cultural interaction is and provide feedback to help keep them on track through the use of an augmented reality headset. This is particularly important in high-context cultures where gestures and formal power hierarchies are important to respect if you want to achieve your objective. Suffice it say, this is a really hard problem to work on, but it's fun to be out on the edge of our current capabilities, working with team leads and colleagues who are up for the task.

I've enjoyed working with my peers on problem sets and group projects, and even just interacting on Ed to collectively solve assignments. Office hours with professors are usually pretty interesting. After expressing my interest in neuro-inspired computing, Prof. Verma invited a former TA for the course to present a paper about hyperdimensional computing, which seems like a promising research direction. I had great conversations with Prof. Geambasu about privacy preserving machine learning. Hearing Prof. Blei's thoughts on interesting research directions is epic because he's got such a birds-eye view of the field. The punchline here is that Columbia is a terrific research institution and it's fun to be a part of that. I even hung out with Jacob Devlin at a happy hour one night and picked his brain about self-supervised learning. 

At times, I felt like I was drinking from a fire hose but I guess that's what graduate school is for; it exposes you to a breadth of new ideas and trusts that you have enough mathematical and engineering maturity to be able to go deep on any of these topics. Naturally, you can't be an expert at everything so I think the key thing is to know that these ideas exist and figure out how to quickly page things into memory, as demanded by whatever project you might be working on.