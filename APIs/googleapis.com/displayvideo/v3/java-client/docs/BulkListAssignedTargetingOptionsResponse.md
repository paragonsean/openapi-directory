

# BulkListAssignedTargetingOptionsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lineItemAssignedTargetingOptions** | [**List&lt;LineItemAssignedTargetingOption&gt;**](LineItemAssignedTargetingOption.md) | The list of wrapper objects, each providing an assigned targeting option and the line item it is assigned to. This list will be absent if empty. |  [optional] |
|**nextPageToken** | **String** | A token identifying the next page of results. This value should be specified as the pageToken in a subsequent call to &#x60;BulkListAssignedTargetingOptions&#x60; to fetch the next page of results. This token will be absent if there are no more line_item_assigned_targeting_options to return. |  [optional] |



