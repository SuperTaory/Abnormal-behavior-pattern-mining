from getdata import *
from PAA import *
from MLES import *
from DTW import dtw_distance
from TSD import *


# 定义子序列类
class Subsequence(object):

    def __init__(self, num, start, end):
        self.seq = []
        self.num = num
        self.start = start
        self.end = end
        self.length = end - start + 1
        self.distance = 0

    def print_data(self):
        print('{:>4s}{:5d}{:5d}{:5d}{:>8.2f}'.format(str(self.num), self.start, self.end, self.length, self.distance))


# 划分子序列
def division(data):
    # 采用多层次极值点特征分析法处理序列
    tags = EIIR(data)
    # 获取序列切割点
    cp = MSR(tags, -9)
    # 打印切割点
    print('切割点信息：')
    for i in range(len(cp) // 10):
        print(cp[i * 10:i * 10 + 10])
        last = i * 10 + 10
    print(cp[last:])

    # 根据切割点划分子序列
    subsequence_num = len(cp) - 1
    # 初始化子序列集合
    subsequence_collections = []
    # 切割子序列并保存
    for i in range(subsequence_num):
        sequence = Subsequence(i + 1, cp[i], cp[i + 1])
        for j in range(cp[i], cp[i + 1] + 1):
            sequence.seq.append(data[j])
        subsequence_collections.append(sequence)
    return subsequence_collections


# 计算DTW距离
def get_dtw_distance(sequence, sequences):
    for i in range(len(sequences)):
        if sequences[i].num != sequence.num:
            sequences[i].distance = float(dtw_distance(sequence.seq, sequences[i].seq)[-1, -1])
    return sequences


# 打印子序列信息
def print_sequences(sequences):
    print('时间序列划分如下：')
    print('{:^4s}{:^4s}{:^4s}{:^3s}{:^8s}'.format('序列', '起始', '结束', '长度', 'DTW距离'))
    for i in range(len(sequences)):
        seq = sequences[i]
        seq.print_data()


# 建立数据模型
data = get_data()
# PAA处理数据
reduced_data = paa(data)
# 划分序列
seq_collections = division(reduced_data)
# 打印划分后的时间序列图
get_coordinate(reduced_data, seq_collections)
# 选取模版子序列
normal_sequence = seq_collections[3]
# 计算模版序列与其他子序列的DTW距离并打印
final_sequences = get_dtw_distance(normal_sequence, seq_collections)
print_sequences(final_sequences)
# DTW距离阀值
dtw_threshold = 35
# 输出异常序列信息
print('异常序列如下：')
for i in range(len(final_sequences)):
    if final_sequences[i].distance >= dtw_threshold:
        final_sequences[i].print_data()
