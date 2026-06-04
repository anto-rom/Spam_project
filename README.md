# Spam Detection Rules – Agentforce

## Overview
This repository contains rule-based logic and regex patterns to automatically classify and close spam emails in Agentforce / Salesforce.

The solution is designed as a hybrid approach:
- Rule-based classification (high precision)
- Regex pattern matching (flexibility)
- Optional scoring model (future-ready)

---

## Architecture

1. Incoming Email
2. Rule Evaluation (JSON rules)
3. Regex Matching
4. Spam Score Calculation
5. Action:
   - Auto-close
   - Route to agent
   - Archive
   - Review queue

---

## Rule Layers

| Layer | Description |
|------|------------|
| High Confidence | Direct spam (auto-close) |
| Domain Rules | Suspicious senders |
| Pattern Matching | Subject/body regex |
| Campaign Detection | Repeated messages |
| Scoring | Final decision |

---

## Usage

Rules are stored in:

- `/config/spam_rules.json`
- `/config/regex_patterns.json`

These can be integrated into:
- Agentforce Flows
- Apex logic
- Python pipelines
- Snowflake SQL

---

## Future Improvements

- ML-based classification
- Language detection
- Behavioral sender scoring
- Real-time campaign detection
