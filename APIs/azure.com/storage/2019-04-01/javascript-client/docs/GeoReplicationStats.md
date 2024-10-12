# StorageManagementClient.GeoReplicationStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canFailover** | **Boolean** | A boolean flag which indicates whether or not account failover is supported for the account. | [optional] [readonly] 
**lastSyncTime** | **Date** | All primary writes preceding this UTC date/time value are guaranteed to be available for read operations. Primary writes following this point in time may or may not be available for reads. Element may be default value if value of LastSyncTime is not available, this can happen if secondary is offline or we are in bootstrap. | [optional] [readonly] 
**status** | **String** | The status of the secondary location. Possible values are: - Live: Indicates that the secondary location is active and operational. - Bootstrap: Indicates initial synchronization from the primary location to the secondary location is in progress.This typically occurs when replication is first enabled. - Unavailable: Indicates that the secondary location is temporarily unavailable. | [optional] [readonly] 



## Enum: StatusEnum


* `Live` (value: `"Live"`)

* `Bootstrap` (value: `"Bootstrap"`)

* `Unavailable` (value: `"Unavailable"`)




