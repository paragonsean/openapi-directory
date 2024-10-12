# TimeSeriesInsightsClient.QueryResultPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuationToken** | **String** | If returned, this means that current results represent a partial result. Continuation token allows to get the next page of results. To get the next page of query results, send the same request with continuation token parameter in \&quot;x-ms-continuation\&quot; HTTP header. | [optional] [readonly] 
**progress** | **Number** | Approximate progress of the query in percentage. It can be between 0 and 100. When the continuation token in the response is null, the progress is expected to be 100. | [optional] [readonly] 
**properties** | [**[PropertyValues]**](PropertyValues.md) | Collection of time series properties and values for each of the timestamps.  Can be null if server was unable to fill the page in this request, or can be empty if there are no more objects when continuation token is null. | [optional] [readonly] 
**timestamps** | **[Date]** | The timestamps of the values of the time series. If an aggregation over intervals is used, timestamps represent the start of corresponding intervals. If events are retrieved, timestamps are values of timestamp $ts property of events. Can be null if server was unable to fill the page in this request, or can be empty if there are no more objects when continuation token is null. | [optional] [readonly] 


