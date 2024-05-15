import sys

from utils_ai import ChatApp

if __name__ == '__main__':
    provider_name = sys.argv[1]
    profile_path = sys.argv[2]
    ChatApp.run(provider_name, profile_path)
