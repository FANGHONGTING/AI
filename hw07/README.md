# HW07: 胸部X光肺炎影像二分类

## 基本信息
- **学生**：方泓婷
- **课程**：《人工智能导论》
- **作业**：HW07
- **任务**：胸部X光肺炎影像二分类（Normal vs Pneumonia）

## 数据集
- **名称**：Chest X-Ray Images (Pneumonia)
- **来源**：Kaggle
- **原始数据**：正常1341张，肺炎3875张
- **处理后**：训练集2145张，验证集537张，测试集624张

## 模型结构
| 层类型 | 输出尺寸 | 参数量 |
|--------|----------|--------|
| Conv2D(32) + MaxPool | 126×126×32 | 896 |
| Conv2D(64) + MaxPool | 61×61×64 | 18,496 |
| Conv2D(128) + MaxPool | 28×28×128 | 73,856 |
| Flatten | 25088 | 0 |
| Dense(256) + Dropout(0.5) | 256 | 6,422,784 |
| Dense(1) Sigmoid | 1 | 257 |
| **总计** | | **6,516,289** |

## 超参数
| 参数 | 值 |
|------|------|
| 输入尺寸 | 128×128×3 |
| Batch Size | 16 |
| Epochs | 10 |
| 优化器 | Adam (lr=0.001) |
| 损失函数 | binary_crossentropy |

## 测试集结果
| 指标 | 值 |
|------|------|
| Accuracy | 84.46% |
| Precision | 80.97% |
| Recall | 98.21% |
| F1-Score | 88.76% |

## 混淆矩阵
预测正常 预测肺炎
实际正常: 144 90
实际肺炎: 7 383

## 运行方式
1. 在Kaggle Notebook中打开 `train.ipynb`
2. 挂载数据集：Chest X-Ray Images (Pneumonia)
3. 依次运行所有单元格

## 运行环境
- Kaggle Notebook (CPU)
- TensorFlow 2.19.0
- Python 3.12

## 文件结构
hw07/
├── train.ipynb # 训练代码
├── requirements.txt # 依赖包
├── README.md # 项目说明
├── report.md # 实验报告
└── figures/ # 图表
├── training_curves.png
└── confusion_matrix.png
