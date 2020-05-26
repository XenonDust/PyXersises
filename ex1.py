

ret_list=[]
def new_ticket(airline,srce,dstn,counter):
    print("AL1:"+(srce[:3].upper())+":"+(dstn[:3].upper())+":"+str(counter)
    ret_list.append(counter+1)
    if len(ret_list)>5:
        ret_list.remove(ret_list[0])
    return ret_list
