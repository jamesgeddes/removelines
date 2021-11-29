import os

path = os.getcwd()


ignore_files = ["remove-lines.py", "to-remove"]

with open("to-remove", "r", newline="") as pattern_file:
    remove_patterns = [l for l in (line.strip() for line in pattern_file) if l]


for root, directories, files in os.walk(path, topdown=False):
    for name in files:
        out = []
        current_file = os.path.join(root, name)
        print(current_file)
        if any([ignore_file in current_file for ignore_file in ignore_files]):
            pass
        else:
            with open(current_file, "r") as in_file:
                in_file_lines = in_file.readlines()
            print("IN FILE:")
            print(in_file_lines)
            for in_file_line in in_file_lines:
                print(in_file_line)
                keep_var = True
                for remove_pattern in remove_patterns:
                    if remove_pattern in in_file_line:
                        keep_var = False
                        print("R: " + remove_pattern + " IS IN " + in_file_line)
                        break

                if keep_var:
                    print("OUTPUTTING")
                    print(in_file_line)
                    out.append(in_file_line)
            print("\n\n\nFINAL\n\n\n")
            print(out)
            with open(current_file, "w") as out_file:
                for line in out:
                    out_file.write(line)
