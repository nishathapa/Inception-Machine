try:
    # p=5/0
    p = 78
    j= 98

    r=p/0

    f = open("ac.txt")

    for line in f:
        print(line)

except FileNotFoundError as e:
    print(e.filename)
except Exception as e:
    print(e)
except ZeroDivisionError as e:
    print(e)



# except FileNotFoundError:
#     print("printed error")
# except ZeroDivisionError:
#     print("Divided by zero")
#
# # i = 0/0
 
    
# we added here just for fun
