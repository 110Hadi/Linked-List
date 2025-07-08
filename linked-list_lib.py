####Library For Linked List Functions

list_directory = {


}

def create(name, length):
    '''
        Creates a list with the name <name> and <length> number of elements.
         

    '''
    list_directory[name] = [[],[],length]

    #### Initializing the linked list pointer array:

    curr_list =  list_directory[name]

    
    for i in range(length):
        curr_list[1].append(i + 1)
    print(curr_list[1])

create('j',2)
