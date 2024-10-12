# IconsApi

All URIs are relative to *http://api.thenounproject.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getIconsByTerm**](IconsApi.md#getIconsByTerm) | **GET** /icons/{term} | Get icons by term |
| [**getRecentIcons**](IconsApi.md#getRecentIcons) | **GET** /icons/recent_uploads | Get recent icons |


<a id="getIconsByTerm"></a>
# **getIconsByTerm**
> getIconsByTerm(term, limitToPublicDomain, limit, offset, page)

Get icons by term

Returns a list of icons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    IconsApi apiInstance = new IconsApi(defaultClient);
    String term = "term_example"; // String | Icon term
    Integer limitToPublicDomain = 56; // Integer | Limit results to public domain icons only
    Integer limit = 56; // Integer | Maximum number of results
    Integer offset = 56; // Integer | Number of results to displace or skip over
    Integer page = 56; // Integer | Number of results of limit length to displace or skip over
    try {
      apiInstance.getIconsByTerm(term, limitToPublicDomain, limit, offset, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling IconsApi#getIconsByTerm");
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
| **term** | **String**| Icon term | |
| **limitToPublicDomain** | **Integer**| Limit results to public domain icons only | [optional] |
| **limit** | **Integer**| Maximum number of results | [optional] |
| **offset** | **Integer**| Number of results to displace or skip over | [optional] |
| **page** | **Integer**| Number of results of limit length to displace or skip over | [optional] |

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
| **200** | No response was specified |  -  |

<a id="getRecentIcons"></a>
# **getRecentIcons**
> getRecentIcons(limit, offset, page)

Get recent icons

Returns list of most recently uploaded icons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    IconsApi apiInstance = new IconsApi(defaultClient);
    Integer limit = 56; // Integer | Maximum number of results
    Integer offset = 56; // Integer | Number of results to displace or skip over
    Integer page = 56; // Integer | Number of results of limit length to displace or skip over
    try {
      apiInstance.getRecentIcons(limit, offset, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling IconsApi#getRecentIcons");
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
| **limit** | **Integer**| Maximum number of results | [optional] |
| **offset** | **Integer**| Number of results to displace or skip over | [optional] |
| **page** | **Integer**| Number of results of limit length to displace or skip over | [optional] |

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
| **200** | No response was specified |  -  |

