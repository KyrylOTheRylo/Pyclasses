"""
Load file Mosiichuk Kyrylo
"""

import json
import os
import re
import classes


def _input_data_check(dict_):
    keys_in = ["json", "csv", "encoding"]
    keys_out = ["fname", "encoding"]
    main_keys = ["input", 'output']
    for i in keys_in:
        if not any(x == i for x in dict_[main_keys[0]].keys()):
            raise BaseException

    for j in keys_out:
        if not any(x == j for x in dict_[main_keys[1]].keys()):
            raise BaseException


def loader_from_ini(file_name):
    """
    loading data from ini file
    :param file_name: Name of the file .ini if that file exist
    :return: dict json_file
    """

    print(f"ini {file_name}:", end="")
    if re.findall(r'.(\w+)', file_name)[1] == "ini":
        print(' OK')
    else:

        raise BaseException

    with open(file_name) as f:
        json_file = json.load(f)
        _input_data_check(json_file)

    return json_file


def load_data(info, file_name, encoding):
    """
    loading main data for another operations and putting that in memory
    :param info: object of the class Info
    :param file_name:  data filepath
    :param encoding: encoding of a file
    """
    classes.Builder.load(file_name, info, encoding)


def load_second(second_file, encoding):
    """
    loading second file in memory and raise exception if something went wrong

    :param second_file: file_path
    :param encoding: encoding of the file
    :return: None
    """

    with open(second_file, encoding=encoding) as f:
        dict_ = {
            "avg_mark": "середній відсоток набраних балів",
            "lowest_mark": "найменьший відсоток набраних балів"
        }
        data_json = json.load(f)
        for key in dict_:

            tmp = dict_[key]
            if tmp in data_json:
                dict_[key] = data_json[tmp]
                if dict_["avg_mark"].isnumeric() and dict_["lowest_mark"].isnumeric():
                    return dict_
            else:
                return None


def check_eq(info, dict_):
    """
    checking statistics in main file with values in second file
    :param info: class info
    :param dict_: dict of params from the second file
    :return: True if equals or False if not
    """
    if dict_ is not None:

        if (info.get_avr_mark() == int(dict_["avg_mark"])) and (info.get_smallest_mark() == int(dict_["lowest_mark"])):
            return True
        else:
            return False
    else:
        return False


def outputprint(info, output_file, encoding2):
    """

    :param info: Class Info object
    :param output_file: output file
    :param encoding2: encoding of the output file

    """
    if re.findall(r'.(\w+)', output_file)[1] == "txt":
        print(f"output {os.path.basename(output_file)}:", end="")
        info.output(output_file, encoding2)
        print(" OK", end="")
    else:
        raise BaseException


def load(info, file_name, second_file, encoding1):
    """
    checking formats of files if it correct doing manipulations with them and writing report
    if something went wrong raising error and stops
    :param info: Class Info
    :param file_name: main file
    :param second_file: second file
    :param encoding1: encoding of main and second files
    """
    print(f"input-csv {os.path.basename(file_name)}:", end="")
    if re.findall(r'.(\w+)', file_name)[1] == "csv":
        load_data(info, file_name, encoding1)
        print(' OK')
        if re.findall(r'.(\w+)', second_file)[1] == "json":
            print(f"input-json {os.path.basename(second_file)}:", end="")
            dict_ = load_second(second_file, encoding1)
            print(" OK")
            print("json?=csv:", end="")
            if check_eq(info, dict_):
                print(" OK")
            else:
                print(" UPS")
        else:
            raise BaseException
    else:
        raise BaseException
