### Handlers



#### Handlers

```
cd $WORKDIR/sample-code/handlers
vagrant up
```


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

