# FEniCS installation
This repository is for students of CFD and FEM Courses at Bursa Technical University to install FEniCS on their computers with Windows OS.

## Enabling WSL and VMP on Windows
First enable WSL and VMP (Sanal Makine Platformu). Search `Windows Ozelliklerini Ac veya Kapat` in TR characters from the Start menu and enable the `Linux icin Windows Alt sistemi` and `Sanal Makine Platformu` as follows:

Please note that this operation needs a root user authentication.

![enable_wsl](./figures/enable_wsl_vmp.png)
 
Restart your computer.

## Ubuntu 20.04.4 LTS on Windows
Install Ubuntu 20.04.4 LTS from the Microsoft store shown as follows:
![install_ubuntu](./figures/install_ubuntu.png)

Install Ubuntu 20.04.4 LTS. The terminal window will appear after the download process finishes.
Then it will show up the first line (1). Wait for a few minutes. Then the following three lines will appear
and Ubuntu asks you to name your installation (2). Finaly, you need to create a password (3) and (4)
![install_ubuntu2](./figures/install_ubuntu2.png)

## Update WSL to WSL2
To use FEniCS on Jupyter Notebook we need a newer version of WSL.
To update it, download file on [this link](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi) and install.
Then open Windows PowerShell and run the following commands:
```
wsl --set-default-version 2
wsl --set-version Ubuntu-20.04 2
wsl -l -v
```
Then you should see the output below:
```
NAME STATE VERSION
* Ubuntu -20.04 Running 2
```


