from logging import logProcesses


sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for element in location:
      scoops_sold += element

print(scoops_sold)

# Using nested loops 
# here we're using a temp variable location to get data from sales_data
# we then print the location 
# followed by a nested loop with temp variable element in location
# we use the other variable scoops sold to then add together with sales data using operator +=