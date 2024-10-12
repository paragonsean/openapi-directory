

# QueryResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cacheHit** | **Boolean** | Whether the query result was fetched from the query cache. |  [optional] |
|**dmlStats** | [**DmlStatistics**](DmlStatistics.md) |  |  [optional] |
|**errors** | [**List&lt;ErrorProto&gt;**](ErrorProto.md) | Output only. The first errors or warnings encountered during the running of the job. The final message includes the number of errors that caused the process to stop. Errors here do not necessarily mean that the job has completed or was unsuccessful. For more information about error messages, see [Error messages](https://cloud.google.com/bigquery/docs/error-messages). |  [optional] [readonly] |
|**jobComplete** | **Boolean** | Whether the query has completed or not. If rows or totalRows are present, this will always be true. If this is false, totalRows will not be available. |  [optional] |
|**jobCreationReason** | [**JobCreationReason**](JobCreationReason.md) |  |  [optional] |
|**jobReference** | [**JobReference**](JobReference.md) |  |  [optional] |
|**kind** | **String** | The resource type. |  [optional] |
|**numDmlAffectedRows** | **String** | Output only. The number of rows affected by a DML statement. Present only for DML statements INSERT, UPDATE or DELETE. |  [optional] [readonly] |
|**pageToken** | **String** | A token used for paging results. A non-empty token indicates that additional results are available. To see additional results, query the [&#x60;jobs.getQueryResults&#x60;](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/getQueryResults) method. For more information, see [Paging through table data](https://cloud.google.com/bigquery/docs/paging-results). |  [optional] |
|**queryId** | **String** | Query ID for the completed query. This ID will be auto-generated. This field is not yet available and it is currently not guaranteed to be populated. |  [optional] |
|**rows** | [**List&lt;TableRow&gt;**](TableRow.md) | An object with as many results as can be contained within the maximum permitted reply size. To get any additional rows, you can call GetQueryResults and specify the jobReference returned above. |  [optional] |
|**schema** | [**TableSchema**](TableSchema.md) |  |  [optional] |
|**sessionInfo** | [**SessionInfo**](SessionInfo.md) |  |  [optional] |
|**totalBytesProcessed** | **String** | The total number of bytes processed for this query. If this query was a dry run, this is the number of bytes that would be processed if the query were run. |  [optional] |
|**totalRows** | **String** | The total number of rows in the complete query result set, which can be more than the number of rows in this single page of results. |  [optional] |



