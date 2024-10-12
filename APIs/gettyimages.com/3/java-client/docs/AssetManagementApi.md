# AssetManagementApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3AssetManagementAssetsSendEventsGet**](AssetManagementApi.md#v3AssetManagementAssetsSendEventsGet) | **GET** /v3/asset-management/assets/send-events |  |


<a id="v3AssetManagementAssetsSendEventsGet"></a>
# **v3AssetManagementAssetsSendEventsGet**
> GetSendEventsResponse v3AssetManagementAssetsSendEventsGet(acceptLanguage, lastOffset, eventCount)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetManagementApi;

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

    AssetManagementApi apiInstance = new AssetManagementApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    OffsetDateTime lastOffset = OffsetDateTime.now(); // OffsetDateTime | Specifies a date/time (with timezone information) for continuing retrieval of events.  Events occuring _after_ the `last_offset` value provided will be returned.
    Integer eventCount = 56; // Integer | Specifies the number of events to return. Default is 50, maximum value is 100.
    try {
      GetSendEventsResponse result = apiInstance.v3AssetManagementAssetsSendEventsGet(acceptLanguage, lastOffset, eventCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetManagementApi#v3AssetManagementAssetsSendEventsGet");
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
| **lastOffset** | **OffsetDateTime**| Specifies a date/time (with timezone information) for continuing retrieval of events.  Events occuring _after_ the &#x60;last_offset&#x60; value provided will be returned. | [optional] |
| **eventCount** | **Integer**| Specifies the number of events to return. Default is 50, maximum value is 100. | [optional] |

### Return type

[**GetSendEventsResponse**](GetSendEventsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | EventCountOutOfRange |  -  |

