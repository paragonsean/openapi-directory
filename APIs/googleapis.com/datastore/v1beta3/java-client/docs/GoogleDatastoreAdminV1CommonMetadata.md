

# GoogleDatastoreAdminV1CommonMetadata

Metadata common to all Datastore Admin operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The time the operation ended, either successfully or otherwise. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The client-assigned labels which were provided when the operation was created. May also include additional labels. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The type of the operation. Can be used as a filter in ListOperationsRequest. |  [optional] |
|**startTime** | **String** | The time that work began on the operation. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the Operation. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| OPERATION_TYPE_UNSPECIFIED | &quot;OPERATION_TYPE_UNSPECIFIED&quot; |
| EXPORT_ENTITIES | &quot;EXPORT_ENTITIES&quot; |
| IMPORT_ENTITIES | &quot;IMPORT_ENTITIES&quot; |
| CREATE_INDEX | &quot;CREATE_INDEX&quot; |
| DELETE_INDEX | &quot;DELETE_INDEX&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| INITIALIZING | &quot;INITIALIZING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| FINALIZING | &quot;FINALIZING&quot; |
| SUCCESSFUL | &quot;SUCCESSFUL&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



