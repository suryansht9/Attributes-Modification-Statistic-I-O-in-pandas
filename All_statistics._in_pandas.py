# This code creates a DataFrame using pandas and displays all its attributes.
# It includes columns for Name, Age, City, and Mobile Number.
'''import pandas as pd
data={'Name':['Alice','Bob','Charlie','David','Eva','Frank',"Grace"],
       'Age':[25,30,35,40,45,50,55],        
       'City':['New York','Los Angeles','Chicago',"Houston","Phoenix","Philadelphia","San Antonio"],
        "Mob_No.":[1234567890,9876543210,1122334455,2233445566,3344556677,4455667788,5566778899],
        "Marks_in_college":[85,90,78,88,92,95,80]}
df=pd.DataFrame(data)
# Display all attributes of the DataFrame
print(df)

# Displaying the DataFrame statistics
print(df.min(),"this is the minimum value of each column")
print(df.max(),"this is the maximum value of each column")
print(df["Marks_in_college"].mean(),"this is the mean value of each column")
print(df.count(),"this is the count of each column")
print(df["Marks_in_college"].sum(),"this is the summo of marks in college")
print(df.isnull(),"this checks if the DataFrame has any null values")
print(df.isnull().sum(),"this checks if the DataFrame has any null values and returns the count of null values in each column")
print(df["Marks_in_college"].median(),"this is the median value of each column")'''


#now i am going to create one more datframe with null values and then i will check the null values in the dataframe
import pandas as pd
data_with_nulls = {
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva', 'Frank', 'Grace'],
    'Age': [25, 30, None, 40, 45, 50, 55],
    'City': ['New York', None, 'Chicago', 'Houston', 'Phoenix', None, 'San Antonio'],
    "Mob_No.": [1234567890, 9876543210, 1122334455, None, 3344556677, 4455667788, 5566778899],
    "Marks_in_college": [85, None, 78, 88, 92, None, 80]
}
ok=pd.DataFrame(data_with_nulls)
print(ok)

#first of all i will check the null values in the dataframe
print(ok.isnull().count(), "this checks if the DataFrame has any null values and returns the count of null values in each column")
#now i will check the null values in the dataframe and then i will fill the null values with 0
print(ok.isnull().sum(), "this checks if the DataFrame has any null values and returns the count of null values in each column")
#now i will fill the null values with 0
ok.fillna(0, inplace=True)
print(ok, "this fills the null values with 0")
print(ok.fillna(method=("ffill")), "this fills the null values with the previous value in the column")
print(ok.fillna(method=("bfill")), "this fills the null values with the next value in the column")
print(ok.drop_duplicates(), "this drops the duplicate values in the DataFrame")
print(ok.dropna(), "this drops the rows with null values in the DataFrame")