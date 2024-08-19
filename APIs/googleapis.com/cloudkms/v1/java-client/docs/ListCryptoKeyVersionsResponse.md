

# ListCryptoKeyVersionsResponse

Response message for KeyManagementService.ListCryptoKeyVersions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cryptoKeyVersions** | [**List&lt;CryptoKeyVersion&gt;**](CryptoKeyVersion.md) | The list of CryptoKeyVersions. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in ListCryptoKeyVersionsRequest.page_token to retrieve the next page of results. |  [optional] |
|**totalSize** | **Integer** | The total number of CryptoKeyVersions that matched the query. |  [optional] |



