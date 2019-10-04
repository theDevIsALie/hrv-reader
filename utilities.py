import bpy
import sys


def get_rgba(crt_line, crt_line_num, index, op):
    # Red value (r)
    try:
        _r = crt_line[index]
        try:
            int(crt_line[index])
            if int(crt_line[index]) < 0 or int(crt_line[index]) > 255:
                op.report({'ERROR'}, f"Red value should be between 0-255 on line {crt_line_num}")
                r = 255
            else:
                # r value defined correctly
                r = int(crt_line[index])
        except:
            op.report({'ERROR'}, f"Red value should be an int on line {crt_line_num}")
            r = 255
    except:
        op.report({'ERROR'}, f"Missing red value on line {crt_line_num}")
        r = 255

    # Green value (g)
    try:
        _g = crt_line[index + 1]
        try:
            int(crt_line[index + 1])
            if int(crt_line[index + 1]) < 0 or int(crt_line[index + 1]) > 255:
                op.report({'ERROR'}, f"Green value should be between 0-255 on line {crt_line_num}")
                g = 255
            else:
                # g value defined correctly
                g = int(crt_line[index + 1])
        except:
            op.report({'ERROR'}, f"Green value should be an int on line {crt_line_num}")
            g = 255
    except:
        op.report({'ERROR'}, f"Missing green value on line {crt_line_num}")
        g = 255

    # Blue value (b)
    try:
        _b = crt_line[index + 2]
        try:
            int(crt_line[index + 2])
            if int(crt_line[index + 2]) < 0 or int(crt_line[index + 2]) > 255:
                op.report({'ERROR'}, f"Blue value should be between 0-255 on line {crt_line_num}")
                b = 255
            else:
                # b value defined correctly
                b = int(crt_line[index + 2])
        except:
            op.report({'ERROR'}, f"Blue value should be an int on line {crt_line_num}")
            b = 255
    except:
        op.report({'ERROR'}, f"Missing blue value on line {crt_line_num}")
        b = 255

    # Alpha value (a)
    try:
        _a = crt_line[index + 3]
        try:
            int(crt_line[index + 3])
            if int(crt_line[index + 3]) < 0 or int(crt_line[index + 3]) > 255:
                op.report({'ERROR'}, f"Alpha value should be between 0-255 on line {crt_line_num}")
                a = 255
            else:
                # a value defined correctly
                a = int(crt_line[index + 3])
        except:
            op.report({'ERROR'}, f"Alpha value should be an int on line {crt_line_num}")
            a = 255
    except:
        op.report({'ERROR'}, f"Missing alpha value on line {crt_line_num}")
        a = 255

    # Convert all the values into a blender color value (0 -> 1)
    red = r / 255
    green = g / 255
    blue = b / 255
    alpha = a / 255

    return red, green, blue, alpha


def get_xyz(crt_line, crt_line_num, index, op):
    # Positions of the voxel
    # X position (x)
    try:
        _x = crt_line[index]
        try:
            x = float(crt_line[index])
        except:
            op.report({'ERROR'}, f"x should be a float on line {crt_line_num}")
            x = 0
    except:
        op.report({'ERROR'}, f"x value is missing on line {crt_line_num}")
        x = 0

    # Y position (y)
    try:
        _y = crt_line[index + 1]
        try:
            y = float(crt_line[index + 1])
        except:
            op.report({'ERROR'}, f"y value should be a float on line {crt_line_num}")
            y = 0
    except:
        op.report({'ERROR'}, f"y value is missing on line {crt_line_num}")
        y = 0

    # Z position (z)
    try:
        _z = crt_line[index + 2]
        try:
            z = float(crt_line[index + 2])
        except:
            op.report({'ERROR'}, f"z value should be a float on line {crt_line_num}")
            z = 0
    except:
        op.report({'ERROR'}, f"z value is missing on line {crt_line_num}")
        z = 0

    return x, y, z
