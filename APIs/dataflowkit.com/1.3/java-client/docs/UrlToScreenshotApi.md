# UrlToScreenshotApi

All URIs are relative to *https://api.dataflowkit.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**urlToScreenshot**](UrlToScreenshotApi.md#urlToScreenshot) | **POST** /convert/url/screenshot | Capture web page Screenshots. |


<a id="urlToScreenshot"></a>
# **urlToScreenshot**
> File urlToScreenshot(url2screenshotrequest)

Capture web page Screenshots.

Automate URL to Screenshot Conversion right in your application.  Specify request parameters like URL, Proxy, and actions to convert web pages to screenshots using Headless Chrome.  Get resulted pictures in JPG or PNG formats even from websites blocked in your area for some reason utilizing our worldwide pool of proxies.  Simulate real-world human interaction with the page. For example, before capturing a web page, you may need to scroll it.  Generate ready-to-run code for your favorite language at [https://dataflowkit.com/url-to-screenshot](https://dataflowkit.com/url-to-screenshot)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UrlToScreenshotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dataflowkit.com/v1");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    UrlToScreenshotApi apiInstance = new UrlToScreenshotApi(defaultClient);
    Url2screenshotrequest url2screenshotrequest = new Url2screenshotrequest(); // Url2screenshotrequest | 
    try {
      File result = apiInstance.urlToScreenshot(url2screenshotrequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UrlToScreenshotApi#urlToScreenshot");
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
| **url2screenshotrequest** | [**Url2screenshotrequest**](Url2screenshotrequest.md)|  | |

### Return type

[**File**](File.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/jpeg, image/png, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns jpg or png file. |  -  |
| **400** | Bad Request. Invalid payload specified. |  -  |
| **401** | Unauthorized. &#x60;api_key&#x60; parameter is missed or incorrect |  -  |
| **500** | Internal Server Error is a very general HTTP status code that means something has gone wrong on the web site&#39;s server. |  -  |

