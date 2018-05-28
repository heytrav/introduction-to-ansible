### First Steps with Ansible


#### Installing Ansible

* Target Ansible version &ge; 2.4.2.0
* [Official Documentation](http://docs.ansible.com/ansible/latest/intro_installation.html)
* Explore a couple approaches using:
  * OS package manager
  * Python package manager (pip)


#### Requirements

* Requires Python 2.6 or 2.7 on the control machine (i.e. your pc)
* Requires Python 2.6 on managed nodes
* Python 3 support is currently a tech preview


#### Ansible in this course

* The following slides describe alternative ways to install Ansible <!-- .element: class="fragment" data-fragment-index="0" -->
* However, Ansible is already installed on your PCs <!-- .element: class="fragment" data-fragment-index="1" -->
* To activate: <!-- .element: class="fragment" data-fragment-index="2" -->
     <pre class="fragment" data-fragment-index="3"><code data-trim>
     $ source ~/catalystcloud-ansible/ansible-venv/bin/activate
     </code></pre>


#### Installing OS package

* Ansible available with OS typically a bit out of date

<asciinema-player autoplay="0"  loop="loop" font-size="medium" speed="1"
                                                                                       theme="solarized-light" src="lib/apt-cache-policy-ansible.json" cols="200" rows="10"></asciinema-player>


#### Python Virtual Environment

* Set up local Python environment
  * virtualenv
  * virtualenvwrapper
* Can have multiple Python versions
* Install Ansible and dependencies


#### Installing requisite OS libraries

```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python-pip python-virtualenv
```


#### Install local Python

```
$ virtualenv ansible-venv
$ source ansible-venv/bin/activate
(ansible-venv) $ pip install -U pip
(ansible-venv) $ pip install ansible
```
* <!-- .element: class="fragment" data-fragment-index="0" -->Create a python virtual environment named <em>ansible-venv</em>
* <!-- .element: class="fragment" data-fragment-index="1" -->Activate ansible-venv as base of Python interpreter
* <!-- .element: class="fragment" data-fragment-index="2" -->Update Python package manager (pip)
* <!-- .element: class="fragment" data-fragment-index="3" -->Use Python package manager to install Ansible


#### Ansible release cycle

* It is worth keeping up to date with Ansible [releases](https://docs.ansible.com/ansible/latest/release_and_maintenance.html)
* Use pip or a PPA to get a recent version
* Ansible is developed and released on a flexible 4 months release cycle
* Ansible supports the two most recent major stable releases
