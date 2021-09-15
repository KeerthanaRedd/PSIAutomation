import gorcery
import Dmart
import RatnaDeep
def Gorcery_cal():
    gorcery_items = 0
    # again =True
    switcher = {
        '1': 'Dmart',
        '2': 'RatnaDeep'
    }
    print("list of shop in your area", switcher)
    again = True
    while again == True:
        print("list of shop in your area", switcher)
        store = switcher[input("enter in which store you want to shop")]
        if (store == 'Dmart'):
            check = Dmart.select_items_in_Dmart()
            for i in check:
                gorcery_items += i
            print("Total amount you have to pay for shopped items", gorcery_items)
            gorcery_items = 0
        elif (store == 'RatnaDeep'):
            check = RatnaDeep.select_items_in_RD()
            for i in check:
                gorcery_items += i
            print("Total amount you have to pay for shopped items", gorcery_items)
            gorcery_items = 0
        print("----------------------------------------------")
        again = input("want to shop again by selecting the gorcery stores click y/n").upper()
        if (again == 'N'):
            return 0
        else:
            again = True