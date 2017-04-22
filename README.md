# python-data

## Requirements
* [Install Miniconda](http://conda.pydata.org/docs/install/quick.html)
* Install Docker

## Setup Conda Environment
<pre># Create a conda env from yml file
conda env create -f conda-env.yml

# activate env
source activate python-data-env

# list all packages
conda list

# update conda env after installing new libs
conda env export --file conda-env.yml
</pre>

### Setup Conda inside PyCharm
Another way is to setup the env with PyCharm in Preferences -> Project -> Interpreter
