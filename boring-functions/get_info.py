def get_info(number_in_array:int):
    #this is the file that containes all passwords and other settings
    Master_file = open("setup\Importentfile.txt")

    #and this puts it so that i can read it as an list
    Master_file_content = Master_file.readlines()

    loacl_var:str = Master_file_content[number_in_array]
    loacl_var:str = str(loacl_var.strip("\n"))
    return loacl_var

def get_sheets(number_in_array:int,server_name:str):
    #this is the file that containes all passwords and other settings
    Team_sheets = open(f"team_files\\{server_name}\\{server_name}google_seets.txt")

    #and this puts it so that i can read it as an list
    Team_sheets = Team_sheets.readlines()

    loacl_var:str = Team_sheets[number_in_array]
    loacl_var:str = str(loacl_var.strip("\n"))
    return loacl_var