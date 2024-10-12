# IconApi

All URIs are relative to *http://api.thenounproject.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getIconById**](IconApi.md#getIconById) | **GET** /icon/{id} | Get icon by id |
| [**getIconByTerm**](IconApi.md#getIconByTerm) | **GET** /icon/{term} | Get icon by term |


<a id="getIconById"></a>
# **getIconById**
> getIconById(id)

Get icon by id

Returns a single icon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IconApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    IconApi apiInstance = new IconApi(defaultClient);
    Integer id = 56; // Integer | Icon id
    try {
      apiInstance.getIconById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IconApi#getIconById");
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
| **id** | **Integer**| Icon id | |

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

<a id="getIconByTerm"></a>
# **getIconByTerm**
> getIconByTerm(term)

Get icon by term

Returns a single icon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IconApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    IconApi apiInstance = new IconApi(defaultClient);
    String term = "term_example"; // String | Icon term
    try {
      apiInstance.getIconByTerm(term);
    } catch (ApiException e) {
      System.err.println("Exception when calling IconApi#getIconByTerm");
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

