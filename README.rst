gnat-stimgen - Stimulus Generator for the GNAT 🎭
=================================================

Stimulus generator for the Go-No Go Association Task used for L'ART's 2023/2024
experiments.


Installation
------------

Just download the :code:`gnat-stimgen.exe` from the GitHub repo's releases and
place it wherever is convenient, then run it from the command line as shown
below. No installation necessary.


Usage
-----

:code:`gnat-stimgen.exe [OPTIONS] [LANGUAGE_PAIR]`

Arguments:
^^^^^^^^^^

:LANGUAGE_PAIR: 
   The optional argument LANGUAGE_PAIR can be one of EngCym, GerLtz, or ItaLmo
   (default: EngCym). Specifies the dataset for which experimental blocks should
   be generated.

Options:
^^^^^^^^

:--help: 
   Show a help message and exit.


License
-------

This software is free and open source, available under the Apache License,
Version 2.0. See the :code:`LICENSE` file for more information.

Contributing
------------

If you are using the gnat-stimgen to generate experimental blocks for a new
language pair (e.g. an adaptation, extension or replication of one of our
studies), you're more than welcome to make a pull request for the new language
pair file. However, if the logic of the block generation is altered (i.e.
your experimental design is different in some way) then it's best to make a
fork. It would still be great to give us a ping so we can link to your fork.
