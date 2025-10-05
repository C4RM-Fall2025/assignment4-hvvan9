def getBondPrice(y, face, couponRate, m, ppy=1):
    y_per = y / ppy
    n = int(m * ppy)
    c = face * couponRate / ppy

    bondPrice = 0.0
    for t in range(1, n + 1):
        cf = c if t < n else c + face
        df = (1 + y_per) ** (-t)
        bondPrice += cf * df

    return bondPrice
