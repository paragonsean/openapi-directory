# HtmlRendererApi

All URIs are relative to *https://api.exoapi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**htmlRendererPost**](HtmlRendererApi.md#htmlRendererPost) | **POST** /html-renderer |  |


<a id="htmlRendererPost"></a>
# **htmlRendererPost**
> File htmlRendererPost(htmlRendererPostRequest)



Generate high-quality PDF documents or images from HTML

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HtmlRendererApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exoapi.dev");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    HtmlRendererApi apiInstance = new HtmlRendererApi(defaultClient);
    HtmlRendererPostRequest htmlRendererPostRequest = new HtmlRendererPostRequest(); // HtmlRendererPostRequest | 
    try {
      File result = apiInstance.htmlRendererPost(htmlRendererPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HtmlRendererApi#htmlRendererPost");
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
| **htmlRendererPostRequest** | [**HtmlRendererPostRequest**](HtmlRendererPostRequest.md)|  | |

### Return type

[**File**](File.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf, image/png, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 🟢 200 OK |  -  |
| **401** | 🟡 401 Unauthorized |  -  |
| **429** | 🟡 429 Too many requests |  -  |
| **500** | 🔴 500 Internal server error |  -  |

