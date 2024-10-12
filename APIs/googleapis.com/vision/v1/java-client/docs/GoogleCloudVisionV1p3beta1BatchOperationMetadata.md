

# GoogleCloudVisionV1p3beta1BatchOperationMetadata

Metadata for the batch operations such as the current state. This is included in the `metadata` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The time when the batch request is finished and google.longrunning.Operation.done is set to true. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the batch operation. |  [optional] |
|**submitTime** | **String** | The time when the batch request was submitted to the server. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| SUCCESSFUL | &quot;SUCCESSFUL&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



