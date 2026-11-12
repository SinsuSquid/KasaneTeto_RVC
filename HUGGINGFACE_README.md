---
language:
- ja
- ko
- en
license: other
tags:
- rvc
- rvc-v2
- voice-conversion
- kasane-teto
- utau
- vocaloid
- applio
---

# Kasane Teto (重音テト) — Studio Master RVC v2 Model (40kHz) 🥖

> 🐙 **Code & Training Pipeline**: Full dataset preparation and training scripts are available on GitHub at [**SinsuSquid/KasaneTeto_RVC**](https://github.com/SinsuSquid/KasaneTeto_RVC).

An artisan, booth-clean **Retrieval-based Voice Conversion (RVC v2)** model for **Kasane Teto (重音テト)**, trained on an enterprise **NVIDIA A100-SXM4-40GB GPU** using the official 2024 uncompressed anechoic studio UTAU voicebank from [kasaneteto.jp](https://kasaneteto.jp/).

---

## 🌟 Why This Model?

Most existing Kasane Teto RVC models on the internet suffer from:
- Background music (BGM) bleed and phase cancellation from automated vocal rippers (UVR5).
- Artificial room reverb baked directly into the neural vocoder.
- Glitchy pitch tracking (`harvest` / `pm` octave drops).

**This model fixes that entirely:**
- **Zero Reverb / Zero BGM**: Sourced directly from 400 clean anechoic booth recordings (`TETO-OUset240323.zip`).
- **State-of-the-art Pitch Tracking**: Extracted via `RMVPE` (Robust Model for Vocal Pitch Estimation).
- **Phonetic Timbre**: Clustered via `ContentVec` and indexed with a dedicated 129 MB FAISS `.index` file.
- **Trained on NVIDIA A100 SXM4**: 200 epochs, 3,600 gradient updates, lowest Mel-spectral generator loss **36.014**.

---

## 📦 Files in this Repository

| File | Size | Description |
| :--- | :--- | :--- |
| `KasaneTeto.pth` | 53 MB | HiFi-GAN 40kHz Generator PyTorch model weights |
| `KasaneTeto.index` | 129 MB | FAISS feature retrieval index |
| `KasaneTeto.onnx` | 106 MB | Standalone ONNX runtime model (Zero-PyTorch CPU/Edge) |
| `KasaneTeto_RVC_v2.zip` | 168 MB | One-click bundle for Applio / RVC WebUI |
| `output_teto_kimi.wav` | 197 KB | Audio sample (*"Kimi wa jitsu ni baka da na"*) |

---

## 🚀 How to Use

### Option A: Applio / RVC WebUI (1-Click Install)
1. Copy the download link of `KasaneTeto_RVC_v2.zip`.
2. In Applio or RVC WebUI, navigate to the **Download** tab.
3. Paste the URL and click **Download Model**.

### Option B: Manual Placement
- Place `KasaneTeto.pth` into your `logs/` or `weights/` folder.
- Place `KasaneTeto.index` into your `logs/KasaneTeto/` folder.

### Recommended Inference Settings
- **f0 Method**: `rmvpe`
- **Index Rate**: `0.75` (higher = more distinctive Teto UTAU timbre)
- **Protect Consonants**: `0.33`
- **Pitch Shift**: `0` (or `+12` when converting male vocals to female range)

---

## 📜 Credits & Licensing

- **Original Character & Voice Provider**: Twindrill (ツインドリル) & Oyamano Mayo (小山乃舞世).
- **Official Twindrill Portal**: [kasaneteto.jp](https://kasaneteto.jp/)
- **License**: Free for non-commercial fan creations with attribution, adhering strictly to the official [Twindrill Voice License Guidelines](https://kasaneteto.jp/guideline/voice.html).
- **Pipeline & Training**: Trained by [SinsuSquid](https://github.com/SinsuSquid/KasaneTeto_RVC) on NVIDIA A100 GPUs.
