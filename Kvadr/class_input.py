class Input():
    def __init__(self):
        self.input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
        with open(self.input_path, 'r') as f:
            self.input = f.read()