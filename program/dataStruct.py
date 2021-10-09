'''this is a tool for beginner programmers,
I'm just making python implementation of various datastrucutes
because when you start programming, it's important to use them 
but it's really hard for a beginner to create them rahter to use them'''


class Stack:
    def __init__(self):
        self.stack_ = []
    
    def is_empty(self):
        return(len(self.stack_) == 0)
    
    def insert(self, data):
        self.stack_.append(data)
    
    def delete(self):
        return(self.stack_.pop(-1))

class Queue:
    def __init__(self):
        self.queue_ = []
    
    def is_empty(self):
        return(len(self.queue_) == 0)
    
    def insert(self, data):
        self.queue_.append(data)
    
    def delete(self):
        return(self.queue_.opo(0))

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return(len(self.queue) == 0)
    
    def insert(self, priority, data):
        self.queue.append((priority, data))

    def delete(self):
        if self.is_empty(): return []
        else:
            max_ = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] > self.queue[max_][0]:
                    max_ = i
            item = self.queue[max_]
            del self.queue[max_]
            return item

class Deque:
    def __init__(self):
        self.deque_ = []

    def is_empty(self):
        return(len(self.deque_) == 0)
    
    def insert(self, data, position='r'):
        '''insert the data in the deque, position must be 'r'(rear) or 'f'(front)'''
        if position == 'r': self.deque_.append(data)
        elif position == 'f': self.deque_.insert(0, data)
        else: raise ValueError("mode must be 'r' for rear or 'f' for front")
    
    def delete(self, position='r'):
        '''extract the data from the deque, position must be 'r'(rear) or 'f'(front)'''
        if position == 'r': return(self.deque_.pop(-1))
        elif position == 'f': return(self.deque_.pop(0))
        else: raise ValueError("mode must be 'r' for rear or 'f' for front")

class Array:
    def __init__(self, size, base_value=0):
        self.arr = [[base_value for x in range(size[0])] for y in range(size[1])]
        self.size = size

    def insert(self, position, data):
        '''insert @data at @position (must be Row then Column)'''
        self.arr[position[1]][position[0]] = data
    
    def extract(self, position):
        '''Extract the data at @position (must be Row then Column)'''
        return(self.arr[position[1]][position[0]])

    def row(self, position):
        return(self.arr[position])
    
    def column(self, position):
        return([self.arr[x][position] for x in range(self.size[1])])
