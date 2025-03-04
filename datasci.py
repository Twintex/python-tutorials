import pandas as pd

#Dictionary of customer purchase data 

data = { 
    "Customer_ID" : [101, 102, 103],
    "Purchase_Amount" : [250.75, 320.60, 150.40],
    "Location" : ["New York", "Los Angeles", "Chicago"],

}

df = pd.DataFrame(data)

print(df)
