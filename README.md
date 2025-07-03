# Assignment-6-Medians-and-Order-Statistics-Elementary-Data-Structures

## Assignment 6: Medians and Order Statistics & Elementary Data Structures

### Medians and Order Statistics & Elementary Data Structures

---

## Part 1: Selection Algorithms

The main objective of this part is to implement and analyze deterministic selection using median of medians and randomized quickselect algorithm. 

### Time Complexity Analysis

| Algorithm            | Best Case | Average Case | Worst Case | Space Complexity |
|----------------------|-----------|--------------|------------|------------------|
| Randomized Select    | O(n)      | O(n)         | O(n^2)     | O(1)             |
| Deterministic Select | O(n)      | O(n)         | O(n)       | O(n)             |

Randomized select is efficient in practice because it has a low overhead and expected linear time. Deterministic MoM on the other hand has a linear time but with larger constants and more recursion which makes it less efficient. The following are the empirical results of the two analyses. 

### Empirical Results

| Input Size | Randomized Time (seconds) | Deterministic Time (seconds) |
|------------|---------------------------|-------------------------------|
| 1000       | 0.001606                  | 0.006830                      |
| 2000       | 0.002999                  | 0.010559                      |
| 5000       | 0.010174                  | 0.024297                      |
| 10000      | 0.046885                  | 0.046875                      |

**Observation**: The observation from the results above is that randomized select is outperforming the deterministic method in terms of time taken which means it is much better and more efficient.

---

## Part 2: Elementary Data Structures

The purpose of this section is to implement structures. We are going to implement a custom array with insert, delete and access, Stack (LIFO) using array, Queue (FIFO) using array, and Singly Linked List with insertion, deletion, and traversal. 

### Time Complexity Summary

| Operation              | Array | Stack | Queue | Linked List |
|------------------------|-------|-------|--------|--------------|
| Insert (end or head)   | O(1)  | O(1)  | O(1)   | O(1)         |
| Delete (index or value)| O(n)  | O(1)  | O(n)   | O(n)         |
| Access (by index)      | O(1)  | O(1)  | O(1)   | O(n)         |

---

### Output Summary from the Code

Array contents: [5, 10]

Array after deletion: [10]

Stack peek: 2

Stack after pop: [1]

Queue dequeue: A

Queue after dequeue: ['B']

Linked List traversal: [300, 200, 100]

Linked List after deletion: [300, 100]


---

## Discussion

The first observation was that array has a fast access by index, but there are slower deletions except when removing the last element. Stacks and Queues on the other hand are more efficient for push/pop and enqueue/dequeue operations while the Linked lists is best in terms of dynamic memory scenarios. They are also more flexible but their access time is longer. 

---

## Conclusion

Based on the above results, stacks can be useful in recursion, parsing, and backtracking operations while queues are best for scheduling, streaming, and buffering tasks. Linked lists on the other hand can be used on tasks such as real-time insert/delete operations where we don't need memory reallocation.

