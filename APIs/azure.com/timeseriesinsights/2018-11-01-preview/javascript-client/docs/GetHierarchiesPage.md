# TimeSeriesInsightsClient.GetHierarchiesPage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuationToken** | **String** | If returned, this means that current results represent a partial result. Continuation token allows to get the next page of results. To get the next page of query results, send the same request with continuation token parameter in \&quot;x-ms-continuation\&quot; HTTP header. | [optional] [readonly] 
**hierarchies** | [**[TimeSeriesHierarchy]**](TimeSeriesHierarchy.md) | Partial list of time series hierarchies returned in a single request. Can be empty if server was unable to fill the page in this request, or there is no more objects when continuation token is null. | [optional] [readonly] 


