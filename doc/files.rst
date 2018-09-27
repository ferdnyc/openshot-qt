.. Copyright (c) 2008-2016 OpenShot Studios, LLC
 (http://www.openshotstudios.com). This file is part of
 OpenShot Video Editor (http://www.openshot.org), an open-source project
 dedicated to delivering high quality video editing and animation solutions
 to the world.

.. OpenShot Video Editor is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

.. OpenShot Video Editor is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

.. You should have received a copy of the GNU General Public License
 along with OpenShot Library.  If not, see <http://www.gnu.org/licenses/>.

Files
=====

Before we can begin making a video, we need to import files into OpenShot. Most media file types are
recognized, such as videos, images, and audio files. Files can be viewed and managed in the **Project Files** panel.

Import Files
------------
There are many ways to import media files into OpenShot.

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Import Method
     - Description
   * - Drag-and-Drop
     - Drag files from your file manager (file explorer, finder, etc...) to the **Project Files** panel
   * - Right-Click
     - Right click in the **Project Files** panel, choose :menuselection:`Import Files...`
   * - :menuselection:`File` menu
     - Choose :menuselection:`File --> Import Files...` from the OpenShot main menu
   * - Toolbar button
     - Click the |Import| (Import) button in the toolbar at the top of the OpenShot main window

.. |Import| image:: /images/tb_import.svg
   :height: 16
   :width: 16


.. image:: images/quick-start-drop-files.jpg

File Menu
---------
To view the file menu, right click on a file (in the **Project Files** panel). Here are the actions you can use from the
file menu.

.. image:: images/file-menu.jpg

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Description
   * - :menuselection:`Import Files...`
     - Import files into your project
   * - :menuselection:`Thumbnail`/:menuselection:`Detail`
     - Toggle the view between details and thumbnails
   * - :menuselection:`Preview File`
     - Preview a media file
   * - :menuselection:`Split Clip...`
     - Split a file into many smaller clips
   * - :menuselection:`Edit Title`
     - Edit an existing title SVG file
   * - :menuselection:`Duplicate Title`
     - Make a copy, and then edit the copied title SVG file
   * - :menuselection:`Add to Timeline`
     - Add many files to the timeline in one step
   * - :menuselection:`File Properties`
     - View the properties of a file, such as frame rate, size, etc...
   * - :menuselection:`Remove from Project`
     - Remove a file from the project

Split Clip
----------
If you need to cut a file into many smaller clips before editing, the **Split
Clip** dialog is built exactly for this purpose. Right click on a file, and
choose :menuselection:`Split Clip...` from the context menu. This opens the
**Split Clip** dialog. Use this dialog to quickly cut out as many small clips as
you need. The dialog stays open after you create a clip, to allow you to repeat
the steps for your next clip. When you are finished, simply close the dialog.

.. image:: images/file-split-dialog.jpg

.. list-table::
   :header-rows: 1
   :widths: 5 19 76

   * - \#
     - Name
     - Description
   * - \1
     - Start of Clip
     - Mark the starting frame of your clip by clicking this button
   * - \2
     - End of Clip
     - Mark the ending frame of your clip by clicking this button
   * - \3
     - Name of clip
     - Enter an optional name
   * - \4
     - :guilabel:`Create`
     - Create the clip and add it to **Project Files**.
       (This also resets the **Split Clip** dialog, so you can repeat
       these steps for additional clips.)

Add to Timeline
---------------
In certain cases, you might need to add many files to the timeline at the same time. For example, a photo slide show,
or a large number of short video clips. The **Add to Timeline** dialog can automate this task for you. First, select
all files you need to add, right click, and choose :menuselection:`Add to Timeline`.

.. image:: images/file-add-to-timeline.jpg

.. list-table::
   :header-rows: 1
   :widths: 5 24 71

   * - \#
     - Name
     - Description
   * - \1
     - Selected Files
     - The list of files that will be added to the timeline
   * - \2
     - Order of Files
     - Use these buttons to reorder the list of files:
       |GoUp| (move up), |GoDown| (move down), |Shuffle| (randomize),
       |Remove| (remove)
   * - \3
     - Timeline Position
     - Choose the starting position and track where these files will be inserted on the timeline
   * - \4
     - Fade Options
     - Fade In, Fade Out, both, or none
   * - \5
     - Zoom Options
     - Zoom In, Zoom Out, or none
   * - \6
     - Transition
     - How to transition between files: You can select a specific transition,
       let OpenShot pick a transition at random, or use none at all.

.. |GoUp| image:: images/go-up.svg
   :width: 16
   :height: 16
.. |GoDown| image:: images/go-down.svg
   :width: 16
   :height: 16
.. |Shuffle| image:: images/view-refresh.svg
   :width: 16
   :height: 16
.. |Remove| image:: images/list-remove.svg
   :width: 16
   :height: 16

Properties
----------
To view the properties of any imported file in your video project, right click
on the file, and choose :menuselection:`File Properties`. This will launch the
**File Properties** dialog, which displays information about your media file.
For certain types of images (i.e. image sequences), you can adjust the frame
rate on this dialog also.

.. image:: images/file-properties.jpg

.. list-table::
   :header-rows: 1
   :widths: 5 22 73

   * - \#
     - Name
     - Description
   * - \1
     - File Properties
     - Select an image sequence in the **Project Files** panel,
       right click and choose :menuselection:`File Properties`
   * - \2
     - Frame Rate
     - For image sequences, you can also adjust the frame rate of the animation
