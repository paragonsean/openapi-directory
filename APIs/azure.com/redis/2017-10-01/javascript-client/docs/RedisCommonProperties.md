# RedisManagementClient.RedisCommonProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableNonSslPort** | **Boolean** | Specifies whether the non-ssl Redis server port (6379) is enabled. | [optional] 
**redisConfiguration** | **{String: String}** | All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value etc. | [optional] 
**shardCount** | **Number** | The number of shards to be created on a Premium Cluster Cache. | [optional] 
**tenantSettings** | **{String: String}** | A dictionary of tenant settings | [optional] 


