---
title: "Designing a Deep Learning Desktop Machine"
date: 2018-06-15
categories:
    - MLOps
tags:
    - MLOps
    - hardware
header:
    teaser: /assets/images/dl_machine/zeus_parts.JPG
excerpt: TLDR; Designing a deep learning desktop machine for multiple users.
---
TLDR; Designing a deep learning desktop machine for multiple users.

In this post, we'll be thinking through our criteria for building a deep learning desktop machine that is performant enough for multiple users. As of mid-2018, the first question that probably comes to mind is, why not just use one of the cloud platforms? The answer for our team of ~20 data scientists comes down to the cost of GPUs/hour. As I write this post, Google Cloud Platform GPU costs in the US are as follows: NVIDIA Tesla K80 (\\$0.45/hour), NVIDIA Tesla P100 (\\$1.46/hour), NVIDIA Tesla V100 (\\$2.48/hour), TPU [Tensorflow models only] (\\$6.50/hour). We're really bad about remembering to shut down our GPU instances in the cloud so these costs can quickly add up.

<figure class="align-center">
  <img src="/assets/images/dl_machine/zeus_parts.JPG" alt="Computer parts">
  <figcaption>Our colleague, Zeus, carting the computer parts to our lab.</figcaption>
</figure>

These costs are top of mind for us when we're developing a model and running our initial tests or when we're deploying a live model. In other words, we have no problem with the team using the cloud to run a *training* job on the cloud once we've finished model development and need to scale up our compute power, but why pay a boatload of money to develop and debug a model? Furthermore, if you want to serve a model that requires a GPU for performance at inference time, you should consider the costs of running a GPU around the clock on a cloud platform.

Now that we have our motivation for building a machine, what type of machine should we buy or build? Our two criteria for a machine were 1) price and 2) power. 

### Price
One machine vendor I came across during my search is Lambda Labs, which sells deep learning machines with various configurations. I was pleased to see that the specs on their <a href="https://lambdal.com/raw-configurator?product=quad" target="_blank">premium quad machine</a> were nearly the same as our build. However, at $10k for this machine, you're paying quite a premium for convenience as I'll show below.

If you only have a budget of ~$5k, you'll want to maximize power within that constraint, which meant we needed to build something ourselves. If you're building a machine, I'd encourage you to check out <a href="https://pcpartpicker.com" target="_blank">pcpartpicker.com</a>. You can check out machines that other people have built, <a href="https://pcpartpicker.com/user/tmorrill/saved/m4CNNG" target="_blank">such as our machine</a>, but the most important thing is that they ensure that your build parts will all be compatible with one another. There were two small differences from the build list displayed here: 1) we got 3 NVIDIA 1080 Ti GPUs, not 2, and 2) we had 128gb of DDR4 RAM from another machine that we swapped into this build when we constructed it and replaced the other machine's RAM with the 64gb of RAM listed on the parts list. If you made those two changes to our parts list, the build would cost ~$6K.

The finish the discussion on price, if we added a 4th GPU to our build (which wouldn't be possible with our chosen motherboard, but let's set that aside for a moment) we'd be at ~\\$7K, which is still \\$3k less than Lambda Lab's build. If you find the convenience of someone building the machine for you and not to mention installing the OS and some deep learning libraries, then the $3k markup is probably worth it for many teams!

### Power
Our second criterion was power. My goal was to increase utilization on the deep learning machines that we build. In the past, we've built ~1 machine per team member, but as we've scaled out, that has become less feasible. I have also observed that these machines typically only had 1 user but had the power to handle additional users (i.e. low utilization). I wanted to build a powerful enough machine so that three people could comfortably use the machine - one person per GPU. Each NVIDIA 1080 Ti GPU has 11gb of RAM, which allows for prototyping and training fairly large models. For example, some of our language models require a huge vocabulary and the word embeddings take up a large memory footprint.

Beyond the GPU, it is helpful to have a powerful CPU and a decent amount of memory to do things like data preprocessing. Tensorflow's Dataset API (<a href="https://www.tensorflow.org/performance/datasets_performance" target="_blank">Datasets Performance Guide</a>) does a great job making use of the CPU's power to preprocess your data batches while the GPU handles the matrix computation. Finally, if you're reading your data from disk as batches, memory isn't such a huge issue. However, it's still nice to have the flexibility of holding a fairly large dataset in memory.

With these things in mind, we purchased an Intel Core i7-7820X 3.6GHz 8-Core Processor, which has 16 virtual threads. In other words, if we partitioned the machine for three people, they would each have ~5 CPU cores to go about their work, which is sufficient for most of our workloads. We also install 128gb of DDR4 RAM in the machine, providing ~40gb of memory to each of the three users - not bad!

<figure class="align-center">
  <img src="/assets/images/dl_machine/kid_in_a_candy_shop.JPG" alt="Kid in a candy shop">
  <figcaption>I looked like a kid in a candy shop while assembling the machine.</figcaption>
</figure>

In this post, we have covered off the key design principles for a multi-user deep learning desktop machine. In a later post, I'll address how we can actually partition this machine for multiple data scientists to use comfortably.


