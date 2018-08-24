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

test: setup run clean

# Platform Commands
# Windows
setup-win:
	rm -f chromedriver
	cp drivers/windows/chromedriver .

test-win: setup-win test

# Linux
setup-linux:
	rm -f chromedriver
	cp drivers/linux/chromedriver .

test-linux: setup-linux test

# Installs Anaconda on Linux (good for Ubuntu Subsystem)
setup-conda:
	wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda-2.3.0-Linux-x86_64.sh
	bash Anaconda-2.3.0-Linux-x86_64.sh
