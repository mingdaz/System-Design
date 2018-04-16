def getShortURL(id, base):
    res = []
    while id > 0:
        digit = id % base
        res.append(digitMap(digit))
        id /= base
    while len(res) < 6:
        res.append(digitMap(0))
    return ''.join(reversed(res))

def digitMap(digit):
    if digit <= 9:
        # 0-9
        return chr(48+chr)   
    elif digit <= 35:
        # A-Z
        return chr(65+digit)
    else:
        # a-z
        return chr(97+digit)