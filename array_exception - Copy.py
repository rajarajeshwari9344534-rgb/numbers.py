"""
Samples for type hints
"""
#Introducing type hints
import typing
def add(x:int, y:int) -> int:
    """
    name: add
    accepts two integers and returns their
    returns: integer
    """

    x = int(x)
    y = int(y)
    return (x + y)
print(add(10, 5))

def greeting(name:str) -> str:
    return f"Hello {name}"
print (greeting("Sachin"))
print(greeting("90"))