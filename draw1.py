def draw_line():
    print ("#" + "=" * 16 + "#")

def draw_top_half():
    for line in range(1, 5):
        print ("|" + " " * (-2 * line + 8) + "<>" + "." * (4 * line - 4) + "<>" + " " * (-2 * line + 8) + "|")

def draw_bottom_half():
    for line in range(4, 0, -1):
        print ("|" + " " * (-2 * line + 8) + "<>" + "." * (4 * line - 4) + "<>" + " " * (-2 * line + 8) + "|")

draw_line()
draw_top_half()
draw_bottom_half()
draw_line()