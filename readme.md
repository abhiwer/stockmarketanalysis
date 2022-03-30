
Creating a Virtual Environment for Python Application

You may need to install venv package first before using going further
#You can use pip to find venv package.
Links:
<https://towardsdatascience.com/virtual-environments-104c62d48c54#:~:text=A%20virtual%20environment%20is%20a,a%20system%2Dwide%20Python).>

<https://realpython.com/python-virtual-environments-a-primer/>

<https://docs.python.org/3/tutorial/venv.html>

python3 -m venv nameOfYourEnvironment   

ex:
python3 -m venv alphaenv


Activation:

For windows:

go to <alphaenv\Scripts\activate.bat> as per python docs


But go to your environment i.e, alphaenv  and after goto Scripts and  do .\activate

Sortcut:
use terminal for this operattion in VS code.

Basic Terminlogy to be used:
ls to find the current directory items.
cd to change directory
cd .. to get back
Use Tab for autocompletetion of directories name

lets get started:

cd <yourenvironmentname>  i.e, cd alphaenv in my case
ls  # it is used to make sure we are in right dir.
cd to got to scripts i.e, cd Scripts or cd .\Scripts\
ls
.\activate     # use this to activate the virtual environment.


 Shortcut 2: Without using terminal :

 Go to view > command palette > python select interpreter > select the the interpreter from your project folder, that exits in your virtual environment.

 Address: alphaenv>scripts>python3.exe