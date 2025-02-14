def main():
    try:
        file1 = open("test.txt", "w")
        file1.write("Hello!")
    finally:
        file1.close()