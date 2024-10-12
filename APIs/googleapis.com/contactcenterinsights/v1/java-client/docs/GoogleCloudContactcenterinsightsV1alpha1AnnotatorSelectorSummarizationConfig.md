

# GoogleCloudContactcenterinsightsV1alpha1AnnotatorSelectorSummarizationConfig

Configuration for summarization.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationProfile** | **String** | Resource name of the Dialogflow conversation profile. Format: projects/{project}/locations/{location}/conversationProfiles/{conversation_profile} |  [optional] |
|**summarizationModel** | [**SummarizationModelEnum**](#SummarizationModelEnum) | Default summarization model to be used. |  [optional] |



## Enum: SummarizationModelEnum

| Name | Value |
|---- | -----|
| SUMMARIZATION_MODEL_UNSPECIFIED | &quot;SUMMARIZATION_MODEL_UNSPECIFIED&quot; |
| BASELINE_MODEL | &quot;BASELINE_MODEL&quot; |



