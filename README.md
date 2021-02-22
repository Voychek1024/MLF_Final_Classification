# ML_Foundations
2020 Winter Machine Learning Foundations
Final Project

#### 选题：
X光影像肺炎分类

#### 要求：
	基于给定的数据集，建立一个模型，使之能够尽可能的将对照和病人区分开来。
	根据给定的数据集，建立一个模型，使之能够尽可能的将病毒性肺炎和细菌性肺炎区分开来。

#### 数据文件：
	本数据集中所有图片均为jpeg 格式。绝大多数的图片均是单通道灰度图，极个别为彩色图像。色图像。整个数据集分为训练集、验证集和测试集，分别存放在 train、val和test文件夹中。在子数据集中分别有两个子文件夹，为NORMAL和PNEUMONIA，分别存放对照x光图片和肺炎x光图片。在PNEUMONIA文件夹中，有两个类型的肺炎图片，分别为细菌性肺炎和病毒性肺炎，区分标准为若名字中带有bacteria即为细菌性肺炎x光图片，带有virus即为病毒性肺炎x光图片。

#### 进展：
任务状态![status](https://img.shields.io/badge/status-completed-%23008080)

- [x] 环境配置
- [x] ResNet二分类网络构建
- [x] 训练调参，OneHotEncode
- [x] 引入注意力机制
- [x] 结果分析
- [x] 书写论文

#### 环境配置：
Anaconda3 (Python 3.8.x)

pytorch, numpy, opencv, matplotlib, joblib, sklearn
