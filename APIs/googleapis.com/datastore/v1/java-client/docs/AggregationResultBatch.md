

# AggregationResultBatch

A batch of aggregation results produced by an aggregation query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationResults** | [**List&lt;AggregationResult&gt;**](AggregationResult.md) | The aggregation results for this batch. |  [optional] |
|**moreResults** | [**MoreResultsEnum**](#MoreResultsEnum) | The state of the query after the current batch. Only COUNT(*) aggregations are supported in the initial launch. Therefore, expected result type is limited to &#x60;NO_MORE_RESULTS&#x60;. |  [optional] |
|**readTime** | **String** | Read timestamp this batch was returned from. In a single transaction, subsequent query result batches for the same query can have a greater timestamp. Each batch&#39;s read timestamp is valid for all preceding batches. |  [optional] |



## Enum: MoreResultsEnum

| Name | Value |
|---- | -----|
| MORE_RESULTS_TYPE_UNSPECIFIED | &quot;MORE_RESULTS_TYPE_UNSPECIFIED&quot; |
| NOT_FINISHED | &quot;NOT_FINISHED&quot; |
| MORE_RESULTS_AFTER_LIMIT | &quot;MORE_RESULTS_AFTER_LIMIT&quot; |
| MORE_RESULTS_AFTER_CURSOR | &quot;MORE_RESULTS_AFTER_CURSOR&quot; |
| NO_MORE_RESULTS | &quot;NO_MORE_RESULTS&quot; |



