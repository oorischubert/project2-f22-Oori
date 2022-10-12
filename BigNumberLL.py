#Group:
#Oori Schubert
#Wesley Gilpin


class Link:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
      return str(self.data)

#The stack is displayed in reverse order (top at the bottom).
# The constructor of BigNumberLL accepts one input String argument that may contain a negative sign (first character).
#When the big number is displayed, the number of digits that composed the number (i.e. size of the Linked-List) is also displayed at first between square brackets.
#If the user enters meaningless zero on the left, they are removed from the Link-list before displaying.
#To ease the reading of the big number, a comma “,” is placed every three digits. Basic methods to implement
#insertLast: If you read a String, character by character from left to right, you need to be able to insert each integer (converted from the character) inside the linked-list while keeping the ordering of a queue. For example: 3,458, do insertLast(3), insertLast(4), etc. This method can be used inside your constructor.
#insertFirst: reverse the order of insertion. This method is not needed for this preliminary part of the project but it is a kernel method which is needed by the next tasks. While doing an operation (for example addition), you often perform it step by step from the right to the left. The resulting integer needs to be inserted in the list using insertFirst to make sure that the ordering of the final number is correct.
#deleteFirst: it is used by the trimFront method.
#trimFront: if the BigNumber list contains a lot of zeros on the left, you can trim this number
#(remove the zeros) and reduce its size. This method can be used inside your constructor.
# str : Convert the big number list into a string that can be used to print by the Stack. A negative sign must be added at the beginning of the String if the number is negative (i.e. ’positive’ flag equal to False). The size of the linked-list is also displayed at first between square brackets. For full credit, you will also include a comma “,” to separate all the thousands. For example: 3458 is “3,458”; 345 is “345”, 12349875 is “12,349,875”. Hint: various techniques possible. You could scan the linked-list from right to left, keep track of the number of digits, and check the remainder while dividing by 3.
#All following Tasks 1, 2, and 3 can be implemented in any order. Task 4 and 5 should be the last two you implement.


  
class BigNumberLL: ### To complete
    
    def __init__(self, number):
        self.first = None
        self.last = None
        self.size = 0
        self.positive=True
        if number[0]=="-":
          self.positive=False
          number=number[1:]
        for i in range(len(number)):
            self.insertLast(int(number[i]))
        self.trimFront()
    
    def insertLast(self, data):
        if self.first == None:
            self.first = Link(data)
            self.last = self.first
        else:
            newLink = Link(data)
            self.last.next = newLink
            newLink.prev = self.last
            self.last = newLink
        self.size += 1
    
    def insertFirst(self, data):
        if self.first == None:
            self.first = Link(data)
            self.last = self.first
        else:
            newLink = Link(data)
            self.first.prev = newLink
            newLink.next = self.first
            self.first = newLink
        self.size += 1
    
    def deleteFirst(self):
        if self.first == None:
            return None
        else:
            temp = self.first
            self.first = self.first.next
            self.size -= 1
            return temp.data
    
    def trimFront(self):
        while self.first.data == 0:
            self.deleteFirst()
    
    def __str__(self):
        display = ""
        display += "["
        display += str(self.size)
        display += "] "
        if not self.positive:
            display += "-"
        current = self.last
        count = 0
        while current != None:
            display += str(current.data)
            count += 1
            if count % 3 == 0:
                display += ","
            current = current.prev
        return display
    
 



