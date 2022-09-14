# User manual

Team : Charly G. & Théo Pirouelle

<a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/language-python-blue?style=flat-square" alt="laguage-python" />
</a>

<img src="https://upload.wikimedia.org/wikipedia/fr/thumb/d/dc/Logo_parcoursup.svg/langfr-250px-Logo_parcoursup.svg.png" alt="parcoursup" style="zoom:40%;" />

---

## Table of contents
- [Installation guides](#installation-guides)
  * [Linux](#linux)
    + [Python's installation](#pythons-installation)
    + [Program installation](#program-installation)
    + [Program launch](#program-launch)
  * [Windows](#windows)
    + [Python's installation](#pythons-installation-1)
    + [Program installation](#program-installation-1)
    + [Program launch](#program-launch-1)
  * [MacOS](#macos)
    + [Python's installation](#pythons-installation-2)
    + [Program installation](#program-installation-2)
    + [Program launch](#program-launch-2)
- [Program use](#program-use)
  * [CSV file format](#csv-file-format)
  * [Program use](#program-use-1)
  * [Possible errors](#possible-errors)

---

# Installation guides

## Linux

### Python's installation

If you are using Ubuntu 16.10 or newer, then you can easily install Python 3.6 with the following commands:

```sh
sudo apt-get update
sudo apt-get install python3.6
```



If you are using another version of Ubuntu (e.g. the latest LTS release) or you want to use a more current Python, we recommend using the [deadsnakes PPA](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa) to install Python 3.8:

```sh
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8
```



If you are using other Linux distribution, chances are you already have Python 3 pre-installed as well. If not, use your distribution’s package manager. For example on Fedora, you would use `dnf`:

```sh
sudo dnf install python3
```



To see which version of Python 3 you have installed, open a command prompt and run:

```sh
python3 --version
```



### Program installation

Install `unzip` on Linux:

```sh
sudo apt install unzip
```



To unzip a `.zip` file:

```sh
# In current directory
unzip filename.zip

# To different directory
unzip filename.zip -d /path/to/directory
```



### Program launch

Open a terminal, move to the `src` directory of the project with the `cd` command.

To run the program, enter the command:

```sh
python3 main.py
```





## Windows

### Python's installation

Find all download resources at [python.org](https://www.python.org/downloads/windows/).

Full details of the python installation documentation at [docs.python.org](https://docs.python.org/3/using/windows.html).



### Program installation

Install [Winrar](https://www.win-rar.com/download.html) or [7zip](https://www.7-zip.org/download.html).

To unzip the file `fileName.zip` right click on it and select extract.



### Program launch

Open a terminal, move to the `src` directory of the project with the command `cd`.

To run the program, enter the command:

```sh
py main.py
```





## MacOS

### Python's installation

Find all download resources at [python.org](https://www.python.org/downloads/mac-osx/).



You can also download [Xcode](https://developer.apple.com/xcode/). If you are doing a fresh install of [Xcode](https://developer.apple.com/xcode/), you will also need to add the command line tools by running the following command in the terminal:

```sh
xcode-select --install
```



[Homebrew](http://brew.sh/#install) is a decent package manager, to install it open the terminal and run :

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```



Once you’ve installed [Homebrew](http://brew.sh/#install), insert the [Homebrew](http://brew.sh/#install) directory at the top of your `PATH` environment variable. You can do this by adding the following line at the bottom of your `~/.profile` file:

```sh
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```



If you have OS X 10.12 (Sierra) or older use this line instead:

```sh
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```



Now, we can install Python 3:

```sh
brew install python
```



At this point, you have the system Python 2.7 available, potentially the [Homebrew version of Python 2](https://docs.python-guide.org/starting/install/osx/#install-osx) installed, and the Homebrew version of Python 3 as well.

- `python` will launch the Homebrew-installed Python 3 interpreter.
- `python2` will launch the Homebrew-installed Python 2 interpreter (if any).
- `python3` will launch the Homebrew-installed Python 3 interpreter.



If the [Homebrew](http://brew.sh/#install) version of Python 2 is installed then `pip2` will point to Python 2. If the [Homebrew](http://brew.sh/#install) version of Python 3 is installed then `pip` will point to Python 3.

To see which version of Python you have, open a terminal and run:

```sh
python --version
```



### Program installation

To unzip the file `fileName.zip`, double click on the file.



### Program launch

Open a terminal, move to the `src` directory of the project with the command `cd`.

To run the program, enter the command:

```sh
python3 main.py
```





# Program use

## CSV file format

The `.csv` file format should be as follows:

|         | Name1                  | Name2                  | Name3                  |
| ------- | ---------------------- | ---------------------- | ---------------------- |
| School1 | PrefSchool,PrefStudent | PrefSchool,PrefStudent | PrefSchool,PrefStudent |
| School2 | PrefSchool,PrefStudent | PrefSchool,PrefStudent | PrefSchool,PrefStudent |
| School3 | PrefSchool,PrefStudent | PrefSchool,PrefStudent | PrefSchool,PrefStudent |

or

|       | School1                | School2                | School3                |
| ----- | ---------------------- | ---------------------- | ---------------------- |
| Name1 | PrefStudent,PrefSchool | PrefStudent,PrefSchool | PrefStudent,PrefSchool |
| Name2 | PrefStudent,PrefSchool | PrefStudent,PrefSchool | PrefStudent,PrefSchool |
| Name3 | PrefStudent,PrefSchool | PrefStudent,PrefSchool | PrefStudent,PrefSchool |

For example:

|          | Tom  | Bob  | Alice |
| -------- | ---- | ---- | ----- |
| ENSEEIHT | 1,2  | 2,1  | 3,3   |
| INSA     | 2,1  | 1,2  | 3,1   |
| ENSIMAG  | 1,3  | 2,3  | 3,2   |



With any number of columns and rows.

The `.csv` file should be placed in the `src/csvFiles/` directory.



## Program use

At the start of the program, the user is asked for the full name of the `.csv` file:
The file name must be in the format `filename.csv`.

<img src="doc/pictures/Screenshot 2021-06-06 152423.png" alt="PU" />



The user is then asked if the association is made on the elements of the row header or the column header.
The answer given can be:

- `r`, `row`, `rows`, `l`, `ligne`, `lignes` for the binding on the header row ;
- `c`, `col`, `column`, `columns`, `colonne`, `colonnes` for the binding on the header column.

<img src="doc/pictures/Screenshot 2021-06-06 155624.png" alt="PU" />



The program asks the user for the capacity for each school.
The capacity provided must be higher or equal to 0.

<img src="doc/pictures/Screenshot 2021-06-06 160259.png" alt="PU" />



The result is then displayed.

The program first displays the students assigned to each school with the name of the school and the names of the students in a box.
In the second step, it displays the number of rounds the program made to assign all students to a school.

<img src="doc/pictures/Screenshot 2021-06-06 163039.png" alt="PU" />



## Possible errors

When asking the user for a `.csv` file name, if the proposed name does not contain the extension of a `.csv` file, the `Warning: Incorrect file name !` error appears.

<img src="doc/pictures/Screenshot 2021-06-06 163342.png" alt="PU" />



When asking the user for the `.csv` file name, if the proposed name is not found in the expected directory, the `Warning: CSV file not found` error appears.

<img src="doc/pictures/Screenshot 2021-06-06 163459.png" alt="PU" />



When asking the user for the capacity of a school, if the value entered is not an integer, the `Warning: You must enter an integer !` error appears.

<img src="doc/pictures/Screenshot 2021-06-06 163725.png" alt="PU" />



When asking the user for the capacity of a school, if the value entered is less than 0, the `Warning: The capacity must be higher than 0 !` error appears.

<img src="doc/pictures/Screenshot 2021-06-06 163759.png" alt="PU" />
