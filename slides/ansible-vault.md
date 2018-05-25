### Protecting Secrets in Ansible


#### Protecting Secrets in Ansible

* There is one big problem with <!-- .element: class="fragment" data-fragment-index="0" -->`playbook-dict.yml`
* The database password is in plain text in playbook <!-- .element: class="fragment" data-fragment-index="1" -->
* Ansible provides a tool for managing secrets <!-- .element: class="fragment" data-fragment-index="2" -->
* <!-- .element: class="fragment" data-fragment-index="3" -->`ansible-vault` helps you encrypt/decrypt files containing secrets for your app

<pre class="fragment" data-fragment-index="4"><code data-trim>
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
   $ gedit $WORKDIR/working-with-playbooks/ansible/secrets.yml
     ---
     vault_staging_database_password: <some password>
     vault_production_database_password: <some password>
   ```
* Encrypt `ansible/secrets.yml`
   ```
   $ ansible-vault encrypt ansible/secrets.yml
   New Vault password: 
   Confirm New Vault password: 
   Encryption successful

   ```
   * Make sure you can remember your password!



#### Integrating vaulted secrets
* Import `secrets.yml` using `vars_files`
   ```
   vars_files:
     - secrets.yml
   ```
* Replace references to staging/production database passwords
   ```
   database:
     staging:
       password: "{{ vault_staging_database_password }}"
     production:
       password: "{{ vault_production_database_password }}"
   ```
* Run playbook using <code style="color:red;">--ask-vault-pass</code> flag



#### vault password file
* Typing the vault password all the time is annoying <!-- .element: class="fragment" data-fragment-index="0" -->
* You can put your vault password in a file and reference it a CLI option <!-- .element: class="fragment" data-fragment-index="1" -->
   * `--vault-password-file path/to/password/file`
* By convention this file is called <!-- .element: class="fragment" data-fragment-index="2" -->`.vault_password`
   ```
   echo "mysecretpassword" > ansible/.vault_password
   ```
* Be sure you add this file to <!-- .element: class="fragment" data-fragment-index="3" -->`.gitignore`!!!



#### An even lazier way
* It is possible to configure location of vault password file in `ansible.cfg`
   ```
   [defaults]
   vault_password_file = ansible/.vault_password
   ```
* Unnecessary to type `--vault-password-file blah/blah/blah` on command line


#### Summary
* `ansible-vault` is a way to secrets safe
   * passwords
   * API keys
   * SSL keys
* Easy to distribute encrypted secrets with code without compromising them
* Automatically integrates into automation tasks
