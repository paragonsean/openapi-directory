

# ListKeyRingsResponse

Response message for KeyManagementService.ListKeyRings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyRings** | [**List&lt;KeyRing&gt;**](KeyRing.md) | The list of KeyRings. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in ListKeyRingsRequest.page_token to retrieve the next page of results. |  [optional] |
|**totalSize** | **Integer** | The total number of KeyRings that matched the query. |  [optional] |



