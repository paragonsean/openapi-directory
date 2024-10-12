# NftApi

All URIs are relative to *https://api.chain49.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNFTMetaV2**](NftApi.md#getNFTMetaV2) | **GET** /{blockchain}/v2/nft/{nftContract}/{nftTokenId} | Get NFT metadata V2 |


<a id="getNFTMetaV2"></a>
# **getNFTMetaV2**
> GetNFTMetaV2200Response getNFTMetaV2(blockchain, nftContract, nftTokenId)

Get NFT metadata V2

Only works on Ethereum-like blockchains (currently ethereum and bsc)  Get metadata like name or description for a specified contract and token ID. The resulting data contains a link which can then be used to request the IPFS link for the actual image to display in a block explorer for example.  Note: this route was implemented by us and is therefore not yet supported by existing blockbook clients.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NftApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.chain49.com");
    
    // Configure API key authorization: X-RapidAPI-Host
    ApiKeyAuth X-RapidAPI-Host = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Host");
    X-RapidAPI-Host.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Host.setApiKeyPrefix("Token");

    // Configure API key authorization: X-API-Key
    ApiKeyAuth X-API-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-API-Key");
    X-API-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-API-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-RapidAPI-Key
    ApiKeyAuth X-RapidAPI-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-RapidAPI-Key");
    X-RapidAPI-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-RapidAPI-Key.setApiKeyPrefix("Token");

    NftApi apiInstance = new NftApi(defaultClient);
    String blockchain = "ethereum"; // String | NFT-compatible blockchain name
    String nftContract = "0x05756b07725dA0101813475333f372a844789Dc2"; // String | Address of NFT contract
    String nftTokenId = "22"; // String | Unique token ID of NFT
    try {
      GetNFTMetaV2200Response result = apiInstance.getNFTMetaV2(blockchain, nftContract, nftTokenId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NftApi#getNFTMetaV2");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **blockchain** | **String**| NFT-compatible blockchain name | |
| **nftContract** | **String**| Address of NFT contract | |
| **nftTokenId** | **String**| Unique token ID of NFT | |

### Return type

[**GetNFTMetaV2200Response**](GetNFTMetaV2200Response.md)

### Authorization

[X-RapidAPI-Host](../README.md#X-RapidAPI-Host), [X-API-Key](../README.md#X-API-Key), [X-RapidAPI-Key](../README.md#X-RapidAPI-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

