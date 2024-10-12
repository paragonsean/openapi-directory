# CrawlUrlApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCrawlUrlCollection**](CrawlUrlApi.md#getCrawlUrlCollection) | **GET** /crawl-urls | Retrieves the collection of CrawlUrl resources. |
| [**getCrawlUrlItem**](CrawlUrlApi.md#getCrawlUrlItem) | **GET** /crawl-urls/{id} | Retrieves a CrawlUrl resource. |


<a id="getCrawlUrlCollection"></a>
# **getCrawlUrlCollection**
> List&lt;CrawlUrlRead&gt; getCrawlUrlCollection(page)

Retrieves the collection of CrawlUrl resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrawlUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    CrawlUrlApi apiInstance = new CrawlUrlApi(defaultClient);
    Integer page = 56; // Integer | The collection page number
    try {
      List<CrawlUrlRead> result = apiInstance.getCrawlUrlCollection(page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrawlUrlApi#getCrawlUrlCollection");
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
| **page** | **Integer**| The collection page number | [optional] |

### Return type

[**List&lt;CrawlUrlRead&gt;**](CrawlUrlRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CrawlUrl collection response |  -  |

<a id="getCrawlUrlItem"></a>
# **getCrawlUrlItem**
> CrawlUrlRead getCrawlUrlItem(id)

Retrieves a CrawlUrl resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrawlUrlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    CrawlUrlApi apiInstance = new CrawlUrlApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      CrawlUrlRead result = apiInstance.getCrawlUrlItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrawlUrlApi#getCrawlUrlItem");
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
| **id** | **String**|  | |

### Return type

[**CrawlUrlRead**](CrawlUrlRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CrawlUrl resource response |  -  |
| **404** | Resource not found |  -  |

