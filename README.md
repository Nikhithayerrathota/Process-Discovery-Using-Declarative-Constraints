Incremental Process Discovery Using Declarative Constraints
1. Introduction

This repository contains the full prototype developed for the master thesis:

Incremental Process Discovery Using Declarative Constraints

The objective of this work is to investigate how incremental evolution of declarative constraints affects procedural process discovery.

The implementation is developed in Python using PM4Py and integrates the Alloy Log Generator for event log generation from DECLARE specifications.

2. Conceptual Framework
Base Rule Extraction (R_base)

A Wizard-based mechanism is used to extract an initial DECLARE specification from domain knowledge or from a procedural model.

R_base represents the core behavioral constraints of the imperative process model in declarative form.

Relaxation of the Base Rule Set

R_base is relaxed with respect to new rules.

The relaxed constraint set is denoted as:

R_existing

Incremental Injection of New Rules (R_new)

Additional constraints are introduced incrementally:

R_new^inc

Construction of the Trial Rule Set

R_trial = R_existing ∪ R_new^inc

Where:

R_existing = relaxed base constraint set

R_new^inc = incrementally injected new constraints

R_trial = temporary rule set used for consistency checking

Consistency Verification

R_trial is exported as a .decl file and validated in MP-Declare.

If valid traces are generated, the rule set is consistent.

If 0 traces are generated, inconsistency is detected.

Final DECLARE Specification

Once consistency is ensured, the validated rule set is exported as:

model.decl

3. Event Log Generation

The final DECLARE specification is used by:

AlloyLogGenerator.jar

Configuration:

Minimum trace length: 1

Maximum trace length: 50

Number of traces: 20

Vacuity: enabled

Output:

generated_log.xes

Timestamps are programmatically added.

4. Procedural Process Discovery

Using the Inductive Miner from PM4Py:

Convert BPMN to WF-net

Import generated XES log

Repair timestamps

Apply Inductive Miner

Export discovered WF-net in PNML format

5. Pipeline Overview

BPMN
→ WF-net
→ R_base
→ R_existing
→ R_new^inc
→ R_trial
→ Consistency check
→ DECLARE model
→ Event log generation
→ Inductive Miner
→ Discovered WF-net

6. Generated Artifacts

model_from_bpmn.pnml

generated_log.xes

discovered_model.pnml

7. Requirements

Python 3.x

PM4Py

Java

8. Execution

Configure paths in main.py and run:

python main.py

9. Research Contribution

Incremental process discovery using declarative constraints.

Formal construction:

R_trial = R_existing ∪ R_new^inc
