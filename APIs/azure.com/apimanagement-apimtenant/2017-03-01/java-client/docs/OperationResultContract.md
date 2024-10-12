

# OperationResultContract

Operation Result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionLog** | [**List&lt;OperationResultLogItemContract&gt;**](OperationResultLogItemContract.md) | This property if only provided as part of the TenantConfiguration_Validate operation. It contains the log the entities which will be updated/created/deleted as part of the TenantConfiguration_Deploy operation. |  [optional] [readonly] |
|**error** | [**TenantAccessUpdateDefaultResponse**](TenantAccessUpdateDefaultResponse.md) |  |  [optional] |
|**id** | **String** | Operation result identifier. |  [optional] |
|**resultInfo** | **String** | Optional result info. |  [optional] |
|**started** | **OffsetDateTime** | Start time of an async operation. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of an async operation. |  [optional] |
|**updated** | **OffsetDateTime** | Last update time of an async operation. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STARTED | &quot;Started&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |



