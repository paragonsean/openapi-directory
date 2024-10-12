

# OperationStatus

Operation status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | Operation end time. Format: ISO-8601. |  [optional] |
|**error** | [**OperationStatusError**](OperationStatusError.md) |  |  [optional] |
|**id** | **String** | ID of the operation. |  [optional] |
|**name** | **String** | Name of the operation. |  [optional] |
|**properties** | [**OperationStatusExtendedInfo**](OperationStatusExtendedInfo.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Operation start time. Format: ISO-8601. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Operation status. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



