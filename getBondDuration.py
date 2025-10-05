def getBondPrice(y, face, couponRate, m, ppy=1):

    y_per = y / ppy                 # yield per period
    n = int(m * ppy)                # total number of periods
    c = face * couponRate / ppy     # coupon payment per period

    bondPrice = 0.0
    for t in range(1, n + 1):
        # last period includes coupon + face
        cf = c if t < n else c + face
        df = (1 + y_per) ** (-t)    # discount factor
        bondPrice += cf * df

    return bondPrice
