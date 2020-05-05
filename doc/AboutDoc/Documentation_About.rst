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
In the issue tracker, subjects that contain explanations that should probably be included in the documentation can be labeled ** `docs. <https://github.com/OpenShot/openshot-qt/labels/docs>`_ **
Questions that are answered often in github or reddit can be tagged *FAQ* / are tagged **question**

.. TODO: Add link reddit + link github

|  Tutorials how to add changes to github: 
|  Github on Pull requests https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork
|  Github text howto https://opensource.com/life/16/3/submit-github-pull-request
|  Github video howto https://www.youtube.com/watch?v=rgbCcBNZcdQ

It is possible to edit files directly in the Github web interface.
To edit a file via the web interface,
you can just click the pencil icon in its upper-right corner.

When you started editing,
Github would see that you do not have permissions to make changes directly to files here.
So it would set you up with a copy ("fork") under your account,
where you can make changes before submitting them as a Pull Request.

Editing on the web is perfectly workable.
The only downside being that there is no real way to preview your changes.
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

.. code-block:: console

  pip3 install sphinx sphinx-rtd-theme

Anyone who would like to contribute and needs help with installing and using Sphinx can ask for support in the issues tracker.

Tutorial video:	https://www.youtube.com/watch?v=ouHVkMo3gwE

ReST Basic Syntax
-----------------
`List of basic syntax </Documentation_RestSyntax.rst>`_  in Openshot documentation.  

- Some explanation here:  https://hyperpolyglot.org/lightweight-markup
- or here: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
- Video tutorials here:  https://www.youtube.com/results?search_query=restructuredtext+tutorial

Software 

- Notepad++ ReST template:	https://github.com/steenhulthin/reStructuredText_NPP
- Linux: 

File naming and directory structure
-----------------------------------

| Files are stored in \docs
| File names may not contain spaces. Spaces in filenames cause problems with Sphinx. 
| For multi-word filenames, ReST documentation filenames are separated by an underscore ( _ ).
| Image filenames are separated by a dash ( - ). 
| Images are named after the file they belong to, and sorted in the doc\\images subdirectory. 

.. NOTE: Or maybe not, see Images

Translations go into their own directory. 

File structure
--------------

Every file starts with 5 hidden segments (See `template <Template.rst>`_ )

- Copyright notice
- Openshot description
- Openshot disclaimer
- License notice
- Referral anchor for the title

Followed by the title with double underlining (with == )
Then a short description of what the chapter will be about, and why the reader should care (or skip). 
Subtitles are single underlined ( -- )

Sentences should be written one sentence per line, and do not need to end on a space.
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

Comments for why things are documented a certain way can be hidden after a double dot and start with "NOTE: ". 
They may contain a link to a relevant issue in the tracker for more information. 

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

Images
------

**Please make sure to add your images under the GPL3 as well.**

**PNG** is the preferred format for screenshots, as it's not subject to compression artifacts the way JPG is. 
JPG is fine too, though, if the quality is high enough (Compression of 90% or better). 
Clarity is the priority, not file size. 

Animated GIFs are not suitable as screenshots, because the animated component is only visible when the docs are viewed in web form. 
Also the quality and/or file size ratio tends to be abysmal and thus multi-megabyte GIFs can take forever to download and start animating. 
They are however suitable as alternative to Video. 

Images should be **696px wide** at their **maximum**. 
The page layout has a width cap that makes it the effective maximum width for images. 
For this reason 4:3 pictures are preferred over widescreen. 
Images should be whatever shape they need to be in order to show the necessary information, there is no fixed aspect.
But since images will be scaled to fit the width of the page, in general images should not be unnecessarily wide. 
Otherwise they can end up too small when displayed.

.. NOTE: Verification Needed; 
  Is this set in the server? Does it apply to all browsers? Does this apply to offline docs too?
  From a test by ferdnyc "when I have a Chrome window open with the manual loaded into it, once the window hits about 1160px wide, that's it — the content stops getting any wider. Past that width (which is including the sidebar), the only thing that grows is the empty space to the right of the content container. And at that size, the images are scaled to 696px wide."
  https://github.com/OpenShot/openshot-qt/issues/2989

There is no demo art package availeble for sceenshots. 
Screenshots showing different content is an opportunity to illustrate the variety of different features and configurations available.
However during a step-by-step tutorial for a feature, it makes sense to have a set of consistent imports for all of the steps. 
So that the illustrations reflect exactly what the user would expect to see in the actual software.
|
Images should be named descriptively, so the names have relevance long-term.
It should say what it is, and it should be what it says. 
They should (not?) be named for the tutorial page they belong to. 

.. QUESTION: Opinions differ, see File naming and directory structure

They can be named for Action-WindowName or ActionStepNumber. 
Images belonging to a sequence should be numbered. 
Names like intro-tutorial-step-1.png (followed by -step-2.png through -step-n.png), 
interface-export-simple.png and so on. 

.. QUESTION: Should image sequences be in the same resolution? 
  So they can be combined to animation?

Tutorial art
------------
The color for arrows is *#aec255ff*

The green constrasts well with the dark GUI of Openshot
The font used in the art is *Ubuntu* and can be found in the repo or the Openshot installation. 

There is a green callout circle  used for numbering in the repo under docs/images/circle.svg. 
It is editable in software that can edit SVG files (e.g. Inkscape and Illustrator). 
The green arrow is not yet in the repo.

.. TODO: upload font and callout circle to dir

.. QUESTION: because it is an SVG, is the number changed in ReST?

.. PROPOSAL: save all tutorial art into docs/pointers/ or something like that?


Video
-----
The manual should ideally be useful in print form as well,
but for extra clarification a video or GIF can be included.
Any animated elements should enhance the information presented in the static content, rather than replace it. 
Whatever happens in the animation should also be described in full detail in the accompanying text.
So make sure a discription and pictures are suitable for offline documentation first. 

Video may be preferrable over animated GIF, because embedded videos are clearer and higher quality.
They are also click-to-play which avoids forcing a large initial download on the user. 
For short actions, GIFS may however be a lot easier. 

Beside GIF, only Youtube videos can be embedded with the tag
\.. youtube \:: 

.. NOTE: https://github.com/OpenShot/openshot-qt/pull/3394

Tables
------
Todo: Issues with tables

https://github.com/OpenShot/openshot-qt/issues/1262
https://github.com/OpenShot/openshot-qt/pull/1272

..  TODO: Table specifications
