#tutorial 6
class _myPrivateClass:
    def __init__(self, name):
        self.name = name
class notPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _myPrivateClass(name)
    def _display(self):
        print('hello')
    def display(self):
        print('hi')