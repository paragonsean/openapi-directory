# VideosLanguagesApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLanguages**](VideosLanguagesApi.md#getLanguages) | **GET** /languages | Get all languages |


<a id="getLanguages"></a>
# **getLanguages**
> List&lt;Language&gt; getLanguages(filter)

Get all languages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosLanguagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosLanguagesApi apiInstance = new VideosLanguagesApi(defaultClient);
    String filter = "texttracks"; // String | The attribute by which to filter the results.  Option descriptions:  * `texttracks` - Only return text track supported languages 
    try {
      List<Language> result = apiInstance.getLanguages(filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosLanguagesApi#getLanguages");
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
| **filter** | **String**| The attribute by which to filter the results.  Option descriptions:  * &#x60;texttracks&#x60; - Only return text track supported languages  | [optional] [enum: texttracks] |

### Return type

[**List&lt;Language&gt;**](Language.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.language+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The languages were returned. |  -  |

