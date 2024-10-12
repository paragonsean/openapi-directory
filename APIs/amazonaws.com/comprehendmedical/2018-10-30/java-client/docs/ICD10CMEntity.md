

# ICD10CMEntity

The collection of medical entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in the detection and analysis. Attributes and traits of the entity are also returned. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**Integer**](Integer.md) |  |  [optional] |
|**text** | [**String**](String.md) |  |  [optional] |
|**category** | [**ICD10CMEntityCategory**](ICD10CMEntityCategory.md) |  |  [optional] |
|**type** | [**ICD10CMEntityType**](ICD10CMEntityType.md) |  |  [optional] |
|**score** | [**Float**](Float.md) |  |  [optional] |
|**beginOffset** | [**Integer**](Integer.md) |  |  [optional] |
|**endOffset** | [**Integer**](Integer.md) |  |  [optional] |
|**attributes** | [**List**](List.md) |  |  [optional] |
|**traits** | [**List**](List.md) |  |  [optional] |
|**icD10CMConcepts** | [**List**](List.md) |  |  [optional] |



