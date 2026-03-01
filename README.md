# Incremental Process Discovery Using Declarative Constraints

**Prototype for Master's Thesis**

This project explores how incremental changes in declarative constraints affect process discovery. Developed in Python with **PM4Py**, it integrates the **Multi-Perspective Declare Log Generator** to create event logs from DECLARE specifications.

---

## Research Goal

The goal is to study how controlled changes in declarative constraints impact the process models discovered from event logs. The focus is on incrementally building and validating rule sets before log generation.

---

## Approach

- **R_base**: Initial DECLARE specification from a sound WF-net  
- **R_existing**: Relaxed base constraints  
- **R_new^inc**: Incremental constraints added  

### Trial Rule Set:
**R_trial = R_existing ∪ R_new^inc**

The rule set is validated through MP-Declare:  
- If traces can be generated, the model is **consistent** and exported as `model.decl`.

---

## Workflow

1. **BPMN → WF-net → DECLARE extraction → Relaxation → Incremental injection → Consistency check (MP-Declare) → Event log (Alloy) → Inductive Miner (PM4Py) → Discovered WF-net**

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

To install PM4Py, run:

```bash
pip install pm4py
Execution

Set the tool paths inside main.py

Run the following command:

python main.py
**
## Research Contribution**

A formal approach to incremental declarative rule evolution

A controlled strategy for consistency validation

An integrated pipeline linking declarative modeling, event log creation, and process discovery
