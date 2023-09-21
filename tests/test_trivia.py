import hashlib
import subprocess


class TestTrivia:
    def test(self):
        output = subprocess.getoutput("python trivia.py 0")

        assert output == read_reference()


def read_reference():
    with open("reference.txt") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)
