---
layout: post
title: "Tackling Climate Change with Machine Learning Paper Review"
date: 2019-09-21
categories:
    - Paper Reviews
commentIssueId: 31
---
TLDR; Paper review of <a href="https://arxiv.org/abs/1906.05433" target="_blank"> Tackling Climate Change with Machine Learning</a>

Recently-ish (June 2019), a paper was released by a number of researchers on how machine learning can be brought to bear on climate change. The <a href="https://www.ipcc.ch/sr15/" target="_blank">impact</a> that climate change will likely have on humanity within the next several decades cannot be overstated - it will be catastrophic if we do not take action now.

Many of the top US, Canadian, and European institutions contributed, namely CMU, Stanford, Google, University of Montreal, and DeepMind. The paper is 53 pages long so kudos to you if you make it through this whole recap, and even more kudos if you make it through the whole 53-page paper. In this post, I will highlight some points that I found interesting from each of the climate change solution domains.

<br>
<div style="text-align:center;"><img src="/assets/paper_reviews/climate_change_ml_applications.png" style="max-width:720px"></div>
<div style="text-align:center"></div>
<br>

## Introduction
Highlighted portions and commentary:
1. Entrepreneurs and investors would be wise to read this paper. There are some terrific opportunities for those that are willing to take risks and work on one of humanity's most important challenges.
    * I have always thought it would be neat to generate a green score for businesses (e.g. restaurants, hotels, tour operators, etc.) and have that be one of the criteria on a Google or Yelp review. I'd bet if the data was reliable, it would influence consumer buying preferences.
1. Jevons paradox is mentioned several times throughout the paper, which is an interesting economic concept. In short, it is a situation where increased efficiency results in higher overall demand. Autonomous vehicles exemplify this in that they are more efficient and encourage people to use them more (and thus generate more greenhouse gasses). The punchline here is that we need to look out for unintended consequences of certain technologies.
1. Website for collaborators and relevant data: <a href="https://climatechange.ai/" target="_blank">https://climatechange.ai/</a>.
1. There is a supremely human element to climate change as echoed by the last sentence in the introduction section, "While we hope that ML will be useful in reducing costs associated with climate action, humanity also must decide to act." I'll never forget a college professor telling me that combating climate change is more of a political battle than a technological one.

## Mitigation
#### Electricity Systems
TLDR; electricity systems powered by fossil fuels are responsible for ~25% of all human-caused greenhouse gas emissions.

Highlighted portions and commentary:
1. This is the longest and ostensibly highest impact section of the paper.
1. Key points:
    * transition to low-carbon electricty sources (e.g. wind, solar, etc.) in lieu of carbon emitting sources (e.g. coal, natural gas, etc.)
    * reduce emissions from carbon-emitting power plants in the interim
    * implement changes globally (e.g. not just the developed or developing world)
    * ML can be helpful on all fronts by informing research, deployment, and operation of electrical system technologies.
1. ML can reduce emissions from today's standby generators, which emit CO<sub>2</sub> even when they are not generating power, and enable the transition to carbon-free systems by helping improve necessary technologies (namely forecasting, scheduling, and control) and by helping create advanced electricty markets that accommodate both variable electricity and flexible demand.
1. Generate demand forecasts that optimize for electricity scheduling cost or GHG emissions as opposed to forecast accuracy.
1. Scheduling and dispatch is the process used to determine how much power each power plant should produce. These are NP-hard optimization problems that can be approached using ML instead. Neural networks, genetic algorithms, fuzzy logic, and reinforcement learning can all help here.
1. Nest was used by Southern Californa Edison to manage grid usage to prevent electricity blackouts. <a href="https://www.greentechmedia.com/articles/read/inside-nests-50000-home-virtual-power-plant-for-southern-california-edison#gs.tdtnm6" target="_blank">Link</a>
1. ML can be used to accelerate materials research for solar fuels and battery storage technologies. Active learning, and generative models have been applied to the synthesis, characterization, modeling, and design of new and existing materials. It is also interesting to note that explainable ML models are advancing theoretical physics from empirical results.
1. A really challenging problem associated with solar panels is that they introduce demand volatility due to the variable nature of their output. Computer vision on satellite data can be used to estimate the output capacity for a particular geographic region and ML techniques can be used to forecast solar panel output, allowing power plant operators to plan accordingly.
1. Nuclear fusion reactors (as opposed to fission reactors) have the potential to produce safe and carbon-free electricity using a virtually limitless supply of hydrogen fuel. Fusion reactor research has a huge number of tunable parameters. ML can help narrow the search space. Simulation modeling can also be used for hydrogen plasma dynamics modeling.
    - <a href="https://www.nature.com/collections/bccqhmkbyw" target="_blank">Overview of nuclear fusion</a>
1. ML can use sensor/satellite imagery to suggest pipeline maintenance and prevent methane gas leaks. Predictive maintenance can also proactively suggest electricty grid upgrades.
1. Make energy consumption forecasts for data-limited locales (e.g. developing world). For example, in the developed world researchers might identify a relationship between electricity consumption and cell tower usage. In the developing world, where electricity consumption data may not be available and cell tower usage data may be available, impute the energy usage.

#### Transportation
TLDR; the transportation sector accounts for ~25% of all energy-related CO<sub>2</sub> emissions.

Highlighted portions and commentary:
1. At present, more than two-thirds of transportation emissions are from road travel. However, for all you frequent flyers out there, air travel has the highest emission intensity, measured by grams of CO<sub>2</sub> per person-km.
1. Key points for reducing GHG emissions:
    - decreasing transportation activity
    - increasing vehicle efficiency
    - reducing the carbon impact of fuel
    - shifting to lower-carbon options, like rail.
1. ML can improve vehicle engineering, enable intelligent infrastructure, and provide information to policy-makers.
1. ML can assist in reducing the number of vehicle-miles traveled by making long trips less necessary, increasing loading, and optimizing vehicle routing.
1. Computer vision can be used to count vehicles, bicyclists, and pedestrians for road and urban planning.
1. ML can provide information about mobility patterns, which is a direct input to agent-based travel demand models, one of the main transport planning tools.
1. ML can predict taxi time for airplanes on the tarmac, reducing the amount of fuel burned on the ground waiting.
1. Simulation modeling could help determine if ride-sharing services are actually taking customers away from lower carbon options and in fact increasing GHG emissions.
1. Freight routing and consolidation is a huge opportunity! This is like the classic knapsack problem (or like the <a href="https://www.youtube.com/watch?v=TO8lwvIR4Tw" target="_blank">Amazon Locker problem</a>). The gist of it is that you want to maximize the utilization of a truck or shipping container by filling it to the brim.
1. ML can be used to optimize vehicle designs for power efficiency.
1. Robots and drones can help with last-mile delivery.
1. Platooning is a neat concept that is best employed with autonomous trucks. The idea would be to drive very close together to reduce air resistence and increase fuel efficiency.
1. Reinforcement learning can be used for reducing traffic congestion.
1. Cars should essentially be mobile batteries for execess solar energy production.
1. ML can play a role in battery research.
1. (As an avid CitiBike and Divvy Bike user,) ML can be used to rebalance bikes throughout the city from high inventory to low inventory neighborhoods.

#### Buildings & Cities
TDLR; Energy consumed in buildings is responsible for a quarter of global energy-related emissions (i.e. energy-related as compared to other sources of emissions such as methane from farming, etc.).

Highlighted portions and commentary:
1. Optimizing buildings can be done by modeling data on energy consumption and optimizing energy use in smart buildings.
1. <a href="https://www.nytimes.com/2019/04/17/nyregion/nyc-energy-laws.html" target="_blank">NYC is requiring</a> building owners to collectively reduce their emissions by 40% by 2040.
1. RL and transfer learning can be used to make predictions about new buildings (e.g. commercial to residential).
1. Harmonic analysis utilizes the Fourier transform to pick out "signatures" of individual appliances to break down energy usage in a building. So cool!
    - Useful when you all you have is aggregate building-level energy usage. 
1. Smart buildings assist grid operators in managing energy demand.
    - Grocery stores are great candidates for this.
1. Learning user behavior is a great little project that anyone could work on to optimize a building. For example, learning when to turn on AC, heat, or lighting based on usage patterns could make for a cool use case that saves money.
    - You could use Raspberry Pis, smart plugs, or really anything that could control your AC, heating, or lighting.
1. <a href="https://ieeexplore.ieee.org/document/8675180" target="_blank">RL</a> that uses edge devices for IoT-based energy management in cities. This is a neat project idea.
1. ML can be used to obtain district-level data:
    - derive high-level patterns where data on individual buildings exist
    - where data on energy use and infrastructure is completely lacking, ML can infer the data.
1. Back to my point above about a great startup for rating the greenness of a business, you might look at the following papers to identify buildings that may be laggards in terms of efficiency:
    - <a href="https://www.aaai.org/ocs/index.php/AAAI/AAAI11/paper/viewFile/3759/4088" target="_blank">A Large-Scale Study on Predicting and Contextualizing Building Energy Usage</a>
    - <a href="https://www.sciencedirect.com/science/article/pii/S0306261917312692" target="_blank">Building energy retrofit index for policy making and decision support at regional and national scales</a>
    - <a href="hhttps://hal.archives-ouvertes.fr/hal-01730717v1/document" target="_blank">A geoprocessing framework to compute urban indicators: The MApUCE tools chain</a>
1. As someone who has done a fair bit of social listening with Twitter data, it was great to see several use cases. Social data can provide information to urban planners about how an urban space is being used (e.g. parks, etc.).
1. As someone who has struggled with fusing data from a variety of sensor feeds, there were some interesting references to techniques for sifting through huge feeds from edge devices.
    - <a href="https://www.cs.helsinki.fi/u/jilu/paper/bigdataapplication03.pdf" target="_blank">Geospatial Big Data: Challenges and Opportunities</a>
    - <a href="https://www.iit.cnr.it/sites/default/files/07501696.pdf" target="_blank">Hypothesis Transfer Learning for efficient data
computing in Smart Cities environments</a>
    - <a href="https://spiral.imperial.ac.uk/bitstream/10044/1/42700/9/07797232.pdf" target="_blank">A deep learning approach to on-node sensor
data analytics for mobile or wearable devices</a>
    - <a href="https://ieeexplore.ieee.org/document/8647113" target="_blank">Intelligent and energy-efficient data prioritization in green smart cities: Current challenges and future directions</a>
    - <a href="https://openaccess.leidenuniv.nl/bitstream/handle/1887/57500/Big_data_analytics_for_mitigating_carbon_emissions_in_smart_cities_opportunities_and_challenges.pdf?sequence=1" target="_blank">Big data analytics for mitigating carbon emissions in smart cities: opportunities and challenges</a>
    - <a href="https://arxiv.org/abs/1301.3485" target="_blank">A semantic matching energy function for
learning with multi-relational data</a>
    - <a href="https://homes.cs.washington.edu/~pedrod/papers/hois.pdf" target="_blank">Ontology matching: A machine learning approach</a>
    - <a href="https://ieeexplore.ieee.org/document/7230259" target="_blank">Methodologies for cross-domain data fusion: An overview</a>
    - <a href="https://www.researchgate.net/publication/315698712_A_Survey_on_Ensemble_Learning_for_Data_Stream_Classification" target="_blank">Ensemble learning for data stream analysis: A survey</a>

#### Industry
TLDR; The industrial sector (e.g. cement production, oil & gas pipelines, etc.) spends billions annually collecting data on factories and supply chains, making this a ripe domain for machine learning modeling. Cement & steel production together acccount for 9% of all global GHG emissions.

Highlighted portions and commentary:
1. <a href="https://www.sciencedirect.com/science/article/pii/S0301421516302130" target="_blank">Energy-saving implications from supply chain improvement: An exploratory study on China's consumer goods retail system</a>.
    - this paper addresses how much energy is spent on storing perishable foods past their harvest season (e.g. apples in warehouses, etc.).
    - instead of storing perishable foods, sensors could detect when food is likely to spoil so that it can be sold quickly or removed from a storage crate before it ruins the rest of the shipment.
1. Proper management of refrigerants (e.g. freon for airs conditioners, etc.) ranks #1 on <a href="https://www.drawdown.org/solutions-summary-by-rank" target="_blank">Project Drawdown's</a> list of solutions to combat climate change.
1. Reducing food waste ranks #3 on <a href="https://www.drawdown.org/solutions-summary-by-rank" target="_blank">Project Drawdown's</a> list of solutions to combat climate change.
1. Recommender systems could encourage consumers to purchase goods that account for the whole lifecycle of a product (e.g. a car's production through disposal)
    - <a href="https://www.orizzontenergia.it/download/Articoli%20e%20Interviste/Auto%20Elettrica.pdf" target="_blank"> Comparative
environmental life cycle assessment of conventional and electric vehicles</a>
    - <a href="https://www.sciencedirect.com/science/article/pii/S0160412003002459?via%3Dihub" target="_blank">Life cycle assessment: Part 1: Framework,
goal and scope definition, inventory analysis, and applications</a>
1. DeepMind used <a href="https://deepmind.com/blog/article/deepmind-ai-reduces-google-data-centre-cooling-bill-40" target="_blank">reinforcement learning</a> to optimize the energy usage in Google's data centers.

#### Farms & Forest
TLDR; Deforestation and unsustainable agriculture are freeing large amounts of sequestered carbon held in trees, peat bogs, and soil.

Highlighted portions and commentary:
1. Peatlandas cover only 3% of earth's land area, yet are the largest source of sequestered carbon on earth.
1. A single peat fire in Indonesia in 1997 is reported to have released 20-50% of global fossil fuel emissions during that year.
1. Cattle farming generates methane, a particularly potent greenhouse gas.
    - Agriculture is responsible for 14% of GHG emissions.
1. Permafrost is expected to cause a 12-17% increase in global emissions over the next few decades.
1. Satellite imagery can be used to estimate the amount of carbon sequestered in every parcel of land as well as how much GHG  it releases.
1. Forests and peatlands can be monitored for fire risk.
    - RL can be used to predict the spatial progression of fire, allowing firefighters to do controlled burns to manage the forest.
1. Drones can be used to plant seeds.
1. Project Drawdown estimates around a third of potential climate change mitigation solutions involve better land management and agriculture. 
1. The Jevons paradox is at play again if we make forest harvesting more efficient.
1. Again, the politics of this situation also rears its head. Agriculture involves a complex web of large-scale farming interests, small-scale farmers, agricultural equipment manufacturers, and chemical companies.

#### Carbon Dioxide Removal
TLDR; Many experts argue that global emissions need to become net-negative if we are to avoid the most serious consequences of climate change.

Highlighted portions and commentary:
1. ML can be used to accelerate materials discovery for sorbents that can absorb CO<sub>2</sub>.
    - ML for materials research was a big theme throughout the paper.
1. This is one of the smaller sections in the paper, perhaps indicating white space for entrepreneurs and researchers.

## Adaptation
<div style="text-align:center;">
<a href="https://www.youtube.com/watch?v=XGi2a0tNjOo&feature=youtu.be" target="_blank"><img src="/assets/paper_reviews/climate_modeling.png" style="max-width:720px">
</a>
</div>
<div style="text-align:center">
<a href="https://www.youtube.com/watch?v=XGi2a0tNjOo&feature=youtu.be" target="_blank">Introduction to Climate Modeling</a></div>
<br>
#### Climate Prediction
Highlighted portions and commentary:
1. Climate modeling is clearly something that simulation experts, computer scientists, data scientists, and climate scientists can all work together on.
1. The compute requirements to simulate the climate are staggering.
    - <a href="https://repository.library.noaa.gov/view/noaa/14319" target="_blank">Position paper on high performance computing needs in Earth system prediction</a>
    - <a href="https://journals.ametsoc.org/doi/full/10.1175/BAMS-D-13-00255.1" target="_blank">The Community Earth System Model (CESM) Large Ensemble Project: A Community Resource for Studying Climate Change in the Presence of Internal Climate Variability</a>
    - <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018GL078202" target="_blank">Could Machine Learning Break the Convection Parameterization Deadlock?</a>
1. Learn the basics of climate modeling from:
    - <a href="climate.be/textbook" target="_blank">climate.be/textbook</a>
    - <a href="https://www.youtube.com/watch?v=XGi2a0tNjOo&feature=youtu.be" target="_blank">Introduction to Climate Modeling</a>
1. Climate modeling resources for practictioners:
    - <a href="https://www.nature.com/articles/s41586-019-0912-1" target="_blank">Deep learning and process understanding for data-driven Earth system science</a>
    <a href="EnviroNet: ImageNet for environment" target="_blank">climate.be/textbook</a>
    - <a href="https://ams.confex.com/ams/2019Annual/webprogram/Session49023.html" target="_blank">Introduction to Climate Modeling</a>
    <a href="climate.be/textbook" target="_blank">climate.be/textbook</a>
    - <a href="https://journals.ametsoc.org/doi/full/10.1175/BAMS-D-15-00135.1" target="_blank">The Art and Science of Climate Model Tuning</a>
1. Deep learning can be used to emulate physical processes, such as high-resolution cloud simulation, which requires a physics based based model that is very computationally expensive.
    - <a href="https://arxiv.org/abs/1708.00588" target="_blank">Hidden physics models: machine learning of nonlinear partial differential equations</a>
    - <a href="https://arxiv.org/abs/1711.10561" target="_blank">Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Differential Equations</a>
    - <a href="https://arxiv.org/abs/1806.07366" target="_blank">Neural ordinary differential equations</a>
1. There are proposals for climate models that learn continuously from data and from high-resolution simulations.
    - This is a framework proposed to be written in Julia (vs. Fortran/C++ for most existing climate modeling software), which may be more accessible to new developers.
    - <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017GL076101" target="_blank">Earth system modeling 2.0 : a blueprint for models that learn from observations and targeted high-resolution simulations</a>
1. Overall, this section felt very concrete and provided some clear starting points for researchers, computer scientists, and data scientists to get involved.

#### Societal Impacts
TLDR; If humanity does not meet its climate goals, then adaptation is the logical next step, which leads to the following questions: How do we reduce vulnerability to climate impacts? How do we support rapid recovery from climate-induced disruptions?

Highlighted portions and commentary:
1. Sensor networks can be used to monitor ecosystems, which has implications for biodiversity, agriculture, disease, and natural resources (e.g. clean water, fish, etc.).
1. Anomaly detection and data imputation techniques can be used to handle frequent sensor node failures.
    - <a href="https://dslpitt.org/uai/papers/07/p75-dereszynski.pdf" target="_blank">Probabilistic models for anomaly detection in remote sensor data streams</a>
    - <a href="http://isiarticles.com/bundles/Article/pre/pdf/76940.pdf" target="_blank">Anomaly detection in streaming environmental sensor data: A data-driven modeling approach</a>
1. Existing infrastructure (e.g. electrical, water, and transportation infrastructure etc.) will come under increasing strain as the climate changes
    - Predictive maintenance and anomaly detection can be used to keep these systems operational.
1. Social listening (e.g. social media, credit card transactions, mobile phone signals, etc.) can be used to obtain a pulse on distressed locales, which can allow for more targeted emergency response after natural disasters.
    - Social data can also be used to monitor migrants as communities affected by climate change are displaced.
    - Meanwhile, the paper mentioned that immigrants and refugees are vulnerable groups, and systems that surveil them can easily be exploited by bad actors.
1. Blending large scale simulation of crop yields with ML:
    - <a href="https://arxiv.org/abs/1705.02355" target="_blank">Accelerating science with generative adversarial networks: an application to 3d particle showers in multilayer calorimeters</a>
    - <a href="https://www.ics.uci.edu/~welling/publications/papers/WhyMLneedsStatistics.pdf" target="_blank">Are ML and statistics complementary?</a>

#### Solar Geoengineering
TLDR; The gist of solar geoengineering is to reduce the amount of solar radiation that makes to the earth, thus reducing the amount that the atmosphere can be warmed.

Highlighted portions and commentary:
1. Again, the author mentions, "the hardest and most important problems raised by solar geoengineering are non-technical," which I take to mean that politics are the real challenge.
1. ML could be used to accelerate research into aerosols that are chemically nonreactive but refelective, cheap, and easy to keep aloft.
    - Again, this highlights the materials research theme.
1. ML might also help to ease the computational load of simulating the effect of aerosols.
1. Can potentially use reinforcement learning to model the effect of pumping aerosols into the atmosphere and the control required to operate the system.
1. The author highlights the moral hazard of this technology. My sense is that he means this type of technology may allow humanity to become even more complacent and take no further action on climate change.
    - This type of technology feels a bit like escapism, a theme explored in a terrific sci-fi book called the <a href="https://en.wikipedia.org/wiki/The_Dark_Forest" target="_blank">The Dark Forest</a>, by Cixin Liu, the second book in an amazing trilogy.

## Tools for Action
#### Tools for Individuals
TLDR; Individual action is important to combat climate change.

Highlighted portions and commentary:
1. ML can help estimate an individuals carbon footprint and provide counterfactuals (i.e. answer what if questions).
1. RL can be used to optimize home appliance electricity usage. Multi-agent systems can coordinate to keep peak energy demand low.
1. CycleGANS have been used to visualize potential consequences of extreme weather events on houses and cities.
    - <a href="https://arxiv.org/abs/1905.03709" target="_blank">Visualizing the consequences of climate change using cycle-consistent adversarial networks</a>
1. <a href="https://tmrow.com" target="_blank">tmrow.com</a>

#### Tools for Society
TLDR; ML/AI can provide tools for policy, markets, and large-scale planning.

Highlighted portions and commentary:
1. The author mentioned the tragedy of the commons, which is worth reading a little about if you've never encountered the concept. Climate change is an easy example of this phenomena.
    - <a href="https://en.wikipedia.org/wiki/Tragedy_of_the_commons" target="_blank">Tragedy of the Commons</a>
1. RL and bandit optimization techniques can be used to price goods (or "bads") such as greehouse gas emissions.
    - <a href="https://arxiv.org/abs/1803.09967" target="_blank">Reinforcement learning for fair dynamic pricing</a>
1. Multi-objective optimization is another technique that is broadly useful to incorporate tradeoffs in policy-making, infrastructure development, etc.
1. Other interesting methods cited: particle swarm, genetic, or evolutionary algorithms to search for pareto-optimal solutions.

#### Education
TLDR; This is partially a "people" problem, so education is a natural solution.

Highlighted portions and commentary:
1. Multi-armed bandit and adpaptive learning techniques can be used to optimize individual learning. 

#### Finance
TLDR; forecasting which companies, economies, etc. are most likely to be impacted by climate change can highlight medium and long-term risks.

Highlighted portions and commentary:
1. ML can be used as a portfolio optimization technique that attempts to price in the environmental impacts of the companies in the portfolio (e.g. timber companies, etc.).
1. Carbon pricing (e.g. cap-and-trade) introduction <a href="https://media.rff.org/documents/RFF-CCIB-17.pdf" target="_blank">here</a>.