import numpy as np

def check_signal(close):
    if len(close) < 30:
        return None
    src = np.array(close)
    length = 30
    mult = 1.786

    mid = np.convolve(src, np.ones(length)/length, 'valid')
    dev = mult * np.std(src[-length:])
    upper = mid[-1] + dev
    lower = mid[-1] - dev

    price = src[-1]

    if price >= upper:
        return 'SELL (chạm band trên)'
    elif price <= lower:
        return 'BUY (chạm band dưới)'
    return None
