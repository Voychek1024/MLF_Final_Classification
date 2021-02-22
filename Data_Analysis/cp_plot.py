import matplotlib.pyplot as plt
import joblib

dir_list = ["2x_triage/v3_resnet34_CBAM",       # 0
            "2x_triage/v2_resnet34_512px",      # 1
            "2x_triage/v1_resnet34_224px",      # 2
            "2x_diagnose/v3_resnet34_CBAM",     # 3
            "2x_diagnose/v2_resnet34_512px",    # 4
            "2x_diagnose/v1_resnet34_224px"]    # 5

if __name__ == '__main__':
    in_file_1 = joblib.load("{}/train_accuracy.pkl".format(dir_list[4]))
    in_file_2 = joblib.load("{}/train_loss.pkl".format(dir_list[4]))
    in_file_3 = joblib.load("{}/val_accuracy.pkl".format(dir_list[4]))
    in_file_4 = joblib.load("{}/val_loss.pkl".format(dir_list[4]))
    in_file_5 = joblib.load("{}/train_accuracy.pkl".format(dir_list[5]))
    in_file_6 = joblib.load("{}/train_loss.pkl".format(dir_list[5]))
    in_file_7 = joblib.load("{}/val_accuracy.pkl".format(dir_list[5]))
    in_file_8 = joblib.load("{}/val_loss.pkl".format(dir_list[5]))
    print(in_file_1)
    idx = [i for i in range(40)]
    fig = plt.figure()
    plt.title('Diagnose ResNet34 Train Performance')
    plt.grid(True)
    ax = fig.add_subplot(111)
    ax.plot(idx, in_file_5, c='r', label='224px train accuracy')
    ax.plot(idx, in_file_1, c='g', label='512px train accuracy')
    ax.plot(idx, in_file_7, c='y', label='224px val accuracy')
    ax.plot(idx, in_file_3, c='b', label='512px val accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

    fig = plt.figure()
    plt.title('Diagnose ResNet34 Train Performance')
    plt.grid(True)
    ax = fig.add_subplot(111)
    ax.plot(idx, in_file_6, c='r', label='224px train loss')
    ax.plot(idx, in_file_2, c='g', label='512px train loss')
    ax.plot(idx, in_file_8, c='y', label='224px val loss')
    ax.plot(idx, in_file_4, c='b', label='512px val loss')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()
