# CloudDatastoreApi.QueryResultBatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endCursor** | **Blob** | A cursor that points to the position after the last result in the batch. | [optional] 
**entityResultType** | **String** | The result type for every entity in &#x60;entity_results&#x60;. | [optional] 
**entityResults** | [**[EntityResult]**](EntityResult.md) | The results for this batch. | [optional] 
**moreResults** | **String** | The state of the query after the current batch. | [optional] 
**readTime** | **String** | Read timestamp this batch was returned from. This applies to the range of results from the query&#39;s &#x60;start_cursor&#x60; (or the beginning of the query if no cursor was given) to this batch&#39;s &#x60;end_cursor&#x60; (not the query&#39;s &#x60;end_cursor&#x60;). In a single transaction, subsequent query result batches for the same query can have a greater timestamp. Each batch&#39;s read timestamp is valid for all preceding batches. This value will not be set for eventually consistent queries in Cloud Datastore. | [optional] 
**skippedCursor** | **Blob** | A cursor that points to the position after the last skipped result. Will be set when &#x60;skipped_results&#x60; !&#x3D; 0. | [optional] 
**skippedResults** | **Number** | The number of results skipped, typically because of an offset. | [optional] 
**snapshotVersion** | **String** | The version number of the snapshot this batch was returned from. This applies to the range of results from the query&#39;s &#x60;start_cursor&#x60; (or the beginning of the query if no cursor was given) to this batch&#39;s &#x60;end_cursor&#x60; (not the query&#39;s &#x60;end_cursor&#x60;). In a single transaction, subsequent query result batches for the same query can have a greater snapshot version number. Each batch&#39;s snapshot version is valid for all preceding batches. The value will be zero for eventually consistent queries. | [optional] 



## Enum: EntityResultTypeEnum


* `RESULT_TYPE_UNSPECIFIED` (value: `"RESULT_TYPE_UNSPECIFIED"`)

* `FULL` (value: `"FULL"`)

* `PROJECTION` (value: `"PROJECTION"`)

* `KEY_ONLY` (value: `"KEY_ONLY"`)





## Enum: MoreResultsEnum


* `MORE_RESULTS_TYPE_UNSPECIFIED` (value: `"MORE_RESULTS_TYPE_UNSPECIFIED"`)

* `NOT_FINISHED` (value: `"NOT_FINISHED"`)

* `MORE_RESULTS_AFTER_LIMIT` (value: `"MORE_RESULTS_AFTER_LIMIT"`)

* `MORE_RESULTS_AFTER_CURSOR` (value: `"MORE_RESULTS_AFTER_CURSOR"`)

* `NO_MORE_RESULTS` (value: `"NO_MORE_RESULTS"`)




