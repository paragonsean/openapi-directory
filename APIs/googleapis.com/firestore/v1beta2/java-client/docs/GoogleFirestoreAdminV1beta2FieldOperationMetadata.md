

# GoogleFirestoreAdminV1beta2FieldOperationMetadata

Metadata for google.longrunning.Operation results from FirestoreAdmin.UpdateField.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bytesProgress** | [**GoogleFirestoreAdminV1beta2Progress**](GoogleFirestoreAdminV1beta2Progress.md) |  |  [optional] |
|**documentProgress** | [**GoogleFirestoreAdminV1beta2Progress**](GoogleFirestoreAdminV1beta2Progress.md) |  |  [optional] |
|**endTime** | **String** | The time this operation completed. Will be unset if operation still in progress. |  [optional] |
|**field** | **String** | The field resource that this operation is acting on. For example: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}&#x60; |  [optional] |
|**indexConfigDeltas** | [**List&lt;GoogleFirestoreAdminV1beta2IndexConfigDelta&gt;**](GoogleFirestoreAdminV1beta2IndexConfigDelta.md) | A list of IndexConfigDelta, which describe the intent of this operation. |  [optional] |
|**startTime** | **String** | The time this operation started. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the operation. |  [optional] |



## Enum: StateEnum

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



