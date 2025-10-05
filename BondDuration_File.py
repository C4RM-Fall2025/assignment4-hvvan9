def getBondDuration(y, face, couponRate, m, ppy=1):
    y_per = y / ppy
    n = int(m * ppy)
    c = face * couponRate / ppy

    price = 0.0
    weighted_pv_sum = 0.0

    for t in range(1, n + 1):
        cf = c if t < n else c + face
        df = (1 + y_per) ** (-t)
        pvcf = cf * df
        price += pvcf
        weighted_pv_sum += t * pvcf

    return (weighted_pv_sum / price) / ppy
