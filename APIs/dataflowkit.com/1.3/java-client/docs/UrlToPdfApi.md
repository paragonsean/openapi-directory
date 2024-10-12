# UrlToPdfApi

All URIs are relative to *https://api.dataflowkit.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**urlToPdf**](UrlToPdfApi.md#urlToPdf) | **POST** /convert/url/pdf | Save web page as PDF |


<a id="urlToPdf"></a>
# **urlToPdf**
> File urlToPdf(url2pdfrequest)

Save web page as PDF

Automate URL to PDF Conversion right in your application.  Specify request parameters like URL, Proxy, and actions to render web pages to PDF using Headless Chrome.  Get resulted PDF even from websites blocked in your area for some reason utilizing our worldwide pool of proxies.  Simulate real-world human interaction with the page. For example, before saving a web page to PDF, you may need to scroll it.  Generate ready-to-run code for your favorite language at [https://dataflowkit.com/url-to-pdf](https://dataflowkit.com/url-to-pdf)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UrlToPdfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dataflowkit.com/v1");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    UrlToPdfApi apiInstance = new UrlToPdfApi(defaultClient);
    Url2pdfrequest url2pdfrequest = new Url2pdfrequest(); // Url2pdfrequest | 
    try {
      File result = apiInstance.urlToPdf(url2pdfrequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UrlToPdfApi#urlToPdf");
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
| **url2pdfrequest** | [**Url2pdfrequest**](Url2pdfrequest.md)|  | |

### Return type

[**File**](File.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A PDF file. |  -  |
| **400** | Bad Request. Invalid payload specified. |  -  |
| **401** | Unauthorized. &#x60;api_key&#x60; parameter is missed or incorrect |  -  |
| **500** | Internal Server Error is a very general HTTP status code that means something has gone wrong on the web site&#39;s server. |  -  |

