

# ListOperationsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationId** | **String** | The ID of the application. |  |
|**maxResults** | **Integer** | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value. If you do not specify a value for MaxResults, the request returns 50 items per page by default. |  [optional] |
|**nextToken** | **String** | The token for the next page of results.  |  [optional] |
|**filters** | [**List&lt;Filter&gt;**](Filter.md) | The filters of an operation. |  [optional] |



