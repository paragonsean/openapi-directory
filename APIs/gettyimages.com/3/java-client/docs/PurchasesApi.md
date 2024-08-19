# PurchasesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3PurchasedAssetsGet**](PurchasesApi.md#v3PurchasedAssetsGet) | **GET** /v3/purchased-assets | Get Previously Purchased Images and Video |


<a id="v3PurchasedAssetsGet"></a>
# **v3PurchasedAssetsGet**
> PreviousAssetPurchases v3PurchasedAssetsGet(acceptLanguage, dateTo, page, pageSize, dateFrom, companyPurchases)

Get Previously Purchased Images and Video

This endpoint returns a list of all assets purchased on gettyimages.com by the username used for authentication.  Use of this endpoint requires configuration changes to your API key. Please contact your sales representative to learn more.  You&#39;ll need an API key and access token to use this resource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PurchasesApi;

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

    PurchasesApi apiInstance = new PurchasesApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    OffsetDateTime dateTo = OffsetDateTime.now(); // OffsetDateTime | If specified, retrieves previous purchases on or before this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD).
    Integer page = 1; // Integer | Identifies page to return. Default is 1.
    Integer pageSize = 75; // Integer | Specifies page size. Default is 75, maximum page_size is 100.
    OffsetDateTime dateFrom = OffsetDateTime.now(); // OffsetDateTime | If specified, retrieves previous purchases on or after this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD).
    Boolean companyPurchases = false; // Boolean | If specified, returns the list of previously purchased assets for all users in your company. Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false.
    try {
      PreviousAssetPurchases result = apiInstance.v3PurchasedAssetsGet(acceptLanguage, dateTo, page, pageSize, dateFrom, companyPurchases);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PurchasesApi#v3PurchasedAssetsGet");
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
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **dateTo** | **OffsetDateTime**| If specified, retrieves previous purchases on or before this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD). | [optional] |
| **page** | **Integer**| Identifies page to return. Default is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Specifies page size. Default is 75, maximum page_size is 100. | [optional] [default to 75] |
| **dateFrom** | **OffsetDateTime**| If specified, retrieves previous purchases on or after this date. Dates should be submitted in ISO 8601 format (i.e., YYYY-MM-DD). | [optional] |
| **companyPurchases** | **Boolean**| If specified, returns the list of previously purchased assets for all users in your company. Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false. | [optional] [default to false] |

### Return type

[**PreviousAssetPurchases**](PreviousAssetPurchases.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | PageNumberLessThanOne |  -  |
| **401** | Unauthorized |  -  |
| **403** | InsufficientPermissions |  -  |

