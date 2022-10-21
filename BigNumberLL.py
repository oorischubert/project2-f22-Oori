#Group:
#Oori Schubert
#Wesley Gilpin


class Link:
    def __init__(self, data):
        self.data = data
        self.prev = None   
        self.next = None   

    def __str__(self) -> str:
      return str(self.data)
  
class BigNumberLL: ### To complete
    
    def __init__(self, number=None):
        self.first = None
        self.last = None
        self.size = 0
        self.positive=True
        if number is not None:
            if number[0]=="-":
                self.positive=False
                number=number[1:] #skip negative sign
            for i in range(len(number)):
                self.insertLast(int(number[i]))
            self.trimFront()
    
    def insertLast(self, data) -> None:
        if self.first == None:
            self.first = Link(data)
            self.last = self.first
        else:
            newLink = Link(data)
            self.last.next = newLink
            newLink.prev = self.last 
            self.last = newLink
        self.size += 1
    
    def insertFirst(self, data) -> None:
        if self.first == None:
            self.first = Link(data)
            self.last = self.first
        else:
            newLink = Link(data)
            self.first.prev = newLink
            newLink.next = self.first
            self.first = newLink
        self.size += 1
    
    #Delete from double linked list if 0
    def deleteFirst(self):
        if self.first == None:
            return None
        else:
            temp = self.first
            self.first = self.first.next
            self.first.prev = None
            self.size -= 1
    
    def trimFront(self) -> None:
        while self.first.data == 0 and self.size is not 1:
            self.deleteFirst()
            
    def __str__(self) -> str:
        display = "[%s] "%(self.size)
        numDisplay = ""
        if not self.positive:
            display += "-"
        current = self.last #start at end
        count = 0
        while current != None:
            numDisplay += str(current.data)
            count += 1
            if count % 3 == 0 and current.prev is not None:
                numDisplay += ","
            current = current.prev #go backwards
        newNumDisplay = ""
        for i in range(len(numDisplay)): #flip the number to corretly show
            newNumDisplay += numDisplay[len(numDisplay)-i-1]
        return display + newNumDisplay
    
    def __gt__(self,y) -> bool:
        #Scan size of each 
        if self.positive and not y.positive: return True
        if not self.positive and y.positive: return False
        if self.positive:
            if self.size > y.size: return True
            elif self.size < y.size: return False
        if not self.positive:
            if self.size < y.size: return True
            elif self.size > y.size: return False
            newNumSelf = self
            newNumY = y
            newNumSelf.positive = True
            newNumY.positive = True
            return newNumY > newNumSelf
        else: 
            current = self.first
            yCurrent = y.first
            while current is not None:
                if self.positive: 
                    if current.data > yCurrent.data: return True
                elif not self.positive:
                  if current.data < yCurrent.data: return True
                current = current.next
                yCurrent = yCurrent.next
            return False

    def __lt__(self,y) -> bool:
        return(y>self)

    def __eq__(self,y) -> bool:
        if  self>y or y>self: return False
        else: return True 
        
    def __add__(self,y) -> "BigNumberLL":
        newNum = BigNumberLL()
        if self.positive and not y.positive:
            y.positive = True
            return self - y
        elif y.positive and not self.positive:
            self.positive = True
            return y - self
        if not self.positive and not y.positive:
            newNum.positive = False
        if self.size > y.size:
            biggerN = self
            smallerNum = y
        else: #order doesnt matter if they are equal size
            biggerN = y
            smallerNum = self
        bigCurrent = biggerN.last
        smallCurrent = smallerNum.last
        remainder = 0
        while bigCurrent is not None:
            bigData = bigCurrent.data
            if smallCurrent is None:
                smallData = 0
            else: 
                smallData = smallCurrent.data
                smallCurrent = smallCurrent.prev
            newData = bigData + smallData + remainder #add remainder to new row
            if newData >= 10:
                remainder = int(str(newData)[0])
                newNum.insertFirst(int(str(newData)[1]))
            else:
                remainder = 0
                newNum.insertFirst(newData)
            bigCurrent = bigCurrent.prev
        if remainder is not 0:
            newNum.insertFirst(remainder)
        return newNum

    def __sub__(self,y) -> "BigNumberLL":
        newNum = BigNumberLL()
        if not self.positive and y.positive:
            y.positive = False
            return self + y
        elif not self.positive and not y.positive:
            y.positive = True
            return y+self
        if y>self:
            biggerN = y
            smallerNum = self
            newNum.positive = False
        else: #order doesnt matter if they are equal size
            biggerN = self
            smallerNum = y
        bigCurrent = biggerN.last
        smallCurrent = smallerNum.last
        remainder = 0
        while bigCurrent is not None:
            bigData = bigCurrent.data
            if smallCurrent is None:
                smallData = 0
            else: 
                smallData = smallCurrent.data
                smallCurrent = smallCurrent.prev
            newData = bigData - smallData + remainder #add remainder to new row
            remainder = 0 #refresh
            if newData < 0:
                newData = 10 + newData
                remainder -=1
            newNum.insertFirst(newData)
            bigCurrent = bigCurrent.prev
        newNum.trimFront()
        return newNum

    def scale(self, factor) -> "BigNumberLL":
        newNum = BigNumberLL()
        current = self.last
        remainder = 0
        while current is not None:
            newData = (current.data * factor) + remainder
            remainder = 0 #refresh
            while newData >= 10:
                newData -= 10 #move over to remainder
                remainder += 1
            newNum.insertFirst(newData)
            current = current.prev
        newNum.insertFirst(remainder)
        newNum.trimFront()
        return newNum
    
    def __mul__(self,y) -> "BigNumberLL":
        newNum = BigNumberLL()
        if (self.positive and not y.positive) or (not self.positive and y.positive):
            newNum.positive = False
        current = self.last
        yCurrent = y.last
        remainder = 0 #used?
        while current is not None:
            self.scale(yCurrent)
            newNum += self
            current = current.prev
        newNum.trimFront()
        return newNum

#513 27 19 243

