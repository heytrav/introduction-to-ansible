### Filters


#### Filters
```
cd $WORKDIR/filters
.
├── ansible.cfg
├── data.csv
├── hosts
├── playbook-formatting.yml
├── playbook-list.yml
├── playbook-lookup.yml
└── undefined.yml
```


#### Filters
* A subset of functionality provided by Jinja2
* Toolset for
   * formatting data
   * iteration
   * filtering


#### Using filters

* Filter syntax:
   * <!-- .element: class="fragment" data-fragment-index="0" --><code style="color:blue;">variable</code><code style="color:red;"> | </code><code style="color:blue;">filtername</code>
   *  <!-- .element: class="fragment" data-fragment-index="1" --><code>variable</code> contains data of some kind 
   *  <!-- .element: class="fragment" data-fragment-index="2" -->The "<code>|</code>" is the <em>pipe</em> symbol 
* Filters will <!-- .element: class="fragment" data-fragment-index="3" -->_usually_ be used within Jinja2 expression syntax
   *  <!-- .element: class="fragment" data-fragment-index="4" --><code style="color:green;">{{</code><code style="color:blue;">  data </code><code> | </code><code style="color:blue;">filter</code><code style="color:green;"> }}</code> 



#### Formatting data
##### `to_yaml` & `to_json`

* Output data in <!-- .element: class="fragment" data-fragment-index="0" -->_yaml_ or _json_ format respectively
* Can be used to generate config files that are consumed by applications <!-- .element: class="fragment" data-fragment-index="1" -->
* Variants for making output <!-- .element: class="fragment" data-fragment-index="2" -->_prettier_
   * <!-- .element: class="fragment" data-fragment-index="3" -->`to_nice_yaml`
   * <!-- .element: class="fragment" data-fragment-index="4" -->`to_nice_json`


##### Exercise: Output myfirstapp as a yaml formatted file
* Add the following task to <!-- .element: class="fragment" data-fragment-index="0" -->`playbook-formatting.yml`
   <pre class="fragment" data-fragment-index="1"><code data-trim>
        - name: Output myfirstapp as yaml config
          copy:
            dest: /home/train/myfirstapp.yml
            content: "{{ myfirstapp | to_nice_yaml  }}"
            owner: train
            group: train
            mode: 0644
    </code></pre>
* Run the playbook <!-- .element: class="fragment" data-fragment-index="2" -->
   ```
   ansible-playbook playbook-formatting.yml
   ```
* Extra credit: use <!-- .element: class="fragment" data-fragment-index="3" -->`to_nice_yaml` and adjust indentation



#### Filtering on defined
* There are different ways to deal with undefined variables
* Force failure
   * <code>{{ variable | </code><code style="color:red;">mandatory</code><code> }}</code>
* Provide a default
   * <code>{{ variable | </code><code style="color:green;">default('ok')</code><code> }}</code>


#### The `mandatory` filter

* Run <!-- .element: class="fragment" data-fragment-index="0" -->`undefined.yml`
* The mandatory filter causes the playbook to terminate at start when it attempts to access the variable <!-- .element: class="fragment" data-fragment-index="1" -->
* Run a second time, but pass a value to <!-- .element: class="fragment" data-fragment-index="2" -->_someport_ using an extra variable
* Using <!-- .element: class="fragment" data-fragment-index="3" -->`mandatory` filter not strictly necessary because Ansible will crash anyway if it encounters an undefined variable 



#### Setting default values
* Note value of <!-- .element: class="fragment" data-fragment-index="0" -->`db_port` in playbook output 
   ```
   TASK [Output value of a variable that hasn't been defined] ****
   ok: [localhost] => {
       "db_port": "3306"
   }
   ```
* The <!-- .element: class="fragment" data-fragment-index="1" -->`default` filter can be used to set default value for an undefined variable
* This is a better approach to handling undefined variables than <!-- .element: class="fragment" data-fragment-index="2" -->`mandatory` (IMHO)
* Run playbook with <!-- .element: class="fragment" data-fragment-index="3" -->`-e someport2=5432` as an extra variable



#### Filtering Data Structures
* There are a plethora of filters for processing data structures
    * Sorting
    * Shuffling
    * Slicing
    * Set theory operations
* Filters can be chained for processing complex structures
   ```
   myvar: {{ data | filter1 | filter2 | filter3 .. }}
   ```



#### Processing lists

* The <!-- .element: style="stretch" -->`map` filter is useful for processing lists
* Useful when chained to to other filters
* In `playbook-list.yml` add the following
   <pre style="font-size:12pt;"><code data-trim>
  security_group_names: "{{ security_groups | map(attribute='name') | unique | list }}"
  </code></pre>


#### Extracting from containers
* `map` can extract data from dictionaries
   * <code style="font-size:18pt;">{{ [0,2] | map('extract', list1) | list }}</code>
   * <code style="font-size:18pt;"e>{{ ['day', 'year'] | map('extract', dict1) | list }}</code>
* Add these to the vars section and add debug tasks to display them



#### Processing IP Addresses

* The <!-- .element: class="fragment" data-fragment-index="0" -->`ipaddr` filter can be used to test vailidity of IP addresses
   * <!-- .element: class="fragment" data-fragment-index="1" --><code>'192.168.1.1' | ipaddr</code><code class="fragment" data-fragment-index="2" style="color:green"> => '192.168.1.1'</code>
   * <!-- .element: class="fragment" data-fragment-index="3" --><code>'192.168.25.1.25' | ipaddr</code><code class="fragment" data-fragment-index="4" style="color:red"> => false</code>
* <!-- .element: class="fragment" data-fragment-index="5" -->`ipaddr` can also extract IP address from CIDR notation
   * <code style="font-size:20pt;">'10.14.33.0/24' | ipaddr('address')</code><code class="fragment" data-fragment-index="6" style="color:green;"> => '10.14.33.0</code>


#### Processing IP Addresses

* <!-- .element: class="fragment" data-fragment-index="0" -->`ipv4` and `ipv6` validate specific IP v4 and v6, respectively
   * <code>myipv4 | ipv4</code>
   * <code>myipv6 | ipv6</code>


#### Processing Filesystem Paths
* The `basename` filter extracts the base file name frm a path
   * `'/home/train/somefile.txt' | basename` 
   * returns `somefile.txt`
* Alternatively, extract the directory path with `dirname`
   * `'/home/train/somefile.txt' | dirname`
   * returns `/home/train`


#### Set theory tools

* Ansible provides a few useful filters for working with sets of data
* union
  - union of two lists
* intersect
  - unique list of items in two lists
* difference
  - list of items in list 1 but not in list 2


#### Using set theory filters

* Have a look at `set-filters.yml`
* Demonstrates a few simple set operations
* Run the playbook

  ```
  $ ansible-playbook set-filters.yml
  ```


#### Union

Combination of items in two sets

![union](img/union.svg "Union") <!-- .element: width="20%" height="20%" -->

All items in<!-- .element: class="fragment" data-fragment-index="0" --> _list1_ and _list2_ 

<pre  class="fragment" data-fragment-index="0"><code data-trim data-noescape>
all_items: "{{ list1 | <mark>union(list2)</mark> }}"
# apple,banana,orange,strawberry,peach,...
</code></pre>


#### Intersection

Items that are in first *and* second list

![Intersect](img/intersect.svg "Intersection") <!-- .element: width="20%"
height="20%" -->

Items that are in both <!-- .element: class="fragment" data-fragment-index="0" --> _list1_ and  _list2_

<pre  class="fragment" data-fragment-index="0"><code data-trim data-noescape>
intersect_lists "{{ list1 | <mark>intersect(list2)</mark> }}"
# apple, strawberry
</code></pre>


#### Difference

Items that are in first set **but not** second set

![Difference](img/difference.svg "Difference")<!-- .element: width="20%"
height="20%" -->

Items that are in e<!-- .element: class="fragment" data-fragment-index="0" --> _list1_ **but not in  _list2_**

<pre  class="fragment" data-fragment-index="0"><code data-trim data-noescape>
difference_list: "{{ list1 | <mark>difference(list2)</mark> }}"
# banana, orange, lime
</code></pre>



#### Summary
* Ansible/Jinja2 provide a lot of filters for
  * Processing string/text data
  * Processing complex data
* [Official Documentation](https://docs.ansible.com/ansible/latest/playbooks_filters.html)

