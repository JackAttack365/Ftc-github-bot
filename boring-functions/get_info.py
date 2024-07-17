def get_info(number_in_array:int):
    #this is the file that containes all passwords and other settings
    Master_file = open("setup\Importentfile.txt")

    #and this puts it so that i can read it as an list
    Master_file_content = Master_file.readlines()

    loacl_var:str = Master_file_content[number_in_array]
    loacl_var:str = str(loacl_var.strip('\n'))
    return loacl_var