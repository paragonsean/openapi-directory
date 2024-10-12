# SqlManagementClient.SyncGroupProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflictResolutionPolicy** | **String** | Conflict resolution policy of the sync group. | [optional] 
**hubDatabasePassword** | **String** | Password for the sync group hub database credential. | [optional] 
**hubDatabaseUserName** | **String** | User name for the sync group hub database credential. | [optional] 
**interval** | **Number** | Sync interval of the sync group. | [optional] 
**lastSyncTime** | **Date** | Last sync time of the sync group. | [optional] [readonly] 
**schema** | [**SyncGroupSchema**](SyncGroupSchema.md) |  | [optional] 
**syncDatabaseId** | **String** | ARM resource id of the sync database in the sync group. | [optional] 
**syncState** | **String** | Sync state of the sync group. | [optional] [readonly] 



## Enum: ConflictResolutionPolicyEnum


* `HubWin` (value: `"HubWin"`)

* `MemberWin` (value: `"MemberWin"`)





## Enum: SyncStateEnum


* `NotReady` (value: `"NotReady"`)

* `Error` (value: `"Error"`)

* `Warning` (value: `"Warning"`)

* `Progressing` (value: `"Progressing"`)

* `Good` (value: `"Good"`)




