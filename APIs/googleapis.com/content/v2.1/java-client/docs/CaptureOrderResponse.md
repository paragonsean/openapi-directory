

# CaptureOrderResponse

Response message for the CaptureOrder method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionStatus** | [**ExecutionStatusEnum**](#ExecutionStatusEnum) | The status of the execution. Only defined if the request was successful. Acceptable values are: * \&quot;duplicate\&quot; * \&quot;executed\&quot; |  [optional] |



## Enum: ExecutionStatusEnum

| Name | Value |
|---- | -----|
| EXECUTION_STATUS_UNSPECIFIED | &quot;EXECUTION_STATUS_UNSPECIFIED&quot; |
| EXECUTED | &quot;EXECUTED&quot; |
| DUPLICATE | &quot;DUPLICATE&quot; |



