class Clock12:
    """ version 1"""

    def __init__(self, *args):
        self._h: int = 0
        self._m: int = 0
        if len(args) == 0:
            return
        elif len(args) > 2:
            raise TypeError(
                'Clock12.__init__ can not take more than 2 positional arguments.')
        elif len(args) == 2:
            self.set_time(args[0], args[1])
        else:
            if isinstance(args[0], int):
                self._from_int(args[0])
            elif isinstance(args[0], Clock12):
                self._assign(args[0])
            else:
                raise TypeError(
                    'The single argument of Clock12.__init__ should be int or Clock12')

    def get_hour(self):
        return self._h

    def get_minute(self):
        return self._m

    def set_time(self, h: int, m: int):
        self._is_good_time(h, m)
        self._set_time(h, m)

    def _is_good_time(self, h: int, m: int):
        return self._is_good_hour(h) and self._is_good_minute(m)

    def _assign(self, other):
        self._set_time(other.get_hour(), other.get_minute())

    def _from_int(self, minute: int):
        minute %= 12 * 60

        self._set_time(*divmod(minute, 60))

    def _is_good_hour(self, h: int):
        if not isinstance(h, int):
            raise TypeError(str(type(h)) + ' is improper for hour value')
        if 0 <= h < 12:
            return True
            raise ValueError(str(h) + ' is improper for hour value')

    def _is_good_minute(self, m: int):
        if not isinstance(m, int):
            raise TypeError(str(type(m)) + ' is improper for minute value')
        if 0 <= m < 60:
            return True
            raise ValueError(str(m) + ' is improper for minute value')

    def _set_time(self, h: int, m: int):
        self._h = h
        self._m = m

    def output(self):
        print('h=', self.get_hour(), 'm=', self.get_minute())

    def input(self):
        h0 = int(input("Enter hour (0..11): "))
        m0 = int(input("Enter minute (0..59): "))
        self.set_time(h0, m0)
