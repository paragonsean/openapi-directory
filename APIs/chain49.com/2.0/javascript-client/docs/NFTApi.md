# Chain49Api.NFTApi

All URIs are relative to *https://api.chain49.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNFTMetaV2**](NFTApi.md#getNFTMetaV2) | **GET** /{blockchain}/v2/nft/{nftContract}/{nftTokenId} | Get NFT metadata V2



## getNFTMetaV2

> GetNFTMetaV2200Response getNFTMetaV2(blockchain, nftContract, nftTokenId)

Get NFT metadata V2

Only works on Ethereum-like blockchains (currently ethereum and bsc)  Get metadata like name or description for a specified contract and token ID. The resulting data contains a link which can then be used to request the IPFS link for the actual image to display in a block explorer for example.  Note: this route was implemented by us and is therefore not yet supported by existing blockbook clients.

### Example

```javascript
import Chain49Api from 'chain49_api';
let defaultClient = Chain49Api.ApiClient.instance;
// Configure API key authorization: X-RapidAPI-Host
let X-RapidAPI-Host = defaultClient.authentications['X-RapidAPI-Host'];
X-RapidAPI-Host.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-RapidAPI-Host.apiKeyPrefix = 'Token';
// Configure API key authorization: X-API-Key
let X-API-Key = defaultClient.authentications['X-API-Key'];
X-API-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-API-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-RapidAPI-Key
let X-RapidAPI-Key = defaultClient.authentications['X-RapidAPI-Key'];
X-RapidAPI-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-RapidAPI-Key.apiKeyPrefix = 'Token';

let apiInstance = new Chain49Api.NFTApi();
let blockchain = "ethereum"; // String | NFT-compatible blockchain name
let nftContract = "0x05756b07725dA0101813475333f372a844789Dc2"; // String | Address of NFT contract
let nftTokenId = "22"; // String | Unique token ID of NFT
apiInstance.getNFTMetaV2(blockchain, nftContract, nftTokenId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain** | **String**| NFT-compatible blockchain name | 
 **nftContract** | **String**| Address of NFT contract | 
 **nftTokenId** | **String**| Unique token ID of NFT | 

### Return type

[**GetNFTMetaV2200Response**](GetNFTMetaV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

