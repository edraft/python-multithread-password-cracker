import string

from Worker import Worker


class Cracker:

    def __init__(self):
        self.__threads = []
        self.__maxlength = 0
        self.found = False
        self.result = ''

    def setup(self, maxlength: int):
        self.__maxlength = maxlength
        self.__threads.append(Worker('lower', self.__maxlength, string.ascii_lowercase, self))
        self.__threads.append(Worker('upper', self.__maxlength, string.ascii_uppercase, self))
        self.__threads.append(Worker('alpha', self.__maxlength, string.ascii_lowercase + string.ascii_uppercase, self))
        self.__threads.append(Worker('number', self.__maxlength, string.digits, self))
        chars = string.printable.replace(string.ascii_lowercase, '')
        chars = chars.replace(string.ascii_uppercase, '')
        chars = chars.replace(string.digits, '')
        self.__threads.append(Worker('chars', self.__maxlength, chars, self))
        self.__threads.append(Worker('all', self.__maxlength, string.printable, self))

    def run(self):
        for t in self.__threads:
            t.start()

        for t in self.__threads:
            t.join()

        if self.result == '':
            return 'No matches found'
        else:
            return self.result
