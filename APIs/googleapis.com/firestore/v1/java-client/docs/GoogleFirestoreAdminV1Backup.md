

# GoogleFirestoreAdminV1Backup

A Backup of a Cloud Firestore Database. The backup contains all documents and index configurations for the given database at a specific point in time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**database** | **String** | Output only. Name of the Firestore database that the backup is from. Format is &#x60;projects/{project}/databases/{database}&#x60;. |  [optional] [readonly] |
|**databaseUid** | **String** | Output only. The system-generated UUID4 for the Firestore database that the backup is from. |  [optional] [readonly] |
|**expireTime** | **String** | Output only. The timestamp at which this backup expires. |  [optional] [readonly] |
|**name** | **String** | Output only. The unique resource name of the Backup. Format is &#x60;projects/{project}/locations/{location}/backups/{backup}&#x60;. |  [optional] [readonly] |
|**snapshotTime** | **String** | Output only. The backup contains an externally consistent copy of the database at this time. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the backup. |  [optional] [readonly] |
|**stats** | [**GoogleFirestoreAdminV1Stats**](GoogleFirestoreAdminV1Stats.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| NOT_AVAILABLE | &quot;NOT_AVAILABLE&quot; |



