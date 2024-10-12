

# ListInstancesResponse

Response from ListInstances.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instances** | [**List&lt;Instance&gt;**](Instance.md) | The list of instances matching the request filters, up to the requested ListInstancesRequest.pageSize. |  [optional] |
|**nextPageToken** | **String** | If provided, a page token that can look up the next ListInstancesRequest.pageSize results. If empty, the results list is exhausted. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



