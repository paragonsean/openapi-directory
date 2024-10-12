

# ServerOperationProperties

The properties of a server operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The operation description. |  [optional] [readonly] |
|**errorCode** | **Integer** | The operation error code. |  [optional] [readonly] |
|**errorDescription** | **String** | The operation error description. |  [optional] [readonly] |
|**errorSeverity** | **Integer** | The operation error severity. |  [optional] [readonly] |
|**estimatedCompletionTime** | **OffsetDateTime** | The estimated completion time of the operation. |  [optional] [readonly] |
|**isCancellable** | **Boolean** | Whether the operation can be cancelled. |  [optional] [readonly] |
|**isUserError** | **Boolean** | Whether or not the error is a user error. |  [optional] [readonly] |
|**operation** | **String** | The name of operation. |  [optional] [readonly] |
|**operationFriendlyName** | **String** | The friendly name of operation. |  [optional] [readonly] |
|**percentComplete** | **Integer** | The percentage of the operation completed. |  [optional] [readonly] |
|**serverName** | **String** | The name of the server. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The operation start time. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The operation state. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;Pending&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCEL_IN_PROGRESS | &quot;CancelInProgress&quot; |
| CANCELLED | &quot;Cancelled&quot; |



