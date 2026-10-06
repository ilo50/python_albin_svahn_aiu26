def room_check(nr):
    if not isinstance(nr, (int | float)):
        raise TypeError("wrong type bro")

    nr = int(nr)

    if nr < 0:
        raise ValueError("no negative floors")
    
    s = str(nr) 

    if len(s) != 3:
        print(len(s))
        raise ValueError("Too small floor number, must be 3 numbers")

    if not 0 <= int(s[0]) <= 4:
        raise ValueError("unvalid floor")

    print(f"your are on floor {s[0]}")

