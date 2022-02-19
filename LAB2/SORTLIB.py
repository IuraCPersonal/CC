
class quicksort():
    def __init__(self) -> None:
        pass

    def sort(self, array: list = None, start: "int >= 0" = 0, end: "int > 1" = 2) -> list:
        '''
        :param array: list
            The given array that should be sorted.
        :param start: int > 0
            Starting index.
        :param end: int > 0
            Ending index.
        '''

        low, high = start, end
        pivot = array[int((low + high) / 2)]

        while (low <= high):

            while array[low] < pivot:
                low += 1

            while array[high] > pivot:
                high -= 1

            if (low <= high):
                array[low], array[high] = array[high], array[low]
                low += 1
                high -= 1

        if (high > start):
            self.sort(array, start, high)

        if (low < end):
            self.sort(array, low, end)


class mergesort():
    def __init__(self) -> None:
        pass

    def sort(self, array: list = None) -> list:
        '''
        :param array: list
            The given array that should be sorted.
        '''

        if len(array) > 1:
            middle = len(array) // 2
            left, right = array[:middle], array[middle:]

            self.sort(left)
            self.sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k], i = left[i], i + 1
                else:
                    array[k], j = right[j], j + 1
                k = k + 1

            while i < len(left):
                array[k] = left[i]
                i, k = i + 1, k + 1

            while j < len(right):
                array[k] = right[j]
                j, k = j + 1, k + 1


class heapsort():
    def __init__(self) -> None:
        pass

    def __heapify(self, arr, size, idx):
        # Initialize largest as root at index i, left = 2 * i + 1, right = 2 * i + 2.
        largest, left, right = idx, 2 * idx + 1, 2 * idx + 2

        if left < size and arr[largest] < arr[left]:
            largest = left

        if right < size and arr[largest] < arr[right]:
            largest = right

        if largest != idx:
            arr[idx], arr[largest] = arr[largest], arr[idx]

            self.__heapify(arr, size, largest)

    def sort(self, array: list = None) -> list:
        '''
        :param array: list
            The given array that should be sorted.
        '''

        length = len(array)

        # Build a maxheap.
        for i in range(length // 2 - 1, -1, -1):
            self.__heapify(array, length, i)

        # One by one extract elements
        for i in range(length - 1, 0, -1):
            # Perform the swapping
            array[i], array[0] = array[0], array[i]
            self.__heapify(array, i, 0)


class cocktailsort():
    def __init__(self) -> None:
        pass

    def sort(self, array: list = None) -> list:
        '''
        :param array: list
            The given array that should be sorted.
        '''

        length = len(array)
        swapped = True
        start, end = 0, length - 1

        while swapped == True:
            # reset the swapped flag on entering the loop,
            # because it might be true from a previous
            # iteration.
            swapped = False

            # loop from left to right same as the bubble
            # sort
            for i in range(start, end):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True
            
            # if nothing moved, then array is sorted.
            if (swapped == False):
                break
                
            # otherwise, reset the swapped flag so that it
            # can be used in the next stage
            swapped = False
            end -= 1

            # from right to left, doing the same
            # comparison as in the previous stage
            for i in range(end - 1, start - 1, -1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

            # increase the starting point, because
            # the last stage would have moved the next
            # smallest number to its rightful spot.
            start += 1