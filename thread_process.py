# Потоки и процессы в Python
# В Python используется GIL (Global Interpreter Lock), который однопоточный.
# Все потоки, которые создаются с помощью threading будут работать внутри потока GIL.
# В связи с этим они будут обрабатываться только одним ядром. Ни о какой работе одновременно на нескольких физических ядрах процессора не может быть и речи.
# А так как threading будет выполняться только на одном ядре процессора, то нету преимущества по скорости, только наоборот — threading замедлит работу.

from threading import Thread
import time
import datetime


def sum(x, count):
    time_start = datetime.datetime.now()
    print(f'Поток 1. Старт {time_start}')

    res = x
    for i in range(count):
        res += x/100000
    print(res)

    time_stop = datetime.datetime.now()
    print(f'Поток 1. Стоп {time_stop}')
    cont_time = time_stop - time_start
    print(f'Поток 1. Прошло {cont_time.seconds} секунд {cont_time.microseconds} микросекунд')



def sub(x, count):
    time_start = datetime.datetime.now()
    print(time_start)

    res = x
    for i in range(count):
        res -= x/100000
    print(res)

    time_stop = datetime.datetime.now()
    print(time_stop)
    cont_time = time_stop - time_start
    print(f'Поток 2. Прошло {cont_time.seconds} секунд {cont_time.microseconds} микросекунд')


def count_time():
    time_start = datetime.datetime.now()
    time_stop = datetime.datetime.now()
    cont_time = time_stop - time_start
    print(f'Прошло {cont_time.seconds} секунд {cont_time.microseconds} микросекунд')

seconds = time.time()
local_time = time.ctime(seconds)
# print(local_time)
struct_time = time.localtime(seconds)
time_string = time.strftime("%d.%m.%Yг. %A %H:%M:%S", struct_time)
print(f'Текущее время {time_string}')
print('='*50)



count = 50000000


th_1 = Thread(target=sum, args=(1, count))
th_1.start()
# th_2 = Thread(target=sub, args=(1, count))
# th_2.start()

for i in range(10):
    time.sleep(0.5)
    print(f'Цикл {i}')

# sum(1, count)
# sub(1, count)



