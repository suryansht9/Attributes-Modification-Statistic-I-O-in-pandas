import pandas as pd
data={'Name':['Alice','Bob','Charlie','David','Eva','Frank',"Grace"],
       'Age':[25,30,35,40,45,50,55],        
       'City':['New York','Los Angeles','Chicago',"Houston","Phoenix","Philadelphia","San Antonio"],
        "Mob_No.":[1234567890,9876543210,1122334455,2233445566,3344556677,4455667788,5566778899],
        "Marks_in_college":[85,90,78,88,92,95,80]}
df=pd.DataFrame(data)
# Display all attributes of the DataFrame
print(df)

# Displaying the DataFrame modifications
print(df.assign(Total_marks=[100, 100, 100, 100, 100, 100, 100]), "this adds a new column Total_marks with all values as 100")
print(df.insert(2, "Country", ["USA", "USA", "USA", "USA", "USA", "USA", "USA"]), "this inserts a new column Country at index 2 with all values as USA")
print(df) 
print(df.drop(columns=["Total_marks"]), "this drops the Marks_in_college column")
print(df.rename(columns={"Marks_in_college": "College_Marks"}), "this renames the Marks_in_college column to College_Marks")
