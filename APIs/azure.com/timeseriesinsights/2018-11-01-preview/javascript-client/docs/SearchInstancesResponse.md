# TimeSeriesInsightsClient.SearchInstancesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuationToken** | **String** | If returned, this means that current results represent a partial result. Continuation token allows to get the next page of results. To get the next page of query results, send the same request with continuation token parameter in \&quot;x-ms-continuation\&quot; HTTP header. | [optional] [readonly] 
**hitCount** | **Number** | Total number of instances matching the query based on the input. | [optional] [readonly] 
**hits** | [**[InstanceHit]**](InstanceHit.md) | The list of instances matching the query based on the input. May be empty. | [optional] [readonly] 


