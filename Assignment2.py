class LinkedList:
    class ListNode:
        def __init__(self, data=None):
            self.next
            self.prev
            self.data

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def append(self, data):
        n = LinkedList.ListNode(data)

        if self.first is None:         # Special case for empty lists
            self.first = n
            self.last = n
        else:  # Add the node to the end.
            n.prev = self.last    # the old .last becomes the new nodes previous
            self.last.next = n    # the old .last needs it's next to point to the new node
            self.last = n         # point the .last node to be the new node.

        self.count += 1

    def size(self):
        return self.count

    def iter(self):
        curr = self.first
        while curr:
            ret = curr.data
            curr = curr.next
            yield ret

    def delete(self, data):
        curr = self.first
        deleted_fl = False

        if curr is None:  # LIST IS EMPTY, TRIVIAL CASE
            deleted_fl = False
        elif curr.data == data:  # REMOVE FROM FRONT
            self.first = curr.next
        elif self.tail.data == data:  #REMOVE FROM END
            self.tail = self.tail.prev
            self.tail.next = None
            deleted_fl = True
        else:  # SEARCH THE REST TO SEE IF IT MATCHES
            while curr:
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    deleted_fl = True

        if deleted_fl:
            self.count -= 1

    def contains(self, data):
        for n in self.iter():
            if data == n:
                return True
            return False

    def search(self, data):
        curr = self.first
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def clear(self):
        self.first = None
        self.last = None

#########################################################
####### IMPLEMENT THE FOLLOWING 2 FUNCTIONS  ############
#########################################################
    def charCount(self, aggregated=False):
         """ Returns the total number of characters contained in the nodes of the linked list.
         If the `aggregated' argument is True, the result should be a single integer
         representing the sum of character counts of all elements in the LinkedList.  If False,
         the result should be a list of integers representing the count of characters of each
         node.  In both cases, if the list is empty, return `None'.  The aggregated version of
         this method should be O(1) and the dis-aggregated version should be O(n).

         :param aggregated: If True, aggregate the counts into a single value. If False, return
         a list of counts.
         :return: A single integer or list of integers as described above.
         """
         pass


    def reverse(self, in_place=False):
        """ Reverses the order of elements of the list, either in place (modifies the existing
        list) or replicates and returns a new copy of the list.  If in_place==True then
        modifications should be made to `self'. If in_place==False do not modify self, but
        rather create a new list and return the new list to the caller.  If the list is empty,
        in_place==True should do nothing, and in_place==False should return a new empty
        LinkedList.  Reverse should be no worse than O(n).

        :param in_place: If True, operations are performed on this instantiation of the List.
        Returns a new reversed version of the list otherwise.
        :return: If in_place == True, returns None, otherwise returns a new LinkedList object.
        """
        pass



class Queue:
## STUDENT TO RENAME TO class Deque ##
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None


    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def enqueue(self, data):
        n = Queue.QueueNode(data)
        if self.top is None:  # EMPTY
            self.top = n
            self.bottom = n
        else:
            self.bottom.prev = n
            n.next = self.bottom
            self.bottom = n
        self.size += 1

    def dequeue(self):
        ret = self.top

        if self.size == 1:
            self.top = None
            self.bottom = None
        elif self.size > 1:
            self.top = self.top.prev
            self.top.next = None

        if self.size >= 1:
            self.size -= 1
            return ret.data

#########################################################
####### IMPLEMENT THE FOLLOWING 4 FUNCTIONS  ############
#########################################################
        def addFirst(self, data):
            """ Creates a new node at the beginning of the queue, containing the value of data.

            :param data: The data to be contained in the newly created element.
            :return: None
            """
            pass


        def addLast(self, data):
            """ Creates a new node at the beginning of the queue, containing the value of data.

            :param data: The data to be contained in the newly created element.
            :return: None
            """
            pass


        def removeFirst(self):
            """ Returns the data of the node that is at the "start" of the Deque.
            :return: The data stored in the node that is at the "start" of the Deque.
            """
            pass


        def removeLast(self):
            """ Returns the data of the node that is at the "end" of the Deque.
            :return: The data stored in the node that is at the "end" of the Deque.
            """
            pass