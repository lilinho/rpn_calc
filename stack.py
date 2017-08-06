class Stack:

    def __init__(self):
        self.buf = []

    def push_on_stack(self, obj):
        return self.buf.append(obj)

    def pop_off_stack(self):
        return self.buf.pop()

    def clear(self):
        for i in range(0, len(self.buf)):
            self.buf.pop()

    def peek(self):
        return self.buf[len(self.buf)-1]

    def third(self):
        if len(self.buf) > 2:
            return self.buf[len(self.buf)-3]
        else:
            return 0

    def second(self):
        if len(self.buf) > 1:
            return self.buf[len(self.buf)-2]
        else:
            return 0
