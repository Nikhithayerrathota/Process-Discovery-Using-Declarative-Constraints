# Incremental Process Discovery Using Declarative Constraints

## 1. Introduction

This repository contains the full prototype developed for the master thesis:

Incremental Process Discovery Using Declarative Constraints

The objective of this work is to investigate how incremental evolution of declarative constraints affects procedural process discovery. The prototype integrates declarative modeling, constraint relaxation, synthetic log generation, and procedural discovery into a unified experimental pipeline.

The implementation is developed in Python using PM4Py and integrates the Alloy Log Generator for event log generation from DECLARE specifications.

---

## 2. Conceptual Framework

### 2.1 Base Rule Extraction (R_base)

A Wizard-based mechanism is used to extract an initial DECLARE specification from domain knowledge or from a procedural model.

This initial constraint set is denoted as:

R_base

R_base represents the core behavioral constraints of the imperative process model in declarative form.

---

### 2.2 Relaxation of the Base Rule Set

To allow additional behavioural constraints _base has to be relaxed wrt to New Rules

The relaxed constraint set is denoted as:

R_existing

R_existing is derived from R_base by performing constraint relaxation wrt to new rules.

---

### 2.3 Incremental Injection of New Rules (R_new)

To model process evolution, additional constraints are introduced:

R_new

Rather than merging all rules at once, the system performs incremental injection. Let:

R_new^inc


---

### 2.4 Construction of the Trial Rule Set

The trial rule set is constructed as the union of the relaxed existing constraints and the incrementally injected rules:

R_trial = R_existing ∪ R_new^inc

Where:

- R_existing = relaxed base constraint set wrt to new rules
- R_new^inc = incrementally injected new constraints
- ∪ = set union operator
- R_trial = temporary rule set used for consistency checking 



---

### Consistency Verification

After constructing the trial rule set

R_trial = R_existing ∪ R_new^inc

a consistency check is performed in the MP-Declare tool.

The rule set R_trial is exported as a `.decl` file and validated under the configured parameters.  

If valid traces are successfully generated, the rule set is considered consistent.

If R_trial generates 0 traces, inconsistency is detected, indicating that the constraint combination is unsatisfiable.

Formally:


### 2.6 Final DECLARE Specification

Once consistency is ensured, the validated rule set is exported as:

model.decl

This DECLARE file becomes the input for event log generation.

---

## 3. Event Log Generation Using Alloy

The final DECLARE specification (.decl file) is used by:

AlloyLogGenerator.jar

Configuration used in this prototype:

- Minimum trace length: 1
- Maximum trace length: 50
- Number of traces: 20
- Vacuity: enabled
- Constraint shuffling iterations: 1
- Interval splits: 1
- Maximum same instances: 1

The output is a synthetic event log:

generated_log.xes

Since Alloy-generated logs may not contain timestamps, timestamps are programmatically added to ensure compatibility with process mining algorithms.

---

## 4. Procedural Process Discovery

The discovered procedural model is obtained using the Inductive Miner from PM4Py.

The procedural discovery pipeline performs:

1. Import BPMN model.
2. Convert BPMN to Workflow Net (WF-net).
3. Import generated XES log.
4. Repair timestamps.
5. Display all traces.
6. Apply Inductive Miner.
7. Convert discovered process tree to WF-net.
8. Export discovered model in PNML format.

---

## 5. Complete Pipeline Overview

Imperative Model (BPMN)  
→ Convert to WF-net  
→ Extract DECLARE specification (R_base)  
→ Relax constraints (R_existing)  
→ Inject R_new incrementally  
→ Construct trial rule set (R_trial = R_existing ∪ R_new^inc)  
→ Check consistency  
→ Export final DECLARE model  
→ Generate event log (Alloy)  
→ Repair log  
→ Apply Inductive Miner  
→ Export discovered WF-net  

---

## 6. Generated Artifacts

The system produces:

- model_from_bpmn.pnml  
  WF-net derived from the BPMN model.

- generated_log.xes  
  Synthetic event log generated from the DECLARE specification.

- discovered_model.pnml  
  WF-net discovered from the generated log.

---

## 7. Technical Requirements

- Python 3.x
- PM4Py
- Java (required for Alloy Log Generator)

Install PM4Py:

pip install pm4py

---

## 8. Execution Instructions

1. Configure file paths in main.py:
   - BPMN file
   - DECLARE file (.decl)
   - AlloyLogGenerator.jar

2. Run:

python main.py

The script executes the complete declarative-to-procedural pipeline.

---

## 9. Research Contribution

This prototype contributes to research in:

- Incremental process discovery using declarative constraints
- consistency checking
The formal construction of the trial rule set:

R_trial = R_existing ∪ R_new^inc

provides a systematic foundation for studying incremental process discovery under declarative constraints.

---

## 10. Author

Master Thesis Prototype  
Incremental Process Discovery Using Declarative Constraints
