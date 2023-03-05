def split_and_join(line):
    old_line =line.split(" ")
    new_line ="-".join(old_line)
    return new_line
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
