"""
This module hosts the Clipboard class for common clipboard functions
"""


import pyperclip

class Clipboard:
    """An instance of a clipboard with access to common clipboard actions

    Properties:
        quote_styles (dict) - style quote option to surround the text

    Arguments:
        retain_newlines (bool) - indicates whether newlines should be
            preserved, defaults to False
        quote_style (str) - indicates the style of quotes to use, single or
            double options, defaults to single
    """

    quote_styles = {'single': "'", 'double': '"'}


    def __init__(self, retain_newlines=False, quote_style='single'):
        # Defaults to single quotes if a quote wtyle isn't provided
        self.quote_style = self.quote_styles.get(quote_style, "'")
        self.retain_newlines = retain_newlines

    @staticmethod
    def get_last_entry():
        """Returns the last clipboard entry, replacing double newlines"""
        last_entry = pyperclip.paste()
        return last_entry

    @staticmethod
    def add_entry(text):
        """Appends a text entry to the clipboard"""
        pyperclip.copy(text)

    def add_text_quotes(self, text):
        """Replaces newlines with single quotes for suppled text

        Args:
            text (str) - a field of text to receive quotes around newlines

        Returns:
            A quoted whitespace stripped string wtih multiple newlines truncated
        """

        endquote = self.quote_style if not self.retain_newlines else f"{self.quote_style}\n"
        quoted_text = ", ".join(
            self.quote_style + row.strip() + endquote
            for row in text.split("\n")
            if row.strip() != '')

        # Puts commas on the correct line if newlines are retained
        return quoted_text.replace('\n, ', ',\n')
