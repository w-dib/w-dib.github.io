---
title: How we pivoted with grace
description: ""
date: 2021-07-24T18:05:26.537Z
preview: ""
image:
  path: public/assets/lib/pivot.png
  alt: pivot with the bros
tags: []
categories: startups
---
How we pivoted our startup with grace
=====================================

If you've been in the MENA startup ecosystem, you've definitely heard that "90% of startups fail before they do X or Y". A [report conducted by CBS Insights](https://www.cbinsights.com/research/startup-failure-post-mortem/?utm_campaign=cbi-social&utm_content=173297792&utm_medium=social&utm_source=linkedin&hss_channel=lcp-1140722#2021update2) on US startups suggested that "70% of upstart tech companies fail --- usually around 20 months after first raising financing (with around $1.3M in total funding closed)".

![ ](https://cdn.sanity.io/images/tbcelk7e/production/54bab97865a34f77a7a398157c0dc506b5fa644b-1000x2500.webp)

CBS Insights: [Why Startups Fail](https://www.cbinsights.com/research/startup-failure-reasons-top/)

I'm fascinated by the above graph. Based on a survey with 101 founders, the most likely reason for failure was no market need, at 42%. The least likely reason (7%) for a startup's demise was due to a failure to pivot in time.

To clarify, not all pivots are great. The above graph also shows that 10% of founders failed because of a pivot gone bad. Still, founders were four times as likely to fail due to a poor market fit.

Having been in the exact same position myself just a few months ago, I can imagine only two scenarios for this. Founders in my shoes who've closed up shop were either:

too stubborn to admit that their hypothesis was poor, and decided they'd rather burn their cash to prove their point than switch tracks; or

too worried about the repercussions of pivoting. Questions that have personally kept me up at night include: what will my existing and future investors think? What about my existing clients? What if we fail once we pivot? What will happen to my colleagues then?

### Mistake #1: building a solution looking for a problem

The most eventful memory of 2018 for me was co-founding [Addenda](https://www.khaleejtimes.com/business/local/an-insurance-ecosystem-that-runs-on-blockchain), the B2B precursor to [hala insurance](http://www.joinhala.com/). My brother Karim and I formally quit our jobs in July of that year, and started Addenda with the intention of disrupting back office workflows between insurance companies. Super sexy proposition, right?

![ ](https://cdn.sanity.io/images/tbcelk7e/production/185cd30ccb6c1cab291a18b029d83a135be05736-1345x513.webp)

the now defunct www.addenda.tech landing page

Addenda was the result of our obsession with blockchain and decentralization. Armed with just a few years of experience in the insurance sector, I drafted a vague business plan showcasing how much insurers can save on operational costs by using blockchain.

The idea was this: in a region oversaturated with insurance companies that agree on so very little, we thought we could capitalize on their lack of trust between each other. What we didn't know at the time was that blockchain was just the foot in the door to get insurance CEOs to sit down on the same table and cooperate.

Everyone won. Insurers got on front page headlines being "innovative" by transacting on-chain, and we got to learn the *actual* problems and inefficiencies insurance companies face directly from the inside.

*Hint: their problems were not a result of the lack of blockchain in their day-to-day lives.*

### Fast forward a month

[Addenda was accepted](https://gulfbusiness.com/dubais-fintech-hive-accelerator-begins-second-edition/) into Dubai's Fintech Hive Accelerator program in August 2018, where we gathered a small team of blockchain experts and decided to make a big dent in insurance, regardless of how. By the end of 2018, Karim and I began to deplete what little savings we had left. Unsurprisingly, building the blockchain was not the hard part - finding the use case was!

As we progressed, we realized we had no specific focus. Which insurance line of business were we trying to disrupt? Were we after reducing fraud in life insurance? Did we want to speed up payouts in travel insurance claims? Or was Addenda all about transacting payments between brokers, insurers, and re-insurance companies?

To say that we pivoted a few times while we were still a B2B company would be an understatement. Below are some samples of unsuccessful prototypes that we later identified as "solutions looking for a problem":

### Life Insurance Blockchain

![ ](https://cdn.sanity.io/images/tbcelk7e/production/0c829d046e04a357eabb67d75a3e2eba70c0e96d-1049x500.webp)

This was the first time we actually used the Hyperledger Fabric distributed ledger

What it was: A blockchain prototype where encrypted data representing life insurance policies was shared in real-time between insurance companies. With this tool, underwriters would have been able to check the history of policy applicants via their Emirates ID. For life insurance, an MVP would have prevented problems that plague the industry: from anti-selection, non-disclosure, to over exposure.

What we wish we made: We really wanted to use this for medical insurance. A decentralized layer of medical history would have really reduced the onboarding process time and underwriting cost due to policy applicant history being available pseudonymously on a distributed ledger. To tackle privacy concerns, we wanted to use OTPs. To look up an Emirates ID, the policyholder would need to authorize the insurer's search via a 4 digit SMS. We thought we could get into medical insurance through a life insurance prototype, but most insurers were worried about privacy and regulatory constraints.

### Claim Process Blockchain

![ ](https://cdn.sanity.io/images/tbcelk7e/production/bfbcd0caa02c0f1d5ccbcd00e27c807655a53cc3-422x720.webp)

Proposed screen for filing a car accident on the Dubai Police app

What it was: This was a really cool idea that I wish actually worked out. Along with our insurance partners, we wanted to push this prototype to the Dubai police. The idea was to have a dashboard for all of the people involved in a car accident, from the policyholder and insurer, to the repair shops on the backend. You'd know where your car was, whether a claim was accepted, what the status of repair was, and when to pick it up again.

Why it failed: Barely any garages or repair shops were willing to use another layer of software (extra operation cost) to report car repair statuses to insurers. We also never really made proper contact with the Dubai police.

### FAC close-out blockchain

![ ](https://cdn.sanity.io/images/tbcelk7e/production/a06920f8e920d4ee1ea3dfdc5a4adcb64caf104b-983x720.webp)

What it was: This prototype was another solution looking for a problem. We built this with the intention of speeding up VAT payment reconciliation between brokers, insurers, and reinsurers. This pivot never really took off beyond PoC.

Why it failed: it was a dumb idea.

### Car accident history blockchain

![ ](https://cdn.sanity.io/images/tbcelk7e/production/9a796fcd9d0563429a58a0980b6df6978db48fa3-1227x776.webp)

What it was: We called this the "Addenda Engine". This proof of concept involved 8 or 9 UAE insurance companies, and was used to track the history of a car's accidents via it's chassis. I genuinely thought this would take off. We started with a sample size of 400,000 accidents, and identified several cases where the same car had been totaled several times, indicating a serious fraudulent case. For reasons I don't want to disclose publicly (if you know, you know), we never proceeded with this PoC.

You'd think at this point, we would have let go of blockchain PoCs, right?

Wrong. Here's what happened instead:

![ ](https://cdn.sanity.io/images/tbcelk7e/production/dfa589cadcd9e7b682b495b8d03686f20848009e-492x469.webp)

### Motor Subrogation Blockchain (AKA MIRSAAS)

![ ](https://cdn.sanity.io/images/tbcelk7e/production/f113a7ef007336d8f6b40cb56d4bbc8ec6c2dbb9-1287x894.webp)

Our first commercial blockchain use case

What it was: MIRSAAS was a disaster of a name. It stood for Motor Insurance Recovery Software As A Service. Horrible name put aside, this was our baby. This is the product that actually took off and we invoiced real companies real money for it.

We launched with 9 insurance companies in November 2019, who used MIRSAAS to reconcile 30,000,000 AED in car insurance claim payables and receivables over the course of 10 months.

Yes, our unit economics were poor. Yes, the product was bloated. Yes, we upset some big insurers who did not want transparency... but, hey! We had a fantastic UI/UX. We even provided our insurance companies with claim APIs to integrate with us at no cost.

The product was straight forward:

A car accident takes place, then the car owner informs their insurance company (insurer A).

Insurer A then informs the at-fault insurance company (Insurer B) of the accident, showing them a police report confirming that they are indeed liable to pay for the repair costs.

Several repair quotations are provided digitally to an expert surveyor.

The customer repairs their car, and the repair shop sends the invoice to Insurer A.

Insurer A updates the claim documentation as and when they get more data.

Consolidated claim documentation is updated in real-time, and Insurer B always knows exactly how much they owe Insurer A.

The vision: we wanted to own the entire value chain of an accident, and we thought we had figured it out. What if customers got paid through us? What if we tracked every single car accident in the UAE? What if insurers would reconcile the complex web of payables and receivables through MIRSAAS?

![ ](https://cdn.sanity.io/images/tbcelk7e/production/cad37242a8b4e1ee4cde0e56cacab3c05bc2d405-1079x548.webp)

This is where we were right before we pivoted to B2C

### The big boy pivot

Right, so by now we've built a functional blockchain. We have seed stage investors, 9 clients in the UAE, a team of all-star developers, and a running PoC with the top 6 Bahraini insurers. 6 of Kuwait's largest insurers had also signed contracts with us. Why'd we pivot to B2C? Below is the Q&A nobody asked for:

> Was it because of COVID-19?

Nope. We were paid per claim, and the big 'Rona was an inconvenience for sure, as curfews meant less claims, meaning less money for us, but it wasn't disastrous per say.

> OK so was it because of a co-founder dispute?

Nope. Despite what the picture below would show you, we were always on the same page. I'd like to think we still are.

![ ](https://cdn.sanity.io/images/tbcelk7e/production/31fdd045070f5f8b572d9fffa4f6d26cf9c0e121-1456x819.webp)

Left to right: Karim, Harsh, and Walid

> OK, fine! Are you actually going to tell us?

Yes, dear reader who is also me, I will tell you. Half way through our adventure with Addenda, we realized several things. Skip to the third one if you want the most important thing.

-   Not all insurance companies want transparency for their payables and receivables. The 80/20 rule applied here in a hilarious way: 20% of the companies owed 80% of the market hundreds of millions of AED in car accident claims. Using such a service - even if it saved them X,000,000 AED in operational costs, would have bankrupt them.
-   We hated B2B with a passion. We hated the archaic insurance systems we dealt with. We hated pitching to people who did not care about their own companies. We hated the sales cycles, the call backs, the bluffs, the "competition", and most of all... we hated our product.
-   We realized that we did not quit our jobs and build Addenda to solve such a small problem in the grand scheme of things. Here's what I mean:

![ ](https://cdn.sanity.io/images/tbcelk7e/production/4d4e136d2d0e073df3cfae9730f6b61e079beee5-934x436.png)

A mix of public and private data we gathered from 2017/2018 the UAE market

Instead of looking at the big picture (i.e.: building a full stack insurance company), we focused on the little yellow box above. Our total target market was a fraction of what it could have been. Why focus on overhead *reduction* when we could focus on the 7 billion dirhams in premium? Imagine pitching a product to an insurance company's claims departments that they feared would make them redundant. That was MIRSAAS.

We were clearly on the wrong side of the digital divide. What's even better is that the above graph is only representative for car insurance. What about home insurance, pet insurance, and travel insurance? What if we took the knowledge we gained from how internally dysfunctional insurance companies are, and instead built something that actually matches the marketing material?

Being insurance customers ourselves, we had a good idea what the customers' biggest problems were in insurance, and we knew that we were not focusing on them with Addenda.

### Where others saw chaos, we saw opportunity.

I consulted with Karim and our investors. Once we clarified the idea of the full-stack insurance company, we knew we needed to pull the plug.

Moments after we made the decision, I sent an email to all of our partners canceling each contract we had. The phone started ringing minutes later. They thought I was insane. Two rumors spread in the market: either the Addenda bros were bankrupt, or they sold Addenda for millions. Neither was true, but we played our cards close to our chest.

On the same day, we stopped the prototypes in Kuwait and Bahrain, and we decided to leave motor insurance subrogation and moved onto [hala](http://www.joinhala.com/).

### Pivoting like an elephant on roller-skates

The products and pivot(s) above were far from graceful. More often than not, we'd trash "brilliant" ideas that turned out to be vaporware at best. But every time we switched lanes, we learned something new.

Below are the three reasons why our biggest pivot to date actually worked:

We were lucky to have amazing investors who invested in the founders, not the startup. We informed each and every one of them why we wanted to build hala instead, and they had our backs throughout the entire process.

We learned from the mistakes of Addenda, and did proper market research with hala prior to launching it. We are no longer interested in building solutions looking for a problem. We want to revolutionize insurance from the ground up.

We were blessed with a phenomenal team that adapted within seconds to the news, and independently upskilled themselves to match roles needed for a B2C startup. For example, our B2B account manager (originally an electrical engineer) immediately took up a digital marketing course and today handles social media and content marketing.

Others told us we'd never be able to make it. VCs advised us that this is career suicide for a B2B startup raising series A. Today we have 23 people and we're breaking records month-on-month, every month.

If startup success is fire, pivoting is gasoline.
