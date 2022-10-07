import pwdGenerator
import file_writer

pwdGenerator.passwordGenerator(20)
pwdGenerator.passwordGenerator(30)

file_writer.create_pwd_file("test.txt", "--------------------- Passwords ---------------------")

file_writer.create_new_entry("test.txt", "magno", "magno.maximo@test.ch", pwdGenerator.passwordGenerator(20), "test", "", "")
file_writer.create_new_entry("test.txt", "tester", "tester.testing@test.ch", pwdGenerator.passwordGenerator(20), "hi", "", "")