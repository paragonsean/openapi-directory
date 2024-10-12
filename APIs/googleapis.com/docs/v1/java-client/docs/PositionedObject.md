

# PositionedObject

An object that's tethered to a Paragraph and positioned relative to the beginning of the paragraph. A PositionedObject contains an EmbeddedObject such as an image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**objectId** | **String** | The ID of this positioned object. |  [optional] |
|**positionedObjectProperties** | [**PositionedObjectProperties**](PositionedObjectProperties.md) |  |  [optional] |
|**suggestedDeletionIds** | **List&lt;String&gt;** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. |  [optional] |
|**suggestedInsertionId** | **String** | The suggested insertion ID. If empty, then this is not a suggested insertion. |  [optional] |
|**suggestedPositionedObjectPropertiesChanges** | [**Map&lt;String, SuggestedPositionedObjectProperties&gt;**](SuggestedPositionedObjectProperties.md) | The suggested changes to the positioned object properties, keyed by suggestion ID. |  [optional] |



