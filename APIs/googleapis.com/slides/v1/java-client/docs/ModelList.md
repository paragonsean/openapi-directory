

# ModelList

A List describes the look and feel of bullets belonging to paragraphs associated with a list. A paragraph that is part of a list has an implicit reference to that list's ID.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**listId** | **String** | The ID of the list. |  [optional] |
|**nestingLevel** | [**Map&lt;String, NestingLevel&gt;**](NestingLevel.md) | A map of nesting levels to the properties of bullets at the associated level. A list has at most nine levels of nesting, so the possible values for the keys of this map are 0 through 8, inclusive. |  [optional] |



