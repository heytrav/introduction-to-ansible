### Running Ansible


#### Running Ansible

* There are two ways to run ansible: <!-- .element: class="fragment" data-fragment-index="0" -->
  - ad hoc <!-- .element: class="fragment" data-fragment-index="1" -->
    * Run a single task <!-- .element: class="fragment" data-fragment-index="2" -->
    * <!-- .element: class="fragment" data-fragment-index="3" --><code>ansible &lt;pattern&gt; [options]</code>
  - Playbook <!-- .element: class="fragment" data-fragment-index="4" -->
    * Run multiple tasks sequentially <!-- .element: class="fragment" data-fragment-index="5" -->
    * <!-- .element: class="fragment" data-fragment-index="6" --><code>ansible-playbook &lt;pattern&gt; [options]</code>


#### Ad hoc tasks with Ansible

  ansible <pattern> [options]

* <!-- .element: class="fragment" data-fragment-index="0" -->Perform a few _ad hoc_ operations with Ansible 
    * Check connection to server <!-- .element: class="fragment" data-fragment-index="1" -->
    * Install packages <!-- .element: class="fragment" data-fragment-index="2" -->
    * Run system commands <!-- .element: class="fragment" data-fragment-index="3" -->


#### Before we start

In all the following examples, `$WORKDIR` is the path to the
`introduction-to-ansible/sample-code` directory.

    $ echo $WORKDIR
    /home/train/introduction-to-ansible/sample-code


#### Simulating a remote server

![Vagrant-vm](img/one-vagrant-vm.png "Vagrant VM") <!-- .element:  style="height:50%;" -->

* <!-- .element: class="fragment" data-fragment-index="0" -->For demo purposes in this course we will be using [Vagrant](https://www.vagrantup.com/intro/index.html) to simulate remote hosts.
* <!-- .element: class="fragment" data-fragment-index="1" -->Instance(s) use a centos 7 image
<pre class="fragment" data-fragment-index="2"><code data-trim>
    $ cd $WORKDIR/lesson1
    $ vagrant up --provider virtualbox
    .
    
    ==&gt; default: Machine booted and ready!
</code></pre>

If all went well you now have a remote host to manage! <!-- .element: class="fragment" data-fragment-index="3" -->


#### Behind the scenes
  * Create SSH connection to a host or list of hosts (group) in parallel
  * Copy a small blob of executable code to each remote machine
  * Performs task: execute the code; capturing return code and output
  * Removes the blob of code
  * Closes the SSH connection
  * Report back on outcome of task


#### Connecting Ansible to a Host
* Ansible works by creating an SSH connection with remote hosts <!-- .element: class="fragment" data-fragment-index="0" -->
* Need a way to tell Ansible how to connect to our Vagrant VM via SSH <!-- .element: class="fragment" data-fragment-index="1" -->
                                

#### The Inventory File

<div style="width:50%;float:left;"><ul >

        <li class="fragment" data-fragment-index="0">
            A text file in <code>.ini</code> syntax
        </li>
        <li class="fragment" data-fragment-index="1">Identifies hosts for ansible to interact with
            <ul>
                <li>
                    Each host on a separate line
                </li>
            </ul>
        </li>

        <li class="fragment"
            data-fragment-index="2">Provides optional arguments after host
            <ul>
                <li>connection information</li>
                <li>
                    other arbitrary variables for
                    specific host
                </li>
            </ul>
        </li>

    </ul></div>

<div class="fragment" data-fragment-index="1" style="float:left;width:50%;"><pre><code data-trim>
    #sample inventory

    web1.mycompany.com
    web2.mycompany.com
    app1.mycompany.com

    db.mycompany.com
    lb.mycompany.com

    [auckland]
    web1.mycompany.com
    
    [wellington]
    web2.mycompany.com
</code></pre></div>


#### Sample Inventory File                            

```
[web]
web1.mycompany.com ansible_host=152.240.43.12 opt2=arg2
web2.mycompany.com

[db]
db1.mycompany.com

[app]
app1.mycompany.com
app2.mycompany.com

[lb]
loadbalancer.mycompany.com
```

#### Grouping Hosts
<div style="width:50%;float:left;"><ul>

        <li class="fragment" data-fragment-index="0">
            Sections used to organise hosts into
            <em>groups</em>
            <ul>
                <li>functional roles</li>
                <li>separate regions</li>
            </ul>
        </li>
        <li class="fragment" data-fragment-index="1">
            Either group or specific hosts can be used in
            ansible commands
        </li>
      

    </ul></div>
    <div class="fragment" data-fragment-index="0" style="width:50%;float:left">
        <pre><code data-trim>
            # sample inventory
            [web]
            web1.mycompany.com
            web2.mycompany.com

            [app]
            app1.mycompany.com
            app2.mycompany.com

            [wellington]
            web1.mycompany.com
            app1.mycompany.com

            [auckland]
            web2.mycompany.com
            app2.mycompany.com

        </code></pre>
    </div>


#### Our first inventory file

```
cat $WORKDIR/lesson1/ansible/hosts
```

* <!-- .element: class="fragment" data-fragment-index="0" -->Our inventory file specifies single remote host: _myserver_
* To connect to our Vagrant VM we need to set some special connection variables <!-- .element: class="fragment" data-fragment-index="1" -->
    * `ansible_host`
    * `ansible_user`
    * `ansible_port`
    * `ansible_private_key_file`
* Variables specified on same line as host <!-- .element: class="fragment" data-fragment-index="2" -->



##### Exercise: Edit your inventory file to fill in missing connection information

```
$ vagrant ssh-config
Host default
    HostName ???
    User ???
    Port ???
    .
    IdentityFile ???
    .
    
```

Use the values from your host to fill in missing arguments in <code>ansible/hosts</code>


#### Running _ad hoc_ commands with Ansible

```
ansible <host pattern> [OPTIONS]
```

* _host pattern_ can be:
   * the name of a specific host in inventory
   * a <em>group</em> of hosts from the inventory

| Option   | Argument  | Description |
|---- | ----- | ---- |
|-m  | string | module name to execute; default to _command_ module |
| -a | string | arguments to module |
| -i | string | path to inventory file |
| -b |   | Privilege escalation |
| --become-method | string | which become method to use; default is _sudo_ |


##### Exercise: Ping remote host

<!-- .element: class="fragment" data-fragment-index="0" -->[ping](http://docs.ansible.com/ansible/latest/ping_module.html) is an Ansible module that just checks whether or not Ansible can create a SSH sessions with hosts.

<!-- .element: class="fragment" data-fragment-index="1" -->Use the _ping_  module to check if our host accepts SSH connections
<pre class="fragment" data-fragment-index="2"><code
                        data-trim>
$ ansible myserver -i ansible/hosts -m ping
myserver | SUCCESS => {
    "changed": false,
    "ping": "pong"
}</code></pre>
