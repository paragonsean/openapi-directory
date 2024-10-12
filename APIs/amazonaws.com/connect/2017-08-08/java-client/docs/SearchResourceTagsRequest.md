

# SearchResourceTagsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceId** | **String** | The identifier of the Amazon Connect instance. You can find the instanceId in the Amazon Resource Name (ARN) of the instance. |  |
|**resourceTypes** | **List&lt;String&gt;** | The list of resource types to be used to search tags from. If not provided or if any empty list is provided, this API will search from all supported resource types. |  [optional] |
|**nextToken** | **String** | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return per page. |  [optional] |
|**searchCriteria** | [**SearchResourceTagsRequestSearchCriteria**](SearchResourceTagsRequestSearchCriteria.md) |  |  [optional] |



