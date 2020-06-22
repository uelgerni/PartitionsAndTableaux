# this works by the following method:
# first it yields the trivial partition of the number itself,
# then it yields all the partitions with a 1 at the end by calculating all the partitions of n-1 and appending 1
# then the same for n-2 and appending a 2 etc etc
# you can easily see this if you dont sort the partitions you get back

import time


def partitionGenerator(n, offset=1):
    yield n,  # yield a list
    for i in range(offset, n // 2 + 1):  # going farther would give for example (1,4) in addition to (4,1)
        for partition in partitionGenerator(n - i, i):
            yield partition + (i,)  # yield partition for n-rest, append rest


def partitionPrinter(partitions):
    for partition in partitions:  # this is to get the the first result in our generator function which corresponds to n
        number = str(partition[0]) + " = "
        break
    for partition in partitions:
        result = number
        for i in range(len(partition) - 1):
            result += (str(partition[i]) + " + ")
        result += str(partition[-1])
        print(result)



# partitionPrinter(sorted(partitionGenerator(13), reverse=True))
# time1 = time.time()
# list(partitionGenerator(50))
# time2 = time.time()
# print("{:.10f}".format(time2 - time1))
