---
title: "Knowledge Graph Preliminaries"
date: 2020-12-21
categories:
    - NLP
tags:
    - NLP
header:
    teaser: /assets/images/misc/network.jpg
excerpt: TLDR; I've been researching ways to construct knowledge graphs from text and then use them for NLP reasoning tasks.
---
TLDR; I've been researching ways to construct knowledge graphs from text and then use them for NLP reasoning tasks.

<figure class="align-center">
  <img src="/assets/images/misc/network.jpg" alt="Beads on strings">
</figure>

Knowledge graphs are just that - graphs that encode knowledge. Typically nodes represent semantic concepts such as words or entities, while edges represent relations between these words or entities. For example, fruit, appple, and orange might be three concepts that all get their own node. The graph may contain the relation (i.e. edge type) *is-a* to represent the fact that an apple *is-a* fruit; an orange *is-a* fruit. So what can we do with knowledge graphs that we can't with other rich tools, such as deep learning based question-answering models? In short, my goal is to use the information encoded in knowledge graphs for reasoning tasks. I'll sketch out a few examples of NLP tasks that require reasoning in contrast to mere statistical correlation.

**Example 1 - Semantic Similarity**

I have used the Universal Sentence Encoder and cosine similarity on many occasions to retrieve "similar" documents and have witnessed pretty average performance. From there, I've considered siamese networks to determine if two sentences are similar but to train one of these networks you need a fairly large number of labeled pairs to train on. This approach might work well on something like the <a href="https://www.kaggle.com/c/quora-question-pairs" target="_blank">Quora Question Pairs</a> dataset where you have a huge number of labeled examples. Clustering is another way to attack this problem.

The trouble with any pretrained-embedding/distance based approach (in my view) is that comparing two pieces of text may involve reasoning, not just semantic similarity. For example, you could have a regulation that talks about auto interest rates. In short, businesses use controls (shortish pieces of text) to comply with regulations. So suppose a business has a control that addresses mortgage interest rates. They're semantically similar but the control doesn't apply to the regulation from a business perspective. Similarly, if you have a regulation that says you can only charge a maximum of 4% interest but your control says that you can charge a maximum of 5% interest, a human will still be responsible for identifying that difference and reasoning about why the control does not comply with the regulation. This is why I've been so adamant about exploring approaches that extract facets (entities, chunks, etc. whatever you want to call them) from the sentences and exploring ways to reason about and compare regulatory facets to control facets.

**Example 2 - Question-Answering**
Deep learning based question-answering models typically take as input a short passage and a question, and return an answer span from the provided passage. Here's a sample passage that I made up.

*Passage:* "A nor'easter grounded flights departing from New York City this weekend. LaGuardia, JFK, and Newark were all impacted though transportation officials expect normal operations to resume by early Monday morning."

*Question 1:* Which airports were impacted by the nor'easter?
*Answer 1:* LaGuardia, JFK, and Newark.
NB: this would be a trivial task for a deep learning model trained on SQuAD 2.0. It would simply highlight the text span that answers the question.

*Question 2:* How many airports were impacted by the nor'easter?
*Answer 2:* ?
NB: this would be a non-trivial task for a deep learning models trained on SQuAD 2.0. You and I both know the answer is three, but this required *reasoning* about the passage. <a href="https://demo.allennlp.org/reading-comprehension/MjYxMzAxNg==" target="_blank">Try it</a> for yourself.

### Literature Review
I hope it is clear from the examples above that our current arsenal of deep learning based models is sorely lacking the ability to reason. This motivates the need for neuro-symbolic approaches - hybrid approaches that combine the best of statistical learning and symbolic reasoning. So before we can use a knowledge graph for reasoning tasks, we actually need to construct one! So how does one construct a knowledge graph?

I've been working through a literature review of current methods for constructing knowledge graphs starting with two terrific sources:
* Graham Neubig's Neural Networks for NLP class notes (CMU): <a href="http://phontron.com/class/nn4nlp2020/schedule/knowledge-based-qa.html" target="_blank">Link</a>
* USC Center on Knowledge Graphs's long list of resources: <a href="https://usc-isi-i2.github.io/home/" target="_blank">Link</a>

In future posts, I will dive into how to construct a text-based knowledge graph, which as we noted above, includes extracting entites (i.e. nodes) and relations (i.e. edges) from a corpus of text. These posts will build from the <a href="https://web.stanford.edu/~jurafsky/slp3/17.pdf" target="_blank">Information Extraction</a> chapter from the textbook Speech and Language Processing. From there, I'll need to explore how to reason with this data. Consider Example 2 above - suppose we successfully extracted the 3 airport names, what procedure can we rely on to translate those extracted entities into an answer to the question *How many airports were impacted by the nor'easter?*

The [next post]({% post_url 2020-12-22-Knowledge-Graphs-NER %}) will address entity extraction.