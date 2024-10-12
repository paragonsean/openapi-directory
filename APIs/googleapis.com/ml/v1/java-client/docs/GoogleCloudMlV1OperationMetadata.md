

# GoogleCloudMlV1OperationMetadata

Represents the metadata of the long-running operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The time the operation was submitted. |  [optional] |
|**endTime** | **String** | The time operation processing completed. |  [optional] |
|**isCancellationRequested** | **Boolean** | Indicates whether a request to cancel this operation has been made. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The user labels, inherited from the model or the model version being operated on. |  [optional] |
|**modelName** | **String** | Contains the name of the model associated with the operation. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The operation type. |  [optional] |
|**projectNumber** | **String** | Contains the project number associated with the operation. |  [optional] |
|**startTime** | **String** | The time operation processing started. |  [optional] |
|**version** | [**GoogleCloudMlV1Version**](GoogleCloudMlV1Version.md) |  |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| OPERATION_TYPE_UNSPECIFIED | &quot;OPERATION_TYPE_UNSPECIFIED&quot; |
| CREATE_VERSION | &quot;CREATE_VERSION&quot; |
| DELETE_VERSION | &quot;DELETE_VERSION&quot; |
| DELETE_MODEL | &quot;DELETE_MODEL&quot; |
| UPDATE_MODEL | &quot;UPDATE_MODEL&quot; |
| UPDATE_VERSION | &quot;UPDATE_VERSION&quot; |
| UPDATE_CONFIG | &quot;UPDATE_CONFIG&quot; |



