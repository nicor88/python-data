# python-data

## Requirements
* [Install Miniconda](http://conda.pydata.org/docs/install/quick.html)


## Conda Environment
<pre># Create a conda env from yml file
conda env create -f conda-env.yml
# activate the env
source activate python-data-env
# update conda env file after installing libs
conda env export --file conda-env.yml
# list all the packages in conda env
conda list
</pre>
### Conda Env in PyCharm
Go to Preferences -> Project -> Interpreter and setup the env path
