# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Function with one input
# def greet(name):
#   print(f"Hi {name}")
#   print(f"Nice to meet you {name}")

# name = input("Hi, Whats your name ?")
# greet(name)

#Function with two input
def greet_with(name, life):
  print(f"My name is {name}")
  print(f"I life in {life}")


name = input("Hi, Whats your name ?")
life = input("Where do you life ?")

# greet_with("Krian", "Ekky")

#Nilainya akan urut based on apa yang di sebut duluan diparameter pada function asli. contoh di sini inputan yang pertama adalah name kemudian life. tapi hasilnya akan terbalik. krn, di funtion asli urutan name, life. tapi saat dipanggil life, name. jadi akhirnya life= name, name = life. jadi akan di isi sesuai posisinya. 

#Jadi, saat memanggil parameternya jangan di bolak balik. Sesuaikan functionya.

#Kalau mau di bolak balik bisa seperti contoh di bawah

greet_with(life, name) 

# Nilai nya akan tetap sesuai parameter walaupun dibolak-balik
# greet_with(life =  "Krian", name = "Ekky")