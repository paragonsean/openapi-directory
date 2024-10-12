

# InstancesListResponse

Database instances list response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | [**List&lt;DatabaseInstance&gt;**](DatabaseInstance.md) | List of database instance resources. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#instancesList&#x60;. |  [optional] |
|**nextPageToken** | **String** | The continuation token, used to page through large result sets. Provide this value in a subsequent request to return the next page of results. |  [optional] |
|**warnings** | [**List&lt;ApiWarning&gt;**](ApiWarning.md) | List of warnings that occurred while handling the request. |  [optional] |



