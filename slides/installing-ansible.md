### Installing Ansible


#### Installing Ansible

* Target Ansible version &ge; 2.7
* [Official Documentation](http://docs.ansible.com/ansible/latest/intro_installation.html)
* Explore a couple approaches using:
  * OS package manager
  * Python package manager (pip)


#### Requirements

* Ansible &lt; 2.5 require Python 2.7
   * support for Python 3 considered *tech preview*
* Ansible &ge; 2.5 supports Python 2.7 and Python &ge; 3.5


#### Installing OS package

* Ansible available with OS typically a bit out of date

<asciinema-player autoplay="0"  loop="loop" font-size="medium" speed="1"
                                                                                       theme="solarized-light" src="lib/apt-cache-policy-ansible.json" cols="200" rows="10"></asciinema-player>


#### Installing requisite OS libraries

```
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python-pip python-virtualenv
```


#### Python Virtual Environment
* Set up local Python environment
  * virtualenv
  ```
  virtualenv -p /usr/bin/python3 ~/venv
  ```
* Can have multiple Python versions
* Install Ansible and dependencies


#### Install Ansible
* <!-- .element: class="fragment" data-fragment-index="0" -->Create a python virtual environment
* <!-- .element: class="fragment" data-fragment-index="1" -->Activate virtualenv as base of Python interpreter
* <!-- .element: class="fragment" data-fragment-index="2" -->Update Python package manager (pip)
* <!-- .element: class="fragment" data-fragment-index="3" -->Use Python package manager to install Ansible
    ```
    $ source ~/venv/bin/activate
    (venv) $ pip install -U pip
    (venv) $ pip install ansible
    ```


#### Ansible release cycle

* It is worth keeping up to date with Ansible [releases](https://docs.ansible.com/ansible/latest/release_and_maintenance.html)
* Use pip or a PPA to get a recent version
* Ansible is developed and released on a flexible 4 months release cycle
* Ansible supports the two most recent major stable releases
