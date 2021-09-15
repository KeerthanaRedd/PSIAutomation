#import gorcery
#gorcery_items =gorcery.gorcery_items
items =[]
    #gorcery.items
#need_to_shop = 'True'
    #gorcery.need_to_shop
def select_items_in_Dmart():

    need_to_shop = True
    soap_sampoos={'soaps':{'santoor':25,'lux':30},
                  'shampoo':{"meera":5,"karthika":10},
                  'babysoaps':{'himalaya':60,'jonson':70},}
    while need_to_shop == True:
        print("select items in store")
        print("display items in list")
        print("---------------------------")
        print(soap_sampoos)
        print("---------------------------")
        #item1 = soap_sampoos[input("enter key to select items")]
        #print(item1)
        item2= soap_sampoos[input("enter key to select items")][input("enter key to select items")]
        #items += item2
        items.append(item2)
        #need_to_shop = \
        need_to_shop = (input("enter do you want to select more items from gorcery store Y/N")).upper()
        if need_to_shop == "N" :
            need_to_shop = False
        else:
            need_to_shop = True
        print(need_to_shop)
    print(items)
    return items
    #for i in items:
     #   gorcery_items += i
    #print("Total amount you have to pay for shopped items", gorcery_items)