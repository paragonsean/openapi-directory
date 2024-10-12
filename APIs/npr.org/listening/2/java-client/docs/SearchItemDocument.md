

# SearchItemDocument

A search result, which is either an AggregationAudioItemListDocument or an AudioItemDocument

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ifTypeAggregation** | [**AggregationAudioItemListDocument**](AggregationAudioItemListDocument.md) |  |  [optional] |
|**ifTypeAudio** | [**AudioItemDocument**](AudioItemDocument.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of search result, which is either an AggregationAudioItemListDocument or an AudioItemDocument |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AUDIO | &quot;audio&quot; |
| AGGREGATION | &quot;aggregation&quot; |



