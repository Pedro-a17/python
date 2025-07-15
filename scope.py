global_var = "python_global"

def var():
    global global_var
    global_var = "inside"
    local_var = "python_local"
    print(global_var)
    print(local_var)

if __name__ == '__main__':
    var()
    print(global_var)
