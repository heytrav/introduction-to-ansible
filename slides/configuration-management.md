### Multi-tasking with Ansible


#### Ansible Playbook

* Run sequences of tasks
* Primary means of:
  * Configuration management
  * Deploying applications
  * Provisioning 
  * Orchestration


#### Ansible Playbooks

```
cd $WORKDIR/lesson2
.
├── ansible
│   ├── files
│   │   └── nginx.conf
│   ├── hosts
│   ├── playbook.yml
│   └── templates
│       └── index.html.j2
└── ansible.cfg
```

| Name  | Type  | Description |
|--- | ---- |   ----- |
| playbook.yml | file  | Ansible playbook |
| files        | directory | Artefacts to be placed on remote host |
| templates    | directory | Templates that will be rendered and uploaded to remote host |



#### Create a new VM

```
vagrant up --provider virtualbox
```

* This creates a new VM with additional ports for a static website
  * 80 (HTTP)
  * 443 (HTTPS)


#### Deploy and configure an application

![install](img/ansible-nginx-install.svg "Ansible Install nginx")
* Install nginx package
* Copy our nginx config (`files/nginx.conf`)
* Render template file (<code>templates/index.html.j2</code>) and place it on host
* Re/Start nginx


#### Ansible Playbook Structure
<div style="width:50%;float:left;">
    <img src="img/playbook-anatomy.svg"/>
</div>

<div style="width:50%;float:left;">
<ul>
<li class="fragment" data-fragment-index="0">
    A playbook is a YAML file containing a list of
    <em>plays</em>
</li>
<li class="fragment" data-fragment-index="1">
    A play is a dictionary object

    <ul><li>
            <code style="color:red;">key</code><code>: </code><code style="color:blue;">value</code>
        </li></ul>
</li>
<li class="fragment" data-fragment-index="2">
    Some keys in a play may contain dictionaries or
    lists
</li>
</ul>
</div>


#### Ansible Playbook Structure

                            
* A play must contain:
   * `hosts`
     * A string representing a particular host or _group_ of hosts
       * `hosts: localhost`
       * `hosts: app.mywebsite.com`
       * `hosts: appserver`
     * These are what you will configure



#### Ansible Playbook Structure

* A play may optionally contain:
   * tasks
     * A list of dictionaries
     * What you want to do
   * name
     * Description of the play
   * vars
     * Variables scoped to the play


#### Privilege Escalation

<pre style="font-size:18pt;"><code data-trim data-noescape>
    - name: Set up static website with nginx
      hosts: myserver
      <mark >become: true</mark>
      tasks:
</code></pre>

* The _become_ attribute tells Ansible to run tasks as a certain user
  * By default this is _sudo_
  * Specify user with `become_user`
* Can be in _play_ or _task_ scope
* Accepts  _yes_ or _true_ (_no_ or _false_ are implicit)


#### Structure of a Task

* A task is a dictionary object containing
  * name 
    * Describes what the task does
    * Optional but best practice to use
  * module
    * Dictionary object
    * Key represents Python module which will perform tasks
    * May have arguments


#### Structure of a Task
<div style="width:50%;float:left;">
    <img src="img/playbook-task-anatomy.svg"/>
</div>
<div style="width:50%;float:left;">
    <ul>
        <li>
            Two styles of module object in tasks
            <ul>
                <li>string form</li>
                <li>dictionary form</li>
            </ul>
        </li>
        <li>
            Dictionary form is more suitable for complex arguments
        </li>
        <li>
            Matter of preference/style
        </li>
    </ul>
</div>


#### Run our first playbook

```
cd $WORKDIR/lesson2
ansible-playbook ansible/playbook.yml
```

<asciinema-player  autoplay="0"  loop="loop" font-size="medium" speed="1"
     theme="solarized-light" src="lib/basic-static-site.json" cols="200" rows="15"></asciinema-player>

Visit the <!-- .element: class="fragment" data-fragment-index="0" -->[static site](http://localhost:8080) once playbook has finished.



#### Ansible Abstraction Layer
* Some automation tools abstract common functions from different operating systems
   + `apt` on debian/ubuntu and `yum` on centos => `package`
* Ansible has a _thin_ abstraction layer
   + On Debian/Ubuntu use _apt_ module
   + On Centos use _yum_ module 


#### Idempotent 
* Denoting an element of a set which is unchanged in value when multiplied or otherwise operated on by itself.
* If we perform the same task multiple times should have the same effect as
  running it once
* Eg. If we repeatedly write to a config file, it should change only once



#### Task Results and Idempotency
* Most Ansible modules aim to be _idempotent_
* Output of each task indicates when target action resulted in a change
   + `ok` <!-- .element: style="color:green;"  -->
   + `changed` <!-- .element: style="color:orange;"  -->
   + `failed` <!-- .element: style="color:red;"  -->



#### Summary

* Use Ansible Playbook to run complex tasks
* Playbook consists of array of YAML dictionaries called <em>plays</em>
* Each play contains array of tasks that are executed on remote host
