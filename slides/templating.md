### Templating in Ansible


#### Templating in Ansible

* Sometimes you need dynamic behaviour in plays/tasks
  * File locations
  * Fill in prompted information
  * Secret info (passwords, API keys)
  * Generally sourced from a variable
* Ansible uses a template syntax called Jinja2



#### Jinja2

* Templating language
* Provides tools for 
  * Passing variables
  * Evaluating expressions
  * etc.
* References:
  * [Templating in Ansible](https://docs.ansible.com/ansible/latest/playbooks_templating.html)
  * [Jinja2 official docs](http://jinja.pocoo.org/docs/2.10/templates/)


#### Variables

* Simple variables or expressions
  * <code style="font-size:15pt;">{{ person_name  }}</code> 
  * <code style="font-size:15pt;">{{ 1 + 1 }}</code> 
* Dictionaries
  * <code style="font-size:15pt;">{{ lesson['name'] }}</code>
  * <code style="font-size:15pt;">{{ lesson.name }}</code>
  * <code style="font-size:15pt;">{{ hostvars['myserver'].ansible_distribution }}</code>



##### Exercise: Templating in our playbook

* Edit `vars` section in `static-site.yml` to add:
  * <code style="font-size:15pt;">static_file_directory</code>
  * <code style="font-size:15pt;">nginx_conf_directory</code>

```
vars:
  .
  static_file_directory: /usr/share/nginx/html
  nginx_available_conf: /etc/nginx/sites-available
tasks:
```



##### Exercise: Templating in our playbook

* Use template syntax to replace path for
  * nginx
  * index.html

<pre class="fragment" data-fragment-index="0"><code data-trim>
 - name: Template in nginx config file
   template:
     .
     dest: "{{ nginx_available_conf }}/mysite.conf"
     .

 - name: Copy up static website html
   template:
     .
     dest: "{{ static_file_directory }}/index.html"
     .
</code></pre>

Re-run the ansible playbook <!-- .element: class="fragment" data-fragment-index="1" -->



#### Templates and Quoting

* Be aware that you will often need to put quotes around templated elements
   ```
   dest: "{{ nginx_conf_directory }}/mysite.conf"
   ```
* However sometimes you do not need them
   ```
   command: ls {{ nginx_conf_directory }}
   ```
