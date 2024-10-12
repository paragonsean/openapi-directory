

# OperationResultsDescription

The properties indicating the operation result of an operation on a service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The ID of the operation returned. |  [optional] [readonly] |
|**name** | **String** | The name of the operation result. |  [optional] [readonly] |
|**properties** | **Object** | Additional properties of the operation result. |  [optional] |
|**startTime** | **String** | The time that the operation was started. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the operation being performed. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CANCELED | &quot;Canceled&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| REQUESTED | &quot;Requested&quot; |
| RUNNING | &quot;Running&quot; |



