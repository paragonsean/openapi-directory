# CollectionApi

All URIs are relative to *http://api.thenounproject.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCollectionById**](CollectionApi.md#getCollectionById) | **GET** /collection/{id} | Get collection by id |
| [**getCollectionBySlug**](CollectionApi.md#getCollectionBySlug) | **GET** /collection/{slug} | Get collection by slug |
| [**getCollectionIconsById**](CollectionApi.md#getCollectionIconsById) | **GET** /collection/{id}/icons | Get collection icons by id |
| [**getCollectionIconsBySlug**](CollectionApi.md#getCollectionIconsBySlug) | **GET** /collection/{slug}/icons | Get collection icons by slug |


<a id="getCollectionById"></a>
# **getCollectionById**
> getCollectionById(id)

Get collection by id

Returns a single collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    Integer id = 56; // Integer | Collection id
    try {
      apiInstance.getCollectionById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#getCollectionById");
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
| **id** | **Integer**| Collection id | |

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

<a id="getCollectionBySlug"></a>
# **getCollectionBySlug**
> getCollectionBySlug(slug)

Get collection by slug

Returns a single collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String slug = "slug_example"; // String | Collection slug
    try {
      apiInstance.getCollectionBySlug(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#getCollectionBySlug");
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
| **slug** | **String**| Collection slug | |

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

<a id="getCollectionIconsById"></a>
# **getCollectionIconsById**
> getCollectionIconsById(id, limit, offset, page)

Get collection icons by id

Returns a list of icons associated with a collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    Integer id = 56; // Integer | Collection id
    Integer limit = 56; // Integer | Maximum number of results
    Integer offset = 56; // Integer | Number of results to displace or skip over
    Integer page = 56; // Integer | Number of results of limit length to displace or skip over
    try {
      apiInstance.getCollectionIconsById(id, limit, offset, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#getCollectionIconsById");
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
| **id** | **Integer**| Collection id | |
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

<a id="getCollectionIconsBySlug"></a>
# **getCollectionIconsBySlug**
> getCollectionIconsBySlug(slug, limit, offset, page)

Get collection icons by slug

Returns a list of icons associated with a collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String slug = "slug_example"; // String | Collection slug
    Integer limit = 56; // Integer | Maximum number of results
    Integer offset = 56; // Integer | Number of results to displace or skip over
    Integer page = 56; // Integer | Number of results of limit length to displace or skip over
    try {
      apiInstance.getCollectionIconsBySlug(slug, limit, offset, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#getCollectionIconsBySlug");
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
| **slug** | **String**| Collection slug | |
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

