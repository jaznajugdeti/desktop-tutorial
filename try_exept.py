
try:
    def add_everything_up(a,b):
        sum_ = a +b
        print(sum_)

except TypeError:
    print(a, b, sep='')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
