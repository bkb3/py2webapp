# py2webapp
### Introduction
`py2webapp` is a small python program to convert all your scripts to a webapp, without the hassle! You do need to make small modification to your scripts though!

### Installation
```
git clone https://github.com/bkb3/py2webapp.git
cd py2webapp/
pip3 install requirements.txt
```

### Usage
```
usage: py2webapp [-h] [-v] -f INPUTSCRIPTFILE -c CONFIG

Convert your scripts to webapp

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Show program's version number and exit.
  -f INPUTSCRIPTFILE, --inputscriptfile INPUTSCRIPTFILE
                        Your script to convert to webapp
  -c CONFIG, --config CONFIG
                        Configuration file

github@bkb3
```

### How to
There are two steps:

- Making a `config` file
- Modifying your current working script

First make a config file as:
```
text_input = {
    'Input 1':'arg1',
    'Input 2':'arg2',
}

numerical_input = {
    'Input 3':'arg3',
    'Input 4':'arg4',
}

app_properties = {
    'Name': 'App name',
    'Description': 'Made using py2webapp',
    'Author': 'github@bkb3'
}
```
`Input 1` etc are the name of inputs to your script and should be descriptive enough because they appear in the website later on. The arguments `arg1` etc should be named exactly as required by your script to run. There is NO limitation on the number of these inputs. Note that text and numerical inputs should be separate as shown in the config file.

Then modify your actual script by making a dictionary as:
```
my_dict = {}
my_dict['Results name 1'] = your first result
...
```
The dictionary keys should be descriptive enough as they appear in the website later on. Finally, instead of `return`ing your results, print this dictionary as `print(my_dict)`.

Once you made these changes, you can use `py2webapp` as:

```
python3 py2webapp -f your_modified_script -c your_config_file
```
The webapp will be generated in the same location as your script as `app.py`. This needs to be made executable first as `chmod +x app.py`. Then simply run the app as `python3 app.py`. Your website will run locally at [http://localhost:5050](http://localhost:5050).

Confused? Check the examples directory which has working example scripts and config files.
