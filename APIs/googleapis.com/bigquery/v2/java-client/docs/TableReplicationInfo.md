

# TableReplicationInfo

Replication info of a table created using `AS REPLICA` DDL like: `CREATE MATERIALIZED VIEW mv1 AS REPLICA OF src_mv`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**replicatedSourceLastRefreshTime** | **String** | Optional. Output only. If source is a materialized view, this field signifies the last refresh time of the source. |  [optional] [readonly] |
|**replicationError** | [**ErrorProto**](ErrorProto.md) |  |  [optional] |
|**replicationIntervalMs** | **String** | Required. Specifies the interval at which the source table is polled for updates. |  [optional] |
|**replicationStatus** | [**ReplicationStatusEnum**](#ReplicationStatusEnum) | Optional. Output only. Replication status of configured replication. |  [optional] [readonly] |
|**sourceTable** | [**TableReference**](TableReference.md) |  |  [optional] |



## Enum: ReplicationStatusEnum

| Name | Value |
|---- | -----|
| REPLICATION_STATUS_UNSPECIFIED | &quot;REPLICATION_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| SOURCE_DELETED | &quot;SOURCE_DELETED&quot; |
| PERMISSION_DENIED | &quot;PERMISSION_DENIED&quot; |
| UNSUPPORTED_CONFIGURATION | &quot;UNSUPPORTED_CONFIGURATION&quot; |



