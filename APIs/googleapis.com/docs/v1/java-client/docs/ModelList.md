

# ModelList

A List represents the list attributes for a group of paragraphs that all belong to the same list. A paragraph that's part of a list has a reference to the list's ID in its bullet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**listProperties** | [**ListProperties**](ListProperties.md) |  |  [optional] |
|**suggestedDeletionIds** | **List&lt;String&gt;** | The suggested deletion IDs. If empty, then there are no suggested deletions of this list. |  [optional] |
|**suggestedInsertionId** | **String** | The suggested insertion ID. If empty, then this is not a suggested insertion. |  [optional] |
|**suggestedListPropertiesChanges** | [**Map&lt;String, SuggestedListProperties&gt;**](SuggestedListProperties.md) | The suggested changes to the list properties, keyed by suggestion ID. |  [optional] |



