from datetime import datetime

from Cracker import Cracker

if __name__ == '__main__':
    start = datetime.now()
    cracker = Cracker()
    cracker.setup(12)
    res = cracker.run()
    end = datetime.now()
    dif = end - start
    print(f'\n\nResult: {res}\nEnded after in {round(dif.total_seconds(), 2)} secs')
