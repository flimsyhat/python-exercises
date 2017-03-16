def draw_grid(x, y, width):
    cross_bar = '+' + ' -' * width + ' '
    vert_bar = '|' + ' ' * (2 * width + 1)
    for i in range(y):
        print cross_bar * x + '+'
        for i in range(width):
            print vert_bar * x + '|'
    print cross_bar * x + '+' 
