# IndiaShield: SIDS Methodology and Parameter Justifications

This document outlines the research framework, parameter calibrations, and strategic justifications behind the **Strategic Import Dependency Score (SIDS)** developed for IndiaShield.

---

## 1. Metric Formulation Refresher

The composite index is calculated per supplier using the following formula:

$$SIDS = \frac{IC}{100} \times SSR \times (1 - GSS) \times \frac{1}{DSC} \times 100$$

*   **Import Concentration ($IC$):** Sourced from SIPRI Arms Transfer TIV database.
*   **Single-Source Risk ($SSR$):** Weighted risk of single-source platform lock-in (having $>60\%$ share in a critical weapon category = $1.0$, $>40\%$ = $0.6$, else $0.2$).
*   **Geopolitical Stability Score ($GSS$):** Supplier alignment reliability ($0.0$ = high risk/sanctioned/hostile, $1.0$ = fully integrated ally).
*   **Domestic Substitution Capacity ($DSC$):** Local indigenisation rate ($0.1$ = irreplaceable / deep lock-in, $1.0$ = immediate domestic replacement).

---

## 2. Supplier Parameter Justifications

### Russia (SIDS: 72.0 - Critical Risk)
*   **Import Concentration ($IC$): 45.0%**
    *   *Justification:* Historically, Russia has been India's primary arms supplier, accounting for nearly half of India's total arms volume (TIV), including major platforms like Su-30MKI fighters, T-90 battle tanks, S-400 air defense systems, and Talwar-class frigates.
*   **Geopolitical Stability ($GSS$): 0.20 (Post-2022) / 0.60 (Pre-2022)**
    *   *Justification:* Pre-2022, Russia was a highly reliable supplier. Post-2022 (following the Ukraine War), Russia's score drops to $0.20$ due to heavy international sanctions (CAATSA risks, exclusion from the SWIFT system complicating bilateral payments), and domestic war demands diverting spare parts away from export agreements.
*   **Substitution Capacity ($DSC$): 0.20**
    *   *Justification:* India is deeply locked into Russian platforms. Over $85\%$ of the active main battle tank inventory (T-72/T-90) and $68\%$ of the fighter fleet (Su-30MKI, MiG-29) rely on Russian OEM parts. Substituting these subsystems domestically or sourcing them from Western allies is extremely difficult due to proprietary designs and technical configurations.

### France (SIDS: 24.0 - Low-Moderate Risk)
*   **Import Concentration ($IC$): 11.0%**
    *   *Justification:* Driven heavily by the recent acquisitions of 36 Rafale multirole fighter jets and the co-production of 6 Scorpene-class submarines.
*   **Geopolitical Stability ($GSS$): 0.85**
    *   *Justification:* France has maintained a highly independent foreign policy and did not join historical embargoes against India (e.g. post-1998 nuclear tests). France is a highly stable, non-interfering strategic partner.
*   **Substitution Capacity ($DSC$): 0.50**
    *   *Justification:* France supplies high-end technology (like Snecma M88 jet engines and advanced sonar/combat suites). While these are highly complex, French suppliers are more open to transfer-of-technology (ToT) agreements than US OEMs, resulting in a moderate domestic substitution rating.

### United States (SIDS: 18.0 - Low Risk)
*   **Import Concentration ($IC$): 9.0%**
    *   *Justification:* Derived from acquisitions of utility/transport aircraft (C-17 Globemaster, C-130J), attack helicopters (AH-64E Apache), and maritime patrol aircraft (P-8I Poseidon).
*   **Geopolitical Stability ($GSS$): 0.90**
    *   *Justification:* High strategic alignment under the Quad framework and India's designation as a Major Defense Partner. Embassy risk is extremely low.
*   **Substitution Capacity ($DSC$): 0.40**
    *   *Justification:* US systems come with rigorous end-user monitoring agreements (CISMOA/BECA) and closed proprietary systems. This makes reverse-engineering or domestic integration of local subsystems nearly impossible, leading to a low-medium substitution rating.

### Israel (SIDS: 38.0 - Moderate Risk)
*   **Import Concentration ($IC$): 9.0%**
    *   *Justification:* Anchored in critical subsystems: Phalcon AEW&C radars, Barak-8 air defense missiles, Heron/Searcher UAVs, and precision-guided munitions.
*   **Geopolitical Stability ($GSS$): 0.70**
    *   *Justification:* Israel is a reliable partner, but its score is moderated to $0.70$ due to its own high exposure to Middle Eastern regional escalations, which can suddenly redirect production capacity to domestic needs.
*   **Substitution Capacity ($DSC$): 0.60**
    *   *Justification:* Israel has co-developed several missiles (e.g., Barak-8) directly with India's DRDO. This collaborative model has successfully established local production lines through Bharat Electronics Limited (BEL), resulting in a higher local substitution capacity.

### United Kingdom (SIDS: 12.0 - Low Risk)
*   **Import Concentration ($IC$): 5.0%**
    *   *Justification:* Mainly comprised of spares and upgrades for older systems, such as the Hawk Advanced Jet Trainers and Sea King helicopters.
*   **Geopolitical Stability ($GSS$): 0.90**
    *   *Justification:* Stable bilateral relations and low geopolitical risk of supply disruptions.
*   **Substitution Capacity ($DSC$): 0.70**
    *   *Justification:* Spares for older UK platforms can be maintained through domestic machining or phased out entirely in favor of indigenous systems (like the HAL HTT-40 and Tejas LCA), resulting in high substitution capacity.
