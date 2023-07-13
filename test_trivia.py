import subprocess
import unittest


class TestRunCommand(unittest.TestCase):
    def test(self):
        cmd_line = ["python", "-c", "print('hello')"]
        result = run_command(cmd_line)
        self.assertEqual(result, "hello\n")


class TestTrivia(unittest.TestCase):
    def test(self):
        result = run_command(["python", "trivia.py", "0"])

        self.assertEqual(result, read_reference("reference.txt"))


def read_reference(path):
    with open(path) as f:
        return f.read()

def run_command(cmd_line):
    proc = subprocess.Popen(
        cmd_line,
        stdout=subprocess.PIPE,
    )
    stdout, _ = proc.communicate()
    result = stdout.decode('utf-8')
    return result
