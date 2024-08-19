# DefaultApi

All URIs are relative to *https://api.urlbox.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**renderSync**](DefaultApi.md#renderSync) | **POST** /v1/render/sync | Render a URL as an image or video |


<a id="renderSync"></a>
# **renderSync**
> RenderResponse renderSync(renderRequest)

Render a URL as an image or video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.urlbox.io");
    
    // Configure HTTP bearer authorization: SecretKey
    HttpBearerAuth SecretKey = (HttpBearerAuth) defaultClient.getAuthentication("SecretKey");
    SecretKey.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    RenderRequest renderRequest = new RenderRequest(); // RenderRequest | 
    try {
      RenderResponse result = apiInstance.renderSync(renderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#renderSync");
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
| **renderRequest** | [**RenderRequest**](RenderRequest.md)|  | |

### Return type

[**RenderResponse**](RenderResponse.md)

### Authorization

[SecretKey](../README.md#SecretKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * x-renders-allowed - The number of renders allowed <br>  * x-renders-reset - The date and time when the render count will reset <br>  * x-renders-used - The number of renders used <br>  * x-urlbox-acceptedby - The server that accepted the request <br>  * x-urlbox-cache-status - The cache status of the response <br>  * x-urlbox-cachekey - The cache key used by URLBox <br>  * x-urlbox-renderedby - The server that rendered the response <br>  * x-urlbox-requestid - The request ID assigned by URLBox <br>  |
| **307** | Temporary Redirect |  * Location -  <br>  |
| **400** | Bad request |  * x-urlbox-error-message - An error message describing the reason the request failed <br>  |
| **401** | Unauthorized |  * x-urlbox-error-message - An error message describing the reason the request failed <br>  |
| **500** | Internal server error |  * x-urlbox-error-message - An error message describing the reason the request failed <br>  |

