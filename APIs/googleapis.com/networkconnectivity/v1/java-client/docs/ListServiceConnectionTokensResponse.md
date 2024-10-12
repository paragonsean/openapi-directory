

# ListServiceConnectionTokensResponse

Response for ListServiceConnectionTokens.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. |  [optional] |
|**serviceConnectionTokens** | [**List&lt;ServiceConnectionToken&gt;**](ServiceConnectionToken.md) | ServiceConnectionTokens to be returned. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



