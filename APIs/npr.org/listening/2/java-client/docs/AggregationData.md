

# AggregationData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affiliation** | **String** | A unique identifier for the aggregation |  |
|**affiliationMeta** | [**Affiliation**](Affiliation.md) |  |  [optional] |
|**description** | **String** | A short description or teaser |  [optional] |
|**provider** | **String** | The producer of this aggregation |  [optional] |
|**station** | **String** | Deprecated - clients should switch to use provider. |  [optional] |
|**title** | **String** | The title of this aggregation |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of list returned; will always be &#x60;aggregation&#x60;; useful for parsing search results |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AGGREGATION | &quot;aggregation&quot; |



