# NprListeningService.AggregationData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation** | **String** | A unique identifier for the aggregation | 
**affiliationMeta** | [**Affiliation**](Affiliation.md) |  | [optional] 
**description** | **String** | A short description or teaser | [optional] 
**provider** | **String** | The producer of this aggregation | [optional] [default to &#39;NPR&#39;]
**station** | **String** | Deprecated - clients should switch to use provider. | [optional] [default to &#39;NPR&#39;]
**title** | **String** | The title of this aggregation | 
**type** | **String** | The type of list returned; will always be &#x60;aggregation&#x60;; useful for parsing search results | [default to &#39;aggregation&#39;]



## Enum: TypeEnum


* `aggregation` (value: `"aggregation"`)




