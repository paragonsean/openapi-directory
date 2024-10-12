

# ListBareMetalNodePoolsResponse

Response message for listing bare metal node pools.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bareMetalNodePools** | [**List&lt;BareMetalNodePool&gt;**](BareMetalNodePool.md) | The node pools from the specified parent resource. |  [optional] |
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



