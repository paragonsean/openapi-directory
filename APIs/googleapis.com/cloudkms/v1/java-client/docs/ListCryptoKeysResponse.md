

# ListCryptoKeysResponse

Response message for KeyManagementService.ListCryptoKeys.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cryptoKeys** | [**List&lt;CryptoKey&gt;**](CryptoKey.md) | The list of CryptoKeys. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in ListCryptoKeysRequest.page_token to retrieve the next page of results. |  [optional] |
|**totalSize** | **Integer** | The total number of CryptoKeys that matched the query. |  [optional] |



