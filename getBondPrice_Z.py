def getBondPrice_Z(face, couponRate, times, yc):
    if len(times) != len(yc):
        raise ValueError("times and yc must have same length")

    coupon = face * couponRate
    T = max(times)
    bondPrice = 0.0

    for t, r in zip(times, yc):
        cf = coupon if t < T else coupon + face
        df = (1 + r) ** (-t)
        bondPrice += cf * df

    return bondPrice
