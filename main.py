import subprocess
from datetime import datetime, timedelta
import pm4py

from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.exporter.xes import exporter as xes_exporter
from pm4py.objects.log.obj import EventLog


# =========================================================
# FILE PATHS
# =========================================================

BPMN_FILE = r"C:\Users\I543203\Desktop\base\ProcessTreesImplementation - Copy\BPMN4\BPMN4.bpmn"
DECL_FILE = r"C:\Users\I543203\Desktop\base\ProcessTreesImplementation - Copy\BPMN4\bpmn4.1.decl"

ALLOY_JAR = r"C:\Users\I543203\Downloads\gen (2)\AlloyLogGenerator.jar"

MODEL_FROM_BPMN = r"C:\Users\I543203\Desktop\base\ProcessTreesImplementation - Copy\BPMN4\model_from_bpmn.pnml"
GENERATED_LOG = r"C:\Users\I543203\Desktop\base\ProcessTreesImplementation - Copy\BPMN4\generated_log.xes"
DISCOVERED_MODEL = r"C:\Users\I543203\Desktop\base\ProcessTreesImplementation - Copy\BPMN4\discovered_model.pnml"


# =========================================================
# BPMN → WF-net
# =========================================================

def bpmn_to_pnml():
    print("\n[1] BPMN → WF-net")

    bpmn = pm4py.read_bpmn(BPMN_FILE)
    net, im, fm = pm4py.convert_to_petri_net(bpmn)

    pm4py.write_pnml(net, im, fm, MODEL_FROM_BPMN)
    print(" PNML created:", MODEL_FROM_BPMN)

    print("Displaying BPMN-converted PNML...")
    pm4py.view_petri_net(net, im, fm)


# =========================================================
# DECLARE → Trace Generation (Alloy GUI Settings)
# =========================================================

def declare_to_log():
    print("\n[2] DECLARE → XES Log")

    cmd = [
        "java",
        "-jar",
        ALLOY_JAR,
        "1",          # Min trace length
        "50",         # Max trace length
        "20",         # Number of traces
        DECL_FILE,
        GENERATED_LOG,
        "-vacuity",
        "-shuffle", "1",
        "-is", "1",
        "-msi", "1"
    ]

    print("Running command:")
    print(" ".join(cmd))

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError("Log generation failed")

    print(" Log generated:", GENERATED_LOG)


# =========================================================
#  FIX LOG (ADD TIMESTAMPS)
# =========================================================

def fix_xes():
    print("\n[3] Fixing XES (adding timestamps)")

    log = xes_importer.apply(GENERATED_LOG)

    base_time = datetime.now()
    cleaned_log = EventLog()

    for t_index, trace in enumerate(log):

        if len(trace) == 0:
            continue

        for e_index, event in enumerate(trace):
            event["time:timestamp"] = base_time + timedelta(
                seconds=t_index * 100 + e_index
            )

        cleaned_log.append(trace)

    xes_exporter.apply(cleaned_log, GENERATED_LOG)

    print(" Log fixed and exported")


# =========================================================
# DISPLAY ALL 20 TRACES
# =========================================================

def display_log():
    print("\n[4] Displaying Log")

    log = xes_importer.apply(GENERATED_LOG)

    print("Number of traces:", len(log))
    print("Number of events:", sum(len(trace) for trace in log))

    print("\nAll traces:\n")

    for i, trace in enumerate(log):
        activities = [event.get("concept:name", "?") for event in trace]
        print(f"Trace {i+1} ({len(trace)} events):")
        print(activities)
        print("-" * 80)


# =========================================================
# INDUCTIVE MINER → WF-net
# =========================================================

def log_to_wfnet():
    print("\n[5] Running Inductive Miner")

    log = xes_importer.apply(GENERATED_LOG)

    process_tree = pm4py.discover_process_tree_inductive(log)
    net, im, fm = pm4py.convert_to_petri_net(process_tree)

    pm4py.write_pnml(net, im, fm, DISCOVERED_MODEL)
    print(" Discovered WF-net saved:", DISCOVERED_MODEL)

    print("Displaying discovered PNML...")
    pm4py.view_petri_net(net, im, fm)


# =========================================================
# MAIN
# =========================================================

def main():
    print("==========================================")
    print("  BPMN + DECLARE (Vacuity ON) → WF-NET ")
    print("==========================================")

    bpmn_to_pnml()
    declare_to_log()
    fix_xes()
    display_log()
    log_to_wfnet()

    print("\n PIPELINE COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    main()
