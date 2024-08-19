

# GoogleCloudAiplatformV1GenerateContentResponsePromptFeedback

Content filter results for a prompt sent in the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockReason** | [**BlockReasonEnum**](#BlockReasonEnum) | Output only. Blocked reason. |  [optional] [readonly] |
|**blockReasonMessage** | **String** | Output only. A readable block reason message. |  [optional] [readonly] |
|**safetyRatings** | [**List&lt;GoogleCloudAiplatformV1SafetyRating&gt;**](GoogleCloudAiplatformV1SafetyRating.md) | Output only. Safety ratings. |  [optional] [readonly] |



## Enum: BlockReasonEnum

| Name | Value |
|---- | -----|
| BLOCKED_REASON_UNSPECIFIED | &quot;BLOCKED_REASON_UNSPECIFIED&quot; |
| SAFETY | &quot;SAFETY&quot; |
| OTHER | &quot;OTHER&quot; |



