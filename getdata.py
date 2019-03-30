import csv
from PAA import *
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import pylab as pb


def get_data():

    # 导入数据
    filename = '/Users/zhangliutao/Desktop/energydata_complete.csv'

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        nums, highs = [], []
        # 选取5000条数据作为测试数据
        for i, row in enumerate(reader):
            if 3000 < i <= 8000:
                # current_date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
                nums.append(i)
                high = row[3]
                highs.append(float(high))

    # 设置刻度
    xmajorLocator = MultipleLocator(100)  # 将x主刻度标签设置为20的倍数
    xmajorFormatter = FormatStrFormatter('%5.1f')  # 设置x轴标签文本的格式
    xminorLocator = MultipleLocator(10)  # 将x轴次刻度标签设置为5的倍数

    ymajorLocator = MultipleLocator(1)  # 将y轴主刻度标签设置为0.5的倍数
    ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
    yminorLocator = MultipleLocator(0.2)  # 将此y轴次刻度标签设置为0.1的倍数

    # 创建一个 150 * 6 点（point）的图
    pb.figure(figsize=(100, 6))
    ax = pb.subplot(111)
    pb.plot(nums, highs, c='red')


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

    plt.xlim(3001, 8000)
    plt.ylim(15, 25)
    # plt.title('厨房温度变化图')
    # plt.xlabel('时间/10分钟')
    # plt.ylabel('温度/摄氏度')

    # plt.savefig('/Users/zhangliutao/Desktop/generate_photos/T1.png')
    plt.show()
    # print(len(highs))
    return highs
