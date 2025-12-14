def helloworld():
    """Prints hello world
    Paramaters: none
    Returns: none    
    """
    print("Hello World!")


def helloname(myname):
    """Prints hello and a given name
    Paramaters:
        myname (string): a name
    Returns: none    
    """
    print(f"Hello {myname}")


def sum(x,y):
    """Calculates the sum of two given numbers
    Paramaters:
        x (int): a number
        y (int): a number
    Returns:
        int: sum of x and y    
    """
    return x + y


def average(x,y):
    """Calculates the average of two given numbers
    Paramaters:
        x (int): a number
        y (int): a number
    Returns:
        int: average of x and y    
    """
    return (x + y) / 2


def power(x,y):
    """Calculates the power of one number to the other
    Paramaters:
        x (int): a number
        y (int): a number
    Returns:
        int: x to the power of y    
    """
    return x**y


def evenOrOdd(x):
    """checks if a given number is even or odd
    Paramaters:
        x (int): a number
    Returns:
        bool: true if even and false if odd  
    """
    if x % 2 == 0:
        return True
    else:
        return False