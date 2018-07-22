import random
import os

angka = random.randint(1,20)
salah = 0

def main():
  global salah
  user = input("masukkan angka: ")
  user = int(user)
  if(user > angka):
    print("angka terlalu besar, kecilkan angka")
    salah +=1
  if(user < angka):
    print ("angka terlalu kecil, besarkan angka")
    salah += 1
  if (user == angka):
    selesai()  
  main()

def selesai():
  os.system("clear")
  print ("angka anda tepat!")
  print ("salah: " + str(salah))
  exit()

main()
