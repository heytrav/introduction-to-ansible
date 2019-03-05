### Variables in Ansible


#### Variables in Ansible

* Several different types:
  * Inventory variables
  * Play scoped variables
  * Task variables
  * Extra variables


#### Inventory Variables

* Scoped to a host throughout the execution of a playbook
* Assigned in 
  * The inventory file
  * Specific subdirectories
    * host_vars/_host_
    * group_vars/_group_
* Can be referenced directly when executing play on host
* Available in _hostvars_ dictionary
                            


#### Variables in Inventory File
* Assign variable to a single host <!-- .element: class="fragment" data-fragment-index="0" -->
    <pre style="font-size:10pt;" ><code class="ini" data-trim data-noescape>
[web]
web1.mycompany.com <mark>ansible_host=152.240.43.12 opt2=arg2</mark>
web2.mycompany.com
.
</code></pre>
* Assign variables to groups of hosts <!-- .element: class="fragment" data-fragment-index="1" -->
    <pre style="font-size:12pt;" ><code class="ini" data-trim data-noescape>
[web]
web1.mycompany.com ansible_host=152.240.43.12
web2.mycompany.com
<mark>[web:vars]
proxy=web.mycompany.com
</mark>
</code></pre>


#### Using the host_vars directory

* Ansible will automatically load files under <!-- .element: class="fragment" data-fragment-index="0" -->`host_vars` directory
  * Files with same name as particular host <!-- .element: class="fragment" data-fragment-index="1" -->
  * Any files in a directory with the same name as a host <!-- .element: class="fragment" data-fragment-index="2" -->
    <pre  class="fragment" data-fragment-index="3"><code data-trim data-noescape>
    [web]
    web1.myhost.com
    web2.myhost.com
    </code></pre>
    <pre  class="fragment" data-fragment-index="4"><code data-trim data-noescape>
    $WORKDIR/working-with-playbooks
    └── host_vars
    <mark  class="fragment" data-fragment-index="5">    ├── web1.myhost.com.yml
        └── web2.myhost.com
            └── vars.yml</mark>
    </code></pre>

<!-- .element: class="fragment" data-fragment-index="6" -->_.yml_ or _.yaml_  suffix is optional. Files can also be JSON



##### Exercise: create host inventory

* Create inventory variables for _myserver_ host
* Try either way: <!-- .element: class="fragment" data-fragment-index="0" -->

<pre style="width:100%;"  class="fragment" data-fragment-index="1"><code data-trim>
     cd $WORKDIR/working-with-playbooks
     mkdir -p host_vars
     gedit host_vars/myserver.yml
</code></pre>
<pre style="width:100%;"  class="fragment" data-fragment-index="2"><code data-trim>
     mkdir -p host_vars/myserver
     gedit host_vars/myserver/vars.yml
</code></pre>
<pre style="width:100%;"  class="fragment" data-fragment-index="3"><code data-trim>
    # variables for myserver
    ---
    foo: bar
</code></pre>


#### Using `group_vars`

* Similar to `host_vars` except for groups
  * Files with same name as particular group <!-- .element: class="fragment" data-fragment-index="1" -->
  * Any files in a directory with the same name as a group <!-- .element: class="fragment" data-fragment-index="2" -->
    <pre  class="fragment" data-fragment-index="3"><code data-trim data-noescape>
    [web]
    web1.myhost.com
    [app]
    app1.myhost.com
    </code></pre>
    <pre  class="fragment" data-fragment-index="4"><code data-trim data-noescape>
    $WORKDIR/working-with-playbooks
    └── group_vars
    <mark  class="fragment" data-fragment-index="5">    ├── web.yml
        └── app
            └── vars.yml</mark>
    </code></pre>


##### Exercise: Create group_vars for our app

* Create a `group_vars` directory and variable file 

<pre style="width:100%;"  class="fragment" data-fragment-index="0"><code data-trim>
    cd $WORKDIR/working-with-playbooks/
    mkdir -p group_vars
    gedit group_vars/web.yml
    </code></pre>
<pre style="width:100%;"  class="fragment" data-fragment-index="1"><code data-trim>
    mkdir -p group_vars/web
    gedit group_vars/web/vars.yml
    </code></pre>
<pre style="width:100%;"  class="fragment" data-fragment-index="2"><code data-trim>
    # variables for "web" group
    ---
    bizz: buzz
</code></pre>


#### Using inventory variables

* Inventory variables available to Ansible throughout playbook run

```html
$ less $WORKDIR/working-with-playbooks/templates/index.html.j2
.
.
{% if foo is defined %}
&lt;p&gt;
The value for foo is &lt;em&gt;{{ foo }}&lt;/em&gt;
&lt;/p&gt;
{% endif %}
{% if bizz is defined %}
&lt;p&gt;
The value for bizz is &lt;em&gt;{{ bizz }}&lt;/em&gt;
&lt;/p&gt;
{% endif %}
.
.
```


#### Using Inventory Variables

```
ansible-playbook static-site.yml
```

* Run the ansible playbook again
* Note behaviour of _Copy up static website html_ task
* Reload [website](http://localhost:8000) when finished


#### hostvars

* Dictionary with variables from each host (including inventory variables) 
* Indexed on hostname from inventory 
  * `hostvars['myserver']['foo'] ==  hostvars.myserver.foo` <!-- .element: style="font-size:15pt;"  -->
* Can be accessed across plays in the same playbook run


#### Using `hostvars`
* Have a look at `use-hostvars.yml`
* Run `static-site.yml` and `use-hostvars.yml`
   ```
   ansible-playbook static-site.yml use-hostvars.yml
   ```
* Change <code style="color:red;">foo</code> to <code style="color:red;">hostvars.myserver.foo</code> in <code>playbook-localhost.yml</code> and run playbooks


##### Exercise: View a group variable form hostvars

* The bizz variable still appears as undefined in playbook run
* How would you find that in hostvars?
* A group variable will be defined for every host in a group

```
- name: Output of bizz
  debug:
    var: hostvars.myserver.bizz
```                        
<!-- .element: class="fragment" data-fragment-index="0" -->



#### Play-scoped Variables

* Declared in control section of a play
  * vars - static declaration
  * vars_prompt - interactively prompt user when running playbook
* Can be referenced directly while in play
                            


#### Play-scoped Variables

* Open `static-site.yml` in editor
* Edit as shown: 
* Rerun ansible-playbook 

<pre style="font-size:15pt;"  ><code data-trim data-noescape>
- name: Set up static website with nginx
  hosts: myserver
  become: true
<mark>  vars_prompt:
    - name: "participant_name"
      prompt: "What is your name"
      private: no
  vars:
    base_path: "/"
    course: Introduction to ansible
    lesson:
      name: Working with play variables
      session: 1</mark>
  tasks:
  .
  .
</code></pre>



#### Task Variables
                  
* Contain data discovered while executing a task
* Gathering facts phase of play execution
* Tasks that gather user input
* Become part of the host scope once defined
* In a play they can be directly referenced
* In subsequent plays are available in hostvars dictionary for host
                              


#### Assigning Variables with `set_fact`

```
tasks:
  - name: Assign an arbitrary variable
    set_fact:
      person_name: Homer Simpson

  - name: Assign dictionary
    set_fact:
      person_details:
        street: 754 Evergreen Terrace
        city: Springfield
        state: ST
```


#### Assigning Variables with `register`

```
- name: Execute code and capture the output
  command: uptime
  register: uptime_output

  .
  .
- name: do something with output of uptime
  debug:
    var: {{ uptime_output.stdout }}
```


##### Exercise: Assign Task Variables
<pre class="fragment" data-fragment-index="0"><code data-trim>
    tasks:
        - name: set name of person
          set_fact:
            person_name: Homer Simpson

        - name: Get output of uptime
          command: uptime
          register: uptime_output
        .
        .
</code></pre>

* Use <!-- .element: class="fragment" data-fragment-index="1" -->`set_fact` and `register` in `static-site.yml` to assign task variables
* Rerun ansible playbook <!-- .element: class="fragment" data-fragment-index="2" -->


#### Gathering facts

* Plugin run  before play executes
  * `setup` module
  * Collects detailed information about host and attaches to host scope
  * You can get an idea by running
    *  `ansible myserver -m setup` 
  * Filter facts to find variables you are interested in:
    * <code style="font-size:15pt;"> ansible myserver -m setup -a 'filter=ansible_distribution\*' </code>
                        
                        


##### Exercise: Display System Facts

* Uncomment area in `templates/index.html.j2`
* Re-run ansible-playbook and visit [static website](http://localhost:8080)

```
<!--   remove line
{% if ansible_distribution is defined %}
    <p>  
    System facts: {{ ansible_distribution }} {{ ansible_distribution_major_version }} {{ ansible_architecture }}
    </p>
{% endif %}
-->   remove line
```
<!-- .element: style="font-size:10pt;"  -->
                        


##### Exercise: Turn off fact gathering
* Edit `static-site.yml` as follows
* Re-run ansible-playbook and visit [static website](http://localhost:8080)

<pre><code data-trim data-noescape>
    - name: Set up static website with nginx
      hosts: myserver
      become: true
      <mark>gather_facts: false</mark>
      tasks:
        .
        .
</code></pre>


#### Extra Variables

* Variables passed to ansible or ansible-playbook via command line <!-- .element: class="fragment" data-fragment-index="0" -->
  * <!-- .element: class="fragment" data-fragment-index="1" --><code style="font-size:15pt;">ansible-playbook --extra-vars="key1=value1 key2=value2" playbook.yml</code>
  *  <!-- .element: class="fragment" data-fragment-index="2" --><code style="font-size:15pt;">ansible-playbook -e key1=value1 -e key2=value2 playbook.yml</code>
  * <!-- .element: class="fragment" data-fragment-index="3" --><code style="font-size:15pt;">ansible-playbook -e @extra-variables.yml playbook.yml</code>

                        


#### Variable Precedence

*  Ansible variables in order of increasing precedence:
  * inventory file
  * host facts
  * play vars_files
  * task vars
  * include_vars
  * set_facts/registered variables
  * extra vars
* <!-- .element: class="fragment" data-fragment-index="0" -->[complete list](https://docs.ansible.com/ansible/latest/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
                        


##### Exercise: Variable Precedence

* Pass _extra variables_ to ansible playbook to override previous examples
* For example you can create a new file called <!-- .element: class="fragment" data-fragment-index="1" -->`override-vars.yml`
   <pre  class="fragment" data-fragment-index="1"><code data-trim data-noescape>
     person_name: Marge Simpson
     lesson:
       name: Override variables
       session: 2
</code></pre>
* <!-- .element: class="fragment" data-fragment-index="2" -->Then add this on the command line 
   ```
   ansible-playbook static-site.yml -e @override-vars.yml
   ```


#### Summary

* There are several types of variables in Ansible
  * inventory
  * play scoped
  * task variables
  * extra 

                        
