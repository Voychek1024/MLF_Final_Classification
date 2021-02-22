import numpy as np

if __name__ == '__main__':
    cp_1 = np.loadtxt("cp_triage_224.txt", dtype=np.str, delimiter='\t')
    cp_2 = np.loadtxt("cp_triage_CBAM.txt", dtype=np.str, delimiter='\t')
    list_cp = []
    for i in range(max(len(cp_1), len(cp_2))):
        try:
            if cp_1[i, 1] not in cp_2[:, 1]:
                list_cp.append(cp_1[i, 1])
        except IndexError:
            continue
    for i in range(max(len(cp_1), len(cp_2))):
        try:
            if cp_2[i, 1] in cp_1[:, 1]:
                try:
                    list_cp.remove(cp_2[i, 1])
                except ValueError:
                    continue
        except IndexError:
            continue
    print(list_cp)
