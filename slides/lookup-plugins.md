### Lookup Plugins


#### Lookup Plugins
* The way Ansible accesses data from:
   * data structures like lists, dictionaries
   * Outside sources
       * files 
          * text
          * csv
       * data stores: etcd, consul, redis
       * environment variables


#### Using lookup plugins
* Executed in Jinja2 template expressions <!-- .element: class="fragment" data-fragment-index="0" -->
   * <code style="font-size:16pt;">some_var: "{{ lookup('&lt;plugin name&gt;', '&lt;plugin argument&gt;') }}"</code>
* Evaluated on the control machine <!-- .element: class="fragment" data-fragment-index="1" -->



#### Lookup Plugin Examples
* Return a list <!-- .element: class="fragment" data-fragment-index="0" -->
   ```
   letters: "{{ lookup('items', ['a', 'b', 'c', 'd']) }}"
   ```
* Return a dictionary <!-- .element: class="fragment" data-fragment-index="1" -->
   ```
   simple_dict: "{{ lookup('dict', {a: 'one', b: 'two' }) }}"
   ```
* Read a file from the file system <!-- .element: class="fragment" data-fragment-index="2" -->
   ```
   file_content: "{{ lookup('file', '/etc/myapp/config') }}"
   ```
* Get output of a command <!-- .element: class="fragment" data-fragment-index="3" -->
   ```
   code_version: "{{ lookup('lines', 'git rev-parse --short HEAD') }}"
   ```


#### Dealing with data formats
* Sometimes you need find data in different formats or data stores <!-- .element: class="fragment" data-fragment-index="0" -->
* For example, the <!-- .element: class="fragment" data-fragment-index="1" -->_csvfile_ lookup can grab data from a TSV or CSV file
* <!-- .element: class="fragment" data-fragment-index="2" -->`data.csv` contains the periodic table with elements listed by atomic number
* We can use the <!-- .element: class="fragment" data-fragment-index="3" -->_csvfile_ lookup to read items out

<pre class="fragment" data-fragment-index="3"><code data-trim>
    atomic_mass: "{{ lookup('csvfile', '3 file=../data.csv delimiter=, col=3') }}"
</code></pre>


#### Run playbook example
* The playbook `playbook-lookup.yml` contains examples from previous slide
* Run this playbook to see the results


#### Available Lookups

* List available lookups on your machine
   ```
   ansible-doc -t lookup -l
   ```
* Have a look at the [official documentation page](https://docs.ansible.com/ansible/latest/plugins/lookup.html)


##### Exercise: Use lookup(s) to extract a file
* It is often necessary to upload your SSH public key to a host
* Use lookups to extract `~/.ssh/id_rsa.pub` into a file
* To do this you might need to use a couple lookups <!-- .element: class="fragment" data-fragment-index="0" -->
<pre class="fragment" data-fragment-index="0"><code data-trim>
  vars:
     .
    ssh_public_key_file: "{{ lookup('env', 'HOME') }}/.ssh/id_rsa.pub"
    ssh_public_key: "{{ lookup('file', ssh_public_key_file) }}"

  tasks:
    .
    - debug:
        var: ssh_public_key
</code></pre>



##### Exercise: Find your IP address
* Use a lookup to get your current IP address
* The <!-- .element: class="fragment" data-fragment-index="0" -->_dig_ lookup

<pre class="fragment" data-fragment-index="0"><code data-trim>
  vars:
     .
    ssh_remote_cidr: "{{ lookup('dig', 'myip.opendns.com', '@resolver1.opendns.com') + '/32' | default('0.0.0.0/0', true) }}"

  tasks:
     .
    - debug:
        var: ssh_remote_cidr
</code></pre>


#### Lookups and loops
* We have actually already seen lookups in action <!-- .element: class="fragment" data-fragment-index="0" -->
* Expressed as  <!-- .element: class="fragment" data-fragment-index="1" --><code>with\_</code><code style="color:red;">&lt;plugin name&gt;</code> they form the basis of loops in Ansible
   * <!-- .element: class="fragment" data-fragment-index="2" --><code>with\_</code><code style="color:red;">items</code> - loop over list
   * <!-- .element: class="fragment" data-fragment-index="3" --><code>with\_</code><code style="color:red;">dict</code> - loop through dictionary
   * <!-- .element: class="fragment" data-fragment-index="4" --><code>with\_</code><code style="color:red;">file</code> - loop over files (_item_ contains file contents)


##### Exercise: Use looping lookups
* Use a lookup to list all files in a folder 
* Can be done with the <!-- .element: class="fragment" data-fragment-index="0" -->`fileglob` lookup

<pre class="fragment" data-fragment-index="0"><code data-trim>
  tasks:
    - debug:
        var: item | string
      with_fileglob: 
        - '/var/log/*.log'
</code></pre>


#### Summary
* _lookup_ plugins are a way for Ansible to access different types of data
* They can access data in the play as well as external sources
* Many exist as looping directives when combined with `with_`
