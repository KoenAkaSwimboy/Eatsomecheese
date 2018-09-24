def convert(celcius):
         return celcius * 1.8 + 32;

def table():
    print('{:6}{:3}'.format('F', 'C'))
    for i in range (-30, 50, 10):
        print('{:5}{:8}'.format(convert(i), float(i)))


print(table())