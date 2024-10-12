

# ListSharesResponse

ListSharesResponse is the result of ListSharesRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The token you can use to retrieve the next page of results. Not returned if there are no more results in the list. |  [optional] |
|**shares** | [**List&lt;Share&gt;**](Share.md) | A list of shares in the project for the specified instance. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



