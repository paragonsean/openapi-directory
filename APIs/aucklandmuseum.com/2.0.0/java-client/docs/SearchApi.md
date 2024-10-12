# SearchApi

All URIs are relative to *http://api.aucklandmuseum.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSearch**](SearchApi.md#getSearch) | **GET** /search/{index}/{operation} | Perform simple search queries over Auckland Museum Collections and Cenotaph data |
| [**postSearch**](SearchApi.md#postSearch) | **POST** /search/{index}/{operation} | Perform complex search queries over Auckland Museum Collections and Cenotaph data |


<a id="getSearch"></a>
# **getSearch**
> getSearch(index, operation, q)

Perform simple search queries over Auckland Museum Collections and Cenotaph data

Use this endpoint to perform simple search queries for finding information and subjects you may be interested in  Searches performed via this endpoint run against an [Elastic](www.elastic.co) server. This endpoint mirrors the Elastic search API documented [here](https://www.elastic.co/guide/en/elasticsearch/reference/1.5/search-search.html)  Use the   - &#x60;collectionsonline&#x60; index to perform searches over other all Collections data   - &#x60;cenotaph&#x60; index to perform searches over Cenotaph data 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.aucklandmuseum.com");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String index = "index_example"; // String | search index name Possible values: * `collectionsonline` * `cenotaph` 
    String operation = "operation_example"; // String | One of the supported elasticsearch operations like `_search` or `_suggest`
    String q = "q_example"; // String | One of the supported elasticsearch query parameter values for key `q`
    try {
      apiInstance.getSearch(index, operation, q);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getSearch");
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
| **index** | **String**| search index name Possible values: * &#x60;collectionsonline&#x60; * &#x60;cenotaph&#x60;  | |
| **operation** | **String**| One of the supported elasticsearch operations like &#x60;_search&#x60; or &#x60;_suggest&#x60; | |
| **q** | **String**| One of the supported elasticsearch query parameter values for key &#x60;q&#x60; | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results found |  -  |
| **400** | bad request |  -  |
| **404** | not found |  -  |

<a id="postSearch"></a>
# **postSearch**
> postSearch(index, operation, body)

Perform complex search queries over Auckland Museum Collections and Cenotaph data

Searches performed via this endpoint run against an [Elastic](www.elastic.co) server. This endpoint mirrors the Elastic search API documented [here](https://www.elastic.co/guide/en/elasticsearch/reference/1.5/search-search.html)  Use the   - &#x60;collectionsonline&#x60; index to perform searches over other all Collections data   - &#x60;cenotaph&#x60; index to perform searches over Cenotaph data 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.aucklandmuseum.com");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String index = "index_example"; // String | search index name Possible values: * `collectionsonline` * `cenotaph` 
    String operation = "operation_example"; // String | One of the supported elasticsearch operations like `_search` or `_suggest`
    Object body = null; // Object | body
    try {
      apiInstance.postSearch(index, operation, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#postSearch");
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
| **index** | **String**| search index name Possible values: * &#x60;collectionsonline&#x60; * &#x60;cenotaph&#x60;  | |
| **operation** | **String**| One of the supported elasticsearch operations like &#x60;_search&#x60; or &#x60;_suggest&#x60; | |
| **body** | **Object**| body | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search results found |  -  |
| **400** | bad request |  -  |
| **404** | not found |  -  |

