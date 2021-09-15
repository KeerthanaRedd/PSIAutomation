#import gorcery
#gorcery_items =gorcery.gorcery_items
items =[]
    #gorcery.items
#need_to_shop = 'True'
    #gorcery.need_to_shop
def select_items_in_RD():

    need_to_shop = True
    vegnon_veg = {'veggies': {'Bringle': 27, 'bottlegard': 35},
                  'non_veg': {'chicken': 220, 'mutton': 880}}
    while need_to_shop == True:
        print("select items in store")
        print("display items in list")
        print("---------------------------")
        print(vegnon_veg)
        print("---------------------------")
        #item1 = soap_sampoos[input("enter key to select items")]
        #print(item1)
        item2= vegnon_veg[input("enter key to select items")][input("enter key to select items")]
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