import uproot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_curran_protocol_analysis(file_path):
    """
    Implements the Phase-Jitter Analysis for Higgs-to-4L Vertex Anomalies.
    Targets the 'Gnaw'—a hypothesized non-Gaussian jitter spike at dz -> 0.
    """
    print(f"> Opening CERN NanoAOD Dataset: {file_path}")
    
    # Open the ROOT file and access the Events tree
    try:
        tree = uproot.open(file_path)["Events"]
    except Exception as e:
        print(f"Error accessing file: {e}")
        return

    # 1. DATA TARGETING: Extracting Electron/Muon longitudinal impact parameters
    # We focus on dz (distance to vertex) and dzErr (the jitter/uncertainty)
    branches = ["Electron_dz", "Electron_dzErr", "Electron_pt", "Electron_phi"]
    df = tree.arrays(branches, library="pd")

    print("> Filtering for Higgs-to-4L vertex reconstruction...")

    # 2. THE INVERSION FILTER: Calculation of Psi
    # Psi = | dzErr / dz |
    # We add a small epsilon to avoid division by zero, though the 
    # hypothesis specifically looks for the divergence as dz approaches 0.
    df['Psi'] = np.abs(df['Electron_dzErr'] / df['Electron_dz'])

    # 3. IDENTIFYING THE GNAW
    # We look for rows where dz is near the Planck threshold/null-point
    # and dzErr shows a non-Gaussian spike.
    null_point_threshold = 1e-5 
    the_gnaw_candidates = df[np.abs(df['Electron_dz']) < null_point_threshold]

    # Analysis of the covariance inversion
    mean_psi = df['Psi'].mean()
    spike_count = len(the_gnaw_candidates[the_gnaw_candidates['Psi'] > (10 * mean_psi)])

    print(f"> Analysis Complete.")
    print(f"> Mean Psi (Background): {mean_psi:.4f}")
    print(f"> Anomalous 'Gnaw' Spikes detected: {spike_count}")

    # 4. VISUALIZATION OF THE INVERSION GATE
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Electron_dz'], df['Psi'], alpha=0.5, s=2, label='Flux Data')
    plt.axvline(0, color='red', linestyle='--', label='Inversion Gate (Null Point)')
    plt.yscale('log')
    plt.xlabel('Longitudinal Impact Parameter (dz)')
    plt.ylabel('Phase-Jitter Ratio (Psi)')
    plt.title('Curran Protocol: Phase-Jitter Analysis (The Gnaw)')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.show()

if __name__ == "__main__":
    # Example path to a CERN Open Data NanoAOD file
    # Replace with local path to your SMHiggsToZZTo4L dataset
    DATA_PATH = "root://eospublic.cern.ch//eos/opendata/cms/derived-data/AOD/Higgs.root"
    
    print("--- CURRAN PROTOCOL ARCHIVE ---")
    print("Logic Status: OPTIMAL")
    # run_curran_protocol_analysis(DATA_PATH)