import os
import random
import shutil

if __name__ == '__main__':
    if not os.path.exists('./train_data'):
        os.mkdir('./train_data')
    if not os.path.exists('./test_data'):
        os.mkdir('./test_data')

    source = os.listdir('./dist')
    test_cnt = 0
    for index, path in enumerate(os.listdir('./dist')):
        print(path)
        if random.choice([True, False]) and test_cnt / len(source) <= 0.3:
            shutil.copy('./dist/{}'.format(path), './test_data/{}'.format(path))
            test_cnt += 1
            continue
        shutil.copy('./dist/{}'.format(path), './train_data/{}'.format(path))
