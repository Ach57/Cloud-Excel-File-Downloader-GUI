# Downloading-Application
Overview
The Downloading Application creates a desktop application that interacts with a Google Spreadsheet to download images and organize them into folders based on order IDs. The program requires specific images for its interface, and the paths to these images can be customized by the user.

Description
This program utilizes Google Sheets API to access a Google Spreadsheet containing URLs of images. It then downloads these images and organizes them into folders named after the order IDs. The program provides a user-friendly interface and requires certain images for its graphical elements.

Functionality
Google Spreadsheet Integration: The application connects to a Google Spreadsheet to retrieve URLs of images.
Image Downloading: It downloads images from the URLs obtained from the spreadsheet.
Folder Creation: Folders are created on the local system, named after the order IDs, and images are stored within these folders.
Customizable Image Paths: Users can customize the paths to the images used in the application's interface.

Dependencies
gspread: Python API for Google Sheets
tkinter: GUI toolkit for Python
os: Operating system module for file operations
PIL: Python Imaging Library for image processing

Customizable Image Paths
The following images are used in the application's interface, and their paths can be customized by the user:

downloadIcon: Icon used for downloading actions.
JpgLogo: Logo image.
SubmitIcon: Icon for submission actions.
DeleteIcon: Icon for deletion actions.
StatusIcon: Icon indicating status.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

