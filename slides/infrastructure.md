### Infrastructure As Code


#### Immutable Infrastructure
* Approach to managing services where systems are replaced rather than changed in any way
* Entire stack rebuilt from scratch
   * Servers
   * Network infrastructure
* Ensures reliable and predictable deployments by avoiding
   * Configuration drift
   * Snowflake machines
* Relies on _on demand_ availability of servers


#### Buzzwords!
* [Cattle vs. Pets](https://blog.engineyard.com/2014/pets-vs-cattle)
* [Snow Flake](http://martinfowler.com/bliki/SnowflakeServer.html)
* [Phoenix Servers](http://martinfowler.com/bliki/PhoenixServer.html)



#### Blue green deployments

![Blue green](img/blue_green_deployments.png "Blue Green")
