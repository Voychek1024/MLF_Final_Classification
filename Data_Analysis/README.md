# MLF_Data-Processing
2020 Winter Machine Learning Foundations
Final Project

#### 选题：
X光影像肺炎分类

#### 要求：
	基于给定的数据集，建立一个模型，使之能够尽可能的将对照和病人区分开来。
	根据给定的数据集，建立一个模型，使之能够尽可能的将病毒性肺炎和细菌性肺炎区分开来。

#### 目录文件：

```
C:.
+---.idea
+---2x_diagnose（确诊二分类训练结果）
|   +---v1_resnet34_224px（224px训练结果，下同）
|   +---v2_resnet34_512px（512px训练结果，下同）
|   \---v3_resnet34_CBAM（CBAM224px训练结果，下同）
+---2x_triage（分诊二分类训练结果）
|   +---v1_resnet34_224px
|   +---v2_resnet34_512px
|   \---v3_resnet34_CBAM
+---Data（原生数据集）
|   +---test
|   |   +---NORMAL
|   |   \---PNEUMONIA
|   \---train
|       +---NORMAL
|       \---PNEUMONIA
\---pytorch-grad-cam（注意力机制可视化例程）
```

#### 任务

- [x] 为result_raw.txt设计parser
- [x] 224_512比较，结果对比（绘图，勘误，下同）
- [x] 224_CBAM比较，结果对比
- [x] 224_CBAM比较，Grad-Cam对比

#### 环境配置：

Anaconda3 (Python 3.8.x)

pytorch, numpy, opencv, matplotlib, joblib, sklearn