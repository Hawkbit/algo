# Big O Notation is about saving time or space

# simple search on 100 items can take up to 100 guesses -> O(n) -> linear time
# binary search on 100 items can take up to 7 guesses -> O(log n) -> logarithmic time

# Big O Notation tells how fast the algorithm is - it establishes a worst-case run time

# Big O        Example
# O(log n)     Binary search
# O(n)         Simple search
# O(n log n)   Quicksort
# O(n^2)       Selection sort
# O(n!)        Traveling salesperson

# algorithm speed is not measured in seconds, rather growth of the number of operations
# instead, we discuss how quickly the runtime of the algorithm increases as the size of input increases
# runtime is expressed in Big O notation
#
#
#

# The Travelling Salesperson
# The person wants to travel to five cities most efficently as possible.
# Much of Computer Science belives this O(n!) algorithm can't be more efficient
