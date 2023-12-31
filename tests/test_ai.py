import os
import unittest

from utils_base import Console, String

from utils_ai import AI


class TestAI(unittest.TestCase):
    @unittest.skip("needs API")
    def test_chat(self):
        ai = AI()
        print('')
        for message in [
            "I'm from Sri Lanka",
            "What is the Capital of my country?",
            "How do you get from the capital to Galle?",
        ]:
            print(Console.normal("User: " + message))
            reply = ai.ask(message)
            print(Console.note("AI: " + reply))

    @unittest.skip("needs API")
    def test_draw(self):
        ai = AI()
        for description in [
            'Painting of a romantic dinner with jazz',
            'Pop art of a beautiful scene from Sri Lanka',
            'Winning scenes from the final of the 2023 Cricket World Cup',
        ]:
            image_file = os.path.join(
                'tests', '_output', String(description).kebab + '.png'
            )
            ai.draw(description, image_file)

    @unittest.skip("needs API")
    def test_run(self):
        ai = AI()
        description = '''
            Generate a folder named lk_flowers.
            This folder represents a python repository, for data about
            flowers of Sri Lanka.
            Create an appropriate README.md file.
            Create a LICENSE file.
            Create three sub-folders: src, tests, and workflows.
        '''
        python_code_path = os.path.join('tests', '_output', 'test_run.py')
        ai.run(description, python_code_path)


if __name__ == '__main__':
    unittest.main()
