

# ListLikedAssetsResponse

A response message from a request to list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assets** | [**List&lt;Asset&gt;**](Asset.md) | A list of assets that match the criteria specified in the request. |  [optional] |
|**nextPageToken** | **String** | The continuation token for retrieving the next page. If empty, indicates that there are no more pages. To get the next page, submit the same request specifying this value as the page_token. |  [optional] |
|**totalSize** | **Integer** | The total number of assets in the list, without pagination. |  [optional] |



