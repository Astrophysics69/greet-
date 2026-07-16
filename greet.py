"""
A simple greeting package
"""

def greet():
    return "Hello! Welcome to SayHi Greet!"

def hello(name="User"):
    return f"Hello, {name}!"

def goodbye(name="User"):
    return f"Goodbye, {name}! See you soon!"

def greet_formal():
    return "Greetings and salutations!"

__version__ = "0.3.0"
