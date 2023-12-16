import pandas as pd
import matplotlib.pyplot as plt

#Load the mtcars dataset
mtcars = pd.read_csv("C:\Users\dharu\Downloads")

#Display the first few rows of the dataset
print("First few rows of the mtcars dataset:")
print(mtcars.head())

#Data processing : Example tasks
#1. Filtering: Keep only cars with more than 20 miles per gallon(mpg)
filtered_cars = mtcars[mtcars['mpg']>20]

#2. Grouping : Calculate the average horsepower(hp) by the number of the cylinders(cyl)
avg_hp_by_cyl = mtcars.groupby('cyl')['hp'].mean().reset_index()

#3. Sorting : Sort the dataset by miles per gallon(mpg) in descending order
sorted_mtcars = mtcars.sort_values(by='mpg',ascending=False)

#Display the processed data
print("\nProcessed data(Filtered Cars):")
print(filtered_cars)
print("\nProcessed Data(Average HorsePower by cylinder):")
print(avg_hp_by_cyl)
print("\nProcessed Data(Sorted by MPG):")
print(sorted_mtcars)

#Data Visualisation: Plotting examples
#1. Bar chart for average horsepower by cylinder
plt.figure(figsize=(8,6))
plt.bar(avg_hp_by_cyl['cyl'],avg_hp_by_cyl['hp'],color='blue')
plt.xlabel('Number of cylinders')
plt.ylabel('Average HorsePower')
plt.title('Average HorsePower by Number Of Cylinders')
plt.show()

#2. Scatter Plot for miles per gallon(mpg) vs horsepower(hp)

plt.figure(figsize=(8,6))
plt.scatter(mtcars['hp'],mtcars['mpg'],color='corol')
plt.xlabel('HorsePower')
plt.ylabel('Miles per Gallon')
plt.title('Scatter plot : Miles per Gallon vs HorsePower')
plt.show()
