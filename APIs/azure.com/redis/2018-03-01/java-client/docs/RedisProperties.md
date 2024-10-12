

# RedisProperties

Properties of the redis cache.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessKeys** | [**RedisAccessKeys**](RedisAccessKeys.md) |  |  [optional] |
|**hostName** | **String** | Redis host name. |  [optional] [readonly] |
|**linkedServers** | [**List&lt;RedisLinkedServer&gt;**](RedisLinkedServer.md) | List of the linked servers associated with the cache |  [optional] [readonly] |
|**port** | **Integer** | Redis non-SSL port. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Redis instance provisioning status. |  [optional] [readonly] |
|**redisVersion** | **String** | Redis version. |  [optional] [readonly] |
|**sslPort** | **Integer** | Redis SSL port. |  [optional] [readonly] |
|**sku** | [**Sku**](Sku.md) |  |  |
|**staticIP** | **String** | Static IP address. Required when deploying a Redis cache inside an existing Azure Virtual Network. |  [optional] |
|**subnetId** | **String** | The full resource ID of a subnet in a virtual network to deploy the Redis cache in. Example format: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1 |  [optional] |
|**enableNonSslPort** | **Boolean** | Specifies whether the non-ssl Redis server port (6379) is enabled. |  [optional] |
|**minimumTlsVersion** | [**MinimumTlsVersionEnum**](#MinimumTlsVersionEnum) | Optional: requires clients to use a specified TLS version (or higher) to connect (e,g, &#39;1.0&#39;, &#39;1.1&#39;, &#39;1.2&#39;) |  [optional] |
|**redisConfiguration** | **Map&lt;String, String&gt;** | All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value etc. |  [optional] |
|**shardCount** | **Integer** | The number of shards to be created on a Premium Cluster Cache. |  [optional] |
|**tenantSettings** | **Map&lt;String, String&gt;** | A dictionary of tenant settings |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| DISABLED | &quot;Disabled&quot; |
| FAILED | &quot;Failed&quot; |
| LINKING | &quot;Linking&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| RECOVERING_SCALE_FAILURE | &quot;RecoveringScaleFailure&quot; |
| SCALING | &quot;Scaling&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| UNLINKING | &quot;Unlinking&quot; |
| UNPROVISIONING | &quot;Unprovisioning&quot; |
| UPDATING | &quot;Updating&quot; |



## Enum: MinimumTlsVersionEnum

| Name | Value |
|---- | -----|
| _0 | &quot;1.0&quot; |
| _1 | &quot;1.1&quot; |
| _2 | &quot;1.2&quot; |



