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



#### Alternate ways to provide vault password
* Typing the vault password all the time is annoying <!-- .element: class="fragment" data-fragment-index="0" -->
* You can put your vault password in a file <!-- .element: class="fragment" data-fragment-index="1" -->
   ```
   echo "mysecretpassword" > .vault_password
   ```
* Then run playbook with argument with <!-- .element: class="fragment" data-fragment-index="3" -->`--vault-id`
   <pre style="font-size:11pt;"><code class="shell" data-trim data-noescape>
   ansible-playbook <mark>--vault-id .vault_password</mark> playbook-dict.yml
   </code></pre>
* Be sure you add this file to <!-- .element: class="fragment" data-fragment-index="4" -->`.gitignore`!!!


#### Managing multiple vault secrets
* As of Ansible 2.4 it is possible to have multiple encryption keys
* <!-- .element: class="fragment" data-fragment-index="0" -->Change directory
   ```
    cd $WORKDIR/vault-management
    tree
    ├── ansible.cfg.example
    ├── group_vars
    │   ├── dev
    │   │   └── dev-secret.yml
    │   └── prod
    │       └── prod-secret.yml
    └── inventory
        └── hosts
   ```
* <!-- .element: class="fragment" data-fragment-index="1" -->We want to encrypt dev and prod secrets separately
  * separate devs from prod secrets



#### Using separate vault passwords
##### prompting for password
* <!-- .element: class="fragment" data-fragment-index="0" -->Encrypt the prod secret
   * <!-- .element: class="fragment" data-fragment-index="1" -->For the prod password, let's tell Ansible to **prompt** for a password
   <pre class="fragment" data-fragment-index="1" style="font-size:13pt;"><code data-noescape>ansible-vault encrypt --encrypt-vault-id prod --vault-id prod@prompt \
           group_vars/prod/prod-secret.yml</code></pre>
   * <!-- .element: class="fragment" data-fragment-index="2" -->Ansible will prompt for new password
   * <!-- .element: class="fragment" data-fragment-index="3" -->Encrypted file contains tag for prod
   <pre><code data-noescape>
    $ANSIBLE_VAULT;1.2;AES256;<mark>prod</mark>
    33633335336634393739363636633039376334303533636336373636663139383837663531353134
    6536396633616636383734656439643334653739346462660a323832643834613636393339346232
   </code></pre>



#### Using separate vault passwords
##### password file
* <!-- .element: class="fragment" data-fragment-index="0" -->Encrypt the dev secret
   * <!-- .element: class="fragment" data-fragment-index="1" -->For the dev password, let's use a password file
   <pre class="fragment" data-fragment-index="1" style="font-size:13pt;"><code data-noescape class="shell">echo "mydevvaultpassword" > dev_vault_password
   ansible-vault encrypt --encrypt-vault-id dev \
       --vault-id dev@dev_vault_password group_vars/dev/dev-secret.yml</code></pre>
   * <!-- .element: class="fragment" data-fragment-index="2" -->Ansible will **not** prompt for a password
   * <!-- .element: class="fragment" data-fragment-index="3" -->Encrypted file contains tag for dev
   <pre><code data-noescape>
    $ANSIBLE_VAULT;1.2;AES256;<mark>dev</mark>
    66313465646336616231323030633961613464613065373138333862303936333266653366366639
    3965323362353061396662623835636138343534363239390a333332316361343737666137396439
   </code></pre>



#### Accessing vaulted files
* <!-- .element: class="fragment stretch" data-fragment-index="0" -->You can now use vault-ids when accessing vaulted files
   ```
   ansible-vault view --vault-id dev@dev_vault_password \
      group_vars/dev/dev-secret.yml
   ```
   ```
   ansible-vault view --vault-id prod@prompt \
      group_vars/prod/prod-secret.yml
   ```
* <!-- .element: class="fragment" data-fragment-index="1" -->Or do all at the same time
   ```
   ansible-vault view --vault-id prod@prompt \
      --vault-id dev@dev_vault_password  \
          group_vars/**/*-secret.yml
   ```
   * Ansible will prompt and use the existing file



#### Using vault-ids with ansible-playbook
* Pass `--vault-id` that is relevant for environment 
   ```
    ansible-playbook playbook-dev.yml -i inventory/hosts \
       --vault-id dev@dev_vault_password
   ```
   <!-- style="font-size:12pt;" --> 
* If play requires multiple vault passwords
   ```
    ansible-playbook -i inventory/hosts  \
        --vault-id dev@dev_vault_password  \ 
        --vault-id prod@prompt \
        playbook-dev.yml playbook-prod.yml
   ```



#### Vault Ids and ansible.cfg
* It is possible to configure location of vault password file in `ansible.cfg`
   ```ini
   [defaults]
   # other config
   # dev_vault_password is in ~/.ansible directory, prod_vault_password in
   # working directory
   vault_identity list = dev@~/.ansible/dev_vault_password, prod@prod_vault_password
   ```


#### Adding secure content inline
##### `ansible-vault encrypt_string`
* Sometimes useful to add secure content in a playbook inline
* `encrypt_string` generates vaulted output that can be added to a playbook
   ```
   echo "mysecretPas2wurd1" | ansible-vault --vault-id @prompt encrypt_string \
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
