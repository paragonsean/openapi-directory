

# ICD10CMAttribute

The detected attributes that relate to an entity. This includes an extracted segment of the text that is an attribute of an entity, or otherwise related to an entity. InferICD10CM detects the following attributes: <code>Direction</code>, <code>System, Organ or Site</code>, and <code>Acuity</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**ICD10CMAttributeType**](ICD10CMAttributeType.md) |  |  [optional] |
|**score** | [**Float**](Float.md) |  |  [optional] |
|**relationshipScore** | [**Float**](Float.md) |  |  [optional] |
|**id** | [**Integer**](Integer.md) |  |  [optional] |
|**beginOffset** | [**Integer**](Integer.md) |  |  [optional] |
|**endOffset** | [**Integer**](Integer.md) |  |  [optional] |
|**text** | [**String**](String.md) |  |  [optional] |
|**traits** | [**List**](List.md) |  |  [optional] |
|**category** | [**ICD10CMEntityType**](ICD10CMEntityType.md) |  |  [optional] |
|**relationshipType** | [**ICD10CMRelationshipType**](ICD10CMRelationshipType.md) |  |  [optional] |



