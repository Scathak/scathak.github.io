---
layout: post
title:  "QR and Bar codes helper"
date:   2024-10-07 20:25:39 +0300
categories: jekyll update
---
This is an add-in for MS Excel that helps you work with various codes. After installation, the user has access to two side panels. The first is the code generation panel, which contains several buttons, the most important of which are “Get QR Code” and “Get Barcode”. Both functions take information from the active cell, generate a corresponding code image and place it nearby.
The second panel can help with code recognition from the webcam stream. Several different video sources are available. Built-in webcams and USB-connected cameras should automatically appear in the drop-down list, while LAN IP cameras need to be added manually by pasting their full address into the same drop-down list.

It is quite interesting to use the smartphone's camera as a webcam. It gives you more flexibility with the equipment. In case of WiFi connection it gives you freedom of movement with a preview on your smartphone and an Excel spreadsheet. 

Testing of Android cameras gave quite satisfactory results. These programs use a similar approach. If the smartphone is connected to the computer via a USB cable, the computer must have a client program running that ensures that the driver detects the "virtual" USB camera. The "USB debugging" mode must also be enabled on the smartphone. Another way is to show the camera as an IP camera when connected to WiFi, with the address and connection port entered in the "Camera" panel of the corresponding Excel add-in.

![screenshot of the program](/Screenshot240701.png)

<h3>Download</h3>
 
<a href="/Qrample_Windows_Release_v1.0.zip">Universal Windows installer</a>


