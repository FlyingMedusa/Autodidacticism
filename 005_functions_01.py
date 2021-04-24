
def in_line(name):
    in_line.count += 1
    print('Greetings', name, '- you are:', in_line.count ,'in line.')
    

in_line.count = 0

reservation = in_line

in_line('Thorin')
reservation('Dwalin')
in_line('Kili')