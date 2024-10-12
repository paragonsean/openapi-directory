# DefaultApi

All URIs are relative to *https://api.archive.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchV1FieldsGet**](DefaultApi.md#searchV1FieldsGet) | **GET** /search/v1/fields |  |
| [**searchV1OrganicGet**](DefaultApi.md#searchV1OrganicGet) | **GET** /search/v1/organic |  |
| [**searchV1ScrapeGet**](DefaultApi.md#searchV1ScrapeGet) | **GET** /search/v1/scrape |  |


<a id="searchV1FieldsGet"></a>
# **searchV1FieldsGet**
> List&lt;String&gt; searchV1FieldsGet(paramCallback)



Fields that can be requested

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.archive.org");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String paramCallback = "paramCallback_example"; // String | Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.
    try {
      List<String> result = apiInstance.searchV1FieldsGet(paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#searchV1FieldsGet");
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
| **paramCallback** | **String**| Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Fields that can be requested |  -  |

<a id="searchV1OrganicGet"></a>
# **searchV1OrganicGet**
> OrganicResult searchV1OrganicGet(q, field, size, totalOnly, paramCallback)



Return relevance-based results from search queries 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.archive.org");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String q = "q_example"; // String | Lucene-type search query
    String field = "identifier"; // String | Metadata field
    Integer size = 1000; // Integer | Number of query results to return
    Boolean totalOnly = false; // Boolean | Request total only; do not return hits
    String paramCallback = "paramCallback_example"; // String | Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.
    try {
      OrganicResult result = apiInstance.searchV1OrganicGet(q, field, size, totalOnly, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#searchV1OrganicGet");
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
| **q** | **String**| Lucene-type search query | [optional] |
| **field** | **String**| Metadata field | [optional] [default to identifier] |
| **size** | **Integer**| Number of query results to return | [optional] [default to 1000] |
| **totalOnly** | **Boolean**| Request total only; do not return hits | [optional] [default to false] |
| **paramCallback** | **String**| Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. | [optional] |

### Return type

[**OrganicResult**](OrganicResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organic Search API. Returns results in descending relevance order |  -  |
| **0** | Unexpected error |  -  |

<a id="searchV1ScrapeGet"></a>
# **searchV1ScrapeGet**
> ScrapeResult searchV1ScrapeGet(q, field, sort, size, cursor, totalOnly, paramCallback)



Scrape search results from Internet Archive, allowing a scrolling cursor 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.archive.org");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String q = "q_example"; // String | Lucene-type search query
    String field = "identifier"; // String | Metadata field
    String sort = "sort_example"; // String | sort collations
    Integer size = 1000; // Integer | Number of query results to return
    String cursor = "cursor_example"; // String | Cursor for scrolling (used for subsequent calls)
    Boolean totalOnly = false; // Boolean | Request total only; do not return hits
    String paramCallback = "paramCallback_example"; // String | Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.
    try {
      ScrapeResult result = apiInstance.searchV1ScrapeGet(q, field, sort, size, cursor, totalOnly, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#searchV1ScrapeGet");
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
| **q** | **String**| Lucene-type search query | [optional] |
| **field** | **String**| Metadata field | [optional] [default to identifier] |
| **sort** | **String**| sort collations | [optional] |
| **size** | **Integer**| Number of query results to return | [optional] [default to 1000] |
| **cursor** | **String**| Cursor for scrolling (used for subsequent calls) | [optional] |
| **totalOnly** | **Boolean**| Request total only; do not return hits | [optional] [default to false] |
| **paramCallback** | **String**| Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. | [optional] |

### Return type

[**ScrapeResult**](ScrapeResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Scaping API |  -  |
| **0** | Unexpected error |  -  |

