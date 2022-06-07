# INTSET-SORT
### Integer set average sort mechanism

## 1. Resume
    The code nested in this git repository was meant to sort numbers in a given lottery ticket
    and exemplify how the random values can repeat differently for each time the program runs.
    Those random values aproach each other on average reincidence as the number of tests gets higher.
    Results obtained on default configuration points towards statistics already known in mathematics.
    Further investigation or modifications might change the default results.
## 2. System and Requirements
    The code was developed using Ubuntu/Debian as operating system, and python3 as the compiler.
    'linux.sh' is an script to compyle and run the main code on linux based systems.
## 3. Packages and Instructions[INSTALL LIBRATIES]
    The following debian/ubuntu python3 modules are required to run the code:
    python3
    python3-random
    python3-operator
    python3-collections
    python3-itertools
### To edit the code on '.ipynb' Jupyter is recommended:
    jupyter-notebook
    The file install-packages.sh can be run to install all the recommended libraries:
    chmod +wr ./install-packages.sh
    ./install-packages.sh
### To convert jupyter files('.ipynb') into python('.py'):
    jupyter nbconvert --to script ./inset-v0-3-3.ipynb
## 4. Running the main code [START PROGRAM]
    After installing all the libraries the main code can be run, preferentially on the latest version
    available:
    chmod +wrx ./intset-v0-3-3.sh
    ./intset-v0-3-3.sh
