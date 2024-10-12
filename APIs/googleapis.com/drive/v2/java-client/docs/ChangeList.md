

# ChangeList

A list of changes for a user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | The ETag of the list. |  [optional] |
|**items** | [**List&lt;Change&gt;**](Change.md) | The list of changes. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |  [optional] |
|**kind** | **String** | This is always &#x60;drive#changeList&#x60;. |  [optional] |
|**largestChangeId** | **String** | The current largest change ID. |  [optional] |
|**newStartPageToken** | **String** | The starting page token for future changes. This will be present only if the end of the current changes list has been reached. |  [optional] |
|**nextLink** | **String** | A link to the next page of changes. |  [optional] |
|**nextPageToken** | **String** | The page token for the next page of changes. This will be absent if the end of the changes list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |  [optional] |
|**selfLink** | **String** | A link back to this list. |  [optional] |



