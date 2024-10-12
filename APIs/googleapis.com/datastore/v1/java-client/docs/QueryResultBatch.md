

# QueryResultBatch

A batch of results produced by a query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endCursor** | **byte[]** | A cursor that points to the position after the last result in the batch. |  [optional] |
|**entityResultType** | [**EntityResultTypeEnum**](#EntityResultTypeEnum) | The result type for every entity in &#x60;entity_results&#x60;. |  [optional] |
|**entityResults** | [**List&lt;EntityResult&gt;**](EntityResult.md) | The results for this batch. |  [optional] |
|**moreResults** | [**MoreResultsEnum**](#MoreResultsEnum) | The state of the query after the current batch. |  [optional] |
|**readTime** | **String** | Read timestamp this batch was returned from. This applies to the range of results from the query&#39;s &#x60;start_cursor&#x60; (or the beginning of the query if no cursor was given) to this batch&#39;s &#x60;end_cursor&#x60; (not the query&#39;s &#x60;end_cursor&#x60;). In a single transaction, subsequent query result batches for the same query can have a greater timestamp. Each batch&#39;s read timestamp is valid for all preceding batches. This value will not be set for eventually consistent queries in Cloud Datastore. |  [optional] |
|**skippedCursor** | **byte[]** | A cursor that points to the position after the last skipped result. Will be set when &#x60;skipped_results&#x60; !&#x3D; 0. |  [optional] |
|**skippedResults** | **Integer** | The number of results skipped, typically because of an offset. |  [optional] |
|**snapshotVersion** | **String** | The version number of the snapshot this batch was returned from. This applies to the range of results from the query&#39;s &#x60;start_cursor&#x60; (or the beginning of the query if no cursor was given) to this batch&#39;s &#x60;end_cursor&#x60; (not the query&#39;s &#x60;end_cursor&#x60;). In a single transaction, subsequent query result batches for the same query can have a greater snapshot version number. Each batch&#39;s snapshot version is valid for all preceding batches. The value will be zero for eventually consistent queries. |  [optional] |



## Enum: EntityResultTypeEnum

| Name | Value |
|---- | -----|
| RESULT_TYPE_UNSPECIFIED | &quot;RESULT_TYPE_UNSPECIFIED&quot; |
| FULL | &quot;FULL&quot; |
| PROJECTION | &quot;PROJECTION&quot; |
| KEY_ONLY | &quot;KEY_ONLY&quot; |



## Enum: MoreResultsEnum

| Name | Value |
|---- | -----|
| MORE_RESULTS_TYPE_UNSPECIFIED | &quot;MORE_RESULTS_TYPE_UNSPECIFIED&quot; |
| NOT_FINISHED | &quot;NOT_FINISHED&quot; |
| MORE_RESULTS_AFTER_LIMIT | &quot;MORE_RESULTS_AFTER_LIMIT&quot; |
| MORE_RESULTS_AFTER_CURSOR | &quot;MORE_RESULTS_AFTER_CURSOR&quot; |
| NO_MORE_RESULTS | &quot;NO_MORE_RESULTS&quot; |



