# LanguageApi

All URIs are relative to *https://api.ebay.com/commerce/translation/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**translate**](LanguageApi.md#translate) | **POST** /translate |  |


<a id="translate"></a>
# **translate**
> TranslateResponse translate(translateRequest)



Translates input text inot a given language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/commerce/translation/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    LanguageApi apiInstance = new LanguageApi(defaultClient);
    TranslateRequest translateRequest = new TranslateRequest(); // TranslateRequest | 
    try {
      TranslateResponse result = apiInstance.translate(translateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageApi#translate");
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
| **translateRequest** | [**TranslateRequest**](TranslateRequest.md)|  | |

### Return type

[**TranslateResponse**](TranslateResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

