import threading
from itertools import product
import string
from datetime import datetime


class Tester:

    def __init__(self, charset: []):
        self.__charset = charset

    def __check(self, words: []) -> bool:
        ans = 'test1234'

        return ans in words

    def test2(self):
        start = datetime.now()
        complete_list = []
        for current in range(0, 10):
            print(current + 1)
            a = [i for i in self.__charset]
            for y in range(0, current):
                a = [x + i for i in self.__charset for x in a]

            complete_list = complete_list + a
            if self.__check(complete_list):
                end = datetime.now()
                dif = end - start
                print(f'found in {round(dif.total_seconds(), 2)} secs')
                return

        print('end')

    def test3(self):
        start = datetime.now()
        for i in range(0, 12):
            for attempt in product(charset, repeat=i):
                pw = ''.join(attempt)
                print(pw)
                if pw == 'test':
                    end = datetime.now()
                    dif = end - start
                    print(f'found in {round(dif.total_seconds(), 2)} secs')
                    return


if __name__ == '__main__':
    # charset = string.printable
    charset = string.ascii_lowercase
    charset += string.ascii_uppercase
    for i in range(0, 10):
        charset += str(i)

    tester = Tester(charset)
    # tester.test2()
    tester.test3()
