### Provisioning Machines


#### Provisioning Machines

```
$ cd $INTRO_ANSIBLE_DIR/cloud-provisioning
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


#### Setup
* Need to set up a few things so we can interact with Catalyst Cloud easily
   + *clouds.yaml* file for authenticating with the cloud
   + inventory file with hosts
* Verify that you have files in:
   + `~/.ansible/inventory/cloud-hosts`
   + `~/.config/openstack/clouds.yaml`
* If not, run the setup playbook
   ```
   ansible-playbook  ansible/local-setup.yml
   ```


#### Provisioning machines
* Have a look at `ansible/provision-hosts.yml`
* This playbook does the following:
   * Creates networks/subnets in Catalyst Cloud
   * Create security groups to control access
   * Sets up routers
   * Creates servers
* Run the playbook
   ```
    $ ansible-playbook -K ansible/provision-hosts.yml 
   ```
   <!-- .element: style="font-size:13pt;"  -->

Note: might need to have participants install ansible==2.5.5 and shade==1.28.0
due to problems with openstack modules


##### Exercise: check that hosts are running and reachable
* Use a tool that you have learned about to verify that hosts can be reached
  by SSH
  ```
  $ ansible mycluster -m ping
  ```


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
* Run the deploy playbook
  ```
  ansible-playbook ansible/deploy-app.yml
  ```
* Once deploy is finished visit the new website [website](http://my-app.cat/)


#### Cleaning up
* When you are done playing with cats, please clean up your cluster
  ```
  ansible-playbook -K  ansible/remove-hosts.yml
  ```
  <!-- .element: style="font-size:13pt;"  -->

