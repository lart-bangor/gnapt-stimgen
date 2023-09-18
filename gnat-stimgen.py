"""Shorthand for the gnat-stimgen module for compilation with nuitka.

Compile with nuitka using:
>>> py -m nuitka --onefile --include-package=gnat_stimgen.datasets --windows-icon-from-ico=gnat-stimgen-icon.png gnat-stimgen.py
"""
from gnat_stimgen.__main__ import main

main()
