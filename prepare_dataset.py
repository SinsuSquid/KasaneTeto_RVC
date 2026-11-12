#!/usr/bin/env python3
"""
Kasane Teto UTAU Dataset Preparation Script for RVC v2
Extracts and structures clean phoneme WAVs from TETO-OUset240323.zip.
"""

import os
import shutil
import zipfile
from pathlib import Path

ZIP_PATH = Path("TETO-OUset240323.zip")
DATASET_DIR = Path("dataset")

def prepare_teto_dataset(max_files: int = 400):
    if not ZIP_PATH.exists():
        print(f"[Error] {ZIP_PATH} not found. Please download the voicebank first.")
        return

    DATASET_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[1/3] Inspecting {ZIP_PATH}...")

    extracted_count = 0
    with zipfile.ZipFile(ZIP_PATH, 'r') as z:
        for file_info in z.infolist():
            filename = file_info.filename
            # Filter for .wav files inside the continuous/standard vocal folders
            if filename.endswith(".wav") and not filename.startswith("__MACOSX"):
                # Prioritize standard continuous (VCV) and standalone phonemes
                if any(sub in filename for sub in ["重音テト連続音", "重音テト単独音", "重音テト力み音源"]):
                    base_name = os.path.basename(filename)
                    if not base_name.startswith("._") and len(base_name) > 0:
                        out_path = DATASET_DIR / f"teto_{extracted_count:04d}_{base_name}"
                        with z.open(file_info) as source, open(out_path, "wb") as target:
                            shutil.copyfileobj(source, target)
                        extracted_count += 1
                        if extracted_count >= max_files:
                            break

    print(f"[2/3] Successfully extracted {extracted_count} clean phoneme WAV files to {DATASET_DIR}/")
    print(f"[3/3] Dataset is ready for RVC / Applio preprocessing and training!")

if __name__ == "__main__":
    prepare_teto_dataset()
