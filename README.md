# python-data

## Requirements
* [Install Miniconda](http://conda.pydata.org/docs/install/quick.html)
* Install Docker

## Conda Environment
<pre># create env
conda env create -f conda-env.yml

# activate env
source activate python-data-env

# list all packages
conda list

# update conda env after installing new libs
conda env export --file conda-env.yml
</pre>

### Setup conda inside PyCharm
Another way is to setup the env with PyCharm in Preferences -> Project -> Interpreter
 
