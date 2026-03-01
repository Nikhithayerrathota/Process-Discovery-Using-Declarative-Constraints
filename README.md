# Incremental Process Discovery Using Declarative Constraints

Prototype developed for the Master Thesis:

Incremental Process Discovery Using Declarative Constraints

This project investigates how incremental evolution of declarative constraints affects procedural process discovery.
The implementation is developed in Python using PM4Py and integrates the Alloy Log Generator for event log generation from DECLARE specifications.

## Conceptual Framework

- Extract initial DECLARE specification → R_base
- Relax constraints → R_existing
- Incrementally inject new rules → R_new^inc

Trial rule construction:

R_trial = R_existing ∪ R_new^inc

The trial rule set is validated in MP-Declare. If traces are generated, the model is consistent. The validated specification is exported as model.decl.

## Pipeline

BPMN
→ WF-net
→ DECLARE extraction
→ Constraint relaxation
→ Incremental rule injection
→ Consistency check
→ Event log generation (Alloy)
→ Inductive Miner (PM4Py)
→ Discovered WF-net

## Generated Artifacts

- model_from_bpmn.pnml
- generated_log.xes
- discovered_model.pnml

## Requirements

- Python 3.x
- PM4Py
- Java
- Multi-Perspective Declare Log Generator tool
  (Skydanienko et al., BPM 2017)

  ## External Tool

The project requires the tool described in:

Skydanienko, V., Di Francescomarino, C., Ghidini, C., & Maggi, F. M.
"A tool for generating event logs from multi-perspective Declare models,"
BPM 2017 Demonstration Track, LNCS 10445, Springer, 2017.

Tool download: https://tinyurl.com/y9uqnfok

Demo video: https://youtu.be/e4q_ThtY70E

Install dependency:

pip install pm4py

## Execution

Configure paths in main.py and run:

python main.py

## Research Contribution

Formal construction of the incremental trial rule set:

R_trial = R_existing ∪ R_new^inc
