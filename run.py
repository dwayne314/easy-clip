"""
This module hosts the application entrypoint

To Do:
    Implement a command line interface that allows custom formatting
"""


from clipboard import Clipboard


def run():
    """Executes the script"""
    clipboard = Clipboard()
    last_entry = clipboard.get_last_entry()
    formatted = clipboard.add_text_quotes(last_entry)
    clipboard.add_entry(formatted)

run()
