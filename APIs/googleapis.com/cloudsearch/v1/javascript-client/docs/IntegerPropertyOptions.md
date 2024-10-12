# CloudSearchApi.IntegerPropertyOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integerFacetingOptions** | [**IntegerFacetingOptions**](IntegerFacetingOptions.md) |  | [optional] 
**maximumValue** | **String** | The maximum value of the property. The minimum and maximum values for the property are used to rank results according to the ordered ranking. Indexing requests with values greater than the maximum are accepted and ranked with the same weight as items indexed with the maximum value. | [optional] 
**minimumValue** | **String** | The minimum value of the property. The minimum and maximum values for the property are used to rank results according to the ordered ranking. Indexing requests with values less than the minimum are accepted and ranked with the same weight as items indexed with the minimum value. | [optional] 
**operatorOptions** | [**IntegerOperatorOptions**](IntegerOperatorOptions.md) |  | [optional] 
**orderedRanking** | **String** | Used to specify the ordered ranking for the integer. Can only be used if isRepeatable is false. | [optional] 



## Enum: OrderedRankingEnum


* `NO_ORDER` (value: `"NO_ORDER"`)

* `ASCENDING` (value: `"ASCENDING"`)

* `DESCENDING` (value: `"DESCENDING"`)




