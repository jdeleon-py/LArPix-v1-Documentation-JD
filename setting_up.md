This is a sequence of instructions to install and successfully test the LArPix board.

First off, this is under the assumption that your machine has the capability to install and remove things with the 
pip command.

This first part can be installed without connecting to the physical board.

1. Open the terminal on your machine. 
      - If you are using MAC, use the MAC terminal.
      (From my experience, the native operating system a MAC uses matches up nicely with the larpix board.)
      
      - The next best operating system would be that of Ubuntu supported natively or via
        Virtual Machine, which can be downloaded onto your computer.
      
2. Make a directory to store all your larpix software and files
      - Use the command: 'mkdir larpix'
      
      * Side note:
          The command: 'ls' lets you observe all the contents in your current directory.
          The command: 'cd <directory_name>' lets you go into the directory file named 'directory-name'.
          The command: 'cd ..' moves back a layer in relation to which directory you are currently in.
        
      Use the command: 'cd larpix' to go into your larpix directory file.
      
3. Clone the larpix-control repository from Github and install
      *Inside your larpix directory*
      
      - Use the command: 'git clone https://github.com/larpix/larpix-control' -b v2.3.0
        (This creates a repository, or sub-directory, in the larpix directory you just created.)
        This also installs everything with the working version 2.3.0, which is a safe 'complete' larpix-control package.
        Future versions will utilize larpix-control v3.2.1
       
      - Go into the larpix-control repository.
        Use the command: 'cd larpix-control'
        (Check if your larpix-control repository is even there in the first place by using the command: 'ls')
        
      - Inside the larpix-control repository,
        Use the command: 'pip install -e.'
        
      - Go back to the larpix directory using the command 'cd ..'

      -For good measure, install the larpix-control software via pip as well.
        Use the command: 'pip install larpix-control==2.3.0'
        Minor tests for now will only utilize the version 2.3.0 software.
      
4. Clone the larpix-scripts repository (only clone, no need to install)
      - Inside the larpix directory,
        Use the command: 'git clone https://github.com/larpix/larpix-scripts'

5. Clone larpix-geometry repository and install
      - Inside the larpix directory,
        Use the command: 'git clone https://github.com/samkohn/larpix-geometry'
      
      - Go inside the larpix-geometry repository using the 'cd larpix-geometry' command and
        Use the command: 'pip install -e.'
      
      - Go back to the larpix directory main menu using the command: 'cd ..'
        
6. Clone larpix-backup repository
      (Only necessary if you wanted to to backup files to another location)
      - Use the command: 'git clone https://github.com/samkohn/larpix-backup'

7. You have now installed all the necessary software, but now it's time to check whether all your software 
   VERSIONS are up to date. Not having the correct versions of software will prevent you from 
   using certain tests.
      - Side Note: To check the version of a piece of software,
        Use the command: '<software_name> --version'
      
      - Side Note: In the event you have an outdated piece of software,
        Use the command: 'pip uninstall <thing>' to uninstall the current version
        Use the command: 'pip install <thing>==<version>' to install with the corrected version
      
      - Side Note: Do not worry about installing these following packages in a specific 
        folder/repository/directory. The 'pip' command installs things globally, 
        so it will find the correct folder for you.
        
      - (Package, correct version):
            (pytest, 4.6.9)
            (pytest-arraydiff, 0.3)
            (pytest-astropy, 0.5.0)
            (pytest-doctestplus, 0.3.0)
            (pytest-openfiles, 0.3.2)
            (pytest-remotedata, 0.3.1)
            
8. Run a test to ensure all systems operational.
      - Go to the larpix-control repository
      - Run the command: 'pytest'
      If the test passes give or take a few warnings, you're good to go!
