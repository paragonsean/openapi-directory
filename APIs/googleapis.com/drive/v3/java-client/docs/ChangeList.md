

# ChangeList

A list of changes for a user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changes** | [**List&lt;Change&gt;**](Change.md) | The list of changes. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;drive#changeList\&quot;&#x60;. |  [optional] |
|**newStartPageToken** | **String** | The starting page token for future changes. This will be present only if the end of the current changes list has been reached. The page token doesn&#39;t expire. |  [optional] |
|**nextPageToken** | **String** | The page token for the next page of changes. This will be absent if the end of the changes list has been reached. The page token doesn&#39;t expire. |  [optional] |



