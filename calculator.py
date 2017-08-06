import stack
from math import pow, sqrt, fabs

buff = stack.Stack()


def get_third():
    return buff.third()

def get_second():
    return buff.second()

def get_first():
    return buff.peek()

def proc_number(n):

    buff.push_on_stack(n)
    return buff.peek()


def on_plus():

    reg_x = buff.peek()
    buff.pop_off_stack()
    reg_z = buff.peek()
    buff.pop_off_stack()
    buff.push_on_stack(reg_x+reg_z)
    return buff.peek()

def on_minus():

    reg_x = buff.peek()
    buff.pop_off_stack()
    reg_z = buff.peek()
    buff.pop_off_stack()
    buff.push_on_stack(reg_z-reg_x)
    return buff.peek()

def on_multiply():

    reg_x = buff.peek()
    buff.pop_off_stack()
    reg_z = buff.peek()
    buff.pop_off_stack()
    buff.push_on_stack(reg_z*reg_x)
    return buff.peek()

def on_divide():

    reg_x = buff.peek()
    buff.pop_off_stack()
    reg_z = buff.peek()
    buff.pop_off_stack()
    buff.push_on_stack(reg_z/reg_x)
    return buff.peek()

def on_pow():

    reg_x = buff.peek()
    buff.pop_off_stack()
    reg_z = buff.peek()
    buff.pop_off_stack()
    buff.push_on_stack(pow(reg_z, reg_x))
    return buff.peek()

def on_sqrt():

    reg_x = buff.peek()
    buff.pop_off_stack()
    buff.push_on_stack(sqrt(reg_x))
    return buff.peek()

def is_float(f):
    try:
        float(f)
        return True
    except ValueError:
        return False

def on_ac():
        buff.clear()

def on_pop():
    buff.pop_off_stack()

def change_sign():
    reg_x = buff.peek()
    buff.pop_off_stack()
    if reg_x == 0:
        buff.push_on_stack(reg_x)
        return buff.peek()
    elif reg_x > 0:
        reg_x -= 2*reg_x
        buff.push_on_stack(reg_x)
        return buff.peek()
    else:
        buff.push_on_stack(fabs(reg_x))
        return buff.peek()