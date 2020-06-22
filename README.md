# PartitionsAndTableaux

Contains: 

a generator that returns all partitions of a given number 

a generator that gives all young tableaux to a partition 

an implementation of the Schensted algorithm

a class for Tableaux

a method that does the sliding operation of skewtableaux

a method that can multiply two tableaux

a method that does the row insertion operation





.

There are three versions of the tableaux generator: One standard version with ndarrays, one with lists
because it makes the output smaller and one that does the recursion in the other direction, because it is
maybe a little bit more pretty.

.

The objects are presented using a new child class of ndarrays=matrices from numpy,that we made. Zeros (0) are used to show which entries of
the matrices dont correspond to boxes in the tableau/diagram. Negative ones (-1) are used in diagrams 
and in the deleted boxes of skewtableaux because they are not in the natural numbers and hence dont get 
confused with normal entries of a young tableau.

