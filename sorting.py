import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    # cwd_path = os.getcwd()
    # file_path = os.path.join(cwd_path, file_name)

    file_name = "numbers.csv"

    with open(file_name) as f:
        lines = f.readlines()
        data = dict()

        for line_num, line in enumerate(lines):
            if line_num == 0:
                col_names = line.split(',')
                for col_name in col_names:
                    data[col_name.strip()] = []
            else:
                values = line.split(",")
                for ind, col_name in enumerate(col_names):
                    data[col_name.strip()].append(int(values[ind]))

    print(data)



def main():
    pass


if __name__ == '__main__':
    main()
    read_data("numbers.csv")