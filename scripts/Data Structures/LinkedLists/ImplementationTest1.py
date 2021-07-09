"""
Linked lists are, as the name suggests, a list which is linked.
It consists of nodes which contain data and a pointer to the next node in the list.
The list is connected with the help of these pointers.
These nodes are scattered in memory, quite like the buckets in a hash table.
The node where the list starts is called the head of theblist and the node where it ends, or last node, is called the tail of the list.
The average time complexity of some operations invloving linked lists are as follows:
Look-up : O(n)
Insert : O(n)
Delete : O(n)
Append : O(1)
Prepend : O(1)
Python doesn't have a built-in implementation of linked lists, we have to build it on our own
So, here we go. """