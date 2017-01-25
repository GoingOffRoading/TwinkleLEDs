import randomcolor
rand_color = randomcolor.RandomColor()
print(', '.join(map(str,rand_color.generate(format_='rgbArray', hue='green'))))
