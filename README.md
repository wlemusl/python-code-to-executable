# python-script-to-executable

This project demonstrates how to use cx_Freeze to convert a python script to an executable application. Specifally, it is utilized the "alien-invasion-pygame" python repository as an example.

Keypoints that you MUST know:

1. You must write a setup.py file with similar lines of codes than the one included in this repository.
2. This setup.py file must be included in the same folder of the python code that you want to convert into an executable. In our example, setup.py must be placed with all the files of the "alien-invasion-pygame" folder.
3. Press "shift + right click" to the folder that contains all your python script. For our specific case, it must be the "alien-invasion-pygame" folder.
4. Select "Open PowerShell window here".
5. Type the following line: python setup.py build 
6. And then press "enter".
7. If the PowerShell outputs a message saying that Python was not found, you will need to specify its specific location in your hard drive. It must be something like this: C:\Users\willi\anaconda3 python setup.py build
8. The output should be a folder called "build", which will be located in the same folder where your python code is. The "build" folder will contain the executable and all the requiered libraries and programs to run the executable.
9. cx_Freeze works on Windows, Mac and Linux, but the executable will ONLY run on the same platform from it was converted. So, if you want to run your programs for Windows, freeze it on Windows.

This repository contains ten py files, one txt file, and one folder with three images.
