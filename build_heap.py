# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for k in range(n // 2-1,-1,-1):
      i=k
      while 2*i+1<n:
        min = 2*i+1
        if min >= n:
          break
          
        if min+1<n:
          if data[min]>data[min+1]:
            min= min+1
          
        if data[i] > data[min]:
          swaps.append((i, min))
          (data[i], data[min]) = (data[min], data[i])
          i = min
        else:
          break


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    tips = input()
    # input from keyboard
    if tips[0] == "I":
        n = int(input())
        data = list(map(int, input().split()))
    # checks if lenght of data is the same as the said lenght
        assert len(data) == n

    elif tips[0] == "F":
      file = input()
      f = open("./test/" + file,'r')
      n = int(f.readline())
      data = list(map(int, f.readline().split()))
      assert len(data) == n
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
