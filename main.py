import numpy as np  # numpy是矩阵和数组进行运算或其他处理时所需用到的函数库
import matplotlib.pyplot as plt  # matplotlib是图像处理所需用到的函数库
from uuid import uuid4
import os
import random
import shutil

"""
分离训练集和测试集，并生成csv和图片
"""
if __name__ == '__main__':
    shutil.rmtree('./dist')
    shutil.rmtree('./test_data')
    shutil.rmtree('./train_data')
    os.mkdir('./dist')
    os.mkdir('./train_data')
    os.mkdir('./test_data')
    try:
        os.remove('./test_data.csv')
        os.remove('./train_data.csv')
    except Exception:
        pass

    data_file = open(r"./digits.csv")  # open("文件路径") 该函数用于打开.csv文件，并分配给data_file变量方便使用
    data_list = data_file.readlines()  # readlines()函数用于读取.csv文件并将其读入到data_list变量中
    data_file.close()  # 关闭.csv文件，为了防止之后的处理中不小心对原始.csv文件进行修改
    # len(data_list)  # len(变量名)用于检测读取的文件长度
    # print(data_list[0])  # 运行该语句会直接显示.csv文件中第一个数组的内容

    max_list = []
    min_list = []
    average_list = []
    variance_list = []

    test_cnt = 0
    total_cnt = len(data_list)
    for index, item in enumerate(data_list):
        all_values = [s.strip() for s in item.split(',')]  # split()函数将第1条数据进行拆分，以‘，’为分界点进行拆分

        image_array = np.asfarray(all_values[:-1]).reshape((8, 8))  # asfarray()函数将all_values中的前64个数字进行重新排列
        image_array_back = np.asfarray(all_values[:-1])

        # 最大
        line_max = np.amax(image_array_back)
        max_list.append(line_max)
        # 最小
        line_min = np.amin(image_array_back)
        min_list.append(line_min)
        # 平均
        average_list.append(np.average(image_array_back))
        # 方差
        variance_list.append(np.var(image_array_back))
        # reshape()函数可以对数组进行整型，使其成为8×8的二维数组，asfarry()函数可以使其成为矩阵。
        plt.imshow(image_array, cmap='gray_r', vmin=line_min, vmax=line_max,
                   interpolation='nearest')  # imshow()函数可以将8×8的矩阵中的数值当做像素值，使其形成图片

        path = '/{}_{}.jpg'.format(str(uuid4()), all_values[-1])
        dist_path = './dist' + path
        # plt.savefig(dist_path)
        if random.choice([True, False]) and test_cnt / total_cnt <= 0.3:
            # shutil.copy(dist_path, './test_data' + path)
            test_cnt += 1
            with open('./test_data.csv', 'a+') as csv:
                csv.writelines(item.strip() + "\n")
        else:
            # shutil.copy(dist_path, './train_data' + path)
            with open('./train_data.csv', 'a+') as csv:
                csv.writelines(item.strip() + "\n")
        print(index, '[%.2f%%]' % (index / total_cnt * 100), path)

    plt.close()
    print('done')

    '''
    方差折线图
    '''
    plt.plot([i for i in range(len(variance_list))], variance_list)
    plt.xlabel("line")  # 给x轴起名字
    plt.ylabel("variance")  # 给y轴起名字
    plt.savefig('variance.png')
    plt.show()
    plt.close()

    '''
    最大值散点图
    '''
    plt.scatter([i for i in range(len(max_list))], max_list)
    plt.xlabel("line")  # 给x轴起名字
    plt.ylabel("gray max")  # 给y轴起名字
    plt.savefig('max_scatter.png')
    plt.show()
    plt.close()

    '''
    最大值饼图
    '''
    max_map = {}
    for i in max_list:
        if max_map.get(i) is None:
            max_map[i] = 0
        max_map[i] += 1
    plt.pie(max_map.values(), labels=max_map.keys(), shadow=True, autopct='%1.1f%%')
    plt.savefig('max_pie.png')
    plt.show()
    plt.close()
