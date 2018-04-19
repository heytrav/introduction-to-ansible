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
    ansible
    └── group_vars
    <mark  class="fragment" data-fragment-index="5">    ├── web.yml
        └── app
            └── vars.yml</mark>
    </code></pre>


##### Exercise: Create group_vars for our app

* Create a `group_vars` directory and variable file 

<pre style="width:100%;"  class="fragment" data-fragment-index="0"><code data-trim>
    $ mkdir $WORKDIR/lesson2/ansible/group_vars
    $ gedit $WORKDIR/lesson2/ansible/group_vars/web.yml
    </code></pre>
<pre style="width:100%;"  class="fragment" data-fragment-index="1"><code data-trim>
    $ mkdir $WORKDIR/lesson2/ansible/group_vars/web
    $ gedit $WORKDIR/lesson2/ansible/group_vars/web/vars.yml
    </code></pre>
<pre style="width:100%;"  class="fragment" data-fragment-index="2"><code data-trim>
    # variables for "web" group
    ---
    bizz: buzz
</code></pre>


#### Using inventory variables

* Inventory variables available to Ansible throughout playbook run

```html
$ less $WORKDIR/lesson2/ansible/templates/index.html.j2
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
ansible-playbook ansible/playbook.yml
```

* Run the ansible playbook again
* Note behaviour of _Copy up static website html_ task
* Reload [website](http://localhost:8000) when finished


#### hostvars

* Dictionary with variables from each host (including inventory variables) 
* Indexed on hostname from inventory 
  * `hostvars['myserver']['foo'] ==  hostvars.myserver.foo`
* Can be accessed across plays in the same playbook run


#### hostvars
* Have a look at `playbook-localhost.yml`
* Run `playbook.yml` and `playbook-localhost.yml`
<pre ><code data-trim>
$ ansible-playbook ansible/playbook.yml \
      ansible/playbook-localhost.yml
</code></pre>
* Change <code style="color:red;">foo</code> to <code style="color:red;">hostvars.myserver.foo</code> in <code>playbook-localhost.yml</code> and run playbooks


