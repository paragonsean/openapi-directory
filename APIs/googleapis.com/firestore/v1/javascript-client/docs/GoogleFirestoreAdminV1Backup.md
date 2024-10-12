# CloudFirestoreApi.GoogleFirestoreAdminV1Backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **String** | Output only. Name of the Firestore database that the backup is from. Format is &#x60;projects/{project}/databases/{database}&#x60;. | [optional] [readonly] 
**databaseUid** | **String** | Output only. The system-generated UUID4 for the Firestore database that the backup is from. | [optional] [readonly] 
**expireTime** | **String** | Output only. The timestamp at which this backup expires. | [optional] [readonly] 
**name** | **String** | Output only. The unique resource name of the Backup. Format is &#x60;projects/{project}/locations/{location}/backups/{backup}&#x60;. | [optional] [readonly] 
**snapshotTime** | **String** | Output only. The backup contains an externally consistent copy of the database at this time. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the backup. | [optional] [readonly] 
**stats** | [**GoogleFirestoreAdminV1Stats**](GoogleFirestoreAdminV1Stats.md) |  | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `NOT_AVAILABLE` (value: `"NOT_AVAILABLE"`)




