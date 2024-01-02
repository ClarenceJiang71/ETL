"""
Define the tool to deal with string values 
"""
def check_null(data):
    """
    check if the string data is meaningful or not
    there are several situations where we think the data itself 
    does not have meaning, like it is none, empty string, etc. 
    """

    if not data: 
        return True 
    
    data = data.lower()
    data = data.strip()
    if data == "none" or data == "" or data == "undefined" or data == "null":
        return True 
    
    return False 

def check_str_null_and_transform_to_sql_null(data):
    """
    This method will convert the actual data that is meaningless 
    into the null form where it will get accept as a SQL query to run
    """
    if check_null(str(data)):
        return "NULL"
    
    else:
        return f"'{data}'"
    
def check_number_null_and_transform_to_sql_null(data):
    if data and not check_null(str(data)):
        return data 
    
    return "NULL"
    
def clean_str(data: str):
    """
    remove some weird characters involved in the data
    """
    if check_null(data):
        return data

    data = data.replace("'", "")
    data = data.replace("\"", "")
    data = data.replace(";", "")
    data = data.replace(",", "")
    data = data.replace("@", "")
    data = data.replace("\\", "")  # 把字符串中的反斜杠去除 => abc\bcd > abcbcd

    return data


