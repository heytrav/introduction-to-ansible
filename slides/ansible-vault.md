### Protecting Secrets in Ansible


#### Protecting Secrets in Ansible

* There is one big problem with <!-- .element: class="fragment" data-fragment-index="0" -->`playbook-dict.yml`
* The database password is in plain text in playbook <!-- .element: class="fragment" data-fragment-index="1" -->
* Ansible provides a tool for managing secrets <!-- .element: class="fragment" data-fragment-index="2" -->
* <!-- .element: class="fragment" data-fragment-index="3" -->`ansible-vault` helps you encrypt/decrypt files containing secrets for your app

<pre class="fragment" data-fragment-index="4" style="font-size:13pt;"><code data-trim>
$ ansible-vault --help

Usage: ansible-vault [create|decrypt|edit|encrypt|encrypt_string|rekey|view] [options] [vaultfile.yml]

encryption/decryption utility for Ansible data files

Options:
--ask-vault-pass      ask for vault password
-h, --help            show this help message and exit
</code></pre>



#### `ansible-vault`

* Uses AES256 encryption
* Secret files can be
   * Loaded automatically as `host_vars` or `group_vars` inventory files
   * Included with `include_vars` or `vars_files` directives
* Encrypted files can be distributed with your application



##### Exercise: Protecting our database passwords
* Create a new file called `secrets.yml`
   ```
   mkdir -p group_vars/web
   vim group_vars/web/secrets.yml
   ```
   ```
   ---
   vault_staging_database_password: <some password>
   vault_production_database_password: <some password>
   ```
   <!-- .element: style="font-size:12pt;"  -->
* Encrypt `group_vars/web/secrets.yml`
   ```
   ansible-vault encrypt group_vars/web/secrets.yml
   New Vault password: 
   Confirm New Vault password: 
   Encryption successful

   ```
   <!-- .element: style="font-size:12pt;"  -->
   * Make sure you can remember your password!



#### Integrating vaulted secrets
* Replace references to staging/production database passwords
   ```
   database:
     staging:
       password: "{{ vault_staging_database_password }}"
     production:
       password: "{{ vault_production_database_password }}"
   ```



#### Running Ansible with vault
* Run playbook using <code style="color:red;">--ask-vault-pass</code> flag
   <pre style="font-size:13pt;"><code data-trim data-noescape>
    ansible-playbook playbook-dict.yml <mark>--ask-vault-pass</mark>
    Vault Password: ******
   </code></pre>



#### vault password file
* Typing the vault password all the time is annoying <!-- .element: class="fragment" data-fragment-index="0" -->
* You can put your vault password in a file <!-- .element: class="fragment" data-fragment-index="1" -->
* By convention this file is called <!-- .element: class="fragment" data-fragment-index="2" -->`.vault_password`
   ```
   echo "mysecretpassword" > .vault_password
   ```
* Then run playbook with argument with <!-- .element: class="fragment" data-fragment-index="3" -->`--vault-password-file`
   <pre style="font-size:11pt;"><code class="shell" data-trim data-noescape>
   ansible-playbook <mark>--vault-password-file .vault_password</mark> playbook-dict.yml
   </code></pre>
* Be sure you add this file to <!-- .element: class="fragment" data-fragment-index="4" -->`.gitignore`!!!



#### An even lazier way
* It is possible to configure location of vault password file in `ansible.cfg`
   ```ini
   [defaults]
   vault_password_file = .vault_password
   ```
* Now no longer need to type `--vault-password-file path` on command line


#### Adding secure content inline
##### `ansible-vault encrypt_string`
* Sometimes useful to add secure content in a playbook inline
* `encrypt_string` generates vaulted output that can be added to a playbook
   ```
   echo "mysecretPas2wurd1" | ansible-vault --ask-vault-pass encrypt_string \
       --stdin-name vault_my_password
    New Vault password:  *******
    Confirm New Vault password: *******
   ```
   <!-- .element: style="font-size:12pt;"  -->
   ```
    vault_my_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          37326562653730353232346530336334346163633964373732653132370a373
          353439303265373737653963396666653638366639633966666536383666583
   ```
   <!-- .element: style="font-size:12pt;"  class="fragment" data-fragment-index="0" -->



#### Summary
* `ansible-vault` is a way to secrets safe
   * passwords
   * API keys
   * SSL keys
* Easy to distribute encrypted secrets with code without compromising them
* Automatically integrates into automation tasks


#### Destroy VM
* We are now done with the VM we've been using
* Before we move on we need to stop the current Vagrant VM

```
vagrant halt
vagrant destroy
```
