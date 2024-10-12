

# RedisUpdateProperties

Patchable properties of the redis cache.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sku** | [**Sku**](Sku.md) |  |  [optional] |
|**enableNonSslPort** | **Boolean** | Specifies whether the non-ssl Redis server port (6379) is enabled. |  [optional] |
|**redisConfiguration** | **Map&lt;String, String&gt;** | All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value etc. |  [optional] |
|**shardCount** | **Integer** | The number of shards to be created on a Premium Cluster Cache. |  [optional] |
|**tenantSettings** | **Map&lt;String, String&gt;** | A dictionary of tenant settings |  [optional] |



