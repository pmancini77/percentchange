
"""looked up a formula to figure out how much id make if a stock increased by 5% everyear, decided to build my own function
with the capability of shrinking as well"""
def percent_less(start, period, change_percent, i=1, end=None):
    if end is None:
        end = start * change_percent
    else:
        end *= change_percent
    while i < period:
        i += 1
        return percent_less(end, period, change_percent, i, end)
    return end
print('input 1 to calculate growth; or two to calculate shrinkage:')
g_or_s = int(input())
print('please enter your start, how many periods youre going for and the percentage you are changing')

principal = int(input())
time = int(input())
digit = int(input())
if g_or_s == 1:
    percent = 1 + digit/100
elif g_or_s == 2:
    percent = 1 - (digit/100)
else:
    print('not recognized')

print(percent_less(principal, time, percent))
