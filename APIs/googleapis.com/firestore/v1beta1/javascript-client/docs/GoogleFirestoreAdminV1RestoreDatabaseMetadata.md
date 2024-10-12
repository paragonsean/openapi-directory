# CloudFirestoreApi.GoogleFirestoreAdminV1RestoreDatabaseMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup** | **String** | The name of the backup restoring from. | [optional] 
**database** | **String** | The name of the database being restored to. | [optional] 
**endTime** | **String** | The time the restore finished, unset for ongoing restores. | [optional] 
**operationState** | **String** | The operation state of the restore. | [optional] 
**progressPercentage** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  | [optional] 
**startTime** | **String** | The time the restore was started. | [optional] 



## Enum: OperationStateEnum


* `OPERATION_STATE_UNSPECIFIED` (value: `"OPERATION_STATE_UNSPECIFIED"`)

* `INITIALIZING` (value: `"INITIALIZING"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `FINALIZING` (value: `"FINALIZING"`)

* `SUCCESSFUL` (value: `"SUCCESSFUL"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)




