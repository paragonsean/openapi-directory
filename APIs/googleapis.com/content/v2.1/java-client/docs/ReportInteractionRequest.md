

# ReportInteractionRequest

Request to report interactions on a recommendation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**interactionType** | [**InteractionTypeEnum**](#InteractionTypeEnum) | Required. Type of the interaction that is reported, for example INTERACTION_CLICK. |  [optional] |
|**responseToken** | **String** | Required. Token of the response when recommendation was returned. |  [optional] |
|**subtype** | **String** | Optional. Subtype of the recommendations this interaction happened on. This field must be set only to the value that is returned by {@link &#x60;RecommendationsService.GenerateRecommendations&#x60;} call. |  [optional] |
|**type** | **String** | Required. Type of the recommendations on which this interaction happened. This field must be set only to the value that is returned by {@link &#x60;GenerateRecommendationsResponse&#x60;} call. |  [optional] |



## Enum: InteractionTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;INTERACTION_TYPE_UNSPECIFIED&quot; |
| DISMISS | &quot;INTERACTION_DISMISS&quot; |
| CLICK | &quot;INTERACTION_CLICK&quot; |



