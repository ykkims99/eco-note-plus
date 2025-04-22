# 🌱 Eco-Note+: AI-Optimized Open Notebook

> 에코를 위해 (For EcoNote+)  
> An open-source, low-power, AI-enhanced notebook system for education and digital equity.

## 🔧 Features
- ONNX/TFLite-based local AI inference
- Real-time video enhancement (e.g., ESRGAN)
- Web prefetching optimization
- Fully open hardware: schematics, BOM, and 3D STL included
- Portable and offline-capable design
- Reproducible and installable in one command

## 📂 Folder Structure
- `software/ai_inference/`: Python scripts for inference
- `models/onnx/`: Optimized ONNX models (ESRGAN-lite)
- `docs/tests/`: Benchmark results and field checklists
- `scripts/`: Auto-report generator and monitoring
- `install.sh`: Quick installation of dependencies

## 🖥️ Quick Start
```bash
bash software/install.sh
python3 software/ai_inference/video_enhancer.py
```

## 📜 License
This project is licensed under the MIT License. See `LICENSE` for details.
