# CrawlApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelCrawlItem**](CrawlApi.md#cancelCrawlItem) | **POST** /crawls/{id}/cancel | Creates a Crawl resource. |
| [**getCrawlCollection**](CrawlApi.md#getCrawlCollection) | **GET** /crawls | Retrieves the collection of Crawl resources. |
| [**getCrawlItem**](CrawlApi.md#getCrawlItem) | **GET** /crawls/{id} | Retrieves a Crawl resource. |
| [**postCrawlCollection**](CrawlApi.md#postCrawlCollection) | **POST** /crawls | Creates a Crawl resource. |


<a id="cancelCrawlItem"></a>
# **cancelCrawlItem**
> CrawlReadDetails cancelCrawlItem(id, crawl)

Creates a Crawl resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrawlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    CrawlApi apiInstance = new CrawlApi(defaultClient);
    String id = "id_example"; // String | 
    Crawl crawl = new Crawl(); // Crawl | The new Crawl resource
    try {
      CrawlReadDetails result = apiInstance.cancelCrawlItem(id, crawl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrawlApi#cancelCrawlItem");
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
| **crawl** | [**Crawl**](Crawl.md)| The new Crawl resource | [optional] |

### Return type

[**CrawlReadDetails**](CrawlReadDetails.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Crawl resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="getCrawlCollection"></a>
# **getCrawlCollection**
> List&lt;CrawlRead&gt; getCrawlCollection(projectId, firstUrl, sortCreatedAt, page)

Retrieves the collection of Crawl resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrawlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    CrawlApi apiInstance = new CrawlApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    String firstUrl = "firstUrl_example"; // String | 
    String sortCreatedAt = "sortCreatedAt_example"; // String | 
    Integer page = 56; // Integer | The collection page number
    try {
      List<CrawlRead> result = apiInstance.getCrawlCollection(projectId, firstUrl, sortCreatedAt, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrawlApi#getCrawlCollection");
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
| **projectId** | **String**|  | |
| **firstUrl** | **String**|  | [optional] |
| **sortCreatedAt** | **String**|  | [optional] |
| **page** | **Integer**| The collection page number | [optional] |

### Return type

[**List&lt;CrawlRead&gt;**](CrawlRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Crawl collection response |  -  |

<a id="getCrawlItem"></a>
# **getCrawlItem**
> CrawlReadDetails getCrawlItem(id)

Retrieves a Crawl resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrawlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    CrawlApi apiInstance = new CrawlApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      CrawlReadDetails result = apiInstance.getCrawlItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrawlApi#getCrawlItem");
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

[**CrawlReadDetails**](CrawlReadDetails.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Crawl resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postCrawlCollection"></a>
# **postCrawlCollection**
> Crawl postCrawlCollection(crawl)

Creates a Crawl resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrawlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    CrawlApi apiInstance = new CrawlApi(defaultClient);
    CrawlWrite crawl = new CrawlWrite(); // CrawlWrite | The new Crawl resource
    try {
      Crawl result = apiInstance.postCrawlCollection(crawl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrawlApi#postCrawlCollection");
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
| **crawl** | [**CrawlWrite**](CrawlWrite.md)| The new Crawl resource | [optional] |

### Return type

[**Crawl**](Crawl.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Crawl resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

