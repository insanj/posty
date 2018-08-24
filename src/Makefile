SHELL=/bin/bash
ENV=posty
RUN=posty.py

run:
	source activate $(ENV) && python $(RUN) && source deactivate

setup:
	conda env create --file environment.yml

clean:
	conda env remove --name $(ENV) --yes
	conda clean --source-cache --yes

# Testing
test: setup run clean

# Installs Anaconda on Linux (good for Ubuntu Subsystem)
setup-conda:
	wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda-2.3.0-Linux-x86_64.sh
	bash Anaconda-2.3.0-Linux-x86_64.sh
