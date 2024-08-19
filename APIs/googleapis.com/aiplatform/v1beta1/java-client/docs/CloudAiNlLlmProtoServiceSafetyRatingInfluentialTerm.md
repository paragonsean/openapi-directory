

# CloudAiNlLlmProtoServiceSafetyRatingInfluentialTerm

The influential term that could potentially block the response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beginOffset** | **Integer** | The beginning offset of the influential term. |  [optional] |
|**confidence** | **Float** | The confidence score of the influential term. |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | The source of the influential term, prompt or response. |  [optional] |
|**term** | **String** | The influential term. |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| SOURCE_UNSPECIFIED | &quot;SOURCE_UNSPECIFIED&quot; |
| PROMPT | &quot;PROMPT&quot; |
| RESPONSE | &quot;RESPONSE&quot; |



