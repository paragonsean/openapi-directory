

# GoogleFirestoreAdminV1FieldOperationMetadata

Metadata for google.longrunning.Operation results from FirestoreAdmin.UpdateField.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The time this operation completed. Will be unset if operation still in progress. |  [optional] |
|**field** | **String** | The field resource that this operation is acting on. For example: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}&#x60; |  [optional] |
|**indexConfigDeltas** | [**List&lt;GoogleFirestoreAdminV1IndexConfigDelta&gt;**](GoogleFirestoreAdminV1IndexConfigDelta.md) | A list of IndexConfigDelta, which describe the intent of this operation. |  [optional] |
|**progressBytes** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  |  [optional] |
|**progressDocuments** | [**GoogleFirestoreAdminV1Progress**](GoogleFirestoreAdminV1Progress.md) |  |  [optional] |
|**startTime** | **String** | The time this operation started. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the operation. |  [optional] |
|**ttlConfigDelta** | [**GoogleFirestoreAdminV1TtlConfigDelta**](GoogleFirestoreAdminV1TtlConfigDelta.md) |  |  [optional] |



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



