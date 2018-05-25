### Provisioning Machines
#### Bonus section


#### Provisioning Machines

```
$ cd $WORKDIR/cloud-provisioning
$ tree
.
├── ansible
.
.
├── templates
│   └── index.html
└── wsgi.py
```


#### Provisioning Machines
In this lesson we'll set up a an application in Catalyst Cloud
<dl>
    <dt>App server</dt>
    <dd>Runs a basic Flask (Python) app</dd>
    <dt>DB server</dt>
    <dd>Dedicated postgresql database</dd>
    <dt>Web server</dt>
    <dd>Nginx proxy requests to app server</dd>
</dl>


#### Provisioning machines
* Have a look at `ansible/provision-hosts.yml`
* This playbook does the following:
   * Creates networks/subnets in Catalyst Cloud
   * Create security groups to control access
   * Sets up routers
   * Creates servers
* Run the playbook
   ```
    $ ansible-playbook -i ansible/cloud-hosts \
        ansible/provision-hosts.yml \
        -K -e suffix=-$(hostname)
   ```


##### Exercise: check that hosts are running and reachable
* Use a tool that you have learned about to verify that hosts can be reached
  by SSH
<pre class="fragment" data-fragment-index="0"><code data-trim>
$ ansible -i ansible/cloud-hosts mycluster \
    --ask-vault-pass \
        -m ping
</code></pre>


#### Deploying applications
* `ansible/deploy-app.yml` sets up
   * The database server
      * Installs postgresql
      * Sets up database
   * The application servers
      * Installs Python
      * Sets up framework middleware (gunicorn)
   * The web server
      * Installs nginx
      * Proxy requests to app server


#### Deploy an Application
```
ansible-playbook -i ansible/cloud-hosts \
        ansible/deploy-app.yml --ask-vault-pass
```
* Once deploy is finished visit the new website [website](http://my-app.cat/)


#### Cleaning up
* When you are done playing with cats, please clean up your cluster
```
ansible-playbook \
   -i ansible/cloud-hosts ansible/remove-hosts.yml \
   -K -e suffix=-$(hostname)
```

