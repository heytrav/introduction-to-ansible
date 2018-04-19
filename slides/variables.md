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
<pre class="fragment" data-fragment-index="0"><code class="ini" data-trim data-noescape>
# assign variable to single host
[web]
web1.mycompany.com <mark>ansible_host=152.240.43.12 opt2=arg2</mark>
web2.mycompany.com
.
</code></pre>
<pre class="fragment" data-fragment-index="1"><code class="ini" data-trim data-noescape>
# assign variable to group of hosts

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
    ansible
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
    $ mkdir $WORKDIR/lesson2/ansible/host_vars
    $ gedit $WORKDIR/lesson2/ansible/host_vars/myserver.yml
</code></pre>
<pre style="width:100%;"  class="fragment" data-fragment-index="2"><code data-trim>
    $ mkdir $WORKDIR/lesson2/ansible/host_vars/myserver
    $ gedit $WORKDIR/lesson2/ansible/host_vars/myserver/vars.yml
</code></pre>
<pre style="width:100%;"  class="fragment" data-fragment-index="3"><code data-trim>
    # variables for myserver
    ---
    foo: bar
</code></pre>


