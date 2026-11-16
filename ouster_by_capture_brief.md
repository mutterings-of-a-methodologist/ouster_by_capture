# Ouster by Capture: Does AI Pacing and Transparency Advantage Authoritarian Survival?

This brief asks whether it could be in an authoritarian leader's own interest to join an international agreement that slows and opens up frontier AI, because doing so protects the leader from being removed from power. It also asks when that logic breaks down. The model builds on the selectorate framework used in *Falling Currencies and Leaders: Do Economic Credentials Prevent Leader Removal in the Wake of Currency Crises?* (Chaudhri, 2014), adapting Bueno de Mesquita et al.'s ideas about coalitions to frontier AI governance. Frontier AI is treated as an additional actor in the contest for power, which is why the analysis uses a 2x2 strategic-form game.

**In plain terms:** powerful AI that nobody can inspect can be turned against the person in charge. A rival inside the regime can use it, so can a foreign government, so can ordinary citizens, and the AI itself can slip out of control. An agreement that slows AI and makes it inspectable may lower those risks, at the price of giving up secret advantages. The model asks when that trade is worth it.

**A note on the title:** "capture" here means capable AI ending up under someone else's control instead of the leader's, whether that someone is an insider, a foreign rival, the public, or the AI itself.

*The formal model is set out in the Technical Appendix at the end of this brief.*

## A Short Primer on Selectorate Theory

Selectorate theory (Bueno de Mesquita, Smith, Siverson, and Morrow, *The Logic of Political Survival*, 2003) explains how leaders stay in power by asking who they depend on. Every leader answers to two nested groups. The **selectorate** is everyone with a say in choosing the leader. The **winning coalition** is the smaller group whose support the leader actually needs to stay in office. To survive, the leader must keep that coalition satisfied, and there are two ways to do it: provide **public goods** that everyone enjoys, or hand out **private rewards** that only coalition members receive.

The size of the coalition relative to the selectorate drives the choice. When the coalition is small, private rewards are cheap and effective, and backers stay loyal because they would probably be left out of a challenger's coalition. When the coalition is large, private rewards become too costly to spread around, so leaders rely on public goods. That is why leaders of large-coalition systems (democracies) and small-coalition systems (many autocracies) behave differently, and why losing power costs them different things.

**Core variables of selectorate theory**

| Term | Symbol | Plain meaning |
|---|---|---|
| Selectorate | $S$ | Everyone with a formal say in choosing the leader (voters in a democracy; a party or elite pool in a dictatorship) |
| Winning coalition | $W$ | The essential backers the leader must keep satisfied to stay in office |
| Loyalty norm | $\lambda = W/S$ | The chance that a current coalition member would also be in a challenger's coalition; a low value means backers have more to lose from a change |
| Private rents | $g$ | Perks and patronage paid only to coalition members |
| Public goods | $x$ | Benefits shared by everyone (growth, stability, services) |

**What this brief adds for frontier AI**

| Term | Symbol | Plain meaning | In the app |
|---|---|---|---|
| Treaty choice | $\tau$ | $\tau = 1$: join the pacing and transparency pact; $\tau = 0$: covertly race | Row choice in the 2x2 |
| AI capability | $A_\tau$ | How advanced the leader's AI is under each choice | Built-in setting |
| AI opaqueness | $\omega_\tau$ | How hidden and unguarded frontier AI is | Slider |
| Oversight capacity | $\kappa_{\text{gov}}$ | The state's ability to monitor its own labs and security forces | Slider |
| Compliance cost | $c_{\text{treaty}}$ | Sovereignty and compliance cost of joining the pact | Built-in setting |
| Removal risk | $h_k$ | Chance of removal through channel $k$ (insider, foreign, people, autonomous AI) | Computed |
| Detection probability | $p$ | Chance that covert racing or cheating is caught | Slider |
| Discount factor | $\delta$ | How much the leader values the future versus the present | Slider |
| Racing gain | $B_{\text{race}}$ | Short-term payoff from covertly racing | Built-in setting |
| Sanction | $\mathcal{P}_{\text{defection}}$ | Punishment if defection is detected | Built-in setting |
| Capability-adjustment share | $\eta_\tau$ | Share of the leader's goods affected by the capability path | Built-in setting |
| Goods multipliers | $\alpha_x, \alpha_g$ | How much the leader's public and private goods are scaled by that adjustment | Built-in setting |
| Post-ouster AI disruption | $\phi_{\text{ai}}$ | Extra loss after removal when AI disrupts how rents are allocated | Built-in setting |

## Decision Path and Strategic-Form Setup

The underlying selectorate timeline follows the survival logic from the earlier paper:

1. An incumbent leader chooses whether to **join** an international AI pacing and transparency pact (capped AI capability, less hidden AI, and a compliance and sovereignty cost) or to **defect** into a covert AI race (more capable and more hidden AI, with a short-term gain but a risk of being caught).
2. A challenger decides whether to leave the incumbent in place (`Keep`) or move to remove them (`Oust`). The app lets you switch between four kinds of challenger: (a) a domestic insider coup, (b) foreign outsider subversion, (c) a mass uprising by the people, or (d) an autonomous AI override.
3. The leader is kept or removed, and payoffs follow across the selectorate.

The model keeps Bueno de Mesquita et al.'s core ingredients (see the primer), with the simplifications used in the earlier paper: public goods are close to zero in entrenched autocracies, and private rents are close to zero in established democracies.

**Regime presets.** The app starts from four illustrative presets so the mechanism is visible at once. They are starting points, not estimates, and every slider value can be changed.

* *Entrenched Autocracy (China/Russia style):* a small winning coalition, a larger party and bureaucratic selectorate (low loyalty norm), high private rents, low public goods.
* *Fledgling / Tenuous Autocracy (Syria style, pre-2024):* a tiny winning coalition, a small selectorate (fragile loyalty norm), high private rents but a strained fiscal base, and weak institutional oversight.
* *Established Democracy:* a near-universal selectorate, a winning coalition of about half of it (loyalty norm near 0.5), high public goods, and almost no private rents.
* *Fledgling / Inchoate Democracy:* a large selectorate, a contested winning coalition, mixed public and private goods, and weaker institutional guardrails.

## How the Model Works

**Four ways a leader can be removed.**

* **(a) Insider ouster:** regime insiders use unguarded AI tools, or AI-weakened monitoring, to replace the incumbent.
* **(b) Outsider ouster:** a foreign sponsor backs a challenger or deploys external tools and subversion.
* **(c) People ouster:** mass mobilization succeeds, helped by AI-enabled coordination and information tools.
* **(d) Autonomous AI ouster:** a "country of geniuses in a datacenter" crosses an autonomy or control threshold and displaces the incumbent directly, bypassing the human buy-offs that keep a selectorate loyal.

**Risk of removal.** Each channel's risk rises with how capable and how hidden frontier AI is, and falls with the state's capacity to oversee its own labs and security forces. Oversight capacity is higher under transparency in regimes that have oversight institutions, and constrained under opaque racing. The four risks combine into one overall chance that the leader is removed or kept in the period (Appendix, Sections A and B).

**What the leader gets.** Staying in power pays the leader's goods, adjusted for the cost of the capability path (and for the compliance cost under the pact). Being removed leaves the leader at a reference payoff anchored by the loyalty norm, less any disruption AI causes after the ouster, especially when an autonomous AI or a foreign sponsor takes over how rents are allocated. The leader's net gain from surviving is the gap between the two (Appendix, Section C).

**When joining is preferred.** The leader compares expected utility under each path: the chance of staying times what staying pays, plus the chance of removal times what removal pays. Joining is preferred whenever it yields the higher expected utility. In the simple case where surviving is worth more than being removed, and about the same under both paths, the question reduces to whether joining raises the chance of staying in power. To first order it does when the risk removed by lower capability and less hidden AI, together with the oversight added, outweighs everything else the pact changes (Appendix, Section D).

**Cheating and compliance.** If the interaction repeats, covert racing brings a short-term gain but risks punishment if caught. Compliance holds when the leader is patient enough (the discount factor is above a threshold, $\delta^*$) and the chance of being caught is high enough (detection is above a threshold, $p^*$) (Appendix, Section E).

**The interactive 2x2.** Each cell pairs the leader's choice (join or race) with the selected challenger's choice (keep or oust), reports the payoffs for each side and the pure-strategy Nash equilibria, and shows the multi-channel expected utility alongside (Appendix, Section F).

## Implications for China and Conditions Where Pacing Fails

As an illustration, China maps to the entrenched autocracy profile: a small winning coalition, a larger party-state selectorate (low loyalty norm), high private rents, and low public goods. Because rents are concentrated in a narrow coalition, removal costs the leader a lot. At the same time, hidden frontier AI raises the risk of removal from domestic insiders, foreign rivals, mass mobilization, and autonomous AI override. The autonomous channel cannot be neutralized through loyalty norms or rent distribution. When joining raises the leader's chance of staying in power and both thresholds are met (enough patience, enough detection), adhering to AI pacing and transparency is a rational best response for a leader in this position.

Pacing fails to advantage an entrenched autocrat when:

1. **There is little hidden AI, or control is already strong.** If the pact removes little opaqueness, or existing party-state monitoring already contains internal threats, the gain in survival odds shrinks or turns negative, while racing gains and compliance costs favor racing.
2. **The horizon is short.** Acute regime insecurity or rapid capability shifts can make a leader discount future survival losses so heavily that immediate covert gains win out.
3. **Verification or sanctions are weak.** If covert defection is unlikely to be detected or penalized, defection stays attractive unless the survival gains alone make joining preferable.
4. **Institutional oversight is weak.** Formal transparency does not reduce hidden AI or suppress insider and autonomous risks if the regime lacks the capacity to audit its labs and security organs.
5. **A "loyalty lock" protects against insiders.** A very small coalition relative to the selectorate, paired with high rents, can deter domestic insiders from backing a challenger, for fear of losing their rents, and so temporarily mute the insider channel. Autonomous AI risk remains unbuyable through the loyalty norm.

## Scope and Caveats

To use this framework responsibly in policy and research settings, its boundaries need to be explicit.

* **What it is:** a conditional theoretical mechanism. It shows when hidden frontier capabilities create survival risks that can make pacing self-enforcing for an entrenched autocrat. It does not forecast that Beijing, or any other regime, will adopt or comply with an agreement.
* **Parameter values:** the hazard weights, the adjustment multipliers, the compliance cost, the post-ouster disruption term, and the racing parameters (gain and sanction) are stylized calibrations for sensitivity analysis, not empirical estimates. The app starts from illustrative presets and every slider can be changed.
* **One challenger at a time:** the 2x2 isolates a single challenger, while the overall chance of staying in power combines all four channels. The two views can therefore occasionally point in different directions.
* **When surviving is not clearly worth more than leaving:** the simple reduction in Appendix Section D assumes the net gain from surviving is positive. Where public goods are shared by everyone (as in the democratic presets), the leader may lose little from removal, and expected utility then reflects payoff levels more than survival odds.
* **Autonomous AI:** it is treated as a reduced-form risk, not as a strategic agent.

---

## Technical Appendix

Notation follows the variable tables above. Throughout, $\tau \in \{0, 1\}$ and $\theta = (W, S, x, g, \kappa_{\text{gov}})$.

### A. Removal hazards

For each channel $k \in \{a, b, c, d\}$:

$$
h_k(\theta, \tau) = \min\!\left(1,\, \max\!\left(0,\, \bar{h}_k(\theta) + \beta_k A_\tau + \gamma_k \omega_\tau - \mu_k \kappa_{\text{gov}}(\tau)\right)\right)
$$

Here $\bar{h}_k(\theta)$ is the baseline hazard for channel $k$, and $\beta_k$, $\gamma_k$, $\mu_k$ are channel-specific weights on capability, opaqueness, and oversight. Oversight capacity $\kappa_{\text{gov}}(\tau)$ is higher under transparency ($\tau = 1$) in regimes with oversight institutions, and constrained under opaque racing ($\tau = 0$).

### B. Overall removal and retention

$$
\Pi_{\text{ouster}}(\theta, \tau) = 1 - \prod_{k \in \{a,b,c,d\}} \left(1 - h_k(\theta, \tau)\right), \qquad \Pi_{\text{keep}}(\theta, \tau) = 1 - \Pi_{\text{ouster}}(\theta, \tau)
$$

### C. Payoffs

Retention payoff, following the Keep-versus-Oust structure of the earlier paper:

$$
U_{\text{keep}}(\theta, \tau) = (1 - \eta_\tau)(x + g) + \eta_\tau(\alpha_x x + \alpha_g g) - c_{\text{treaty}}\tau
$$

Post-ouster reference payoff, anchored by the loyalty norm and reduced by post-ouster AI disruption:

$$
U_{\text{oust}}(\theta, \tau) = x + g \cdot \frac{W}{S} - \phi_{\text{ai}}(\theta, \tau)
$$

Net gain from surviving:

$$
\Delta U(\theta, \tau) \equiv U_{\text{keep}}(\theta, \tau) - U_{\text{oust}}(\theta, \tau)
$$

### D. Expected utility and the decision rule

$$
V(\theta, \tau) = \Pi_{\text{keep}}(\theta, \tau)\, U_{\text{keep}}(\theta, \tau) + \Pi_{\text{ouster}}(\theta, \tau)\, U_{\text{oust}}(\theta, \tau) = U_{\text{oust}}(\theta, \tau) + \Pi_{\text{keep}}(\theta, \tau)\,\Delta U(\theta, \tau)
$$

Joining is preferred to covert racing (higher expected utility) whenever

$$
V(\theta, 1) > V(\theta, 0).
$$

Define $\Delta \Pi_{\text{keep}} \equiv \Pi_{\text{keep}}(\theta, 1) - \Pi_{\text{keep}}(\theta, 0) = \Pi_{\text{ouster}}(\theta, 0) - \Pi_{\text{ouster}}(\theta, 1)$. If $\Delta U(\theta, 1) \approx \Delta U(\theta, 0) = \Delta U > 0$, the condition reduces to $\Delta \Pi_{\text{keep}} > 0$. To first order (small hazards, ignoring clipping at 0 and 1), measuring the changes in capability and opaqueness as racing minus pacing and the change in oversight as pacing minus racing:

$$
\Delta \Pi_{\text{keep}} \approx \sum_{k \in \{a,b,c,d\}} \left[\beta_k (A_0 - A_1) + \gamma_k (\omega_0 - \omega_1) + \mu_k \left(\kappa_{\text{gov}}(1) - \kappa_{\text{gov}}(0)\right)\right] > 0
$$

### E. Compliance thresholds

Suppose the interaction repeats with discount factor $\delta \in (0,1)$ and detection probability $p \in [0,1]$. Covert defection yields a short-term racing gain $B_{\text{race}}$ but risks sanctions $\mathcal{P}_{\text{defection}}(\theta)$ with probability $p$. Compliance ($\tau = 1$) holds when

$$
\delta \ge \delta^*(\theta, p) \equiv \frac{B_{\text{race}} + \left[\Pi_{\text{keep}}(\theta, 0)\Delta U(\theta, 0) - \Pi_{\text{keep}}(\theta, 1)\Delta U(\theta, 1)\right]}{B_{\text{race}} + p \cdot \mathcal{P}_{\text{defection}}(\theta)}
$$

and the minimum detection probability needed to deter covert defection is

$$
p^*(\theta, \delta) = \frac{B_{\text{race}} + \left[\Pi_{\text{keep}}(\theta, 0)\Delta U(\theta, 0) - \Pi_{\text{keep}}(\theta, 1)\Delta U(\theta, 1)\right] - \delta B_{\text{race}}}{\delta \, \mathcal{P}_{\text{defection}}(\theta)}.
$$

### F. The 2x2 display

Each cell pairs the leader's choice ($\tau = 1$ or $\tau = 0$) with the selected challenger's choice (`Keep` or `Oust`) and reports the payoffs $(U_{\text{Leader}}, U_{\text{Challenger}})$ and the pure-strategy Nash equilibria, alongside the multi-channel expected utility $V(\theta, \tau)$.
