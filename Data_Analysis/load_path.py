import numpy as np

if __name__ == '__main__':
    idx = np.loadtxt("cp_idx.txt", dtype=np.str, delimiter='\t')
    cp_1 = np.loadtxt("cp_diagnose_224.txt", dtype=np.str, delimiter='\t')
    cp_2 = np.loadtxt("cp_triage_224.txt", dtype=np.str, delimiter='\t')
    cp_1_idx = cp_1[:, 1].tolist()
    idx_list = [eval(item) for item in idx[:, 1]]
    for item in idx_list[0]:
        # print(item)
        print(cp_1[cp_1_idx.index(item), 0])
    # print(cp_1[:, 1])
