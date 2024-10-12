

# ListInstancesResponse

The response for ListInstances.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instances** | [**List&lt;Instance&gt;**](Instance.md) | The list of requested instances. |  [optional] |
|**nextPageToken** | **String** | &#x60;next_page_token&#x60; can be sent in a subsequent ListInstances call to fetch more of the matching instances. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | The list of unreachable instances. It includes the names of instances whose metadata could not be retrieved within instance_deadline. |  [optional] |



