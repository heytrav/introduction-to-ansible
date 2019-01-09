### Iteration and Conditionals


#### Iteration and Conditionals

```
$ cd $WORKDIR/working-with-playbooks
$ tree
.
├── ansible
│   ├── hosts
│   ├── playbook-dict.yml
│   └── playbook-lists.yml
└── ansible.cfg
```


### Iterating through lists


#### Iterating `with_items`

* Step through an array <!-- .element: class="fragment" data-fragment-index="0" -->
* Each element in iteration is assigned to <!-- .element: class="fragment" data-fragment-index="1" -->_item_ variable

<pre class="fragment" data-fragment-index="0"><code data-trim data-noescape>
 vars:
  list_of_files: 
    - file1.txt
    - file2.txt
       .
       .
  tasks:
   - name: Process a list of items        
     copy:                               
       src: "/path/to/local/{{ <mark class="fragment" data-fragment-index="1">item</mark> }}"   
       dest: "/path/to/remote/{{ <mark class="fragment" data-fragment-index="1">item</mark> }}" 
     <mark class="fragment" data-fragment-index="1">with_items: "{{ list_of_files }}"</mark>    
</code></pre>



#### Configuring our fake application _myapp_

* Have a look at <!-- .element: class="fragment" data-fragment-index="0" -->`ansible/playbook-lists.yml`
* Run the playbook and then have a look in <!-- .element: class="fragment" data-fragment-index="1" -->`/etc/myapp/config`
* Playbook adds lines to a configuration file for a fake app <!-- .element: class="fragment" data-fragment-index="2" -->
* There are a number of things we can optimise <!-- .element: class="fragment" data-fragment-index="3" -->



##### Exercise: Remove repetitive *allowed_host* tasks from playbook

* Use `with_items` to refactor tasks
* Replace all allowed host tasks with <!-- .element: class="fragment" data-fragment-index="0" -->
   <pre class="fragment" data-fragment-index="0"><code data-trim>
        - name: Add allowed_hosts entries
          lineinfile:
            path: /etc/myapp/config
            line: "allow_from: {{ item }}"
            insertafter: EOF
          with_items:
            - "{{ allowed_host1 }}"
            - "{{ allowed_host2 }}"
            - "{{ allowed_host3 }}"

  </code></pre>



##### Exercise: Remove repetitive listen tasks from playbook

* Use `with_items` to simply _listen_ tasks
* Replace all the listen tasks with:
   <pre class="fragment" data-fragment-index="0"><code data-trim>
    - name: Add listen port entries
      lineinfile:
        path: /etc/myapp/config
        line: "listen: {{ item }}"
        insertafter: EOF
      with_items: "{{ listen_ports }}"
    </code></pre>



#### Nesting Loops `with_nested`

* It is possible to loop over two lists at once
   ```
   - name: Add allowed ports for each host
     lineinfile:
       path: /etc/myapp/config
       line: "host: {{ item[0] }}:{{ item[1] }}"
       insertafter: EOF
     with_nested:
       - [ "{{ allowed_host1 }}", "{{ allowed_host2 }}", "{{ allowed_host3 }}"]
       - "{{ listen_ports }}"

   ```
   <!-- .element: style="font-size:10pt;"  -->



#### Iterating through dictionaries `with_dict`

* Takes a dictionary argument <!-- .element: class="fragment" data-fragment-index="0" -->
* Each item has <!-- .element: class="fragment" data-fragment-index="1" -->
  * Key <!-- .element: class="fragment" data-fragment-index="2" -->
  * Value <!-- .element: class="fragment" data-fragment-index="3" -->

<pre><code data-trim data-noescape>
- name: Task that iterates over a dictionary
  somemodule:
    arg: <mark class="fragment" data-fragment-index="2">"{{ item.key }}"</mark>
    arg2: <mark class="fragment" data-fragment-index="3">"{{ item.value }}"</mark>
  <mark class="fragment" data-fragment-index="0">with_dict: "{{ dictionary }}"</mark>
</code></pre>



#### More configuration for myapp
 * <!-- .element: class="fragment" data-fragment-index="0" -->`ansible/playbook-dict.yml` sets up database config for our fake application
 * Adds each element of <!-- .element: class="fragment" data-fragment-index="1" -->*database* variable to config
 * Run the playbook and have a look at <!-- .element: class="fragment" data-fragment-index="2" -->`/etc/myapp/app_config`
   ```
   ansible-playbook ansible/playbook-dict.yml
   ```


##### Exercise: Remove repetition from playbook-dict.yml

* Refactor the playbook using `with_dict` to remove repetitive tasks

<pre class="fragment" data-fragment-index="0"><code data-trim>
 - name: Add database config to /etc/myapp/config
   lineinfile:
     path: /etc/myapp/app_config
     line: "database_{{ item.key }}={{ item.value }}"
     regexp: '^database_{{ item.key}}.*'
   with_dict: "{{ database[env_name] }}"
</code></pre>



### Conditionals



#### The `when` clause

* The main way to conditionally do something in Ansible is by using the <!-- .element: class="fragment" data-fragment-index="0" -->`when` clause
* <!-- .element: class="fragment" data-fragment-index="1" -->`when` has identical semantics to a Python _if_ block
   * <!-- .element: class="fragment" data-fragment-index="2" -->`when: some_variable is defined`
   * <!-- .element: class="fragment" data-fragment-index="3" -->`when: env_name == 'staging'`

<pre class="fragment" data-fragment-index="4"><code data-trim data-noescape>
- name: Some task
  command: do something
  <mark>when</mark>: &lt;condition is true&gt;
</code></pre>



##### Exercise: Make our tasks conditional

* Tasks in <!-- .element: class="fragment" data-fragment-index="0" -->`ansible/playbook-dict.yml` assume a _staging_ environment
<pre><code data-trim data-noescape>
  vars:
    .
    <mark>env_name: staging</mark>
</code></pre>
* Add a conditional to  the <!-- .element: class="fragment" data-fragment-index="1" -->`lineinfile` tasks
   + Only execute if <!-- .element: class="fragment" data-fragment-index="2" -->`env_name` is *production*
* Re-run the playbook <!-- .element: class="fragment" data-fragment-index="3" -->

<pre  class="fragment" data-fragment-index="4"><code data-trim>
  - name: Add database config to /etc/myapp/config
    lineinfile:
    .
    .
    when: env_name == 'production'
</code></pre>


##### Exercise: Override default *env_name* to run tasks

* *env_name* is set to _staging_ by default
* Override this to be _production_ and re-run playbook
* Hint: What type of variable has precedence in this situation?

<pre  class="fragment" data-fragment-index="0" style="font-size:12pt;"><code data-trim data-noescape>
ansible-playbook ansible/playbook-dict.yml <mark>-e env_name=production</mark>
</code></pre>
