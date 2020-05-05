import threading
from datetime import datetime
from itertools import product


class Worker(threading.Thread):

    def __init__(self, name: str, maxlength: int, charset: str, cracker):
        self.__name = name
        self.__maxlength = maxlength
        self.__charset = charset
        self.__cracker = cracker
        threading.Thread.__init__(self)

    def __check(self, word: str) -> bool:
        if word == 'test':
            return True

        return False

    def run(self):
        try:
            print(f'Started {self.__name}')
            start = datetime.now()
            for attempt in product(self.__charset, repeat=self.__maxlength):
                if not self.__cracker.found:

                    pw = ''.join(attempt)
                    # print(f'{self.__name}: {pw}')
                    if self.__check(pw):
                        end = datetime.now()
                        dif = end - start
                        print(f'\n{self.__name}: found in {round(dif.total_seconds(), 2)} secs\n')
                        self.__cracker.found = True
                        self.__cracker.result = pw
        except Exception as e:
            print(e)

        print(f'Stopped {self.__name}')
