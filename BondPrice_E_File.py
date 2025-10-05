def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    m = len(yc)  # number of years from yield curve
    bondPrice = 0.0

    for t, r in enumerate(yc, start=1):
        cf = coupon if t < m else coupon + face
        df = (1 + r) ** (-t)
        bondPrice += cf * df

    return bondPrice
