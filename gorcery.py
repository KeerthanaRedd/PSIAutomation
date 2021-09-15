import gorcery_store
print("Apps Available for gorceries")
check = []

def select_store(argument):
    gorcery_store.Gorcery_cal()
    print("hello")
    '''while again==True:
        print("list of shop in your area", switcher)
        store = switcher[input("enter in which store you want to shop")]
        if (store == 'Dmart'):
            check =Dmart.select_items_in_Dmart()
            for i in check:
                gorcery_items += i
            print("Total amount you have to pay for shopped items", gorcery_items)
            gorcery_items =0
        elif (store == 'RatnaDeep'):
            check = RatnaDeep.select_items_in_RD()
            for i in check:
                gorcery_items += i
            print("Total amount you have to pay for shopped items", gorcery_items)
            gorcery_items =0
        print("----------------------------------------------")
        again = input("want to shop again by selecting the gorcery stores click y/n").upper()
        if(again =='N'):
            return 0
        else :
            again = True'''

#print("select gorcery shop")

# Driver program
if __name__ == "__main__":
    argument=0
    #gorcery_items =0
    print("------------------------------")
    call =select_store(argument)
    #select_items_in_Dmart()
    #for i in :
    #    gorcery_items += i
    #print("Total amount you have to pay for shopped items",gorcery_items)