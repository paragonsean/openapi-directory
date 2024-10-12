

# AsyncOperationStatus

Azure async operation status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The date time that the async operation finished. |  [optional] [readonly] |
|**errorInfo** | [**AsyncOperationErrorInfo**](AsyncOperationErrorInfo.md) |  |  [optional] |
|**id** | **String** | Async operation id. |  [optional] [readonly] |
|**name** | **String** | Async operation name. |  [optional] [readonly] |
|**percentComplete** | **BigDecimal** | Async operation progress. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Read Only: The provisioning state of the web service. Valid values are Unknown, Provisioning, Succeeded, and Failed. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The date time that the async operation started. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |



