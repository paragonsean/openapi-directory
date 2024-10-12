

# InlineObject

An object that appears inline with text. An InlineObject contains an EmbeddedObject such as an image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inlineObjectProperties** | [**InlineObjectProperties**](InlineObjectProperties.md) |  |  [optional] |
|**objectId** | **String** | The ID of this inline object. Can be used to update an object’s properties. |  [optional] |
|**suggestedDeletionIds** | **List&lt;String&gt;** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. |  [optional] |
|**suggestedInlineObjectPropertiesChanges** | [**Map&lt;String, SuggestedInlineObjectProperties&gt;**](SuggestedInlineObjectProperties.md) | The suggested changes to the inline object properties, keyed by suggestion ID. |  [optional] |
|**suggestedInsertionId** | **String** | The suggested insertion ID. If empty, then this is not a suggested insertion. |  [optional] |



