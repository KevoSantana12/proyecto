class User:
    def __init__(self, id = None, name = None):
        self.id = id
        self.name = name

    def validate(self):
        if not self.name or len(self.name) == 0:
            raise ValueError("El nombre no puede estar vacio...")
        
