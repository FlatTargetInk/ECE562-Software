# The Viewer

**Program:**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view.py  
**Version:**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pre-Alpha  
**Release Date:**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;March 22, 2017

---

## INFO Contents

1. Configuration Used
2. Using pyuic5.bat

---

### 1. **Configuration Used**
  * Python 3.6.0
  * Anaconda 4.3.0
  * Qt Designer 5.6.2 
    * Qt Designer is included with Anaconda, located in "C:\Wherever_You_Installed\Anaconda3\Library\bin\designer.exe"
  * pyuic5.bat
    * Also included with Anaconda, located in "C:\Wherever_You_Installed\Anaconda3\Library\bin\pyuic5.bat"

### 2. **Using pyuic5.bat**
  * Qt Designer saves files with the extension '.ui'.
  * It is necessary to convert the '.ui' file to the '.py' extension for use with Python.
  * The pyuic5.bat file handles this conversion.
  * Usage:
```
C:\Your_Development_Branch\Directory>pyuic5.bat Qt_Design.ui > Qt_Design.py
```
  * In the above example, 'Qt_Design.ui' is the file to be converted, and 'Qt_Design.py' is the  destination file. Here, the '.ui' file is located in the current working directory, and the '.py' is created in the current working directory. Otherwise, the directories must be specified.
  * The pyuic5.bat file can be run from any directory. 