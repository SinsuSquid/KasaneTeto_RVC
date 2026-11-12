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

### Step 2: Training Pipeline (Applio CLI)
Preprocessed, extracted, and trained on an **NVIDIA A100-SXM4-40GB GPU**:
```bash
# 1. Preprocess (40 kHz, 16 CPU cores)
python core.py preprocess --model-name KasaneTeto --dataset-path ../dataset --sample-rate 40000 --cpu-cores 16

# 2. Extract Features (RMVPE + ContentVec on GPU)
python core.py extract --model-name KasaneTeto --f0-method rmvpe --sample-rate 40000 --embedder-model contentvec --gpu 0

# 3. Train Model (200 Epochs, FP16, VRAM Cached)
python core.py train --model-name KasaneTeto --sample-rate 40000 --total-epoch 200 --batch-size 32 --save-every-epoch 25 --gpu 0 --pretrained --cache-data-in-gpu

# 4. Generate FAISS Feature Index
python core.py index --model-name KasaneTeto --index-algorithm Auto
```

---

## 4. Benchmark & Training Results

- **Hardware**: NVIDIA A100-SXM4-40GB (HBM2e 40GB VRAM)
- **Dataset**: 400 uncompressed studio phonemes sliced into 537 clean audio segments (~13m38s)
- **Speed**: ~10 seconds per epoch (total training runtime: ~35 minutes)
- **Convergence**: 200 epochs, 3,600 gradient updates, lowest generator loss **36.014**
- **Output Weights**:
  - `KasaneTeto.pth` (53 MB) — HiFi-GAN 40kHz generator
  - `KasaneTeto.index` (129 MB) — FAISS retrieval index

---

## 5. Inference

Run voice conversion on any audio sample:
```bash
python core.py infer \
  --input-path ../audio/input_vocal.wav \
  --output-path ../audio/output_teto.wav \
  --pth-path ../weights/KasaneTeto.pth \
  --index-path ../weights/KasaneTeto.index \
  --f0-method rmvpe \
  --index-rate 0.75
```

---

## 6. Credits & Legal Guidelines

- **Character & Voice Concept**: Twindrill (ツインドリル) & Oyamano Mayo (小山乃舞世).
- **Official Portal**: [kasaneteto.jp](https://kasaneteto.jp/)
- **License Compliance**: Non-commercial / fan creations are fully permitted under the official [Twindrill Voice License Guidelines](https://kasaneteto.jp/guideline/voice.html).
