# PartitionsAndTableaux

Contains: 

a generator that returns all partitions of a given number 

a generator that gives all young tableaux to a partition 

a function that does the sliding operation of skewtableaux

a function that can multiply two tableaux

.

There are three versions of the tableaux generator: One standard version with ndarrays, one with lists
because it makes the output smaller and one that does the recursion in the other direction, because it is
maybe a little bit more pretty.

.

The objects are presented using ndarrays=matrices from numpy. Zeros (0) are used to show which entries of
the matrices dont correspond to boxes in the tableau/diagram. Negative ones (-1) are used in diagrams 
and in the deleted boxes of skewtableaux because they are not in the natural numbers and hence dont get 
confused with normal entries of a young tableau.

