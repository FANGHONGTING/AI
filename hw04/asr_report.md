# 任务三：开源语音识别方案对比报告

## 一、调研方案列表

| 方案名称 | 开发方 | 仓库地址 |
|---------|--------|---------|
| OpenAI Whisper | OpenAI | https://github.com/openai/whisper |
| FunASR | Alibaba | https://github.com/alibaba-damo-academy/FunASR |
| Vosk | Alpha Cephei | https://github.com/alphacep/vosk-api |

## 二、详细对比

| 对比维度 | Whisper | FunASR | Vosk |
|---------|---------|--------|------|
| 许可协议 | MIT | MIT | Apache 2.0 |
| 语言支持 | 99+种语言 | 中英文优化 | 20+种语言 |
| 模型体量 | tiny(75MB)/base(150MB) | 中等(约500MB) | 轻量(40-200MB) |
| 是否支持流式/实时 | 否（需第三方） | 是 | 是 |
| 部署难度 | 简单（pip install） | 中等（需配置） | 简单 |
| 依赖要求 | Python + ffmpeg | Python + PyTorch | Python + Kaldi |
| 推理速度（CPU） | 较快 | 中等 | 快 |

## 三、选型理由

本实验选择 **OpenAI Whisper**，原因如下：

1. **安装简单**：一条 pip 命令即可完成安装
2. **开箱即用**：不需要额外配置，命令行直接运行
3. **中文支持好**：原生支持中文识别
4. **模型可选**：tiny/base/small/medium/large，可按需选择
5. **社区活跃**：文档完善，遇到问题容易找到解决方案

## 四、实测感受

在普通笔记本（无GPU）上使用 tiny 模型：
- 识别速度：30秒音频约5秒完成
- 准确率：约90%
- 优点：部署简单，运行流畅
- 缺点：tiny模型对专业词汇识别略有偏差

## 五、总结

Whisper 适合初学者快速上手，作为本实验的识别方案。
