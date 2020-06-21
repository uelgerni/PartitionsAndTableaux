# really fast algorithm because it only has to calculate each partition once, including each sub partition.
# as in: if you do the partition for 6 it only calculates the partition for 4 once
# and gives it back for every case where its needed


def partitionGenerator(n, offset=1):
    yield n,
    for i in range(offset, n // 2 + 1):  # going farther would give for example (1,4) in addition to (4,1)
        for p in partitionGenerator(n - i, i):
            yield p + (i,)


partitions = sorted(partitionGenerator(50), reverse=True)
for partition in partitions:
    print(partition)
