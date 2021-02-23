def parse(file_path):
    f = open(file_path)
    arg1, arg2, argX = f.readline().split(' ')
    arg1, arg2, argX = int(arg1), int(arg2), int(argX)

def create_openfile_path(file_path):
    f = open(file_path + ".out", 'w')
    for i in v_list:
        f.write("OUTPUT")
        f.write('\n')
    f.close()


if __name__ == '__main__':
    print("start")