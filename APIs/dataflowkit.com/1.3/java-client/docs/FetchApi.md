# FetchApi

All URIs are relative to *https://api.dataflowkit.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetch**](FetchApi.md#fetch) | **POST** /fetch | Download web page content |


<a id="fetch"></a>
# **fetch**
> fetch(fetchrequest)

Download web page content

Use fetch endpoint to download web pages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FetchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.dataflowkit.com/v1");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    FetchApi apiInstance = new FetchApi(defaultClient);
    Fetchrequest fetchrequest = new Fetchrequest(); // Fetchrequest | - _Base fetcher type_ is the right choice for fetching server-side rendered pages. It takes fewer resources and works faster than rendering HTML with _Chrome fetcher_ - But for rendering Angular, React, and Vue.js web sites, you should always specify _Chrome fetcher type_. In this case, headless chrome fetcher renders dynamic Javascript content in the same way as real web browsers would do it.  Generate ready-to-run code for your favorite language at [https://dataflowkit.com/render-web](https://dataflowkit.com/render-web) 
    try {
      apiInstance.fetch(fetchrequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling FetchApi#fetch");
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
| **fetchrequest** | [**Fetchrequest**](Fetchrequest.md)| - _Base fetcher type_ is the right choice for fetching server-side rendered pages. It takes fewer resources and works faster than rendering HTML with _Chrome fetcher_ - But for rendering Angular, React, and Vue.js web sites, you should always specify _Chrome fetcher type_. In this case, headless chrome fetcher renders dynamic Javascript content in the same way as real web browsers would do it.  Generate ready-to-run code for your favorite language at [https://dataflowkit.com/render-web](https://dataflowkit.com/render-web)  | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html; charset=utf-8, text/plain; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns utf8 encoded web page content. |  -  |
| **400** | Bad Request. Invalid payload specified. |  -  |
| **401** | Unauthorized. &#x60;api_key&#x60; parameter is missed or incorrect |  -  |
| **500** | Internal Server Error is a very general HTTP status code that means something has gone wrong on the web site&#39;s server. |  -  |

