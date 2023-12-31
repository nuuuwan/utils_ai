from utils_base import File, Log

log = Log('AIExecute')


class AIExecute:
    def run(self, description: str, python_code_path: str):
        message = '\n'.join(
            [
                'Generate some python code that does the following'
                + ' (DO NOT include an introduction or concluding text.'
                + ' INCLUDE ONLY the python code. OUTPUT raw python code.'
                + ' DO NOT OUTPUT markdown.):',
                description,
            ]
        )
        python_code = self.ask(message)
        File(python_code_path).write(python_code)
