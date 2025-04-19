# Outline for Capstone Report
This page is an outline for the final capstone report. 

## Abstract
Self-explanitory

## Introduction
- brief overview of the purpose of IDS/IPS systems and why they are important
- brief overview of c2 frameworks and how they are used in practice
- explain the purpose of the project and what i am trying to accomplish
- explain how the rest of the report is organized

## Related Works
- talk about the existing research on IDS/IPS systems and their effectiveness

## Data Collection
- explain which frameworks were used
- explain the network topology and why its set up the way it is
- talk about how i captured the traffic

## Feature Extraction
- explain which features were extracted and why (had to rely on individual packets not flows, explain how each feature was calculated)

## Model Training
- explain the training progression (type of classifier, dataset progression, ratio enforcement)

## Model Evaluation/Results
- talk about validation reports
- talk about inference reports

## Comparison of Model and ET Open

- **Data Source**  
  - Both the model and ET Open were tested against the same mixed traffic PCAPs for fairness.
  - Mixed traffic PCAPs contain ~10% C2 packets and ~90% normal traffic.

- **How Suricata + ET Open Works**  
  - Suricata is a signature-based intrusion detection system that uses predefined rules to detect threats.
  - ET Open is a free community-maintained rule set covering various threats, including known C2 frameworks.
  - Rules in ET Open trigger on specific patterns, such as IPs, hostnames, or TLS certificate values seen in prior attacks.

- **Key Limitations of ET Open in This Setup**  
  - Detection depends on the presence of known IOCs, which may not appear in lab-generated traffic.
  - TLS-based rules often rely on hostile domains or cert fingerprints that weren’t used in the lab.
  - No alerts were generated in any mixed PCAP, likely due to benign IPs/hostnames and the lack of threat-specific context.

- **Key Strengths of the Model**  
  - The Random Forest model learns from traffic patterns and behaviors, not just known IOCs.
  - Able to identify malicious behavior even when IPs, domains, and certs are new or benign.
  - Performance varied greatly by framework, but the model produced some degree of results while Suricata did not fire any alerts.

- **Conclusion**  
  - Signature-based detection like ET Open is precise but brittle — it fails when indicators are absent.
  - ML-based approaches generalize better but require careful tuning and validation.
  - These methods are not mutually exclusive and could be combined for more robust detection coverage.

## Areas for Improvement/Future Work

- **Feature Extraction Limitations**
  - Packet-level features lack context, no understanding of sessions or flows.
  - Flow-based features (e.g., duration, byte counts, inter-packet timing) could offer more predictive power.
  - Developing and training on significantly larger flow datasets could improve model performance.

- **Model Architecture**
  - The project used a single Random Forest classifier.
  - Future work could explore deep learning, nural networks, or other ML techniques

- **Suricata Rule Behavior**
  - Results highlight how Suricata rules rely on context-specific signatures.
  - Future testing could involve modifying traffic to simulate known indicators (e.g., hostile TLS certs) to verify rule firing.

- **Combined Detection Approaches**
  - Explore how to combine ML predictions with rule-based alerts.

- **Training with Mixed Traffic**
  - Only a subset of mixed traffic was included in training.
  - Future work could incorporate more of this data or test on unseen environments to better generalize performance.

## Conclusion
- summarize the findings of the project




