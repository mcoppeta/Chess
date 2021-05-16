def scale_tuple(scale, t: tuple):
    ret = []
    for i in t:
        ret.append(scale * i)
    return tuple(ret)


def toggle(var: int):
    if var == 0:
        return 1
    return 0


def snap_topleft(frame_size: tuple, frame_pos: tuple, element_size: tuple):
    e_w, e_h = element_size
    f_w, f_h = frame_size
    x, y = frame_pos

    topleft = (x + int((f_w - e_w) / 2), y + int((f_h - e_h) / 2))
    return topleft

# if __name__ == "__main__":
