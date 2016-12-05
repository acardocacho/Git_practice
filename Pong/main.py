def anas_function(x):
    if x==0:
        print('im even')
    elif x==1:
        print('im odd')
    else:
        return anas_function(x-2)
