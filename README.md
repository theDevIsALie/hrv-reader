# hrv-reader - a blender add-on to import HRV format
HRV Reader - A Blender add-on to read the HRV (Human Readable Voxel) file format.

## The HRV format
HRV means "Human Readable Voxel".
It's a simple file format that I created for my personnal projects, I didn't found any good voxel  based 3D file format that were open-source and free.

## How to install the HRV add-on ?
Simply install the add-on from this link: [MediaFire](http://www.mediafire.com/file/i55wq66mlkvihnp/hrv_reader001build.zip/file)
Or you simply create a ZIP with the content of this repository.
Then go on Blender, click "Edit > Preferences > Install", click on the "Install" button and select the ZIP file.
The add-on should now be installed !

## How to use HRV ?
The main goal of HRV is to stay simple and it is !

Let's create a red cube:
```
voxel_at 0 0 0 with_rgba 255 0 0 255
```
If your import this HRV into Blender with the add-on, it will create a red cube at the 0x, 0y, 0z position !
This is the result:
<p align="center">
  <img src="https://i.imgur.com/L2wSTJY.png">
 </p>


This is how it works:
```
voxel_at x y z with_rgba r g b a
```
x -> x position of your cube
y -> y position of your cube
z -> position of your cube

r -> red value (0->255)
g -> green value (0->255)
b -> blue value (0->255)
a -> alpha value (0->255)

Each line on a HRV represents an individual voxel, so you could do:
```
voxel_at 0 0 0 with_rgba 100 100 100 255
voxel_at 0 0 1 with_rgba 200 100 100 255
voxel_at 0 0 2 with_rgba 100 200 100 255
voxel_at 0 0 3 with_rgba 100 100 200 255
```
This is the result:
<p align="center">
  <img src="https://i.imgur.com/w6JLMIR.png">
 </p>

## How to import an HRV file ?
Slide the arrow on the side of the Blender viewport to the left until a menu appear:
<p align="center">
  <img src="https://i.imgur.com/6RKT54s.png">
 </p>

Click the "HRV" button on the side menu:
<p align="center">
  <img src="https://i.imgur.com/NECWmUs.png">
 </p>

Now, you will see a button titled "Import HRV", click on the button and select your **.hrv** file !

Your HRV should now be imported !

