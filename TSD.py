from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import pylab as pb


# 打印划分子序列后的图片
def show_TSD(x, y, data):

    reduced_highs = data
    reduced_nums = []
    for i in range(1, len(reduced_highs)+1):
        reduced_nums.append(i)


    # 设置刻度
    xmajorLocator = MultipleLocator(20)  # 将x主刻度标签设置为20的倍数
    xmajorFormatter = FormatStrFormatter('%5.1f')  # 设置x轴标签文本的格式
    xminorLocator = MultipleLocator(2)  # 将x轴次刻度标签设置为5的倍数

    ymajorLocator = MultipleLocator(1)  # 将y轴主刻度标签设置为0.5的倍数
    ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
    yminorLocator = MultipleLocator(0.2)  # 将此y轴次刻度标签设置为0.1的倍数

    # 创建一个 100 * 6 点（point）的图
    pb.figure(figsize=(100, 6))
    ax = pb.subplot(111)
    pb.plot(reduced_nums, reduced_highs, c='red')

    # 设置x轴和y轴主刻度标签的位置,标签文本的格式
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.xaxis.set_major_formatter(xmajorFormatter)
    ax.yaxis.set_major_locator(ymajorLocator)
    ax.yaxis.set_major_formatter(ymajorFormatter)

    # 显示次刻度标签的位置,没有标签文本
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)

    ax.xaxis.grid(False, which='major')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(False, which='minor')  # y坐标轴的网格使用次刻度
    for i in range(len(x)):
        x_value = x[i]
        y_value = y[i]
        ax.plot([x_value, x_value], [15, y_value], linestyle='--', color='green')

    plt.xlim(1, 1000)
    plt.ylim(15, 25)

    # plt.savefig('/Users/zhangliutao/Desktop/generate_photos/ND_T1.png')
    plt.show()
    return reduced_highs


# 获取切割点坐标信息
def get_coordinate(data, seqs):
    num = len(seqs)
    x_coordinate, y_coordinate = [], []
    for i in range(1, num):
        x_coordinate.append(seqs[i].start+1)
        y_coordinate.append(data[seqs[i].start+1])
    show_TSD(x_coordinate, y_coordinate, data)
