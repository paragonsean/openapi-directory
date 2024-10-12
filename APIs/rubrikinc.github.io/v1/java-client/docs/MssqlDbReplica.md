

# MssqlDbReplica


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityInfo** | [**MssqlDbReplicaAvailabilityInfo**](MssqlDbReplicaAvailabilityInfo.md) |  |  [optional] |
|**hasPermissions** | **Boolean** | &#x60;True&#x60; when the Rubrik cluster has sufficient permissions to perform all necessary operations. |  |
|**instanceId** | **String** | ID of the SQL Server instance managing the replica. |  |
|**instanceName** | **String** | Name of the SQL Server instance managing the replica. |  |
|**isArchived** | **Boolean** | Deprecated. Please use &#39;isDeleted&#39; instead. |  |
|**isDeleted** | **Boolean** | &#x60;True&#x60; when the replica is deleted. |  |
|**isStandby** | **Boolean** | &#x60;True&#x60; when the replica is in standby mode. |  |
|**recoveryForkGuid** | **String** | The recovery fork GUID of the replica. |  [optional] |
|**recoveryModel** | [**RecoveryModelEnum**](#RecoveryModelEnum) | The recovery model of the replica. |  |
|**rootProperties** | [**MssqlRootProperties**](MssqlRootProperties.md) |  |  |
|**state** | **String** | The state of the replica. |  |



## Enum: RecoveryModelEnum

| Name | Value |
|---- | -----|
| SIMPLE | &quot;SIMPLE&quot; |
| FULL | &quot;FULL&quot; |
| BULK_LOGGED | &quot;BULK_LOGGED&quot; |



