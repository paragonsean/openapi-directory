

# ListDraftsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**drafts** | [**List&lt;Draft&gt;**](Draft.md) | List of drafts. Note that the &#x60;Message&#x60; property in each &#x60;Draft&#x60; resource only contains an &#x60;id&#x60; and a &#x60;threadId&#x60;. The messages.get method can fetch additional message details. |  [optional] |
|**nextPageToken** | **String** | Token to retrieve the next page of results in the list. |  [optional] |
|**resultSizeEstimate** | **Integer** | Estimated total number of results. |  [optional] |



