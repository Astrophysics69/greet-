"""
A simple greeting package
"""

def greet():
    """Return a simple greeting"""
    return "Hello! Welcome to sayhi1-greet!"

def hello(name="User"):
    """Greet someone by name"""
    return f"Hello, {name}!"

def goodbye(name="User"):
    """Say goodbye to someone"""
    return f"Goodbye, {name}! See you soon!"

def greet_formal():
    """Return a formal greeting"""
    return "Greetings and salutations!"

__version__ = "0.2.0"
__all__ = ["greet", "hello", "goodbye", "greet_formal"]
