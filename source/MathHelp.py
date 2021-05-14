def scale_tuple(scale, t: tuple):
    ret = []
    for i in t:
        ret.append(scale * i)
    return tuple(ret)


def toggle(var: int):
    if var == 0:
        return 1
    return 0

# if __name__ == "__main__":
