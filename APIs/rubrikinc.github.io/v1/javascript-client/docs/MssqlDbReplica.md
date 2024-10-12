# RubrikRestApi.MssqlDbReplica

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityInfo** | [**MssqlDbReplicaAvailabilityInfo**](MssqlDbReplicaAvailabilityInfo.md) |  | [optional] 
**hasPermissions** | **Boolean** | &#x60;True&#x60; when the Rubrik cluster has sufficient permissions to perform all necessary operations. | 
**instanceId** | **String** | ID of the SQL Server instance managing the replica. | 
**instanceName** | **String** | Name of the SQL Server instance managing the replica. | 
**isArchived** | **Boolean** | Deprecated. Please use &#39;isDeleted&#39; instead. | 
**isDeleted** | **Boolean** | &#x60;True&#x60; when the replica is deleted. | 
**isStandby** | **Boolean** | &#x60;True&#x60; when the replica is in standby mode. | 
**recoveryForkGuid** | **String** | The recovery fork GUID of the replica. | [optional] 
**recoveryModel** | **String** | The recovery model of the replica. | 
**rootProperties** | [**MssqlRootProperties**](MssqlRootProperties.md) |  | 
**state** | **String** | The state of the replica. | 



## Enum: RecoveryModelEnum


* `SIMPLE` (value: `"SIMPLE"`)

* `FULL` (value: `"FULL"`)

* `BULK_LOGGED` (value: `"BULK_LOGGED"`)




