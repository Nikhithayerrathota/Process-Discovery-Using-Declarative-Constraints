# Incremental Process Discovery Using Declarative Constraints

Prototype developed for a Master’s Thesis.

This project investigates how the **incremental evolution of declarative constraints** influences procedural process discovery. The implementation is developed in Python using **PM4Py** and integrates the **Multi-Perspective Declare Log Generator** for event log generation from DECLARE specifications.

---

## 1. Research Objective

The research studies how controlled modifications of declarative constraint sets affect the resulting procedural models discovered from generated event logs.

The focus lies on the formal incremental construction of declarative rule sets and their validation prior to event log synthesis.

---

## 2. Conceptual Framework

Let:

- **R_base** → Initial DECLARE specification extracted from a sound WF-net  
- **R_existing** → Relaxed version of the base constraints  
- **R_new^inc** → Incrementally injected constraints  

### Trial Rule Construction

The incremental trial rule set is formally defined as:

\[
R_{trial} = R_{existing} \cup R_{new}^{inc}
\]

The rule set is validated using MP-Declare:

- If traces can be generated → the model is **consistent**
- The validated specification is exported as `model.decl`

---

## 3. Processing Pipeline

The complete workflow is:


BPMN
↓
WF-net
↓
DECLARE extraction
↓
Constraint relaxation
↓
Incremental rule injection
↓
Consistency check (MP-Declare)
↓
Event log generation (Alloy)
↓
Inductive Miner (PM4Py)
↓
Discovered WF-net


---

## 4. Generated Artifacts

The system produces:

- `model_from_bpmn.pnml` → WF-net derived from BPMN  
- `generated_log.xes` → Event log generated from DECLARE model  
- `discovered_model.pnml` → Process model discovered using Inductive Miner  

---

## 5. External Tools and Dependencies

### Core Requirements

- Python 3.x  
- PM4Py  
- Java  
- Multi-Perspective Declare Log Generator  

Install PM4Py:

```bash
pip install pm4py
Multi-Perspective Declare Log Generator

The project requires the tool described in:

Skydanienko, V., Di Francescomarino, C., Ghidini, C., & Maggi, F. M.
“A tool for generating event logs from multi-perspective Declare models,”
BPM 2017 Demonstration Track, LNCS 10445, Springer, 2017.

Tool: Multi-Perspective Declare Log Generator

Demo video: Watch here

Wizard Algorithm

The DECLARE extraction step adopts the wizard algorithm proposed in:

Barbaro, L., Varricchione, G., Montalti, M., & Di Ciccio, C. (2022).
From Sound Workflow Nets to LTLf Declarative Specifications by Casting Three Spells.

This algorithm is used in the DECLARE specification extraction phase.

6. Execution

Configure tool paths inside main.py

Run:

python main.py
7. Research Contribution

This work provides:

A formal construction of incremental declarative rule evolution

A controlled validation strategy for consistency checking

An integrated pipeline connecting declarative modeling, event log synthesis, and procedural discovery

Empirical observation of how constraint relaxation and incremental injection influence discovered WF-nets

The central formal contribution is the incremental trial construction:

𝑅
𝑡
𝑟
𝑖
𝑎
𝑙
=
𝑅
𝑒
𝑥
𝑖
𝑠
𝑡
𝑖
𝑛
𝑔
∪
𝑅
𝑛
𝑒
𝑤
𝑖
𝑛
𝑐
R
trial
	​

=R
existing
	​

∪R
new
inc
	​


---

This is now structured for easy copying and pasting. You can use it in your project as a clean, professional README.
give in proper markup launguage

Here's your properly formatted README in Markdown for use in your project repository. You can copy and paste this directly into your README.md file:

# Incremental Process Discovery Using Declarative Constraints

Prototype developed for a Master’s Thesis.

This project investigates how the **incremental evolution of declarative constraints** influences procedural process discovery. The implementation is developed in Python using **PM4Py** and integrates the **Multi-Perspective Declare Log Generator** for event log generation from DECLARE specifications.

---

## 1. Research Objective

The research studies how controlled modifications of declarative constraint sets affect the resulting procedural models discovered from generated event logs.

The focus lies on the formal incremental construction of declarative rule sets and their validation prior to event log synthesis.

---

## 2. Conceptual Framework

Let:

- **R_base** → Initial DECLARE specification extracted from a sound WF-net  
- **R_existing** → Relaxed version of the base constraints  
- **R_new^inc** → Incrementally injected constraints  

### Trial Rule Construction

The incremental trial rule set is formally defined as:


R_trial = R_existing ∪ R_new^inc


The rule set is validated using MP-Declare:

- If traces can be generated → the model is **consistent**
- The validated specification is exported as `model.decl`

---

## 3. Processing Pipeline

The complete workflow is:


BPMN
↓
WF-net
↓
DECLARE extraction
↓
Constraint relaxation
↓
Incremental rule injection
↓
Consistency check (MP-Declare)
↓
Event log generation (Alloy)
↓
Inductive Miner (PM4Py)
↓
Discovered WF-net


---

## 4. Generated Artifacts

The system produces:

- `model_from_bpmn.pnml` → WF-net derived from BPMN  
- `generated_log.xes` → Event log generated from DECLARE model  
- `discovered_model.pnml` → Process model discovered using Inductive Miner  

---

## 5. External Tools and Dependencies

### Core Requirements

- Python 3.x  
- PM4Py  
- Java  
- Multi-Perspective Declare Log Generator  

Install PM4Py:

```bash
pip install pm4py
Multi-Perspective Declare Log Generator

The project requires the tool described in:

Skydanienko, V., Di Francescomarino, C., Ghidini, C., & Maggi, F. M.
“A tool for generating event logs from multi-perspective Declare models,”
BPM 2017 Demonstration Track, LNCS 10445, Springer, 2017.

Tool: Multi-Perspective Declare Log Generator

Demo video: Watch here

Wizard Algorithm

The DECLARE extraction step adopts the wizard algorithm proposed in:

Barbaro, L., Varricchione, G., Montalti, M., & Di Ciccio, C. (2022).
From Sound Workflow Nets to LTLf Declarative Specifications by Casting Three Spells.

This algorithm is used in the DECLARE specification extraction phase.

6. Execution

Configure tool paths inside main.py

Run:

python main.py
7. Research Contribution

This work provides:

A formal construction of incremental declarative rule evolution

A controlled validation strategy for consistency checking

An integrated pipeline connecting declarative modeling, event log synthesis, and procedural discovery

Empirical observation of how constraint relaxation and incremental injection influence discovered WF-nets

The central formal contribution is the incremental trial construction:

R_trial = R_existing ∪ R_new^inc
