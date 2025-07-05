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

print(df.head(),"this is the first 5 rows of the DataFrame")
print(df.tail(),"this is the last 5 rows of the DataFrame")
print(df.info(),"this is the info of the DataFrame")
print(df.describe(),"this is the description of the DataFrame")
print(df.memory_usage(),"this is the memory usage of the DataFrame")
#print(df['Name'].is_unique(), "this checks if the DataFrame is unique")