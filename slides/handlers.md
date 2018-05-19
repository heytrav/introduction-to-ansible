### Orchestration



#### Orchestration
* An application may need to interact with multiple services or other app
  components <!-- .element: class="fragment" data-fragment-index="0" -->
* Ansible provides tools to manage services when deploying or updating <!-- .element: class="fragment" data-fragment-index="1" -->
   + After code is deployed <!-- .element: class="fragment" data-fragment-index="2" -->
   + When a configuration is created or updated <!-- .element: class="fragment" data-fragment-index="3" -->
   + When another service is activated/deactivated <!-- .element: class="fragment" data-fragment-index="4" -->



#### Create a Cluster

```
cd $WORKDIR/sample-code/handlers
vagrant up
```
This sets up a cluster in vagrant consisting of 3 separate hosts <!-- .element: class="fragment" data-fragment-index="0" -->


#### Setup Machines
* Initially need to install Python so that Ansible can interact <!-- .element: class="fragment" data-fragment-index="0" -->
   + <!-- .element: class="fragment" data-fragment-index="1" -->`provision-hosts.yml`
* Next we set up each host for its assigned role <!-- .element: class="fragment" data-fragment-index="2" -->
   + deploy.yml<!-- .element: class="fragment" data-fragment-index="3" -->
      + web server running nginx <!-- .element: class="fragment" data-fragment-index="4" -->
      + app server running a basic Python Flask application <!-- .element: class="fragment" data-fragment-index="5" -->
      + a redis server <!-- .element: class="fragment" data-fragment-index="6" -->



#### Run Setup Playbook
```
ansible-playbook -K --ask-vault-pass \
   ansible/provision-hosts.yml ansible/deploy.yml
```

You can now view your <!-- .element: class="fragment" data-fragment-index="0" -->[website](http://my-counter.testsite:8080) 



#### Repeating Playbook Runs

* Run _just_ the `deploy.yml` playbook a few times
   ```
   ansible-playbook --ask-vault-pass ansible/deploy.yml
   ```
   <!-- .element: style="font-size:13pt;"  -->
* Note that many tasks display no change <!-- .element: class="fragment" data-fragment-index="0" -->(i.e. <code style="color:green;">ok</code>)
<asciinema-player class="fragment" data-fragment-index="1"  autoplay="0"  loop="loop" font-size="medium" speed="1"
     theme="solarized-light" src="lib/idempotent-tasks.json" start-at="15" cols="100" rows="15"></asciinema-player>



#### Repeating Playbook Runs
* Idempotent behaviour does not apply to certain types of tasks, for example:
  + cache updates <!-- .element: class="fragment" data-fragment-index="0" -->
  + restart services <!-- .element: class="fragment" data-fragment-index="1" -->
  + custom tasks <!-- .element: class="fragment" data-fragment-index="1" -->
* These tasks always display <!-- .element: class="fragment" data-fragment-index="2" --><code style="color:orange;">changed</code>



####  Performing One-off tasks
* Often necessary trigger certain actions on service when a config is created or changed
   + start
   + restart
   + reload
* Preferable to (re)start services only when necessary
   + config changed
   + application updated


### Handlers
* <!-- .element: class="fragment" data-fragment-index="0" -->A _handler_ is a task that Ansible will execute only once in a play 
* Handlers are triggered using the <!-- .element: class="fragment" data-fragment-index="1" -->_notify_ keyword
    <pre style="font-size:13pt;"><code data-trim data-noescape>
   tasks:
     - name: Change some config
       template:
         dest: /etc/some/config
         .
       <mark>notify: restart service</mark>
   <div class="fragment" data-fragment-index="2">
   handlers:
     - name: <mark>restart service</mark>
       systemd:
          name: service
          state: restartd
   </div>
   </code></pre>
* Will only execute if task result is <!-- .element: class="fragment" data-fragment-index="3" --><code style="color:orange;">changed</code>
* By default, only executed at the end of playbook run <!-- .element: class="fragment" data-fragment-index="4" -->



#### Using Handlers
* `basic-handler.yml` simulates running basic tasks on our servers
   ```
   ansible-playbook --ask-vault-pass ansible/basic-handler.yml
   ```
* Debug tasks do not result in any changes
* Each play has a task to restart specific services
* Let's modify this to run these as _handlers_



#### Create First Handler
* Create a section called _handler_ and move the _restart nginx_ task into it
   ```
     handlers:
       - name: restart nginx
         systemd:
            name: nginx
            state: restarted
   ```


#### Notifying Handlers

* Set tasks to notify handler when changed
   <pre style="font-size=13pt;"><code data-trim data-noescape>
    - name: Set up nginx task 1
      <mark>notify: restart nginx</mark>
      .
      .
    - name: Set up nginx task 2
      <mark>notify: restart nginx</mark>
      .
      .
    - name: Set up nginx task 3
      <mark>notify: restart nginx</mark>
      .
   </code></pre>
* Re run the playbook
* This time the _restart nginx_ task does not run



#### Triggering a Handler
* Tasks in <!-- .element: class="fragment" data-fragment-index="0" -->`basic-handler.yml` have a special attribute to make Ansible think
  a change has occurred
  <pre><code data-trim data-noescape>
  - name: Set up nginx task 1
    .
    <mark>changed_when: nginx_config_changed | default(false)</mark>
  </code></pre>
* We can pass extra variables to interpret task as changed <!-- .element: class="fragment" data-fragment-index="1" -->
   ```
   ansible-playbook --ask-vault-pass \
     ansible/basic-handler.yml  \
        -e nginx_config_changed=true
   ```


#### Triggering Handlers
* Handlers are only triggered once per play
* Try the preceding exercise again with multiple extra vars
* Handler should only run once



##### Exercise: Setup application for SSL
* Create a directory for our certificate and key

```
    - name: Create directory for ssl certs
      file:
        path: /etc/nginx/ssl
        state: directory
        owner: root
        group: root
        mode: '0755'
```



##### Exercise: Set up application for SSL
* Copy and template in self-signed certificate and key
```
    - name: Add ssl cert for site
      copy:
        dest: /etc/nginx/ssl/site.crt
        src: files/site.crt
        owner: root
        group: root
        mode: '0644'

    - name: Add ssl key for site
      copy:
        dest: /etc/nginx/ssl/site.key
        content: "{{ nginx_key }}"
        owner: root
        group: root
        mode: '0600'
```
<!-- .element: style="font-size:10pt;"  -->



##### Exercise: Set up application for SSL
* Change nginx config to use SSL certificate

```
server {
 listen 443 ssl;
 server_name  {{ domain_name }};
 ssl_certificate /etc/nginx/ssl/site.crt;
 ssl_certificate_key /etc/nginx/ssl/site.key;

 location / {
 include proxy_params;
  proxy_pass http://localhost:5000;
 }
}
```

