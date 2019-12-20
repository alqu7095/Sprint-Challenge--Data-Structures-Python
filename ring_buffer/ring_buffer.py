from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()


    def append(self, item):
        # length = capacity
        if self.storage.length == self.capacity:
            #value to oldest item
            self.current.value = item
            if self.current is self.storage.tail:
                # if value is the oldest then move to front
                self.current = self.storage.head
            else:
                #move to next
                self.current = self.current.next
        # then it is not full or completed
        elif self.storage.length < self.capacity:
            #so there's space
            self.storage.add_to_tail(item)
            #after adding to tail the current is the head
            self.current = self.storage.head


    def get(self):
        list_buffer_contents = []
        # current is head
        cur = self.storage.head
        while(cur):
            list_buffer_contents.append(cur.value)
            cur = cur.next

        return list_buffer_contents


    # def get(self):
    #     list_buffer_contents = [item for item in self.storage if item != None]

        # return list_buffer_contents

        # if self.storage != None:
        #     for i in self.storage:
        #         if i != None:
        #             array.append(i)
        # return list_buffer_contents

# if __name__ == "__main__":
#     buffer = RingBuffer(3)
#     print(buffer.get())

#     buffer.append('a')
#     buffer.append('b')
#     buffer.append('c')

#     buffer.append('d')
#     print(buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
