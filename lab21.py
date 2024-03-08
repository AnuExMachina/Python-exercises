string = 'abcdef'

'{:>10}'.format(string)

'{:_<10}'.format(string)

'{:^10}'.format(string)

'{first} {last}'.format(first='Michalina', last='Czechowska')

from datetime import datetime
'{:%Y-%m-%d %H:%M}'.format(datetime(2024, 8, 3, 4, 5))
