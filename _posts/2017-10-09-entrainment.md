---
title: "Entrainment with Visual Stimuli"
date: 2017-10-09
categories: NLP
tags:
    - biometrics
header:
    teaser: /assets/images/entrainment/entrainment.jpg
excerpt: TLDR; I created a strobe video that my brain can entrain with.
---
TLDR; I created a strobe video that my brain can entrain with.

When learning a new skill, especially with programming and hardware, I find it best to start with small experiments, confirm my understanding of the results, and build on from there. Over the past month or so, I set out to detect a well defined phenomemon in my brain using the EEG headset - entrainment with visual stimuli. If this experiment is a success, we will better understand the principles underlying this rather complex source of data - EEG signals. From there, we can move on to machine learning with EEG/biometrics data, which is far more unchartered territory.

<a href="https://en.wikipedia.org/wiki/Brainwave_entrainment" target="_blank">Brainwave entrainment</a> is when your brainwaves synchronize with visual, audio, or tactile stimulus. The goal for this experiment was to watch a video on a computer screen that flashes essentially a strobe light at a defined frequency such as 10 or 12hz and then be able to detect the entrained brainwaves in the EEG recording. *If we can detect a signal in our brainwaves, we can use it to issue commands.* The commands will be limited to a handful of actions (e.g. turn a robot left or right) but we'll be controlling something with our mind. To be sure, the idea here is that if you have multiple signals on the screen such as 10 or 12hz, each of which corresponds to an action, you can issue an action simply by looking at the corresponding frequency!

<figure class="align-center">
  <img src="/assets/images/entrainment/entrainment.jpg" alt="Entrainment">
  <figcaption>A colleague was a real sport and volunteered to try entrainment..</figcaption>
</figure>

A word of caution before proceeding, visual entrainment does pose the risk of seizures so if you're epileptic or you don't respond well to flashing lights, DO NOT TRY THIS EXPERIMENT.

With that out of the way here's our outline:
1. Create the visual stimuli - video recordings of different frequency strobe lights, which is what we're discussing today
2. Record the EEG signal while watching the videos
3. Analyze the data and try to detect the entrained signal

### Create the visual stimuli

I'm sure there are a number of ways of creating a strobe light video and I did spend some time Googling ways do this in programs like iMovie but the path forward wasn't clear to me. The more I thought about it, I figured Python and namely Matplotlib could help. After finishing the script, a colleague mentioned MoviePy, which is probably worth checking out though I'm not sure if it would solve my strobe light problem. In any event, Jake Vanderplas is one of the best teachers out there on the internet and I checked out <a href="http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/" target="_blank">one of his posts</a> to better understand the Matplotlib Animation class, specifically <a href="https://matplotlib.org/api/animation_api.html" target="_blank">the FuncAnimation class.</a> Needless to say, getting this all to run smoothly will take time and I hope I left my code well commented enough to be helpful to anyone else attempting this. The one key concept I'll highlight here is the generator function - the crux of getting this thing to run. Every time this generator function gets called, it *yields* a new frame that gets added to the video and it's up to you to decide what goes into that frame!

{% highlight python %}
def frame_gen(frame_count=frame_count, frame_rate=frame_rate, desired_hz=desired_hz):
    """generates a new frame every time it is called, keeping track of where the video is across different
    frequencies and when to switch from black to white"""
    closest_approx = approximate_hz(desired_hz=desired_hz, frame_rate=frame_rate)
    hz_switch_point_frame = hz_switch_point(frame_count=frame_count, desired_hz=desired_hz)
    
    current_frequency = -1 # zeroeth index of desired_hz (gets incremented by one in modulus in first run)
    on = True
    i = 0
    while True:
        if i % hz_switch_point_frame == 0:
            current_frequency +=1 # incremented by one in the first run
        # black
        if i % (closest_approx[current_frequency]) == 0:
            on = not on
            np_array = np.ones((height, width),dtype=int) * on # switch from black to white
            i += 1
            yield np_array
        # white
        else:
            i += 1
            yield np_array
{% endhighlight %}

Let's take it one line at time.

The approximate_hz function takes in a list of desired frequencies and returns a list containing switch points. In other words, to approximate a 10hz frequency, you would need to switch from black to white every 6 frames (assuming 60 frames per second (FPS)). I learned that you actually can't show a 9hz signal perfectly using a 60FPS monitor. In fact, the only frequencies you can show are those that divide evenly into 60. Think about it: 60 / 9 = 6.667. You can't change the strobe every 6.667 frames. You can only switch every 6 or 7 frames, which means your effective frequency is either 10 or ~8.6hz, respectively. Now imagine that you had a monitor with a 120FPS refresh rate. What would be the closest frequency that would approximate 9hz? Answer: ~9.2hz, which corresponds to a switch every 13 frames. Incidentally, the faster your refresh rate is, the better you can appoximate the frequency. I found this fascinating but I digress. The point here is that you shouldn't be surprised if your entrainment shows up at an unexpected frequency (if you use a frequency that doesn't divide evenly into your refresh rate) when you analyze the data.

The hz_switch_point_function keeps track of which frequency the generator is working on. If you want a movie that's 60 seconds long across 10 and 12 hz, this means you will switch from 10 to 12hz at the 30secondsx60FPS = 1,800th frame.

Finally, the while loop is the main part of the generator function. The i variable is a simple incremeter that keeps track of how many times the function has been called. If i modulus switch point == 0, it's time to switch from black to white! Any other time that modulus != 0, simply yield the existing numpy array. I'm conveniently taking advantage of the fact that matplotlib treats zeros and ones as black and white respectively using cmap="gray".

The final thing I'll note here is that I found FFMPEG to be the fastest movie writer. You can try ImageMagickWriter but it was significantly slower because it writes all the frames out to disk individually and *then* stitches them together.

If you spend a little time reading the code it'll become clearer. There are two scripts worth checking out: 1) entrainment_891011hz_full.ipynb outputs a full screen strobe, and 2) entrainment_1012hz_split_screen.ipynb outputs a split screen strobe.

In the [next post]({% post_url 2017-10-10-detecting-entrainment-part-1%}), we'll cover the analysis of the entrained EEG signal.
