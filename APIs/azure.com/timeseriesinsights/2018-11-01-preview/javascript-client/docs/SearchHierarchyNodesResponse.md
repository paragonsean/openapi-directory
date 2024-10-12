# TimeSeriesInsightsClient.SearchHierarchyNodesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuationToken** | **String** | If returned, this means that current results represent a partial result. Continuation token allows to get the next page of results. To get the next page of query results, send the same request with continuation token parameter in \&quot;x-ms-continuation\&quot; HTTP header. | [optional] [readonly] 
**hitCount** | **Number** | Total number of hierarchy nodes which contains the instances matching the query based on the input. | [optional] [readonly] 
**hits** | [**[HierarchyHit]**](HierarchyHit.md) | The list of hierarchy nodes which contains the instances matching the query based on the input. May be empty. | [optional] [readonly] 


