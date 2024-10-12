# BigQueryApi.TableReplicationInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicatedSourceLastRefreshTime** | **String** | Optional. Output only. If source is a materialized view, this field signifies the last refresh time of the source. | [optional] [readonly] 
**replicationError** | [**ErrorProto**](ErrorProto.md) |  | [optional] 
**replicationIntervalMs** | **String** | Required. Specifies the interval at which the source table is polled for updates. | [optional] 
**replicationStatus** | **String** | Optional. Output only. Replication status of configured replication. | [optional] [readonly] 
**sourceTable** | [**TableReference**](TableReference.md) |  | [optional] 



## Enum: ReplicationStatusEnum


* `REPLICATION_STATUS_UNSPECIFIED` (value: `"REPLICATION_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `SOURCE_DELETED` (value: `"SOURCE_DELETED"`)

* `PERMISSION_DENIED` (value: `"PERMISSION_DENIED"`)

* `UNSUPPORTED_CONFIGURATION` (value: `"UNSUPPORTED_CONFIGURATION"`)




