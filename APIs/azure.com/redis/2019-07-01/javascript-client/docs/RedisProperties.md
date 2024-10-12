# RedisManagementClient.RedisProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessKeys** | [**RedisAccessKeys**](RedisAccessKeys.md) |  | [optional] 
**hostName** | **String** | Redis host name. | [optional] [readonly] 
**instances** | [**[RedisInstanceDetails]**](RedisInstanceDetails.md) | List of the Redis instances associated with the cache | [optional] [readonly] 
**linkedServers** | [**[RedisLinkedServer]**](RedisLinkedServer.md) | List of the linked servers associated with the cache | [optional] [readonly] 
**port** | **Number** | Redis non-SSL port. | [optional] [readonly] 
**provisioningState** | **String** | Redis instance provisioning status. | [optional] [readonly] 
**redisVersion** | **String** | Redis version. | [optional] [readonly] 
**sslPort** | **Number** | Redis SSL port. | [optional] [readonly] 
**sku** | [**Sku**](Sku.md) |  | 
**staticIP** | **String** | Static IP address. Required when deploying a Redis cache inside an existing Azure Virtual Network. | [optional] 
**subnetId** | **String** | The full resource ID of a subnet in a virtual network to deploy the Redis cache in. Example format: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1 | [optional] 
**enableNonSslPort** | **Boolean** | Specifies whether the non-ssl Redis server port (6379) is enabled. | [optional] 
**minimumTlsVersion** | **String** | Optional: requires clients to use a specified TLS version (or higher) to connect (e,g, &#39;1.0&#39;, &#39;1.1&#39;, &#39;1.2&#39;) | [optional] 
**redisConfiguration** | **{String: String}** | All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value etc. | [optional] 
**replicasPerMaster** | **Number** | The number of replicas to be created per master. | [optional] 
**shardCount** | **Number** | The number of shards to be created on a Premium Cluster Cache. | [optional] 
**tenantSettings** | **{String: String}** | A dictionary of tenant settings | [optional] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Disabled` (value: `"Disabled"`)

* `Failed` (value: `"Failed"`)

* `Linking` (value: `"Linking"`)

* `Provisioning` (value: `"Provisioning"`)

* `RecoveringScaleFailure` (value: `"RecoveringScaleFailure"`)

* `Scaling` (value: `"Scaling"`)

* `Succeeded` (value: `"Succeeded"`)

* `Unlinking` (value: `"Unlinking"`)

* `Unprovisioning` (value: `"Unprovisioning"`)

* `Updating` (value: `"Updating"`)





## Enum: MinimumTlsVersionEnum


* `0` (value: `"1.0"`)

* `1` (value: `"1.1"`)

* `2` (value: `"1.2"`)




