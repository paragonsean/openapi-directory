# CloudDatastoreApi.AggregationResultBatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationResults** | [**[AggregationResult]**](AggregationResult.md) | The aggregation results for this batch. | [optional] 
**moreResults** | **String** | The state of the query after the current batch. Only COUNT(*) aggregations are supported in the initial launch. Therefore, expected result type is limited to &#x60;NO_MORE_RESULTS&#x60;. | [optional] 
**readTime** | **String** | Read timestamp this batch was returned from. In a single transaction, subsequent query result batches for the same query can have a greater timestamp. Each batch&#39;s read timestamp is valid for all preceding batches. | [optional] 



## Enum: MoreResultsEnum


* `MORE_RESULTS_TYPE_UNSPECIFIED` (value: `"MORE_RESULTS_TYPE_UNSPECIFIED"`)

* `NOT_FINISHED` (value: `"NOT_FINISHED"`)

* `MORE_RESULTS_AFTER_LIMIT` (value: `"MORE_RESULTS_AFTER_LIMIT"`)

* `MORE_RESULTS_AFTER_CURSOR` (value: `"MORE_RESULTS_AFTER_CURSOR"`)

* `NO_MORE_RESULTS` (value: `"NO_MORE_RESULTS"`)




