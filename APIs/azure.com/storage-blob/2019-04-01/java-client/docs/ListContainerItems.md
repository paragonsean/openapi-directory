

# ListContainerItems

Response schema. Contains list of blobs returned, and if paging is requested or required, a URL to next page of containers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | Request URL that can be used to query next page of containers. Returned when total number of requested containers exceed maximum page size. |  [optional] [readonly] |
|**value** | [**List&lt;ListContainerItem&gt;**](ListContainerItem.md) | List of blobs containers returned. |  [optional] [readonly] |



