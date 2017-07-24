class Node(object):
    """ A singly-linked node. """
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
class LinkedList(object):
    """ A singly-linked list. """
    def __init__(self):
        self.head = None
         
    def insert_start(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        actual_node = self.head
        
        while actual_node.next_node is not None:
            actual_node = actual_node.next_node
            
        actual_node.next_node = new_node
            
    def remove(self, data):
    
        if self.head is None:
            return
        
        current_node = self.head
        previous_node = None
        
        while current_node.data != data:
            if current_node.next_node is not None:
                previous_node = current_node
                current_node = current_node.next_node    
            else:
                print ('can not find remove data')
                return
            
        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node       
             
    def count(self):
        
        actual_node = self.head
        count = 0
        
        while actual_node is not None:
            count += 1
            actual_node = actual_node.next_node
            
        return count
               
    def traverse_list(self): 
        actual_node = self.head      
        while actual_node is not None:
            print("{0}".format(actual_node.data))
            actual_node = actual_node.next_node

def main():
    linked_list = LinkedList()

    linked_list.insert_start(1)
    linked_list.insert_start(2)
    linked_list.insert_start(3)
    linked_list.insert_end(4)

    linked_list.traverse_list()

    linked_list.remove(1)
    linked_list.remove(1)
    linked_list.remove(1)
    linked_list.remove(4)

    linked_list.traverse_list()
    print(linked_list.count())


if __name__ == '__main__':
    main()

