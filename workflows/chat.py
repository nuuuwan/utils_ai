import os
import sys

from utils_base import Console

from utils_ai import ProviderFactory


def main(provider_name: str):
    ai = ProviderFactory.from_name(provider_name)
    print('')
    print(Console.note(f'[{ai.NAME}/{ai.MODEL}]'))
    print('')
    while True:
        message = input('>> ')
        print('')
        if message in ['quit', 'exit', 'q', 'x', 'exit()', 'quit()']:
            print(Console.note('Bye!'))
            print()
            break

        if message.lower().startswith('draw:'):
            image_path = ai.draw(message)
            print(Console.note(image_path))
            print('')
            os.startfile(image_path)
            continue

        reply = ai.chat(message)
        print(Console.note(reply))
        print('')


if __name__ == '__main__':
    provider_name = sys.argv[1]
    main(provider_name)
