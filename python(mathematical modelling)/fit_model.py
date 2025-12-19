#LEAST SQUARES FIT
def fit_model(ns, ts, f):
    num = sum(ts[i] * f(ns[i]) for i in range(len(ns)))
    den = sum(f(ns[i]) ** 2 for i in range(len(ns)))
    a = num / den

    error = sum((ts[i] - a * f(ns[i])) ** 2 for i in range(len(ns)))
    return error
