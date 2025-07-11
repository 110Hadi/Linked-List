####Library For Linked List Functions

list_directory = {

}

def create(name, length):
    '''
        Creates a list with the name <name> and <length> number of elements.
         
    '''
    global list_directory
    sp = -1
    flp = 0
    ep = -1
####                      list-freelist-metadata
    list_directory[name] = [[],[],[length, sp, flp, ep]]

    #### Initializing the linked list pointer array:

    curr_list =  list_directory[name]

    
    for i in range(length):
        list_directory[name][1].append(i+1)
        list_directory[name][0].append('')
    list_directory[name][1].append(-1)
        ##curr_list[1].append(i + 1)
    ##list_directory.update({name : curr_list})


    
# create('j',2)
# print(list_directory)

def flp_init(name):


    flp = 0
    for i in list_directory[name][0]:
        if i != '':
            flp += 1

        if flp >= list_directory[name][2][0]:
            flp = -1
    return flp

####append
####Before using this func ensure that the list is not already full
def linked_append(name, item):
    global list_directory

    curr_list = list_directory[name]
    flp = curr_list[2][2]

    #### Adding item
    if flp != -1:
        curr_list[0][flp] = item
        if curr_list[2][1] == -1:
            curr_list[2][1] = flp ###change in the dict as well
    
        curr_list[2][2] = curr_list[1][flp]

#### Adding another one
def ascending(name):
    global list_directory

    curr_list = list_directory[name]
    sp = curr_list[2][1]
    flp = curr_list[2][2]

    
    ####Preparing a sorted list
    sorted = curr_list[0].sort()
    count = 0
    for i in sorted:
        if i == '':
            sorted.remove('')
            count += 1
    ### Sorted list prepped

    for i in curr_list[0]:
        if i == sorted[0]:
            sp = curr_list[0].index(i)
            break

    pointer = sp
    for count in range(1,5):
        pointer = curr_list[0].index(i)
        for i in curr_list[0]:
            if i == sorted[count]:
                curr_list[1][pointer] = curr_list[0].index(i)
                

    
    # pointer = 0
    # flp = flp_init(name)
    # if flp == 0:
    #     sp = -1
    # else:
    #     sp = curr_list[2][1]



    # curr_list[0][flp] = item
    # sp = flp

    # new_flp = curr_list[1][flp]
    # ep = curr_list[2][3]
    # prev_pointer = 0
    
    # pointer = sp
    # if curr_list[0][pointer] < curr_list[0][flp]:
    #     prev_pointer = pointer
    #     pointer = curr_list[1][pointer]
    # else:
    #      curr_list[1][flp] = pointer
    #      curr_list[1][prev_pointer] = flp
    #      curr_list[1][ep] = new_flp
    #      ##flag for ADDED

    


    

    


####pop
def linked_pop(name, item):
    if name:
        print()
####update
####sort
 ###asc
 ###desc
 ###custom
####Merge






