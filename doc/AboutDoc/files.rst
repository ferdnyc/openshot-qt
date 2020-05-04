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

The source files for the manual are all found in the project repository (the doc/ directory),
 `test <https://github.com/OpenShot/openshot-qt/tree/develop/doc>`_ 


The documentation is written in reStructured Text, or Rest.
This is a plain text format encoded in UTF-8.
It contains special syntax so formatting can be applied by third-party tools.
The tool used by Openshot is Sphinx to create both the online HTML and the offline manual.

You can suggest improvements or submit small changes for our documentation on our github here: 
https://github.com/OpenShot/openshot-qt/issues/2989

Or in *this* reddit thread. 

.. NOTE: Reddit tread to be made, add hyperlink 

The preferred method for submitting large edits would be via GitHub Pull Request. 
But we can make accommodations for anyone who would like to contribute but isn't familiar with version-control systems like Git.


License
-------
We use the GPL-3 license (see above) for documentation, see the header. 
This is both simplicity because it is the same license as the project code. 
And because the documentation gets parsed in other tools before it reaches its final form. 


Github
------
In the issue tracker, subjects that contain explanations that should probably be included in the documentation can me labeled `*docs*. <https://github.com/OpenShot/openshot-qt/labels/docs>`_ 
Questions that are answered often in github or reddit can be tagged *FAQ* / are tagged *question*

:: add link reddit + link github

Tutorials how to add changes to github: 
Github on Pull requests https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork
Github text howto https://opensource.com/life/16/3/submit-github-pull-request
Github video howto https://www.youtube.com/watch?v=rgbCcBNZcdQ

It is possible to edit files directly in the Github web interface.
To edit a file via the web interface,
you can just click the pencil icon in its upper-right corner.
(Take docs/getting_started.rst for example)
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
They can be installed via pip3 install sphinx sphinx-rtd-theme, or using most package managers. 
Anyone who would like to contribute and needs help with installing and using Sphinx can ask for support in the issues tracker.

Tutorial video	https://www.youtube.com/watch?v=ouHVkMo3gwE

Rest Basic Syntax
-----------------
`List of basic syntax <Documentation_RestSyntax.rst>`_  in Openshot documentation.  

Some explanation on  https://wiki.typo3.org/ReST_Syntax
More here 
Video tutorial here 

Software 
Notepad++ Rest template:	https://github.com/steenhulthin/reStructuredText_NPP
Linux: 


File naming and directory structure
-----------------------------------

Files are stored in \docs
Images are named after the file they belong to, and sorted in the doc\images subdirectory. 
.. Or maybe not, see Images
Translations go into their own directory. 

File structure
--------------

Every file starts with 5 hidden segments (See template. )

Copyright notice
Openshot description
Openshot disclaimer
License notice
Referral anchor for the title

Followed by the title with double underlining


Then a short description of what the chapter will be about, and why the reader should care (or skip). 

Subtitles are single underlined
              

Sentences should be written one sentence per line, and *NOT* end on a space. 
The markup language then flows them all together into paragraphs when it generates the formatted docs. 
You can also break at other logical points, like after a comma in a longer sentence, 
or before starting an inline markup command. 
It is a guideline, not a rule.  
This tends to be a pretty good fit for any sort of written prose, when it is in a markup language like adoc/reST/MarkDown and managed in version control. 

There are four reasons for this: 
 Writing that way, there is no worrying about line length or when to wrap. 
 It encourages shorter, simpler sentences which is a good thing when writing docs. 
 The diffs when changes are submitted also tend to be more readable and focused. 
 Lines are easier to translate and less likely to be changed. 













Import Files
------------
There are many ways to import media files into OpenShot.

.. table::
   :widths: 25

   ====================  ============
   Name                  Description
   ====================  ============
   Drag and Drop         Drag and drop the files from your file manager (file explorer, finder, etc...)
   Right Click\→Import   Right click in the **Project Files** panel, choose **Import Files...**
   File Menu\→Import     File menu\→Import Files...
   Import Files Toolbar  Click the **Import Files...** toolbar button (on the top menu)
   ====================  ============

.. image:: images/quick-start-drop-files.jpg

File Menu
---------
To view the file menu, right click on a file (in the **Project Files** panel). Here are the actions you can use from the
file menu.

.. image:: images/file-menu.jpg

====================  ============
Name                  Description
====================  ============
Import Files...       Import files into your project
Thumbnail/Detail      Toggle the view between details and thumbnails
Preview File          Preview a media file
Split Clip...         Split a file into many smaller clips
Edit Title            Edit an existing title SVG file
Duplicate Title       Make a copy, and then edit the copied title SVG file
Add to Timeline       Add many files to the timeline in one step
File Properties       View the properties of a file, such as frame rate, size, etc...
Remove from Project   Remove a file from the project
====================  ============

Split Clip
----------
If you need to cut a file into many smaller clips before editing, the **Split Clip** dialog is built exactly for this
purpose. Right click on a file, and choose Split Clip... from the file menu. This opens the Split Clip dialog. Use this
dialog to quickly cut out as many small clips as you need. The dialog stays open after you create a clip, to allow you
to repeat the steps for your next clip. When you are finished, simply close the dialog.

.. image:: images/file-split-dialog.jpg

.. table::
   :widths: 5 20

   ==  ==================  ============
   #   Name                Description
   ==  ==================  ============
   1   Start of Clip       Choose the starting frame of your clip by clicking this button
   2   End of Clip         Choose the ending frame of your clip by clicking this button
   3   Name of Clip        Enter an optional name
   4   Create Clip         Create the clip (which resets this dialog, so you can repeat these steps for each clip)
   ==  ==================  ============

Add to Timeline
---------------
In certain cases, you might need to add many files to the timeline at the same time. For example, a photo slide show,
or a large number of short video clips. The **Add to Timeline** dialog can automate this task for you. First, select
all files you need to add, right click, and choose Add to Timeline.

.. image:: images/file-add-to-timeline.jpg

.. table::
   :widths: 5 28

   ==  ==================  ============
   #   Name                Description
   ==  ==================  ============
   1   Selected Files      The list of selected files that need to be added to the timeline
   2   Order of Files      Use these buttons to reorder the list of files (move up, move down, randomize, remove)
   3   Timeline Position   Choose the starting position and track where these files need to be inserted on the timeline
   4   Fade Options        Fade in, fade out, both, or none
   5   Zoom Options        Zoom in, zoom out, or none
   6   Transitions         Choose a specific transition to use between files, random, or none
   ==  ==================  ============

Properties
----------
To view the properties of any imported file in your video project, right click on the file, and choose **File Properties**.
This will launch the file properties dialog, which displays information about your media file. For certain types of images
(i.e. image sequences), you can adjust the frame rate on this dialog also.

.. image:: images/file-properties.jpg

.. table::
   :widths: 5 24
   
   ==  ====================  ============
   #   Name                  Description
   ==  ====================  ============
   1   File Properties       Select an image sequence in the **Project Files** panel, right click and choose **File Properties**
   2   Frame Rate            For image sequences, you can also adjust the frame rate of the animation
   ==  ====================  ============

