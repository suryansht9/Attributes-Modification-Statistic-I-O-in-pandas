# This code creates a DataFrame using pandas and displays all its attributes.
# It includes columns for Name, Age, City, and Mobile Number.
import pandas as pd
data={'Name':['Alice','Bob','Charlie','David','Eva','Frank',"Grace"],
       'Age':[25,30,35,40,45,50,55],        
       'City':['New York','Los Angeles','Chicago',"Houston","Phoenix","Philadelphia","San Antonio"],
        "Mob_No.":[1234567890,9876543210,1122334455,2233445566,3344556677,4455667788,5566778899]}
df=pd.DataFrame(data)
# Display all attributes of the DataFrame
print(df)



# Displaying the DataFrame attributes
print(df.shape,"this is the shape of the DataFrame")
print(df.dtypes,"this is the data types of the DataFrame")    
print(df.columns,"these are the columns of the DataFrame")
print(df.index,"this is the index of the DataFrame")
print(df.T,"this is the transpose of the DataFrame")
print(df.empty,"this checks if the DataFrame is empty")
print(df.size,"this is the size of the DataFrame")
print(df.values,"this is the values of the DataFrame")
