# discount bin
def discount_bin(d):
    if d == 0:
        return "None"
    elif d <= 0.20:
        return "Low"
    elif d<= 0.40:
        return "Medium"
    else:
        return "High" 
