# 调试记录

## 错误1：pip安装网络超时

- **现象**：执行 `pip install torch torchvision matplotlib numpy` 时报错，显示网络连接问题
- **原因分析**：默认的PyPI源在国外，网络不稳定
- **修改点**：使用清华镜像源 `-i https://pypi.tuna.tsinghua.edu.cn/simple` 成功安装

## 错误2：运行代码时提示 ModuleNotFoundError: No module named 'torch'

- **现象**：在普通CMD或Anaconda Prompt中运行 `python simple_cnn.py` 提示找不到torch
- **原因分析**：电脑有多个Python环境（Anaconda、Miniconda、系统Python），torch只安装在了其中一个
- **修改点**：使用完整路径 `C:\Anaconda\python.exe simple_cnn.py` 运行，确保使用正确的Python环境

## 总结
两个模型均成功运行，未遇到代码逻辑错误。环境配置问题已解决。
