"""
file with classes Mosiichuk Kyrylo
"""

import csv
import re


class Laba:

    def __init__(self, task):
        self._task = task
        self._avg_mark = 0
        self._amount = 0
        self._highest_mark = 0
        self._tries = []

    def load(self, name, surname, father, points, year):
        """
        loading statistics and adding a try
        :param name:  name of a student
        :param surname: surname of a student
        :param father: father name of a student
        :param points: points for a try
        :param year: try's year
        """
        self.statistics(points)
        self.add(name, surname, father, points, year)

    def add(self, name, surname, father, points, year):
        """
        adding a try
        :param name:  name of a student
        :param surname: surname of a student
        :param father: father name of a student
        :param points: points for a try
        :param year: try's year
        """
        tmp = Try(name, surname, father, points, year)
        self._tries.append(tmp)
        return tmp

    def statistics(self, mark):
        """
        calculating statistics
        :param mark: mark of a try

        """
        self._check_highest_mark(mark)
        self._add_average_mark(mark)

    def _check_highest_mark(self, mark):
        if mark > self._highest_mark:
            self._highest_mark = mark

    def _add_average_mark(self, mark):
        self._avg_mark = (self._avg_mark * self._amount + mark) / (self._amount + 1)
        self._amount += 1

    def get_highest_mark(self):
        """
        :return: highest mark of the lab
        """
        return self._highest_mark

    def get_avg_mark_in_lab(self):
        """
        :return: average mark for the lab
        """
        return self._avg_mark

    def get_amount(self):
        """

        :return: amount of tries
        """
        return self._amount

    def get_task(self):
        """

        :return: task problem
        """
        return self._task

    def get_try(self):
        """
        :return: list of tries
        """
        return self._tries


class Info:

    def __init__(self):
        self._labs = []
        self._low_mark = 100
        self._average_mark = [0, 0]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.clear()

    def load(self, lr_task: str, name: str, surname: str, father: str, points: int, year):
        """
            loading information in memory
        :param lr_task: lab's problem
        :param name: name of a student
        :param surname: surname of a student
        :param father: father name of a student
        :param points: points for a try
        :param year: lab's year
        """
        self.statistics(points)
        find = self.find(lr_task)

        if find is None:
            self.add(lr_task).load(name, surname, father, points, year)

        else:
            find.load(name, surname, father, points, year)

    def statistics(self, mark):
        """
        updating statistics data
        :param mark: mark of a try
        """
        self._check_low_mark(mark)
        self._add_average_mark(mark)

    def _check_low_mark(self, mark):
        # checking is mark lower than lowest mark from previous marks
        if mark < self._low_mark:
            self._low_mark = mark

    def _add_average_mark(self, mark):
        # updating average mark
        num = self._average_mark[1]
        avg_mark = (self._average_mark[0] * num + mark) / (num + 1)
        self._average_mark = [avg_mark, num + 1]

    def find(self, lr_task):
        """
        finding lab if exist
        :param lr_task: lab's problem
        :return: lab if exist
        """
        task = None
        for lab in self._labs:
            if lab.get_task() == lr_task:
                task = lab
        return task

    def add(self, lab):
        """
        adding new lab
        :param lab: lab task
        :return: lab
        """
        tmp = Laba(lab)
        self._labs.append(tmp)
        return tmp

    def clear(self):
        """
        clearing info
        """
        self._labs.clear()
        self._low_mark = 100
        self._average_mark = [0, 0]

    def get_labs(self):
        """

        :return: list of labs
        """
        return self._labs

    def output(self, output_path, encoding):
        """
        outputting processed data to file
        :param output_path: file to output
        :param encoding: encoding of a file
        """
        with open(output_path, "w", encoding=encoding) as out:
            self._output(out)

    def _output(self, out):
        # processing data to better output
        for x in sorted(self._labs, key=lambda lab: lab.get_avg_mark_in_lab(), reverse=True):
            if x.get_highest_mark() >= 90:
                out.write(
                    "\t".join([str(round(x.get_avg_mark_in_lab(), 1)), str(x.get_task()), str(x.get_amount())]) +
                    "\n")
                for try_ in sorted(x.get_try(), reverse=True):
                    if try_.get_points() <= 75:
                        out.write("\t" + "\t".join([str(try_.get_surname()),
                                                    str(try_.get_name()),
                                                    str(try_.get_father()),
                                                    str(try_.get_year()),
                                                    str(try_.get_points())]) + "\n")

    def get_avr_mark(self):
        """
        :return: average mark of all labs
        """
        return int(round(self._average_mark[0]))

    def get_smallest_mark(self):
        """
        :return: smallest mark in all labs
        """
        return int(self._low_mark)


class Try:

    def __init__(self, name, surname, father, points, year):
        self._points = points
        self._year = year
        self._name = name
        self._surname = surname
        self._father = father

    def __gt__(self, other):
        if self.get_points() != other.get_points():
            return self.get_points() > other.get_points()
        elif self.get_year() != other.get_year():
            return self.get_year() < other.get_year()
        elif self.get_surname() != other.get_surname():
            return self.get_surname() < other.get_surname()
        elif self.get_name() != other.get_name():
            return self.get_name() < other.get_name()
        else:
            return self.get_father() < other.get_father()

    def get_name(self):
        """
        :return: name of a student
        """
        return self._name

    def get_surname(self):
        """
        :return: surname of a student
        """
        return self._surname

    def get_father(self):
        """
        :return: father name of a student
        """
        return self._father

    def get_points(self):
        """
        :return: points for a try
        """
        return self._points

    def get_year(self):
        """
        :return: try's year
        """
        return self._year


class Builder:
    @staticmethod
    def load(file_path, info, encoding):
        """
        loading data from file
        :param file_path: data file
        :param info: class info
        :param encoding: encoding of the file
        """
        if isinstance(info, Info):
            info.clear()
        with open(file_path, 'r', encoding=encoding) as s_csv:
            r = csv.reader(s_csv, delimiter=";")
            for row in r:

                if row:
                    if Builder._check_row(row):
                        info.load(row[2].strip(), row[4].strip(), row[5].strip(), (row[0].strip()), int(row[3].strip()),
                                  int(row[1].strip()))
                    else:
                        raise BaseException

    @staticmethod
    def _check_row(row):
        # checking row

        if len(row) != 6:
            return False
        elif not Builder._check_father(row[0]):
            return False
        elif not Builder._check_name(row[4]):
            return False
        elif not Builder._check_surname(row[5]):
            return False
        elif not Builder._check_date(row[1]):
            return False
        elif not Builder._check_task(row[2]):
            return False
        elif not Builder._check_mark(row[3]):
            return False
        else:
            return True

    @staticmethod
    def _check_with_pattern(string, pattern):
        # checking row by a pattern
        result = re.findall(pattern, string)

        tmp = ""
        for x in result:
            tmp = tmp + x
        if tmp == string:
            return True
        else:
            return False

    @staticmethod
    def _check_father(string):
        # checking father name
        PATTERN = r"[a-zA-ZА-Яа-яіїІЇЄє ]*[\`|\-|]{0,1}[a-zA-ZА-Яа-яіїІЇЄє ]*"
        len_ = 30
        if string != string.strip():
            return False
        elif len(string) > len_:
            return False
        elif not Builder._check_with_pattern(string, PATTERN):
            return False
        else:
            return True

    @staticmethod
    def _check_surname(string):
        # checking surname

        PATTERN = r"[a-zA-ZА-Яа-яіїІЇЄє ]*[\`|\-|]{0,1}[a-zA-ZА-Яа-яіїІЇЄє ]*"
        len_ = 27
        if len(string) == 0:
            return False
        elif string != string.strip():
            return False
        elif len(string) > len_:
            return False
        elif not Builder._check_with_pattern(string, PATTERN):
            return False
        else:
            return True

    @staticmethod
    def _check_name(string):
        # checking name
        PATTERN = r"[a-zA-ZА-Яа-яіїІЇЄє ]*[\`|\-|]{0,1}[a-zA-ZА-Яа-яіїІЇЄє ]*"
        len_ = 28
        if len(string) == 0:
            return False
        elif string != string.strip():
            return False
        elif len(string) > len_:
            return False
        elif not Builder._check_with_pattern(string, PATTERN):
            return False
        else:
            return True

    @staticmethod
    def _check_date(string):
        # checking date
        tmp = string.strip()
        if len(string) == 0:
            return False
        elif string != string.strip():
            return False
        elif len(tmp) != 4:
            return False
        elif not tmp.isnumeric():
            return False
        elif int(tmp) < 2001:
            return False
        else:
            return True

    @staticmethod
    def _check_task(string):
        # checking task
        PATTERN = r"[\w \\,\{\}\[\]\+\*\$%_\"-]*"
        len_min_max = [4, 53]
        if len(string) == 0:
            return False
        elif string != string.strip():
            return False
        elif (len(string) <= len_min_max[0]) and (len(string) >= len_min_max[1]):
            return False
        elif not Builder._check_with_pattern(string, PATTERN):
            return False
        else:
            return True

    @staticmethod
    def _check_mark(string):
        # checking mark
        tmp = string.strip()
        if len(string) == 0:
            return False
        elif string != string.strip():
            return False
        elif not tmp.isnumeric():
            return False
        elif int(tmp) > 100:
            return False
        else:
            return True
