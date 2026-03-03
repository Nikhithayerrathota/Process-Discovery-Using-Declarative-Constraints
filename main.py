import os
import subprocess
from datetime import datetime, timedelta
import pm4py
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.exporter.xes import exporter as xes_exporter
from pm4py.algo.evaluation.replay_fitness import algorithm as fitness_evaluator
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator
from pm4py.algo.evaluation.generalization import algorithm as generalization_evaluator
from pm4py.algo.evaluation.simplicity import algorithm as simplicity_evaluator

# ---- paths ----
base_dir = r"C:\Users\I543203\Downloads\Masters-Thesis-Experiement-Results-main\Masters-Thesis-Experiement-Results-main\BPMN5"
download_dir = r"C:\Users\I543203\Downloads\Masters-Thesis-Experiement-Results-main\Masters-Thesis-Experiement-Results-main\BPMN5"

bpmn_file = os.path.join(base_dir, "BPMN5.bpmn")
decl_file = os.path.join(base_dir, "BPMN5.decl")
alloy_jar = os.path.join(download_dir, "AlloyLogGenerator.jar")

pnml_from_bpmn = os.path.join(base_dir, "BPMN5.pnml")
generated_log = os.path.join(base_dir, "generated_log.xes")
discovered_pnml = os.path.join(base_dir, "discovered_model.pnml")


# 1) BPMN → Petri Net
print("\nConverting BPMN to Petri net...")
bpmn = pm4py.read_bpmn(bpmn_file)
net, im, fm = pm4py.convert_to_petri_net(bpmn)
pm4py.write_pnml(net, im, fm, pnml_from_bpmn)
pm4py.view_petri_net(net, im, fm)


# 2) DECLARE → Log (Alloy)
print("\nGenerating event log from DECLARE...")
cmd = [
    "java", "-jar", alloy_jar,
    "1", "50", "20",
    decl_file, generated_log,
    "-vacuity",
    "-shuffle", "1",
    "-is", "1",
    "-msi", "1"
]

result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0:
    print(result.stderr)
    raise RuntimeError("Log generation failed")


# 3) Add timestamps (Inductive Miner needs them)
print("\nAdding timestamps...")
log = xes_importer.apply(generated_log)
start_time = datetime.now()

for t_index, trace in enumerate(log):
    for e_index, event in enumerate(trace):
        event["time:timestamp"] = start_time + timedelta(
            seconds=t_index * 100 + e_index
        )

xes_exporter.apply(log, generated_log)


# 4) Show traces
print("\nLog summary:")
print("Traces:", len(log))
print("Events:", sum(len(t) for t in log))

for i, trace in enumerate(log):
    acts = [e.get("concept:name", "?") for e in trace]
    print(f"Trace {i+1}: {acts}")


# 5) Discover model (Inductive Miner)
print("\nDiscovering model from log...")
tree = pm4py.discover_process_tree_inductive(log)
net2, im2, fm2 = pm4py.convert_to_petri_net(tree)

pm4py.write_pnml(net2, im2, fm2, discovered_pnml)
pm4py.view_petri_net(net2, im2, fm2)

print("\nConstraint Based Workflow Net generated sucessfully .")

print("\nEvaluating discovered WF-net...")

fitness = fitness_evaluator.apply(log, net2, im2, fm2)
precision = precision_evaluator.apply(log, net2, im2, fm2)
generalization = generalization_evaluator.apply(log, net2, im2, fm2)
simplicity = simplicity_evaluator.apply(net2)

print("Fitness:", fitness)
print("Precision:", precision)
print("Generalization:", generalization)
print("Simplicity:", simplicity)
from pm4py.visualization.petri_net import visualizer as pn_visualizer

pdf_path = os.path.join(base_dir, "Final_WF_Net.pdf")

# Create visualization with custom size
gviz = pn_visualizer.apply(
    net2, im2, fm2,
    parameters={
        "format": "pdf",
        "graph_title": "Discovered Workflow Net",
        "rankdir": "LR",          # Left → Right layout
        "bgcolor": "white",
        "fontsize": "20"          # Bigger font
    }
)

pn_visualizer.save(gviz, pdf_path)

print("WF-net exported (large version) to:", pdf_path)
