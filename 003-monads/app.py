class Just:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    def __repr__(self):
        return f"Just({self.value})"
        
class Nothing:
    def __init__(self):
        pass

    def __repr__(self):
        return "Nothing()"
    
def add(*args):
    if any([isinstance(arg, Nothing) for arg in args]):
        return Nothing()
    
    try:
        summed_total = sum([arg.value for arg in args])
        return Just(summed_total)
    except AttributeError:
        return Nothing()

def product(*args):
    if any([isinstance(arg, Nothing) for arg in args]):
        return Nothing()
    
    try:
        product = 1
        for arg in args:
            product = product*arg.value
        return Just(product)
    except AttributeError:
        return Nothing()

def add(*args):
    if any([isinstance(arg, Nothing) for arg in args]):
        return Nothing()
    
    try:
        summed_total = sum([arg.value for arg in args])
        return Just(summed_total)
    except AttributeError:
        return Nothing()
    

def main():
    
    a = Just(10)
    b = Just(2)
    
    c = product(a, b)
    print(c)
    
    
if __name__ == "__main__":
    main()
    