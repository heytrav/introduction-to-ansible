### Organising Infrastructure Code
#### Roles


#### Roles

```
$ cd $WORKDIR/ansible-roles
ansible
├── hosts
└── project.yml
```


#### Making tasks reusable

* At some point in your development process, you may come across
  bits that will be useful across multiple projects
* Important to follow _DRY_ (don't repeat yourself) principles in infrastructure code


#### Identify reusable components
* Have a look at `ansible/project.yml`
* Tasks simulate steps involved in setting up an application
   * Installing language libraries
   * Deploying configuration
   * Set up DB
   * Run handlers to start services
* Components could be reused in other projects


#### Roles

* A mechanism for reusing code in Ansible
  - within a project
  - accross multiple projects
* Typically designed for a specific purpose
* Not executable on their own


#### Decomposing playbook into roles
* Let's start decomposing the playbook into reusable components starting with
  app setup
* Create subdirectory in the ansible folder called *roles*
* In that folder create a subdirectory called *setup-app*
   <pre><code data-noescape data-trim>
ansible-roles
└── ansible
    ├── hosts
    ├── project.yml
    <mark>└── roles
        └── setup-app/</mark>
</code></pre>
* To make things easier
   ```
   cd $WORKDIR/ansible-roles/ansible/roles/setup-app
   ```


#### Creating a basic role
* <!-- .element: class="fragment" data-fragment-index="0" -->Add `tasks` and `handlers` subdirectories
   ```
   mkdir -p tasks handlers
   ```
* <!-- .element: class="fragment" data-fragment-index="2" -->Move following tasks from `project.yml` to `roles/setup-app/tasks/main.yml`
   ```
   - name: Update apt cache
     .
   - name: Check out code for project
     .
   - name: Create python virtual environment
     .
   ```


#### Creating a basic role
* <!-- .element: class="fragment" data-fragment-index="0" -->Create a yaml script for handlers
   ```
   gedit handlers/main.yml
   ```
* <!-- .element: class="fragment" data-fragment-index="1" -->Remove app handler from `project.yml` and paste it into `handlers/main.yml`
   ```
   - name: restart app
   ```
* <!-- .element: class="fragment" data-fragment-index="2" -->Run the `project.yml` playbook again. Note missing *setup-app* tasks


#### Integrating role into play
##### The `roles` keyword
* To integrate a role into a project you need to add a new section to your
  play called `roles`
  <pre class="fragment" data-fragment-index="0"><code data-trim data-noescape>
  - name: Set up python application
    hosts: localhost
    vars:
      .
      .
    <mark>roles:</mark>
    <mark class="fragment" data-fragment-index="1">  - role: setup-app</mark>
  </code></pre>  
* <!-- .element: class="fragment" data-fragment-index="2" -->Run `project.yml` again. Note the *setup-app* tasks and handler both run with a new
  label
  <pre><code data-trim data-noescape>
  TASK [<mark>setup-app :</mark> Update apt cache] 
  </code></pre>



#### Structure of a role
  <pre><code data-trim data-noescape>
  /roles              <span class="fragment" data-fragment-index="0"><-- base directory depends on config</span>
    └── role-name     <span class="fragment" data-fragment-index="1"><-- Arbitrary; what you will import in "roles:"</span>
        ├── defaults
        │   └── main.yml
        ├── files
        │   └── someconfig.conf
        ├── handlers
        │   └── main.yml
        ├── meta
        │   └── main.yml
        ├── tasks
        │   └── main.yml
        ├── templates
        │   └── sometemplate.j2
        └── vars
            └── main.yml
  </code></pre>
<!-- .element: style="font-size:13pt;"  -->
  * Each of these files/folders is optional


#### Components of a role

* tasks
  - tasks that the role will perform
* files
  - Files that will be uploaded
* templates
  - Jinja2 templates that the role will use
* handlers
  - Handlers that will be called from tasks



#### Components of a role (continued)

* vars
  - Variables needed by role (shouldn't be overridden)
* defaults
  - Variables that can be overridden
* meta
  - Dependency information


#### File and directory naming conventions

* The naming of components correspond to directories in the role
* Ansible will look in these directories automatically when running a role
* YAML files named `main.yml` will be loaded automatically when role is
  executed
* Nearly all components are optional


#### Typical Use Cases
* Install supporting libraries/software to multiple machines
* Standardise provisioning of machines across vendors
   - AWS
   - Azure
   - OpenStack
* Tasks needed across entire infrastructure
   - Security hardening



#### Where do roles live?
* In order of _decreasing_ precedence
  - Custom location configured in `ansible.cfg`
     ```ini
     [defaults]
     roles_path = ~/ansible_roles
     ```
  - In `roles` subdirectory in the same place your playbooks live
     ```
     ansible/
        \
         --- playbook1.yml
         |
         --- roles/
     ```
  - `$HOME/.ansible/roles`
  - In `/etc/ansible/roles` directory


#### Exercise: Continue Refactoring `project.yml` into roles
* As in previous example, break `project.yml` into roles for 
  - Configuring app
  - Setting up DB
* See if we can break them up into some useful roles


#### Pre and post tasks

* We still need to make sure that the apt modules runs before
  anything else happens
* Changing these into a *pre_task* ensures it will run before the roles do

<pre class="fragment" data-fragment-index="0"><code data-trim data-noescape>
  <mark>pre_tasks:</mark>

    - name: Update apt cache
      become: yes
      apt:
        update_cache: yes
</code></pre>


#### Open source roles

[Ansible Galaxy](https://galaxy.ansible.com)

* A repository of ansible roles
* Thousands of opensource roles for any purpose
* Can be easily imported into your projects


#### Summary

* Roles provide useful way to reuse code accross projects
  - Simple to include
* Designed to facilitate automation
  - Directory structure
  - Naming conventions
* Ansible Galaxy is an Open Source repository of roles available for all
  purposes
