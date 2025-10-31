# Python code for the above approach
# function to calculate the number
# of divisors of each number
def calcDivisors():
    divisors = [0]*100
    for i in range(1, 100):
        for j in range(i, 100, i):
            divisors[j] += 1
    return divisors

# function for updating the value
def update(x, val, n, BIT):
    while x <= n:
        BIT[x] += val
        x += (x & -x)

# function for calculating the required
# sum between two indexes
def sum(x, BIT):
    s = 0
    while x > 0:
        s += BIT[x]
        x -= (x & -x)
    return s

# function to return answer to queries
def answerQueries(arr, que, n, q):
  
    # Declaring a Set
    s = set()
    BIT = [0] * (n + 1)
    divisors = calcDivisors()
    for i in range(1, n):
      
        # inserting indexes of those numbers
        # which are greater than 2
        if arr[i] > 2:
            s.add(i)
        update(i, arr[i], n, BIT)
    for i in range(q):
        # update query
        if que[i][0] == 1:
            leftIndex = que[i][1]
            rightIndex = que[i][2]
            for it in set(s):
                if it >= leftIndex and it <= rightIndex:
                    # update the value of arr[i] to
                    update(it, divisors[arr[it]] - arr[it], n, BIT)
                    arr[it] = divisors[arr[it]]
                    if arr[it] <= 2:
                        s.remove(it)
        # sum query
        else:
            print(sum(que[i][2], BIT) - sum(que[i][1] - 1, BIT))

# Driver Code
if __name__ == '__main__':
  
    # precompute the number of divisors for each number
    # input array
    arr = [0, 6, 4, 1, 10, 3, 2, 4]
    n = len(arr)
    
    # declaring array of structure of type queries
    que = [(2, 1, 7), (2, 4, 5), (1, 3, 5), (2, 4, 4)]
    
    # answer the Queries
    answerQueries(arr, que, n, len(que))

    # This code is contributed by lokeshpotta20
