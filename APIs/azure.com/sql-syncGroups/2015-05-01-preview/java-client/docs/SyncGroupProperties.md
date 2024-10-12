

# SyncGroupProperties

Properties of a sync group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conflictResolutionPolicy** | [**ConflictResolutionPolicyEnum**](#ConflictResolutionPolicyEnum) | Conflict resolution policy of the sync group. |  [optional] |
|**hubDatabasePassword** | **String** | Password for the sync group hub database credential. |  [optional] |
|**hubDatabaseUserName** | **String** | User name for the sync group hub database credential. |  [optional] |
|**interval** | **Integer** | Sync interval of the sync group. |  [optional] |
|**lastSyncTime** | **OffsetDateTime** | Last sync time of the sync group. |  [optional] [readonly] |
|**schema** | [**SyncGroupSchema**](SyncGroupSchema.md) |  |  [optional] |
|**syncDatabaseId** | **String** | ARM resource id of the sync database in the sync group. |  [optional] |
|**syncState** | [**SyncStateEnum**](#SyncStateEnum) | Sync state of the sync group. |  [optional] [readonly] |



## Enum: ConflictResolutionPolicyEnum

| Name | Value |
|---- | -----|
| HUB_WIN | &quot;HubWin&quot; |
| MEMBER_WIN | &quot;MemberWin&quot; |



## Enum: SyncStateEnum

| Name | Value |
|---- | -----|
| NOT_READY | &quot;NotReady&quot; |
| ERROR | &quot;Error&quot; |
| WARNING | &quot;Warning&quot; |
| PROGRESSING | &quot;Progressing&quot; |
| GOOD | &quot;Good&quot; |



