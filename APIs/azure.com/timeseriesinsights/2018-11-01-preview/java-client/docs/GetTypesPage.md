

# GetTypesPage

Partial list of time series types returned in a single request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continuationToken** | **String** | If returned, this means that current results represent a partial result. Continuation token allows to get the next page of results. To get the next page of query results, send the same request with continuation token parameter in \&quot;x-ms-continuation\&quot; HTTP header. |  [optional] [readonly] |
|**types** | [**List&lt;TimeSeriesType&gt;**](TimeSeriesType.md) | Partial list of time series types returned in a single request. Can be empty if server was unable to fill the page with more types in this request, or there is no more types when continuation token is null. |  [optional] [readonly] |



