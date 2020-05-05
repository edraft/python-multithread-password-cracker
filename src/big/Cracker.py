import string

from big.Worker import Worker


class Cracker:

    def __init__(self):
        self.__threads = []
        self.__maxlength = 0
        self.found = False
        self.result = ''

    def setup(self, maxlength: int):
        self.__maxlength = maxlength
        for i in range(0, self.__maxlength):
            if not self.found:
                self.__threads.append(Worker(f'lower_{i}', i, string.ascii_lowercase, self))
                self.__threads.append(Worker(f'upper_{i}', i, string.ascii_uppercase, self))
                self.__threads.append(Worker(f'alpha_{i}', i, string.ascii_lowercase + string.ascii_uppercase, self))
                self.__threads.append(Worker(f'number_{i}', i, string.digits, self))
                chars = string.printable.replace(string.ascii_lowercase, '')
                chars = chars.replace(string.ascii_uppercase, '')
                chars = chars.replace(string.digits, '')
                self.__threads.append(Worker(f'chars_{i}', i, chars, self))
                self.__threads.append(Worker(f'all_{i}', i, string.printable, self))

    def run(self):
        for t in self.__threads:
            t.start()

        for t in self.__threads:
            t.join()

        if self.result == '':
            return 'No matches found'
        else:
            return self.result
