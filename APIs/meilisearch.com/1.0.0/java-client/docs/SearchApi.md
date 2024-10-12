# SearchApi

All URIs are relative to *http://localhost:7700*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchInIndex**](SearchApi.md#searchInIndex) | **GET** /indexes/books/search | Search in index |
| [**searchInIndex1**](SearchApi.md#searchInIndex1) | **POST** /indexes/books/search | Search in index |


<a id="searchInIndex"></a>
# **searchInIndex**
> searchInIndex(q, offset, limit, attributesToRetrieve, attributesToCrop, attributesToHighlight, cropLength, cropMarker, filter, showMatchesPosition, facets, sort, highlightPreTag, highlightPostTag, matchingStrategy, page, hitsPerPage)

Search in index

Search in index

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
    defaultClient.setBasePath("http://localhost:7700");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String q = "prinec"; // String | 
    String offset = "0"; // String | 
    String limit = "1"; // String | 
    String attributesToRetrieve = "title,author"; // String | 
    String attributesToCrop = "title"; // String | 
    String attributesToHighlight = "*"; // String | 
    String cropLength = "5"; // String | 
    String cropMarker = "[...]"; // String | 
    String filter = "genre=\"fantasy\""; // String | 
    String showMatchesPosition = "true"; // String | 
    String facets = "genre"; // String | 
    String sort = "price"; // String | 
    String highlightPreTag = "<mark>"; // String | 
    String highlightPostTag = "</mark>"; // String | 
    String matchingStrategy = "all"; // String | 
    String page = "2"; // String | 
    String hitsPerPage = "50"; // String | 
    try {
      apiInstance.searchInIndex(q, offset, limit, attributesToRetrieve, attributesToCrop, attributesToHighlight, cropLength, cropMarker, filter, showMatchesPosition, facets, sort, highlightPreTag, highlightPostTag, matchingStrategy, page, hitsPerPage);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchInIndex");
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
| **q** | **String**|  | [optional] |
| **offset** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |
| **attributesToRetrieve** | **String**|  | [optional] |
| **attributesToCrop** | **String**|  | [optional] |
| **attributesToHighlight** | **String**|  | [optional] |
| **cropLength** | **String**|  | [optional] |
| **cropMarker** | **String**|  | [optional] |
| **filter** | **String**|  | [optional] |
| **showMatchesPosition** | **String**|  | [optional] |
| **facets** | **String**|  | [optional] |
| **sort** | **String**|  | [optional] |
| **highlightPreTag** | **String**|  | [optional] |
| **highlightPostTag** | **String**|  | [optional] |
| **matchingStrategy** | **String**|  | [optional] |
| **page** | **String**|  | [optional] |
| **hitsPerPage** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="searchInIndex1"></a>
# **searchInIndex1**
> searchInIndex1(searchInIndex1Request)

Search in index

Search in index

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
    defaultClient.setBasePath("http://localhost:7700");

    SearchApi apiInstance = new SearchApi(defaultClient);
    SearchInIndex1Request searchInIndex1Request = new SearchInIndex1Request(); // SearchInIndex1Request | 
    try {
      apiInstance.searchInIndex1(searchInIndex1Request);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchInIndex1");
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
| **searchInIndex1Request** | [**SearchInIndex1Request**](SearchInIndex1Request.md)|  | [optional] |

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
| **200** |  |  -  |

