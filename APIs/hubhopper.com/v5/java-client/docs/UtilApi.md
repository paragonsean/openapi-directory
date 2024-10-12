# UtilApi

All URIs are relative to *https://apis.hubhopper.com/partner*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**utilLanguagesGet**](UtilApi.md#utilLanguagesGet) | **GET** /util/languages |  |


<a id="utilLanguagesGet"></a>
# **utilLanguagesGet**
> LanguageList utilLanguagesGet(pageSize, page)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.hubhopper.com/partner");
    
    // Configure API key authorization: partner_id
    ApiKeyAuth partner_id = (ApiKeyAuth) defaultClient.getAuthentication("partner_id");
    partner_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //partner_id.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    UtilApi apiInstance = new UtilApi(defaultClient);
    String pageSize = "pageSize_example"; // String | Provide the size of the page to fetch.
    String page = "page_example"; // String | Provide the page number to fetch.
    try {
      LanguageList result = apiInstance.utilLanguagesGet(pageSize, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilApi#utilLanguagesGet");
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
| **pageSize** | **String**| Provide the size of the page to fetch. | [optional] |
| **page** | **String**| Provide the page number to fetch. | [optional] |

### Return type

[**LanguageList**](LanguageList.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 response |  -  |
| **204** | 204 response |  -  |
| **401** | 401 response |  -  |
| **404** | 404 response |  -  |
| **500** | 500 response |  -  |

