### Provisioning Machines
#### Bonus section


#### Provisioning Machines

```
$ cd $WORKDIR/lesson5
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


#### The Provisioning Playbook
