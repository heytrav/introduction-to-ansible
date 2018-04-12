### Types of Automation


#### Types of Automation

* Provisioning <!-- .element: class="fragment" data-fragment-index="0" -->
* Configuration Management <!-- .element: class="fragment" data-fragment-index="1" -->
* Application Deployment <!-- .element: class="fragment" data-fragment-index="2" -->
* Security & compliance <!-- .element: class="fragment" data-fragment-index="3" -->
* Orchestration <!-- .element: class="fragment" data-fragment-index="4" -->


#### Provisioning

* The act of creating a server, network router, loadbalancer, etc. from some type of image
* Can be on bare metal or in cloud hosted virtualisation
* Example: Installation of centos image on a virtual host


#### Provisioning Tools

* Red Hat Kickstart <!-- .element: class="fragment" data-fragment-index="0" -->
* <!-- .element: class="fragment" data-fragment-index="1" -->[FAI](http://fai-project.org/) 
* Debian Preseed <!-- .element: class="fragment" data-fragment-index="2" -->
* Cobbler <!-- .element: class="fragment" data-fragment-index="3" -->
* <!-- .element: class="fragment" data-fragment-index="4" -->[Ansible](https://www.ansible.com) 


#### Configuration Management

* <!-- .element: class="fragment" data-fragment-index="0" -->Often synonomous with _automation_ 
* Determining the state that servers/applications should be in and making sure conditions are met <!-- .element: class="fragment" data-fragment-index="1" -->
* Agentless vs Agents <!-- .element: class="fragment" data-fragment-index="2" -->
* Often declarative syntax with DSL <!-- .element: class="fragment" data-fragment-index="3" -->


#### Configuration Management Tools

* <!-- .element: class="fragment" data-fragment-index="0" -->[Salt](https://saltstack.com) 
* <!-- .element: class="fragment" data-fragment-index="1" -->[Puppet](https://puppetlabs.com) 
* <!-- .element: class="fragment" data-fragment-index="2" -->[Chef](https://www.chef.io) 
* <!-- .element: class="fragment" data-fragment-index="3" -->[Ansible](https://www.ansible.com) 


#### Application Deployment

* Take an artefact of development <!-- .element: class="fragment" data-fragment-index="0" -->
  * Libraries <!-- .element: class="fragment" data-fragment-index="1" -->
  * Executable code <!-- .element: class="fragment" data-fragment-index="2" -->
* Place on platform of choice <!-- .element: class="fragment" data-fragment-index="3" -->
* Make sure it runs <!-- .element: class="fragment" data-fragment-index="4" -->


#### Application Deployment Tools

* <!-- .element: class="fragment" data-fragment-index="0" -->[Fabric](https://www.fabfile.org/)
* <!-- .element: class="fragment" data-fragment-index="1" -->[Capistrano](https://capistranorb.com/)
* <!-- .element: class="fragment" data-fragment-index="2" -->[GoCD](https://thoughtworks.com/go)
* <!-- .element: class="fragment" data-fragment-index="3" -->[Ansible](https://www.ansible.com)


#### Orchestration

* Concerned with automating workflows/processes
* Interconnecting components of an application
  * webservers
  * databases
  * message queues
  * application
* Make sure components function together as a unit


#### Orchestration tools

* [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
* [OpenStack Heat](https://wiki.openstack.org/wiki/Heat)
* [Hashicorp](https://www.terraform.io/)
* [Red Hat CloudForms](https://www.redhat.com/en/technologies/cloud-computing/cloudforms)
* Docker
  * [Kubernetes](https://kubernetes.io)
  * [Swarm](https://docs.docker.com/engine/swarm)
* [Ansible](https://www.ansible.com)


#### Security & Compliance

* Usually driven by some legislative or regulatory law
  * Designed to prevent unwanted disclosure, alteration or destruction of sensitive information
* PCI or government security standard compliance
* Often subject to audit
* Automation removes complexity of managing security in systems


#### Security & Compliance Tools

* Chef Inspec
* Goss (go)
* testinfra (python)
* Ansible


