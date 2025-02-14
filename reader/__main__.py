import tkinter as tk

def main():
    try:
        file1 = open("test.txt", "w")
        file1.write(str(tk.TkVersion))
    finally:
        file1.close()