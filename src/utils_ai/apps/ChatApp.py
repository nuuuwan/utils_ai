import os

from utils_base import Console, File, Log

from utils_ai.providers import ProviderFactory

log = Log('ChatApp')


class ChatApp:
    @staticmethod
    def run(provider_name: str, profile_path: str):
        ai = ProviderFactory.from_name(provider_name)
        print('')
        print(Console.note(f'[{ai.NAME}/{ai.MODEL}]'))
        print('')

        if os.path.exists(profile_path):
            profile_content = File(profile_path).read()
            ai.set_profile(profile_content)
            print(Console.note(f'{profile_path}'))
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
                if image_path:
                    print(Console.note(image_path))
                    print('')
                    os.startfile(image_path)
                continue

            reply = ai.chat(message)
            if reply:
                print(Console.note(reply))
                print('')
