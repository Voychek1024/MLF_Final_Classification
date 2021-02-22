import numpy as np

dir_list = ["2x_triage/v3_resnet34_CBAM",       # 0
            "2x_triage/v2_resnet34_512px",      # 1
            "2x_triage/v1_resnet34_224px",      # 2
            "2x_diagnose/v3_resnet34_CBAM",     # 3
            "2x_diagnose/v2_resnet34_512px",    # 4
            "2x_diagnose/v1_resnet34_224px"]    # 5

if __name__ == '__main__':
    in_file = np.loadtxt("{}/result.txt".format(dir_list[0]), dtype=np.str, delimiter='\n')
    cp_file = np.loadtxt("test_triage.txt", dtype=np.str, delimiter='\t')
    cp_idx = cp_file[:, 1]
    print(in_file.shape)
    ct = 0
    with open("cp_triage_CBAM.txt", "w", encoding="utf-8", newline="\n") as out_file:
        for i in range(len(in_file)):
            if in_file[i] != cp_idx[i]:
                ct += 1
                out_file.write(cp_file[i, 0]+'\t'+str(i)+'\n')
    print(1 - ct / len(in_file))
