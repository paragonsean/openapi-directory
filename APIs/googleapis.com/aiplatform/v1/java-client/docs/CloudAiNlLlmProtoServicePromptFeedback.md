

# CloudAiNlLlmProtoServicePromptFeedback

Content filter results for a prompt sent in the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockReason** | [**BlockReasonEnum**](#BlockReasonEnum) | Blocked reason. |  [optional] |
|**blockReasonMessage** | **String** | A readable block reason message. |  [optional] |
|**safetyRatings** | [**List&lt;CloudAiNlLlmProtoServiceSafetyRating&gt;**](CloudAiNlLlmProtoServiceSafetyRating.md) | Safety ratings. |  [optional] |



## Enum: BlockReasonEnum

| Name | Value |
|---- | -----|
| BLOCKED_REASON_UNSPECIFIED | &quot;BLOCKED_REASON_UNSPECIFIED&quot; |
| SAFETY | &quot;SAFETY&quot; |
| OTHER | &quot;OTHER&quot; |



