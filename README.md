# Kasane Teto (重音テト) RVC v2 Voice Model Pipeline 🥖

A streamlined pipeline to train a state-of-the-art **Retrieval-based Voice Conversion (RVC v2)** neural voice model for **Kasane Teto (重音テト)** using official studio-recorded UTAU voicebanks on high-performance NVIDIA GPUs.

---

## 1. Overview & Architecture

- **Target Persona**: Kasane Teto (重音テト) — 31-year-old chimera synth queen.
- **Dataset Source**: Official Twindrill All-In-One OpenUTAU Voicebank (`TETO-OUset240323.zip`).
  - Studio dry recordings with zero background noise and complete Japanese VCV (Vowel-Consonant-Vowel) phonetic coverage.
- **Model Framework**: RVC v2 (Retrieval-based Voice Conversion) / [Applio](https://github.com/IAHispano/Applio)
  - **Pitch Extractor**: `rmvpe` (Robust Model for Vocal Pitch Estimation)
  - **Feature Representation**: ContentVec (`checkpoint_best_legacy_500.pt`)
  - **Timbre Retrieval**: FAISS Indexing (`.index`)
  - **Sample Rate**: 40 kHz / 48 kHz

---

## 2. Directory Structure

```text
KasaneTeto_RVC/
├── dataset/             # Extracted clean phoneme WAVs (git-ignored)
├── weights/             # Trained .pth model checkpoints and .index files
├── audio/               # Source vocal stems and generated covers
├── prepare_dataset.py   # Automated UTAU voicebank extraction script
├── README.md
└── .gitignore
```

---

## 3. Quick Start & Training Guide

### Step 1: Extract the Voicebank
Run the preparation script to unpack clean phoneme samples:
```bash
python3 prepare_dataset.py
```

### Step 2: Training with Applio / RVC
1. Launch Applio or RVC WebUI / CLI.
2. Set dataset path to `dataset/`.
3. Set model parameters:
   - **Architecture**: `v2`
   - **Target Sample Rate**: `40k`
   - **f0 Method**: `rmvpe`
   - **Batch Size**: `32` (on A100 / high-VRAM GPUs)
   - **Epochs**: `200 - 250`
4. Train feature index (FAISS).

---

## 4. Credits & Legal Guidelines

- **Character & Voice Concept**: Twindrill (ツインドリル) & Oyamano Mayo (小山乃舞世).
- **Official Portal**: [kasaneteto.jp](https://kasaneteto.jp/)
- **License Compliance**: Non-commercial / fan creations are fully permitted under the official [Twindrill Voice License Guidelines](https://kasaneteto.jp/guideline/voice.html).
