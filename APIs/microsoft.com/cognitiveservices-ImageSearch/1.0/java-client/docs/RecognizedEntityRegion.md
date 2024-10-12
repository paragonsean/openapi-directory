

# RecognizedEntityRegion

Defines a region of the image where an entity was found and a list of entities that might match it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchingEntities** | [**List&lt;RecognizedEntity&gt;**](RecognizedEntity.md) | A list of entities that Bing believes match the entity found in the region. The entities are in descending order of confidence (see the matchConfidence field of RecognizedEntity). |  [optional] [readonly] |
|**region** | [**NormalizedRectangle**](NormalizedRectangle.md) |  |  [optional] |



