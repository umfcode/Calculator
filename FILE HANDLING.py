#open()

#"r" = reading
#'w' = write
#'a' = append
#'x' = create

#f = open("newfile.txt", "x")

#f = open("newfile.txt", 'w')
#f.write("This is python advanced class!")
#f.close()

#z = open("newfile.txt",'r')
#print(z.read())

b = open("newfile.txt", 'a')
b.write("We are learning file handling!\n")
b.close()

z = open("newfile.txt",'r')
print(z.read())