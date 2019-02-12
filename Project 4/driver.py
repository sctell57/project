from project5 import * 
import traceback 
import subprocess 

def checkEqual(shipments1,shipments2): 
    #print [str(s) for s in shipments1] 
    #print [str(s) for s in shipments2] 
    ctr = 0 
    if len(shipments1) != len(shipments2): 
        return False 
    while ctr < len(shipments1): 
        shipment1 = shipments1[ctr] 
        shipment2 = shipments2[ctr] 
        if str(shipment1.getId()) != str(shipment2.getId()): 
            return False 
        if len(shipment1.getItems()) != len(shipment2.getItems()): 
            return False 
        i = 0 
        while i < len(shipment1.getItems()): 
            item1 = shipment1.getItems()[i] 
            item2 = shipment2.getItems()[i] 
            if str(item1) != str(item2): 
                return False 
            i = i + 1 
        ctr = ctr + 1 
         
    return True 
         


def test1(): 
    item = Item('sockz',12346,'$4.44') 
    return str(item) == 'sockz 12346 $4.44' 
     
def test2(): 
    item = Item('sockz',12346,'$4.44') 
    return str(item.getName()) == 'sockz'     
     
def test3(): 
    item = Item('sockz',12346,'$4.44') 
    return str(item.getId()) == '12346'         
     
def test4(): 
    item = Item('sockz',12346,'$4.44') 
    return str(item.getPrice()) == '$4.44'         
     
def test5(): 
    shipment = Shipment(55551555) 
    return str(shipment) == '55551555: []' 
     
def test6(): 
    shipment = Shipment(55551555) 
    return str(shipment.getId()) == '55551555'     
     
def test7(): 
    shipment = Shipment(55551555) 
    return shipment.getItems() == []         
     
def test8(): 
    item = Item('sockz',12346,'$4.44') 
    shipment = Shipment(55551555) 
    shipment.addItem(item) 
    return str(shipment) == '55551555: [sockz 12346 $4.44]'     
     
def test9(): 
    item = Item('sockz',12346,'$4.44') 
    shipment = Shipment(55551555) 
    shipment.addItem(item) 
    item = Item('shirt',33233,'$14.78') 
    shipment.addItem(item)         
    return str(shipment) == '55551555: [sockz 12346 $4.44,shirt 33233 $14.78]'         
     
def test10(): 
    item = Item('sockz',12346,'$4.44') 
    shipment = Shipment(55551555) 
    shipment.addItem(item) 
    result = main(['55551555\n','sockz 12346\n','$4.44\n'],[1]) 
     
    return checkEqual([shipment],result) 
     
def test11(): 
    shipments = [] 
    shipment = Shipment(55551555) 
    item = Item('sockz',12346,'$4.44')     
    shipment.addItem(item) 
    item = Item('shorts',33233,'$42.56')     
    shipment.addItem(item)         
    shipments.append(shipment) 

    result = main(['55551555\n','sockz 12346\n','$4.44\n','shorts 33233\n','$42.56\n'],[2]) 
     
    return checkEqual(shipments,result)     
     
def test12(): 
    shipments = [] 

    shipment = Shipment(55551555)     
    item = Item('sockz',12346,'$4.44') 
    shipment.addItem(item)     
    item = Item('shorts',33233,'$42.56')     
    shipment.addItem(item)     
    shipments.append(shipment)     

    item = Item('books',12346,'$4.44') 
    shipment = Shipment(66678) 
    shipment.addItem(item) 
    item = Item('mirror',33233,'$42.56')     
    shipment.addItem(item)             
    shipments.append(shipment)     

    shipment = Shipment(1) 
    item = Item('shoez',12346,'$4.44') 
    shipment.addItem(item)     
    item = Item('pencils',33233,'$42.56')     
    shipment.addItem(item)                             

    shipments.append(shipment)     

    result = main(['55551555\n','sockz 12346\n','$4.44\n','shorts 33233\n','$42.56\n','66678\n','books 12346\n','$4.44\n','mirror 33233\n','$42.56\n','necklace 33233\n','$42.56\n','1\n','shoez 12346\n','$4.44\n','pencils 33233\n','$42.56\n','eraser 33233\n','$42.56\n'],[2,2,2]) 

    return checkEqual(shipments,result)     
     
def test13(): 
    shipments = [] 
    item = Item('sockz',12346,'$4.44') 
    shipment = Shipment(55551555) 
    shipment.addItem(item) 
    shipments.append(shipment) 

    result = main(['55551555\n','sockz 12346\n','$4.44\n','sockz 12347\n','$4.44\n'],[1]) 
     
    return checkEqual(shipments,result)     
     
def test14(): 
    result = False 
    try: 
        main(['55551555\n','sockz12346\n','$4.44\n','sockz 12346\n','$4.44\n'],[2]) 
    except ItemException: 
        result = True 
     
    return result     
     
def test15(): 
    result = False 
    try: 
        main(['55551555\n','sockz 12346\n','4.44\n','sockz 12346\n','$4.44\n'],[2]) 
    except PriceException: 
        result = True 
     
    return result     
     
def test16(): 
    result = False 
    try: 
        main(['55551555\n','sockz 12346\n','$4.447\n','sockz 12346\n','$4.44\n'],[2]) 
    except PriceException: 
        result = True 
     
    return result         
     
def test17(): 
    result = False 
    try: 
        main(['55551555\n','sockz 12346\n','$4.44\n','sockz 12346\n','$-4.44\n'],[2]) 
    except PriceException: 
        result = True 
     
    return result         
     
def test18(): 
    result = False 
    try: 
        main(['55551555\n','sockz 12346\n','$4.44\n','sockz 12346\n','$4.44.56\n'],[2]) 
    except PriceException: 
        result = True 
     
    return result             
     
def test19(): 
    file = open("data.txt","w") 
    file.write("5555155555\nSocks 12346\n$5.59\n") 
    file.close() 
    list = processFile("data.txt") 
    return list == ["5555155555\n","Socks 12346\n","$5.59\n"] 
     
def test20(): 
    shipments = [] 

    shipment = Shipment(55551555)     
    item = Item('sockz',12346,'$4.44') 
    shipment.addItem(item)     
    item = Item('shorts',33233,'$42.56')     
    shipment.addItem(item)     
    shipments.append(shipment)     

    item = Item('books',12346,'$4.44') 
    shipment = Shipment(66678) 
    shipment.addItem(item) 
    item = Item('mirror',33233,'$42.56')     
    shipment.addItem(item)     
    item = Item('necklace',33253,'$42.56')     
    shipment.addItem(item)         
    shipments.append(shipment)     

    shipment = Shipment(1) 
    item = Item('sockz',12346,'$4.44') 
    shipment.addItem(item) 
    item = Item('pencils',33237,'$42.56')     
    shipment.addItem(item)                             
    item = Item('eraser',33233,'$42.56')     
    shipment.addItem(item)         
    shipments.append(shipment)     

    result = main(['55551555\n','sockz 12346\n','$4.44\n','shorts 33233\n','$42.56\n','shorts 33233\n','$42.56\n','66678\n','books 12346\n','$4.44\n','mirror 33233\n','$42.56\n','necklace 33253\n','$42.56\n','1\n','sockz 12346\n','$4.44\n','pencils 33237\n','$42.56\n','eraser 33233\n','$42.56\n'],[2,3,3]) 

    return checkEqual(shipments,result)     
     
def test21(): 
    shipments = [] 

    shipment = Shipment(55551555)     
    item = Item('sockz',12346,'$4.44') 
    shipment.addItem(item)     
    item = Item('shorts',33233,'$42.56')     
    shipment.addItem(item)     
    shipments.append(shipment)     

    item = Item('books',12346,'$4.44') 
    shipment = Shipment(66678) 
    shipment.addItem(item) 
    item = Item('mirror',33233,'$42.56')     
    shipment.addItem(item)         
    shipments.append(shipment)     

    shipment = Shipment(1) 
    item = Item('shoes',12346,'$4.44') 
    shipment.addItem(item) 
    item = Item('pencils',33233,'$42.56')     
    shipment.addItem(item)                                 
    shipments.append(shipment)     

    result = main(['55551555\n','sockz 12346\n','$4.44\n','shorts 33233\n','$42.56\n','66678\n','books 12346\n','$4.44\n','mirror 33233\n','$42.56\n','necklace 33233\n','$42.56\n','1\n','shoes 12346\n','$4.44\n','pencils 33233\n','$42.56\n','eraser 33233\n','$42.56\n'],[2,2,2]) 

    return checkEqual(shipments,result)         
     
failed = False 
ctr = 1 
while ctr <= 21: 
    try: 
        if eval("test"+str(ctr)+"()") == True: 
            print ("PASSED test"+str(ctr)+"!") 
        else: 
            print ("Please check your code for test"+str(ctr)) 
            failed = True 
    except Exception as e: 
        traceback.print_exc() 
        print ("Please check your code for test"+str(ctr)+", it raised an undesired exception") 
        failed = True 
    ctr = ctr + 1 
if not failed: 
    print ("You PASSED ALL TESTS")
    result = subprocess.check_output("curl -k    https://cs.gmu.edu/~kdobolyi/sparc/process.php?user=sparc_1HYLQORP12345678-sample_ass9_3-COMPLETED", shell=True)     
     
else: 
    print ("At least one test is not passing yet.")     
    result = subprocess.check_output("curl -k    https://cs.gmu.edu/~kdobolyi/sparc/process.php?user=sparc_1HYLQORP12345678-sample_ass9_3-PROGRESS", shell=True) 
     
