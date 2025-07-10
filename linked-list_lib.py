####Library For Linked List Functions

list_directory = {

}

def create(name, length):
    '''
        Creates a list with the name <name> and <length> number of elements.
         

    '''
    global list_directory
    list_directory[name] = [[],[],length]

    #### Initializing the linked list pointer array:

    curr_list =  list_directory[name]

    
    for i in range(length):
        list_directory[name][1].append(i+1)
        list_directory[name][0].append('')
        ##curr_list[1].append(i + 1)
    ##list_directory.update({name : curr_list})


    
# create('j',2)
# print(list_directory)

####append
####pop
####update
####sort
 ###asc
 ###desc
 ###custom
####Merge



