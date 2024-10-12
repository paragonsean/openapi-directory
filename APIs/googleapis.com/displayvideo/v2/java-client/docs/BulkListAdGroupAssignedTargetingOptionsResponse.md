

# BulkListAdGroupAssignedTargetingOptionsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token identifying the next page of results. This value should be specified as the pageToken in a subsequent call to &#x60;BulkListAdGroupAssignedTargetingOptions&#x60; to fetch the next page of results. This token will be absent if there are no more AdGroupAssignedTargetingOption resources to return. |  [optional] |
|**youtubeAdGroupAssignedTargetingOptions** | [**List&lt;YoutubeAdGroupAssignedTargetingOption&gt;**](YoutubeAdGroupAssignedTargetingOption.md) | The list of wrapper objects, each providing an assigned targeting option and the youtube ad group it is assigned to. This list will be absent if empty. |  [optional] |



