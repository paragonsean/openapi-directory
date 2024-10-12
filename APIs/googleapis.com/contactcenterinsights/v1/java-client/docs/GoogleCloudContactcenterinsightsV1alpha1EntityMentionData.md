

# GoogleCloudContactcenterinsightsV1alpha1EntityMentionData

The data for an entity mention annotation. This represents a mention of an `Entity` in the conversation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityUniqueId** | **String** | The key of this entity in conversation entities. Can be used to retrieve the exact &#x60;Entity&#x60; this mention is attached to. |  [optional] |
|**sentiment** | [**GoogleCloudContactcenterinsightsV1alpha1SentimentData**](GoogleCloudContactcenterinsightsV1alpha1SentimentData.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the entity mention. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MENTION_TYPE_UNSPECIFIED | &quot;MENTION_TYPE_UNSPECIFIED&quot; |
| PROPER | &quot;PROPER&quot; |
| COMMON | &quot;COMMON&quot; |



