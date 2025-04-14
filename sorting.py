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
        series_1 = []
        series_2 = []
        series_3 = []
        # keys = f.readline()
        lines = f.readlines()

        for line_num, line in enumerate(lines):
            if line_num > 0:
                values = line.split(",")
                series_1.append(int(values[0]))
                series_2.append(int(values[1]))
                series_3.append(int(values[2]))
        data = {'series_1': series_1, "series_2": series_2, 'series_3': series_3}
    print(data)



def main():
    pass


if __name__ == '__main__':
    main()
    read_data("numbers.csv")