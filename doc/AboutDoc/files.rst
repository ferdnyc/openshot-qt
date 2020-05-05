.. Copyright (c) 2020-2020 OpenShot Studios, LLC
 (http://www.openshotstudios.com).
 This file is part of OpenShot Video Editor (http://www.openshot.org),
 an open-source project dedicated to delivering high quality video editing and animation solutions to the world.

.. OpenShot Video Editor is free software:
 you can redistribute it and/or modify it under the terms of the GNU General Public License as published by  the Free Software Foundation, 
 either version 3 of the License,
 or (at your option) any later version.

.. OpenShot Video Editor is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 See the GNU General Public License for more details.

.. You should have received a copy of the GNU General Public License

.. _Documentation_ref:

About the documentation
=======================

The source files for the manual are all found in the project repository, `(the doc/ directory) <https://github.com/OpenShot/openshot-qt/tree/develop/doc>`_ 

The documentation is written in reStructured Text, or ReST. 
This is a plain text format encoded in UTF-8.
It contains special syntax so formatting can be applied by third-party tools.
The tool used by Openshot is Sphinx to create both the online HTML and the offline manual.

You can suggest improvements or submit small changes for our documentation on our github here: 
https://github.com/OpenShot/openshot-qt/issues/2989

Or in *this* reddit thread. 

.. TODO: Reddit thread to be made, bookmarked?, add hyperlink 

The preferred method for submitting large edits would be via GitHub Pull Request. 
But we can make accommodations for anyone who would like to contribute but is not familiar with version-control systems like Git.

License
-------
We use the GPL-3 license (see above) for documentation, see the header. 
This is for simplicity because it is the same license as the project code. 
And because the documentation gets parsed in other tools before it reaches its final form. 

Github
------
In the issue tracker, subjects that contain explanations that should probably be included in the documentation can me labeled `*docs*. <https://github.com/OpenShot/openshot-qt/labels/docs>`_ 
Questions that are answered often in github or reddit can be tagged *FAQ* / are tagged *question*

.. TODO: Add link reddit + link github

Tutorials how to add changes to github: 
| Github on Pull requests https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork
| Github text howto https://opensource.com/life/16/3/submit-github-pull-request
| Github video howto https://www.youtube.com/watch?v=rgbCcBNZcdQ

It is possible to edit files directly in the Github web interface.
To edit a file via the web interface,
you can just click the pencil icon in its upper-right corner.

When you started editing,
Github would see that you do not have permissions to make changes directly to files here.
So it would set you up with a copy ("fork") under your account,
where you can make changes before submitting them as a Pull Request.

Editing on the web is perfectly workable.
The only downside being that there's no real way to preview your changes.
With a local clone you can use a previewing editor or
(if you have the necessary Sphinx tools installed)
generate updated HTML docs and view them in a web browser.

Sphinx
------
`Spinx <https://en.wikipedia.org/wiki/Sphinx_(documentation_generator)>`_ was created to simply generate documentation from Python sourcecode.
It is written in Python, and also used in other environments. 
It is licensed under the BSD license.
It can also export files for translation.

Generating a local copy of the manual requires only the Python-based Sphinx documentation system and the Sphinx RTD theme.  
They can be installed  using most package managers, or via 

.. code-block:: Linux
  pip3 install sphinx sphinx-rtd-theme

Anyone who would like to contribute and needs help with installing and using Sphinx can ask for support in the issues tracker.

Tutorial video:	https://www.youtube.com/watch?v=ouHVkMo3gwE

ReST Basic Syntax
-----------------
`List of basic syntax <Documentation_RestSyntax.rst>`_  in Openshot documentation.  

- Some explanation here:  https://hyperpolyglot.org/lightweight-markup
- or here: https://wiki.typo3.org/ReST_Syntax
- Video tutorials here:  https://www.youtube.com/results?search_query=restructuredtext+tutorial

Software 
- Notepad++ ReST template:	https://github.com/steenhulthin/reStructuredText_NPP
- Linux: 

File naming and directory structure
-----------------------------------

Files are stored in \docs
File names may not contain spaces.
For mult-word filenames, ReST documentation filenames are separated by an underscore ( _ ).
Images filenames are separated by a dash ( - ). 
Images are named after the file they belong to, and sorted in the doc\\images subdirectory. 

.. NOTE: Or maybe not, see Images

Translations go into their own directory. 

File structure
--------------

Every file starts with 5 hidden segments (See 'template <Template.rst>`_ . )

- Copyright notice
- Openshot description
- Openshot disclaimer
- License notice
- Referral anchor for the title

Followed by the title with double underlining (with == )
Then a short description of what the chapter will be about, and why the reader should care (or skip). 
Subtitles are single underlined ( -- )

Sentences should be written one sentence per line, and *NOT* end on a space.
The markup language then flows them all together into paragraphs when it generates the formatted docs.
You can also break at other logical points, like after a comma in a longer sentence,
or before starting an inline markup command.
It is a guideline, not a rule.
This tends to be a pretty good fit for any sort of written prose, when it is in a markup language like ReST and managed in a version control system.

There are four reasons for this:
- Writing that way, there is no worrying about line length or when to wrap. 
- It encourages shorter, simpler sentences which is a good thing when writing docs. 
- The diffs when changes are submitted also tend to be more readable and focused. 
- Lines are easier to translate and less likely to be changed. 

Comments for why things are documented a certain way can be hidden after a double dot and NOTE: and may contain a link to relevant issue in the tracker for more info. 

Translation
-----------
Translation files are generated and managed by Sphinx.
If the images are not translated, they will default back to the original.
Filenames do not get translated.
There may be translation notes hidden in the documentation, blocked out with \.. TRANSLATION NOTE: 

Files for translation will be hosted at `Launchpad <https://translations.launchpad.net/openshot/2.0/+translations>`_.

When translating numbers referencing a screenshot in non-westen languages, please make sure to update the screenshot too. 
If availeble, images of the translation should be saved in their subdirectory *(to be decided)* 

.. TODO: Add subdirectory

.. TRANSLATION NOTE: After translating tables, make sure that the underlining of table rows stay the same length as the new words. 









\
