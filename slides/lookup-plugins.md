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
   items: "{{ lookup('items', ['a', 'b', 'c', 'd']) }}"
   ```
* Return a dictionary <!-- .element: class="fragment" data-fragment-index="1" -->
   ```
   items: "{{ lookup('dict', {'a': 'one', 'b': 'two' }) }}"
   ```
* Read a file from the file system <!-- .element: class="fragment" data-fragment-index="2" -->
   ```
   file_content: "{{ lookup('file', '/etc/myapp/config') }}"
   ```
* Get output of a command <!-- .element: class="fragment" data-fragment-index="3" -->
   ```
   code_version: "{{ lookup('lines', 'git rev-parse --short HEAD') }}"
   ```


#### Lookups and loops
* We have actually already seen lookups in action <!-- .element: class="fragment" data-fragment-index="0" -->
* Combined with  <!-- .element: class="fragment" data-fragment-index="1" -->`with_` they form the basis of loops in Ansible
   * <!-- .element: class="fragment" data-fragment-index="2" --><code>with\_</code><code style="color:red;">items</code> - loop over list
   * <!-- .element: class="fragment" data-fragment-index="3" --><code>with\_</code><code style="color:red;">dict</code> - loop through dictionary
   * <!-- .element: class="fragment" data-fragment-index="4" --><code>with\_</code><code style="color:red;">file</code> - loop over files (_item_ contains file contents)
