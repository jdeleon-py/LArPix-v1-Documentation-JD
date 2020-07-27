This is a sequence of instructions to install and successfully test the LArPix board.

First off, this is under the assumption that your machine has the capability to install and remove things with the 
pip command. Secondly, this tutorial is made under the assuption that the user has access to Jupyter notebooks, 
but it is not strictly required. Third, this installation tutorial will be completed with the application of 
virtual environments with Pythonvia the built-in venv command. This tutorial will install multiple versions of the 
larpix software, and thus will remain organized with localized virtual environments.
Below is a brief rundown of venv's.

* Note: to install jupyter notebooks, deactivate any envs and go back to the global package manager.
* Install jupyterlab with command >>> pip install jupyterlab


**Virtual Environments with Python (VENV)**
---------------------------------------------------------------------------------------------------------------------------------
Virtual Environments are a means of separating python packages based on the specific project being worked on.
Packages are isolated to the env itself, so any updates that can be made are particlar 
to the env and does not interfere with any other project.

For instance, a data science project may have an environment with packages:
  - numpy
  - pandas
  - matplotlib
  - etc...

A web dev project may have a separate env with packages:
  - requests
  - django
  - flask
  - etc...

Where envs come in handy is when the user has multiple projects that require similar environments. 
For instance, consider a situation where the user has an old data science project running optimally with an old version 
of numpy and the user wanted to create a new data science project with a newer version of numpy. If all python packages
are installed globally/systematically without an env, then the numpy package will update to service the new project and 
thereby break the older project. However, with envs aiding both projects, both versions of numpy can exist isolated 
within each specific project environment and everybody is happy.

This concept is applicable to the larpix project in the sense that multiple versions of larpix-control are released
in the testing process. To keep code and files maintained to the point where an update of the larpix-control software
does not break the code or files created, envs for each larpix-control version is created to govern how files are processed.

Basic commands for venv:
  - create a project directory >>> mkdir project
  - >>> cd project
  - create a virtual environment >>> python3 -m venv <venv_name>
  - activate the virtual environment >>> source <venv_name>/bin/activate
  - (Deactivate anytime using the command >>> deactivate)
  - The env is now activated and the user is free to install the necessary packages to the project,
    and free to move about any directory that pertains to the project's env

This tutorial will create two virtual envs - one for larpix-control==2.3.0 and the other for larpix-control==3.2.2


**Directory Tree for larpix project**
---------------------------------------------------------------------------------------------------------------------------------
|larpix <br />
----|larpix_v2_3_0 <br />
--------|description.txt <br />
--------|larpix-backup <br />
------------|... <br />
--------|larpix-control (v2.3.0) <br />
------------|... <br />
--------|larpix-geometry <br />
------------|... <br />
--------|larpix-scripts <br />
------------|... <br />
--------|venv_larpix_v2_3_0 <br />
------------|... <br />
----|larpix_v3_2_2 <br />
--------|description.txt <br />
--------|larpix-backup <br />
------------|... <br />
--------|larpix-control (v3.2.2) <br />
------------|... <br />
--------|larpix-geometry <br />
------------|... <br />
--------|larpix-scripts <br />
------------|... <br />
--------|venv_larpix_v3_2_2 <br />
------------|... <br />
----|Project_LArPix <br />
--------|project_scripts <br />
--------|data_files (to be put into a database later) <br />
--------|... <br />
  

**Installation**
---------------------------------------------------------------------------------------------------------------------------------
1. larpix_v2_3_0
  - In the larpix base directory, make a directory allocated to larpix-control==2.3.0 specifically 
      >>> mkdir larpix_v2_3_0
  
  - Create a virtual environment for larpix-control==2.3.0 
      >>> python3 -m venv venv_larpix_v2_3_0
  
  - Activate the virtual environment to install packages 
      >>> source venv_larpix_v2_3_0/bin/activate
  
  - While venv is activated, install larpix-control package 
      >>> pip install larpix-control==2.3.0

  - Clone scripts/directories from github to reference back to
      >>> larpix-control: git clone https://github.com/larpix/larpix-control.git -b v2.3.0 <br />
      >>> larpix-scripts: git clone https://github.com/larpix/larpix-scripts.git <br />
      >>> larpix-geometry: git clone https://github.com/samkohn/larpix-geometry.git <br />
      >>> larpix-backup: git clone https://github.com/samkohn/larpix-backup.git <br />

  - While venv is activated, install pytest to make sure everything is operational
      >>> pip install pytest==4.6.9 <br />
      >>> pip install pytest-arraydiff==0.3 <br />
      >>> pip install pytest-astropy==0.5.0 <br />
      >>> pip install pytest-doctestplus==0.3.0 <br />
      >>> pip install pytest-openfiles==0.3.2 <br />
      >>> pip install pytest-remotedata==0.3.1 <br />

  - While venv is activated, estbalish a kernel with the working venv as a Jupyter notebook (to analyze data)
      >>> pip install ipykernel <br />
      >>> ipython kernel --user --name=venv_larpix_v2_3_0 <br />
      When you make a new notebook, choose the kernel of the notebook to be venv_larpix_v2_3_0 <br />

  - While venv is activated, make sure all systems are operational with pytest
      Go into the larpix-control directory
      >>> pytest <br />
      The test should pass with a couple of warnings leftover.

  - Deactivate the venv to install the other packages
      >>> deactivate

<br />

2. larpix_v3_2_2
  - In the larpix base directory, make a directory allocated to larpix-control==3.2.2 specifically 
      >>> mkdir larpix_v3_2_2
  
  - Create a virtual environment for larpix-control==3.2.2 
      >>> python3 -m venv venv_larpix_v3_2_2
  
  - Activate the virtual environment to install packages 
      >>> source venv_larpix_v3_2_2/bin/activate
  
  - While venv is activated, install larpix-control package 
      >>> pip install larpix-control==3.2.2

  - Clone scripts/directories from github to reference back to
      >>> larpix-control: git clone https://github.com/larpix/larpix-control.git -b v3.2.2 <br />
      >>> larpix-scripts: git clone https://github.com/larpix/larpix-scripts.git <br />
      >>> larpix-geometry: git clone https://github.com/samkohn/larpix-geometry.git <br />
      >>> larpix-backup: git clone https://github.com/samkohn/larpix-backup.git <br />

  - While venv is activated, install pytest to make sure everything is operational
      >>> pip install pytest==4.6.9 <br />
      >>> pip install pytest-arraydiff==0.3 <br />
      >>> pip install pytest-astropy==0.5.0 <br />
      >>> pip install pytest-doctestplus==0.3.0 <br />
      >>> pip install pytest-openfiles==0.3.2 <br />
      >>> pip install pytest-remotedata==0.3.1 <br />

  - While venv is activated, estbalish a kernel with the working venv as a Jupyter notebook (to analyze data)
      >>> pip install ipykernel <br />
      >>> ipython kernel --user --name=venv_larpix_v3_2_2 <br />
      When you make a new notebook, choose the kernel of the notebook to be venv_larpix_v3_2_2 <br />

  - While venv is activated, make sure all systems are operational with pytest
      Go into the larpix-control directory
      >>> pytest <br />
      The test should pass with a couple of warnings leftover.

  - Deactivate the venv to install the other packages
      >>> deactivate

