# BigQueryApi.GetQueryResultsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cacheHit** | **Boolean** | Whether the query result was fetched from the query cache. | [optional] 
**errors** | [**[ErrorProto]**](ErrorProto.md) | Output only. The first errors or warnings encountered during the running of the job. The final message includes the number of errors that caused the process to stop. Errors here do not necessarily mean that the job has completed or was unsuccessful. For more information about error messages, see [Error messages](https://cloud.google.com/bigquery/docs/error-messages). | [optional] [readonly] 
**etag** | **String** | A hash of this response. | [optional] 
**jobComplete** | **Boolean** | Whether the query has completed or not. If rows or totalRows are present, this will always be true. If this is false, totalRows will not be available. | [optional] 
**jobReference** | [**JobReference**](JobReference.md) |  | [optional] 
**kind** | **String** | The resource type of the response. | [optional] [default to &#39;bigquery#getQueryResultsResponse&#39;]
**numDmlAffectedRows** | **String** | Output only. The number of rows affected by a DML statement. Present only for DML statements INSERT, UPDATE or DELETE. | [optional] [readonly] 
**pageToken** | **String** | A token used for paging results. When this token is non-empty, it indicates additional results are available. | [optional] 
**rows** | [**[TableRow]**](TableRow.md) | An object with as many results as can be contained within the maximum permitted reply size. To get any additional rows, you can call GetQueryResults and specify the jobReference returned above. Present only when the query completes successfully. The REST-based representation of this data leverages a series of JSON f,v objects for indicating fields and values. | [optional] 
**schema** | [**TableSchema**](TableSchema.md) |  | [optional] 
**totalBytesProcessed** | **String** | The total number of bytes processed for this query. | [optional] 
**totalRows** | **String** | The total number of rows in the complete query result set, which can be more than the number of rows in this single page of results. Present only when the query completes successfully. | [optional] 


