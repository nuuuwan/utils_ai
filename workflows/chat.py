import sys

from utils_ai import ChatApp

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python chat.py <OpenAI|MistralAI> <ai_profiles/*.txt>")
        sys.exit(1)
    provider_name = sys.argv[1]
    profile_path = sys.argv[2]
    ChatApp.run(provider_name, profile_path)
