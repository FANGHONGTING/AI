# HW07: 胸部X光肺炎影像二分类

## 基本信息
- **学生**：SONGYAYA34
- **课程**：《人工智能导论》
- **作业**：HW07
- **任务**：胸部X光肺炎影像二分类（Normal vs Pneumonia）

---

## 数据集获取说明

### 数据集名称
Chest X-Ray Images (Pneumonia)

### 数据集来源
Kaggle：https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

### 获取步骤
1. 登录Kaggle网站（https://www.kaggle.com）
2. 在搜索框输入 "Chest X-Ray Images (Pneumonia)"
3. 点击进入数据集页面
4. 点击右上角 "New Notebook" 按钮
5. 数据集会自动挂载到 `/kaggle/input/` 路径下，无需手动下载

---

## 运行环境

| 项目 | 信息 |
|------|------|
| 平台 | Kaggle Notebook |
| Python版本 | 3.12 |
| TensorFlow版本 | 2.19.0 |
| 硬件 | CPU（Intel Xeon） |

---

## 一键运行命令

### 在Kaggle Notebook中运行
1. 打开数据集页面，点击 "New Notebook"
2. 将 `train.ipynb` 中的代码复制到Notebook
3. 点击菜单栏 **Run → Run All Cells**
4. 等待训练完成（约15分钟）

### 在本地运行
```bash
# 1. 克隆仓库
git clone https://github.com/你的用户名/你的仓库名.git
cd 你的仓库名/hw07

# 2. 安装依赖
pip install -r requirements.txt

# 3. 下载数据集到本地
# 从Kaggle下载 chest-xray-pneumonia.zip 并解压

# 4. 修改 train.ipynb 中的数据集路径为本地路径

# 5. 启动Notebook
jupyter notebook train.ipynb
目录结构说明
hw07/
├── train.ipynb           # 训练代码（含完整输出）
├── requirements.txt      # Python依赖包列表
├── README.md            # 项目说明（本文件）
├── report.md            # 实验报告
└── figures/             # 图表文件夹
    ├── training_curves.png
    └── confusion_matrix.png
数据统计
子集	NORMAL	PNEUMONIA	总计
训练集	1,073	1,072	2,145
验证集	268	269	537
测试集	234	390	624

模型结构
层类型	输出尺寸	参数量
Conv2D(32) + MaxPool	126×126×32	896
Conv2D(64) + MaxPool	61×61×64	18,496
Conv2D(128) + MaxPool	28×28×128	73,856
Flatten	25088	0
Dense(256) + Dropout(0.5)	256	6,422,784
Dense(1) Sigmoid	1	257
总计		6,516,289

超参数
参数	值
输入尺寸	128 × 128 × 3
Batch Size	16
Epochs	10
优化器	Adam
学习率	0.001
损失函数	binary_crossentropy
Dropout比例	0.5

最终测试集指标摘要
指标	值
Accuracy（准确率）	84.46%
Precision（精确率）	80.97%
Recall（召回率）	98.21%
F1-Score（F1分数）	88.76%

混淆矩阵
                预测正常    预测肺炎
实际正常:        144          90
实际肺炎:          7         383

关键结论
1. 召回率优先：在医疗诊断场景，召回率（98.21%）比准确率更重要，漏诊代价远大于误诊
2. 数据增强有效：通过旋转、平移、缩放等操作，有效缓解了过拟合
3. 类别平衡处理：通过下采样和类别权重，解决了原始数据的类别不平衡问题
