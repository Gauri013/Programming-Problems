cell_state_list = []
def jailProb():
    begin = 2
    for i in range(0,101):
        isOpen = False
        cell_state_list.append(isOpen)
    end = 101
    while (begin != end ):
        begin = change_cells(begin)
    return cell_state_list

def change_cells(begin):
    for i in range (begin , 101, begin):
        if(cell_state_list[i] ):
            cell_state_list[i] =  False
        else:
            cell_state_list[i] = True 
    return (begin+1)
            
def answer():
    answer_list = jailProb()
    for i in range(1,101):
        if(answer_list[i]):
            print(i,"open")
        else:
            print(i,"close")
        
answer()