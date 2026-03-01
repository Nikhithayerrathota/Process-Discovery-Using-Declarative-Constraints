# Incremental Process Discovery Using Declarative Constraints

**Prototype for Master's Thesis**

This project explores how to perform incremental process discovery using declarative constraints, i.e updating any BPMN with the additional behaviour imposed on the process model by using DECLARE constraints.

---

## Research Goal

The research aims to develop an automated, incremental process discovery–based approach for integrating declarative constraints into existing imperative process models while ensuring behavioral compliance and consistency.

---

## Approach

- **R_base**: Extracted DECLARE specification from a sound WF-net using Wizard Algorithm
- **R_existing**: Relaxed base constraints wrt to New rules
- **R_new^inc**: Incremental addition of new constraints   

### Trial Rule Set:
**R_trial = R_existing ∪ R_new^inc**

The rule set is validated through MP-Declare:  
- If traces can be generated, the model is **consistent** and exported as `model.decl` and generates traces, Process discovery inductive miner is applied on generated event log as a result a Constraint based Workflow net is generated, where as incase of inconsistent R_trail results in 0 trace generation which requirs inconsistent resolution techniques qmis is applied as a result qmis based Rediscovered workflow net is generated.

---

## Workflow

1. **BPMN → WF-net → DECLARE extraction(Wizard Algorithm) → Relaxation → Incremental injection → Consistency check (MP-Declare) → Event log (Alloy) → Inductive Miner (PM4Py) → Rediscovered WF-net**

---

## Output Artifacts

- **model_from_bpmn.pnml**: A **WF-net** derived from the BPMN model. This represents the initial workflow structure before any constraints are applied.  
- **generated_log.xes**: An **event log** generated from the DECLARE model, simulating process execution based on the declarative rules.  
- **discovered_model.pnml**: The **discovered process model** created using the **Inductive Miner** algorithm from the generated event log, representing the inferred workflow structure.

---

## Dependencies

- **Python 3.x**  
- **PM4Py**  
- **Java**  
- **Multi-Perspective Declare Log Generator**
- **Wizard Algorithm**

  To install PM4Py, run:


pip install pm4py
Execution

Set the tool paths inside main.py

Run the following command:

python main.py

## Research Contribution

A formal approach to incremental declarative rule evolution

A controlled strategy for consistency validation

An integrated pipeline linking declarative modeling, event log creation, and process discovery
