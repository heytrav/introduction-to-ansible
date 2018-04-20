### Iteration and Conditionals


#### Iteration and Conditionals

```
$ cd $WORKDIR/lesson3
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

* Step through an array
* Each element in iteration is assigned to _item_ variable

```
 vars:
  list_of_files: 
    - file1.txt
    - file2.txt
       .
       .
  tasks:
   - name: Process a list of items        
     copy:                               
       src: "/path/to/local/{{ item }}"   
       dest: "/path/to/remote/{{ item }}" 
     with_items: "{{ list_of_files }}"    
```


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

* It is possible ot loop over two lists at once
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



#### Iterating through dictionaries `with_dict`

* Takes a dictionary argument
* Each item has
  * Key
  * Value

```
- name: Task that iterates over a dictionary
  somemodule:
    arg: "{{ item.key }}"
    arg2: "{{ item.value }}"
  with_dict: "{{ dictionary }}"

```


#### More configuration for myapp
