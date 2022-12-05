def time_to_integer(time):
    if time == '':
        num = None
    else:
        num = int(time.replace(':',''))
    return(num)

def string_to_float(string):
    if string == '':
        string = None
    else:
        string = float(string)
    return(string)

def string_to_int(string):
    if string == '':
        string = None
    elif string == 'None':
        string = None
    else:
        string = int(string)
    return(string)

def int_to_time(i):
    if i == None:
        time = None
        return(time)
    else:
        string = str(i)
        if len(string) == 3:
            time = (f"{string[0]}:{string[1]}{string[2]}")
        else:
            time = (f"{string[0]}{string[1]}:{string[2]}{string[3]}")
        return(time)
def check_null(value):
    if value == '' or value == 'None':
        value = None
        return value
    else:
        return value