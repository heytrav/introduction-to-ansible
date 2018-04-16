### Mult-tasking with Ansible


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
