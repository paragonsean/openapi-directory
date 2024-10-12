# AssetPublicSignatureApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSiteAssetPublicSignature**](AssetPublicSignatureApi.md#getSiteAssetPublicSignature) | **GET** /sites/{site_id}/assets/{asset_id}/public_signature |  |


<a id="getSiteAssetPublicSignature"></a>
# **getSiteAssetPublicSignature**
> AssetPublicSignature getSiteAssetPublicSignature(siteId, assetId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetPublicSignatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    AssetPublicSignatureApi apiInstance = new AssetPublicSignatureApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String assetId = "assetId_example"; // String | 
    try {
      AssetPublicSignature result = apiInstance.getSiteAssetPublicSignature(siteId, assetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetPublicSignatureApi#getSiteAssetPublicSignature");
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
| **siteId** | **String**|  | |
| **assetId** | **String**|  | |

### Return type

[**AssetPublicSignature**](AssetPublicSignature.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

