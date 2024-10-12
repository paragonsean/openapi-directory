

# ListAssignedInventorySourcesResponse

Response message for AssignedInventorySourceService.ListAssignedInventorySources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignedInventorySources** | [**List&lt;AssignedInventorySource&gt;**](AssignedInventorySource.md) | The list of assigned inventory sources. This list will be absent if empty. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the page_token field in the subsequent call to &#x60;ListAssignedInventorySources&#x60; method to retrieve the next page of results. |  [optional] |



