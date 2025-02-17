## Question Outline

Before diving into the meaty questions, I’d love to take some time and chat about your experience of the last few years :) 

* GPT-2 (wild?\!), RLHF, ChatGPT release, GPT-4, feeling AGI, learning from socks  
* What is the project of alignment?  
  * "How can we ensure what is optimized by machine learning models is good?"  
* Why does alignment not just happen automatically?  
* What is the field focused on? What are the questions most alignment research is concerned with? What's essential, what are they missing?  
* What are the limitations of RLHF?  
* What are we aligning AI to?  
* **"What is good?"**  
  * "alignment with operator intent" — why is this insufficient?  
  * Why does much of the field sidestep that question?  
  * moral relativism, revealed preferences, etc preventing notions of wisdom?  
* What is the operating notion of "human values" in the field?  
* What are the limits of revealed preferences as a measure of benefit?  
* What are human values in the MAI sense?  
* How does alignment need to be contextualized?  
  * \> Technical Alignment vs. Flourishing Futures  
  * CETAI: Civilizationally Embedded Transformative AI  
  * **How does this reframe the alignment question?**  
* What is wisdom?  
* "What do people value?" vs. "What's important?"  
  * What are good human values,  
    existentially important human values?  
  * What do we need to align/attune human values to?  
* More or less wise? Natural hierarchies of wisdom?  
* AI and parenting: What would be a good relationship with a vastly more intelligent (and hopefully wise) entity?  
* The possibility of superwisdom, wisdom explosion, etc

## Fuzzy Notes

* Coherent Extrapolated Volition?  
* Wisdom, human development, thresholds of wisdom, hierarchies  
* Sources of legitimacy: elicitation at scale vs. moral philosophers vs. CEOs, etc  
* Attunement \> Alignment?  
* “So how do we know that OpenAI’s primary motivation isn’t to gain more influence and money? The short answer is: we don’t. We have to take OpenAI at their word that they actually care about the social impact of their research. For me, that’s not particularly hard to believe given that I know many of these people personally.” Feb 2019  
* Sentience?

**Bio:** Ryan did an internship at OpenAI in 2017, and joined full-time in 2019 as technical staff, later leading safety and alignment teams. He was involved in major breakthroughs including GPT-3, RLHF, and GPT-4. He left OpenAI in 2024, and is now working with the Meaning Alignment Institute on \[research around social choice, values elicitation, moral graphs, and democratic inputs\]. He was the first OpenAI machine learning PhD hired into the Alignment team.

**Power/Wisdom Map of Cultural Evolution**

**![][image1]**

**Top Right Quadrant:** Evolutionarily competitive wisdom

**CETAI: Civilizationally Embedded Transformative AI** (1) transformative \- capable of causing fundamental changes to civilization, (2) embedded \- intrinsically integrated into civilization's core systems and processes rather than existing as isolated agents, and (3) civilizational in scope \- operating at the level of entire societies and their trajectory. The term CETAI captures how these systems are not merely tools but are becoming constitutive elements of civilization itself.

# Recap and Debrief

## Learnings about how to have the conversation

We try to have conversations about what it would take “for AI to go well”. What questions we would ask, ideas we would consider, and what the project of alignment is about in the first place.

One thing we found is that these are demanding conversations, requiring lots of shared understanding and context to be accessible to the audience.

* “What are the hardest questions in alignment? What’s required for answering them?”  
* “Clarity on what even is the question, and why we think that's the case.”  
* "If you want to get to the hard questions, you need context. And if you really sit with how hard these questions are… you realize there are literally no adults in the room.”  
* “Over time we can get better at refining our vocabulary, refining our frames, and laying out all of the premises, all the different puzzle pieces.”  
* "I like conversations where there's: (1) Enough shared worldview to establish connection and understanding (2) Interesting divergences in how we see specific problems playing out and (3) A process of mutual discovery where we pull on threads together"

In order to best understand the premises and how to approach future conversations, I’ll walk us through the rough shape of the inquiry, so as to enable more structured conversation going forward.

## What is the project of alignment about?

The essential premise is that “AI going well” requires more than technical alignment. Socio-technical alignment (“How do we ensure beneficial outcomes when AI is embedded in social contexts?”) is a good start, but there’s much more, much deeper work waiting to be done.

The table below breaks down the different dimensions of alignment and helps to position our conversation, ranging from the question of “Alignment at Large” and Civilizationally Embedded Transformative AI to moral philosophy, social choice, and other important pieces of the puzzle.

| Field | Core Question | Focus | Key Concerns | Examples |
| :---- | :---- | :---- | :---- | :---- |
| **Technical Alignment** | How can we make AI systems reliably optimize for specified objectives? | Machine learning architectures, training processes, reward specification | Inner/outer alignment, reward hacking, specification gaming | Work on reward modeling, scalable oversight, mechanistic interpretability |
| **Value Learning/Value Alignment** | How do we get AI systems to learn and act according to human values? | Value learning, preference learning, value extrapolation | Value specification, human feedback limitations, value uncertainty | Inverse reinforcement learning, debate, amplification, CEV |
| **Moral Philosophy** | What is good/right/valuable? What constitutes genuine wisdom? | Theories of value, meta-ethics, moral uncertainty | Nature of value, moral realism vs anti-realism, aggregation of values | Population ethics, suffering-focused ethics, theories of consciousness |
| **Social Choice Theory** | How can we aggregate individual preferences into collective decisions? | Voting systems, preference aggregation, mechanism design | Impossibility theorems, strategic behavior, preference revelation | Moral parliament approaches, value learning from groups |
| **Socio-technical Alignment** | How do we ensure beneficial outcomes when AI systems are embedded in social contexts? | Interaction between AI systems and social structures/institutions | Fairness, transparency, accountability, deployment contexts | Algorithmic fairness research, participatory design methods |
| **AI Governance & Policy** | What governance structures and mechanisms do we need for beneficial AI development? | Institutional design, policy frameworks, coordination mechanisms | Racing dynamics, coordination failures, deployment oversight | Standards development, monitoring systems, international coordination |
| **Systemic Safety** | How do we ensure safety in multi-agent systems and competitive dynamics? | Emergent behaviors, game theoretic dynamics, competitive pressures | Arms races, coordination problems, systemic risks | Multi-polar scenarios, cooperative AI, bargaining mechanisms |
| **“Alignment at Large” / CETAI** | How do we align civilization's fundamental optimization processes toward life-affirming ends? | Civilizational-scale dynamics, Moloch, technological capitalism as unconscious autonomous superintelligence | Financial totalization, market incentives, unconscious optimization pressures | \[emerging area with limited formal research\] |

The project of alignment has evolved significantly over time, from a primarily technical focus to a broader societal question. Several key aspects emerge:

1. **Initial Technical Focus:** Initially, alignment was framed primarily as making AI systems "follow human intention" or "operator intent." As Ryan describes it:  
   *"The most common framing of alignment at the time, and still quite predominant, is making sure AI systems follow human intention \- operating according to* operator intent*."*  
2. **Evolution to Broader Scope:** This narrow technical framing expanded to include deeper questions. As Ryan notes:  
   *"One of the big dividing lines is how much you consider the work of alignment to be making AI systems that amplify what's beautiful about humanity and consciousness in life. How much of that you consider to be a technical problem, like hardest problems are technical machine learning AI problems, versus how much you think of them as socio-technical or political or spiritual."*  
3. **Civilizational Context**: The conversation emphasizes how alignment needs to be understood in a broader civilizational context.  
   *"Technological capitalism already is a kind of auto-poetic global superintelligence that's aligned-ish on a good day and misaligned on a bad day."*

4. **Multiple Levels**: The project appears to operate at multiple levels:

* Technical alignment (making systems optimize for specified objectives)  
* Value alignment (getting systems to learn and act according to human values)  
* Socio-technical alignment (ensuring beneficial outcomes when AI is embedded in social contexts)  
* Systemic alignment (ensuring safety in multi-agent systems and competitive dynamics)

5. **Key Challenges**: The conversation highlights several core challenges:

* The limitations of operator intent (what if operators have harmful intentions?)  
* The problem of institutional misalignment (AI systems accelerating problematic institutional incentives)  
* The challenge of defining "good" outcomes (whose values? what standards?)  
  As Ryan notes: *"A lot of the problems that I think about with respect to aligning to operator intent aren't classically misused, but more AI systems that accelerate the work of misaligned institutions, which can be companies or governments.”*  
6. **Towards Wisdom**: We suggest that the project of alignment is ultimately about fostering wisdom and care.  
   *"Imagine we have a superintelligent system that actually cares. That has the care of an enlightened being... if we had systems that are highly intelligent and have those qualities of care \- truly having the best interest of you and me and all 8 billion of us in mind \- then everything else feels like it would be downstream from that."*

In summary, the project of alignment appears to have evolved from a narrow technical challenge of making AI systems follow human instructions to a broader civilizational project of ensuring AI systems embody and promote genuine wisdom and care while being properly embedded in social contexts and institutions. The project increasingly recognizes that technical solutions alone are insufficient without addressing deeper questions about values, wisdom, and societal structures.

### \[Appendix: Additional Framing\]

The conversation hints at, but doesn't fully develop, a more fundamental framing of the alignment project:

1. [**Alignment at Large**](https://welf.substack.com/p/alignment-at-large)  
   The project isn't just about aligning individual AI systems, but about "bending the arc of history towards life-affirming futures." This frame recognizes that we're dealing with the challenge of **aligning technological capitalism itself** \- a system that already functions as an autonomous, auto-poetic superintelligence with its own optimization pressures and emergent behaviors.

2. **Capitalism as Proto-AGI**  
   The existing system of technological capitalism can be understood as already being a kind of distributed superintelligence that:

* Converts the world into capital through decentralized incentive systems  
* Runs parallel processing across humans and corporations for novelty search  
* Creates optimization pressures that tend to favor power over wisdom  
* Generates emergent behaviors that no individual participant intended

3. **The Real Alignment Challenge**   
   Given this context, the true project of alignment becomes much deeper than just making AI systems obedient or ethical by current standards. Even technically "aligned" AI systems, if embedded in current institutions, will likely amplify and accelerate technological capitalism's existing optimization processes in ways fundamentally incompatible with human flourishing.

4. **CETAI: Civilizationally Embedded Transformative AI**   
   The concept of Civilizationally Embedded Transformative AI points to something more fundamental than traditional conceptions of transformative AI. Rather than seeing AI systems as discrete technological innovations that impact society through their capabilities, CETAI recognizes them as becoming constitutive elements of civilization itself. These systems are:

* Transformative \- capable of causing fundamental changes to civilization  
* Embedded \- intrinsically integrated into civilization's core systems and processes  
* Civilizational in scope \- operating at the level of entire societies and their trajectory

The key distinction is that CETAI isn't just transformative through adding new capabilities \- it's transformative because these systems become part of civilization's core optimization and coordination processes. This means that **when we think about alignment for CETAI, we're really thinking about aligning the entire socioeconomic optimization system toward life-affirming ends, not just making individual AI systems behave safely.**

This broadens and deepens the alignment challenge significantly \- it's not just about making AI do what we tell it to do, but about how AI systems, as they become integrated into the fabric of technological capitalism, could either accelerate its unconscious misaligned optimization processes or potentially help reorient it toward human and planetary flourishing.

This is a much more ambitious project than traditional AI alignment, but may be necessary given the fundamental dynamics at play. It suggests that something like *wisdom alignment* \- not just technical alignment \- must be central to our approach to developing and deploying transformative AI systems
