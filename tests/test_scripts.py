import io
import os
import sys
from unittest import TestCase

from boombash import loader


class TestStandardScripts(TestCase):
    def get_output(self, script):
        saved_stdout = sys.stdout
        output = None
        try:
            out = io.StringIO()
            sys.stdout = out
            loader.load(script)
            output = out.getvalue()
        finally:
            sys.stdout = saved_stdout
        return output

    def test_hello_world(self):
        script_location = "tests/scripts/hello.bm"
        output = self.get_output(script_location)
        self.assertEqual(output, "Hello World\n")

    def test_if_yes(self):
        script_location = "tests/scripts/if_yes.bm"
        output = self.get_output(script_location)
        self.assertEqual(output, "Yes\n")

    def test_if_no(self):
        script_location = "tests/scripts/if_no.bm"
        output = self.get_output(script_location)
        self.assertEqual(output, "No\n")

    def test_greet(self):
        script_location = "tests/scripts/greet.bm"
        output = self.get_output(script_location)
        self.assertEqual(output, "Pratham\n")

    def test_fibonacci(self):
        script_location = 'tests/scripts/fibonacci.bm'
        output = self.get_output(script_location)
        self.assertEqual(output, 'No\n')
    def test_variables(self):
        script_location = 'tests/scripts/variable.bm'
        output = self.get_output(script_location)
        self.assertEqual(output, 'No\n')

    def test_while(self):
        script_location = 'tests/scripts/while.bm'
        output = self.get_output(script_location)
        self.assertEqual(output, 'Hello\nHello\n')

    def test_list(self):
        script_location = 'tests/scripts/list.bm'
        output = self.get_output(script_location)
        self.assertEqual(output , '[1 2 3]\n')
        
    def test_list_get(self):
        script_location = 'tests/scripts/list-get.bm'
        output = self.get_output(script_location)
        self.assertEqual(output , '2\n')

    def test_list_add(self):
        script_location = 'tests/scripts/list-add.bm'
        output = self.get_output(script_location)
        self.assertEqual(output , '5\n')

    def test_list_len(self):
        script_location = 'tests/scripts/list-len.bm'
        output = self.get_output(script_location)
        self.assertEqual(output , '3\n8\n5\n8\n')
