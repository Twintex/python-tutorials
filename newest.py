warehouse_items = ["indomie", "chivita", "rice", "beans", "sugar"]

first_item = warehouse_items[0]

last_item = warehouse_items[-1]

#Two more items added

warehouse_items.insert(-1, "paracetamol") 

warehouse_items.append( "morning fresh")

#Company sent to get an item 

warehouse_items.remove("rice")

#Late delivery

warehouse_items.append("omo")

warehouse_items.append("coke")

#Replay an item

warehouse_items[3] = "amatem"

#Company sent to get item

print(f"warehouse items is {warehouse_items}")