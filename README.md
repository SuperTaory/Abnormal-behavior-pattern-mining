# Abnormal-behavior-pattern-mining
时间序列上基于DTW的异常行为模式挖掘算法的实现
算法主要包括：
    建立时间序列上的行为模式模型；
    对时间序列进行PAA分段线性表示以精简原始数据；
    采用多层次极值划分法划分序列获取子序列，从所有子序列中选取一个模版子序列；
    使用DTW算法计算模版子序列与其他子序列的相似度；
综合上述内容完成异常序列的检测
