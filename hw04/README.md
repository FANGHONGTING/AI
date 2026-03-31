# HW04 大模型文案、剪映声音克隆与开源语音识别实践

## 目录结构
hw04/
├── README.md
├── text_gen.md
├── jianying.md
├── voice.mp3
├── asr_report.md
├── experiment_log.md
├── asr_demo.py
└── requirements.txt

## 任务一：大模型生成文稿
- 所用模型：DeepSeek
- 生成日期：2026年3月31日
- 标题：人工智能如何改变生活
- 文件：text_gen.md

## 任务二：剪映声音克隆
- 使用工具：剪映专业版
- 说明：因克隆音色需要SVIP，使用内置音色替代
- 配音音频：voice.mp3
- 文件：jianying.md

## 任务三：开源语音识别
- 选定方案：OpenAI Whisper
- 使用模型：tiny
- 对比方案：Whisper、FunASR、Vosk
- 代码：asr_demo.py
- 依赖：requirements.txt
- 对比报告：asr_report.md
- 实验记录：experiment_log.md

## 运行方式
安装依赖：
pip install -r requirements.txt

运行识别：
python asr_demo.py

或：
whisper voice.mp3 --model tiny --language Chinese

## 实验环境
- 操作系统：Windows 10
- Python版本：3.14.3
- 硬件：普通笔记本（无GPU）

## 仓库链接
https://github.com/FANGHONGTING/AI
