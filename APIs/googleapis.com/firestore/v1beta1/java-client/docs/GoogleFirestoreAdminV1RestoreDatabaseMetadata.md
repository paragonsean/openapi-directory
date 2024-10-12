

# GoogleFirestoreAdminV1RestoreDatabaseMetadata

Metadata for the long-running operation from the RestoreDatabase request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backup** | **String** | The name of the backup restoring from. |  [optional] |
|**database** | **String** | The name of the database being restored to. |  [optional] |
|**endTime** | **String** | The time the restore finished, unset for ongoing restores. |  [optional] |
|**operationState** | [**OperationStateEnum**](#OperationStateEnum) | The operation state of the restore. |  [optional] |
|**progressPercentage** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  |  [optional] |
|**startTime** | **String** | The time the restore was started. |  [optional] |



## Enum: OperationStateEnum

| Name | Value |
|---- | -----|
| OPERATION_STATE_UNSPECIFIED | &quot;OPERATION_STATE_UNSPECIFIED&quot; |
| INITIALIZING | &quot;INITIALIZING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| FINALIZING | &quot;FINALIZING&quot; |
| SUCCESSFUL | &quot;SUCCESSFUL&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



