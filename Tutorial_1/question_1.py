def std(list, list_len, mean):
    std = 0
    for item in list:
        std += (item - mean) ** 2
    std = ((1/(list_len-1))* std) ** 0.5
    return std


def list_stats(list):
    sum = 0
    for item in list:
        sum += item
    return sum

def pth_percent(list, length, p):
    pth_percentile = 0
    pth_pos = (p/100) * (length+1)
    if (pth_pos) % 1 != 0:
        pth_percentile = (list[int(pth_pos-0.5)] + list[int(pth_pos+0.5)])/2
    else:
        pth_percentile = list[int(pth_pos)]
    return pth_percentile

data_sample = [2099,528,2030,1350,1018,384,1499,1265,375,424,789,810,522,513,488,200,215,486,257,557,260,461,500]
data_len = len(data_sample)
data_sample.sort()
list_len = len(data_sample)
mean = list_stats(data_sample)/list_len
iqr = pth_percent(data_sample, list_len, 75)-pth_percent(data_sample, list_len, 25)

print(f'{pth_percent(data_sample, list_len, 75)}')
