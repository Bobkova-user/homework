data= {}
with open('C:/Users/mashb/Downloads/Виктория.txt', 'r', encoding= "utf-8") as file:
   for i , line in enumerate(file):
       data[i + 1]= list(line.strip().split(";"))

       print(data[1])