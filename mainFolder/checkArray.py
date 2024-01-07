def check_array(ar):
    for x in ar:
        counter = 0
        for g in ar:
            if g == x:
                counter +=1
        if counter > 1:
            return True
    return False