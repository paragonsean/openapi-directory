

# GoogleCloudContactcenterinsightsV1alpha1AnswerFeedback

The feedback that the customer has about a certain answer in the conversation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clicked** | **Boolean** | Indicates whether an answer or item was clicked by the human agent. |  [optional] |
|**correctnessLevel** | [**CorrectnessLevelEnum**](#CorrectnessLevelEnum) | The correctness level of an answer. |  [optional] |
|**displayed** | **Boolean** | Indicates whether an answer or item was displayed to the human agent in the agent desktop UI. |  [optional] |



## Enum: CorrectnessLevelEnum

| Name | Value |
|---- | -----|
| CORRECTNESS_LEVEL_UNSPECIFIED | &quot;CORRECTNESS_LEVEL_UNSPECIFIED&quot; |
| NOT_CORRECT | &quot;NOT_CORRECT&quot; |
| PARTIALLY_CORRECT | &quot;PARTIALLY_CORRECT&quot; |
| FULLY_CORRECT | &quot;FULLY_CORRECT&quot; |



