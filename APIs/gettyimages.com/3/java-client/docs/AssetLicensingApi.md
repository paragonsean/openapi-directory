# AssetLicensingApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3AssetLicensingAssetIdPost**](AssetLicensingApi.md#v3AssetLicensingAssetIdPost) | **POST** /v3/asset-licensing/{assetId} | Endpoint for acquiring extended licenses with iStock credits for an asset. |


<a id="v3AssetLicensingAssetIdPost"></a>
# **v3AssetLicensingAssetIdPost**
> AssetLicensingResponse v3AssetLicensingAssetIdPost(assetId, acceptLanguage, acquireAssetLicensesRequest)

Endpoint for acquiring extended licenses with iStock credits for an asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetLicensingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Api-Key
    ApiKeyAuth Api-Key = (ApiKeyAuth) defaultClient.getAuthentication("Api-Key");
    Api-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Api-Key.setApiKeyPrefix("Token");

    AssetLicensingApi apiInstance = new AssetLicensingApi(defaultClient);
    String assetId = "assetId_example"; // String | Getty Images assetId - examples 520621493, 112301284
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    AcquireAssetLicensesRequest acquireAssetLicensesRequest = new AcquireAssetLicensesRequest(); // AcquireAssetLicensesRequest | Structure that specifies an array of LicenseTypes (multiseat, unlimited, resale, indemnification) to acquire,              and whether or not to use Team Credits. Authenticated User must have access to Team Credits if UseTeamCredits is set to \"true\".
    try {
      AssetLicensingResponse result = apiInstance.v3AssetLicensingAssetIdPost(assetId, acceptLanguage, acquireAssetLicensesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetLicensingApi#v3AssetLicensingAssetIdPost");
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
| **assetId** | **String**| Getty Images assetId - examples 520621493, 112301284 | |
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **acquireAssetLicensesRequest** | [**AcquireAssetLicensesRequest**](AcquireAssetLicensesRequest.md)| Structure that specifies an array of LicenseTypes (multiseat, unlimited, resale, indemnification) to acquire,              and whether or not to use Team Credits. Authenticated User must have access to Team Credits if UseTeamCredits is set to \&quot;true\&quot;. | [optional] |

### Return type

[**AssetLicensingResponse**](AssetLicensingResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | InvalidRequestParameters |  -  |
| **401** | AuthorizationTokenRequired |  -  |
| **402** | NotEnoughCreditsForPurchase |  -  |
| **404** | StandardLicenseNotFound |  -  |

