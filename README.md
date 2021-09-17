Version
===
1.0

What is Easy Clip?
===

Easy Clip is a command line tool that lets a user modify clipboard entries.

Why Easy Clip?
===

Anybody who spends a lot of time on the computer uses frequently has to modify large portions of text into a different format. Easy Clip makes that easy simply by using your clipboard. Easy Clip replaces the need to use fancy editors and other tools for simple text modification through its command line interface.

Features
===

Easy Clip will allow a user to accomplish the following through its interface:

* Add quotes to lines of text eliminating newlines
* Add quotes to lines of text retaining newlines
* Use single or double quotes
* Strip empty lines of text

Installation Instructions
===

1) Clone the repository from GitHub
2) Install the package requirements locally or in a virtual environment

Command Options
===

In Progress

Examples
===

### Easy Clip takes text separated on multiple newlines, adds quotes/commas, and places them on the same line

***Copied From clipboard***

AER55561
AER55562
AER55563

***Pasted To clipboard***

'AER55561', 'AER55562', 'AER55563'

### Easy Clip takes text separated on multiple newlines, adds quotes/commas, and places them on new lines

***Copied From clipboard***

AER55561
AER55562
AER55563

***Pasted To clipboard***

'AER55561',
'AER55562',
'AER55563'


Future Additions
---

* Add support for additional formatting options (e.g. pipe separators, optional quotes, table formatting)
* GUI interface
