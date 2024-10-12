

# ListNegativeKeywordsResponse

Response message for NegativeKeywordService.ListNegativeKeywords.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**negativeKeywords** | [**List&lt;NegativeKeyword&gt;**](NegativeKeyword.md) | The list of negative keywords. This list will be absent if empty. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the page_token field in the subsequent call to &#x60;ListNegativeKeywords&#x60; method to retrieve the next page of results. |  [optional] |



