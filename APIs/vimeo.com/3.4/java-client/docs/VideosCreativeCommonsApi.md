# VideosCreativeCommonsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCcLicenses**](VideosCreativeCommonsApi.md#getCcLicenses) | **GET** /creativecommons | Get all Creative Commons licenses |


<a id="getCcLicenses"></a>
# **getCcLicenses**
> List&lt;CreativeCommons&gt; getCcLicenses()

Get all Creative Commons licenses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosCreativeCommonsApi;

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

    VideosCreativeCommonsApi apiInstance = new VideosCreativeCommonsApi(defaultClient);
    try {
      List<CreativeCommons> result = apiInstance.getCcLicenses();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosCreativeCommonsApi#getCcLicenses");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;CreativeCommons&gt;**](CreativeCommons.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.creativecommons+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Creative Commons licenses were returned. |  -  |

