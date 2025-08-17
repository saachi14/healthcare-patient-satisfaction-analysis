# healthcare-patient-satisfaction-analysis
Data Storytelling with LLMs for Healthcare Performance Analysis
Patient Satisfaction 2024 — Executive Data Story (README)

Contact: 22f3002903@ds.study.iitm.ac.in

1) Key Findings from the Analysis

Dataset (2024):
Q1 -0.01, Q2 1.10, Q3 7.92, Q4 6.62
Current Average (2024): 3.91
Industry Benchmark Target: 4.50

Overall trajectory: Steep climb from Q1 to Q3, followed by a drop in Q4.

Low: Q1 at -0.01 (signals severe dissatisfaction early in the year).

High: Q3 at 7.92 (best quarter; suggests successful interventions mid-year).

Regression: Q4 at 6.62 (still strong vs. early year, but down 1.30 points from Q3).

Average vs. Target: The current average is 3.91, which is 0.59 points below the 4.5 benchmark—indicating performance is below industry expectations despite mid-year gains.

Pattern to note: The Q2→Q3 surge and Q3→Q4 slip imply improvements may be initiative-dependent (e.g., a campaign or staffing push) and not yet stable or embedded in routine operations.

Volatility risk: Wide spread (range 7.93 points from Q1 to Q3) suggests inconsistent patient experience across time—likely reflecting variability in wait times, staffing, or process reliability.

2) Business Implications of the Current Trend

Patient Retention & Referrals: With an average of 3.91, patients are less likely to return and less likely to recommend—pressuring lifetime value and organic growth.

Reputation & Market Position: Persistently sub-benchmark scores risk negative reviews and brand erosion, making acquisition more expensive and slower.

Financial Impact: Lower satisfaction increases no-shows, cancellations, and leakage to competitors, while also inviting penalties or lower reimbursements where experience-linked incentives apply.

Operational Strain: Variability (Q3 peak vs. Q4 dip) signals process fragility—when volume or staffing fluctuates, experience deteriorates, leading to more escalations and higher service recovery costs.

3) Recommendations to Reach the Target (4.5)

Goal: Lift the current average (3.91) to ≥4.5 and stabilize quarter-to-quarter performance by focusing on service quality and wait times.

A) Reduce Wait Times (Access & Throughput)

Predictive scheduling & capacity smoothing

Use historical arrival patterns to set slot length, buffer blocks, and staggered start times.

Create a fast-track lane for brief visits (e.g., injections, lab draws).

Real-time queue visibility

Deploy live wait-time boards (in-clinic + patient portal) and offer SMS updates; set expectations proactively.

Enable self-check-in kiosks + pre-visit intake (forms, insurance, consent) to cut front-desk dwell time.

Throughput huddles & bottleneck playbooks

Twice-daily huddles to anticipate peaks and reassign staff.

Escalation triggers (e.g., if median door-to-room exceeds 12 min for 30 min, call float staff, open overflow rooms).

Appointment integrity

Overbooking rules driven by no-show propensity models—avoid blanket overbooking.

Reminder cadence (T-72h, T-24h, T-3h) with easy confirm/reschedule links.

KPIs (weekly): Median door-to-room time; 90th-percentile wait; % on-time starts; abandonment rate.

B) Elevate Service Quality (Consistency & Empathy)

Standardize the “First 5 Minutes”

Scripted warm greeting, name use, purpose, time expectation, and a pain/comfort check.

Visual ID (role badges) to reduce confusion and repeat explanations.

Teach-Back & Closure

Require teach-back before discharge; end with “Did we answer everything today?” plus a printed/portal After-Visit Summary.

Service Recovery, on the spot

AIDET/HEART techniques for complaints; empower staff with small recovery tokens (e.g., parking vouchers, beverage tickets) tied to a brief form for learning capture.

Micro-coaching from real feedback

Daily review of 3–5 comments per team in huddle; pick 1 behavior to practice (e.g., knock + eye contact).

Peer shadowing of high performers identified from Q3-like days.

KPIs (weekly): Communication/composure sub-scores; % teach-back documented; # same-day recoveries; complaint closure time.

C) Make Improvements Stick (Governance & Feedback Loops)

Quarterly “Experience Control Plan”

Lock in the Q3 playbook: staffing ratios, rooming sequence, pre-visit tasks. Treat deviations as controlled experiments with pre-defined metrics.

Mini-surveys at Critical Moments

1–2 question touchpoint SMS (post check-in, post-rooming, post-discharge) to isolate where satisfaction drops.

Transparency & Recognition

Publish unit-level dashboards; recognize teams that hit median wait targets and ≥4.5 satisfaction.

Cross-functional “SWAT” for peak hours

Rotating team (ops, nursing, front desk, IT) on call for throughput anomalies (EHR slowness, room turnover delays, lab backlogs).

4) Targets & Timeline

Next 30 days (stabilize):

Stand up real-time wait dashboards, pre-visit intake, and huddle playbook.

Aim: Median wait −15%, communication sub-score +0.3.

60–90 days (lift performance):

Implement predictive scheduling, fast-track, and service-recovery toolkit.

Aim: Average ≥4.3, sustained Q/Q improvement.

By year-end (hit & hold):

Average ≥4.5 with ≤0.4 quarter-to-quarter variance.

Hardwire control plan; publish unit scorecards monthly.

5) What to Watch (Leading Indicators)

Access: Median/90th-percentile wait times; % visits starting within 10 minutes of scheduled time.

Quality behaviors: % encounters with teach-back; adherence to First-5-Minutes script.

Recovery: Same-day resolution rate; time to closure; recurrence of issues.

Outcome: Patient Satisfaction Average (currently 3.91) vs. Target 4.5 by unit and provider.

6) Appendix — Data & Notes

Source values (2024): Q1 -0.01, Q2 1.10, Q3 7.92, Q4 6.62.

Average: 3.91 (arithmetic mean of the four quarterly scores).

Interpretation caution: A negative Q1 suggests either a scaled metric or extreme dissatisfaction; confirm scale definition and survey method to ensure comparability across quarters.

Visualization: Pair this README with a simple line chart of quarterly scores plus horizontal lines for the 4.5 target and the 3.91 average to communicate gap and volatility at a glance.

Executive Takeaway

Despite impressive mid-year gains, the average of 3.91 is below the 4.5 benchmark. Closing the gap requires faster, more predictable access and consistent service behaviors. The plan above focuses on shortening waits, standardizing key moments, and embedding successful Q3 practices so performance is repeatable, not episodic.
