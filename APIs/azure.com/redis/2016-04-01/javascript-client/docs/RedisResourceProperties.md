# RedisManagementClient.RedisResourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessKeys** | [**RedisAccessKeys**](RedisAccessKeys.md) |  | [optional] 
**hostName** | **String** | Redis host name. | [optional] [readonly] 
**port** | **Number** | Redis non-SSL port. | [optional] [readonly] 
**provisioningState** | **String** | Redis instance provisioning status. | [optional] [readonly] 
**redisVersion** | **String** | Redis version. | [optional] [readonly] 
**sku** | [**Sku**](Sku.md) |  | [optional] 
**sslPort** | **Number** | Redis SSL port. | [optional] [readonly] 
**enableNonSslPort** | **Boolean** | Specifies whether the non-ssl Redis server port (6379) is enabled. | [optional] 
**redisConfiguration** | **{String: String}** | All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value etc. | [optional] 
**shardCount** | **Number** | The number of shards to be created on a Premium Cluster Cache. | [optional] 
**staticIP** | **String** | Static IP address. Required when deploying a Redis cache inside an existing Azure Virtual Network. | [optional] 
**subnetId** | **String** | The full resource ID of a subnet in a virtual network to deploy the Redis cache in. Example format: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1 | [optional] 
**tenantSettings** | **{String: String}** | tenantSettings | [optional] 


