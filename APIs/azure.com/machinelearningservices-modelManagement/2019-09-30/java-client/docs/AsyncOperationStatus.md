

# AsyncOperationStatus

The async operation status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | The async operation creation time (UTC). |  [optional] |
|**endTime** | **OffsetDateTime** | The async operation end time (UTC)l |  [optional] |
|**error** | [**ModelErrorResponse**](ModelErrorResponse.md) |  |  [optional] |
|**id** | **String** | The async operation id. |  [optional] |
|**operationDetails** | [**AsyncOperationDetails**](AsyncOperationDetails.md) |  |  [optional] |
|**operationLog** | **String** | The async operation log. |  [optional] |
|**operationType** | **String** | The async operation type. |  [optional] |
|**parentRequestId** | **String** | The request id that created this operation |  [optional] |
|**resourceLocation** | **String** | The resource created/updated by the async operation. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The async operation state. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;NotStarted&quot; |
| RUNNING | &quot;Running&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| TIMED_OUT | &quot;TimedOut&quot; |



