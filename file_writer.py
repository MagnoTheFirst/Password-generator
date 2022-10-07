import json

def create_pwd_file(filename, content):
    file = open(filename, "w+")
    file.write(content)
    file.close()

def create_new_pwd(filename, content):
    file = open(filename, "a+")
    file.write(content)
    file.close()

def create_new_entry(filename, username, email, pwd, comment, url, notes):
    #x = "\n" + "{" + "\n \t\t"  + username + ",\n \t\t" + ",\n \t\t" + email + ",\n \t\t"+ pwd + ",\n \t\t" + comment + ",\n \t\t" + url + ",\n \t\t" + ",\n \t\t" + notes + "\n"+"}" + "\n"

    content = {
        "username" : username,
        "email" : email,
        "pwd" : pwd,
        "comment" : comment,
        "url" : url,
        "note" : notes
    }

    json_content = json.dumps(content)
    print(json_content)
    file = open(filename, "a+")
    file.write("\n\n")
    file.write(json_content)
    file.close()