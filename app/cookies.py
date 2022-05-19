import os
def cookieHelper():
    try:
        cookies = {}     
          
        with open('cookies.txt', 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                if(len(line) == 0 or line[0] == '#'):
                    continue
                if len(line.split('\t')) == 7:
                    lst = line.split('\t')[-2:]
                    cookies[lst[0]]  = lst[1]
                else: raise IOError
        return cookies
    except (FileNotFoundError, IOError):
        print('Bug in Cookies file\n\ncheck file again\n\ncheck file name => cookies.txt')

