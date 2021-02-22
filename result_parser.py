import re

pat1 = r'%s(.+?)%s' % ("\[", "\]")
p = re.compile(pat1, re.IGNORECASE)

dir_list = ["2x_triage/v3_resnet34_CBAM",
            "2x_triage/v2_resnet34_512px",
            "2x_triage/v1_resnet34_224px",
            "2x_diagnose/v3_resnet34_CBAM",
            "2x_diagnose/v2_resnet34_512px",
            "2x_diagnose/v1_resnet34_224px"]

if __name__ == '__main__':
    for dir_path in dir_list:
        with open("{}/result.txt".format(dir_path), "w", encoding="utf-8", newline="\n") as out_file:
            with open("{}/result_raw.txt".format(dir_path), 'r', encoding='utf-8') as in_file:
                lines = in_file.readlines()
                for i in range(0, len(lines), 2):
                    try:
                        row = lines[i].strip() + lines[i + 1].strip()
                    except IndexError:
                        row = lines[i].strip()
                    row = re.findall(p, row)
                    num_list = [str(x) for x in eval(row[0])]
                    print(num_list)
                    for item in num_list:
                        out_file.write(item)
                        out_file.write("\n")
