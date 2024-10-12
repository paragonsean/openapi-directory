

# RedisProperties

Parameters supplied to CreateOrUpdate Redis operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableNonSslPort** | **Boolean** | If the value is true, then the non-SLL Redis server port (6379) will be enabled. |  [optional] |
|**redisConfiguration** | **Map&lt;String, String&gt;** | All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value etc. |  [optional] |
|**redisVersion** | **String** | RedisVersion parameter has been deprecated. As such, it is no longer necessary to provide this parameter and any value specified is ignored. |  [optional] |
|**shardCount** | **Integer** | The number of shards to be created on a Premium Cluster Cache. |  [optional] |
|**sku** | [**Sku**](Sku.md) |  |  |
|**staticIP** | **String** | Required when deploying a Redis cache inside an existing Azure Virtual Network. |  [optional] |
|**subnet** | **String** | Required when deploying a Redis cache inside an existing Azure Virtual Network. |  [optional] |
|**tenantSettings** | **Map&lt;String, String&gt;** | tenantSettings |  [optional] |
|**virtualNetwork** | **String** | The exact ARM resource ID of the virtual network to deploy the Redis cache in. Example format: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/Microsoft.ClassicNetwork/VirtualNetworks/vnet1 |  [optional] |



