# ResponseInspectionApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cacheGet**](ResponseInspectionApi.md#cacheGet) | **GET** /cache | Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise. |
| [**cacheValueGet**](ResponseInspectionApi.md#cacheValueGet) | **GET** /cache/{value} | Sets a Cache-Control header for n seconds. |
| [**etagEtagGet**](ResponseInspectionApi.md#etagEtagGet) | **GET** /etag/{etag} | Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately. |
| [**responseHeadersGet**](ResponseInspectionApi.md#responseHeadersGet) | **GET** /response-headers | Returns a set of response headers from the query string. |
| [**responseHeadersPost**](ResponseInspectionApi.md#responseHeadersPost) | **POST** /response-headers | Returns a set of response headers from the query string. |


<a id="cacheGet"></a>
# **cacheGet**
> cacheGet(ifModifiedSince, ifNoneMatch)

Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseInspectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseInspectionApi apiInstance = new ResponseInspectionApi(defaultClient);
    String ifModifiedSince = "ifModifiedSince_example"; // String | 
    String ifNoneMatch = "ifNoneMatch_example"; // String | 
    try {
      apiInstance.cacheGet(ifModifiedSince, ifNoneMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseInspectionApi#cacheGet");
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
| **ifModifiedSince** | **String**|  | [optional] |
| **ifNoneMatch** | **String**|  | [optional] |

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
| **200** | Cached response |  -  |
| **304** | Modified |  -  |

<a id="cacheValueGet"></a>
# **cacheValueGet**
> cacheValueGet(value)

Sets a Cache-Control header for n seconds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseInspectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseInspectionApi apiInstance = new ResponseInspectionApi(defaultClient);
    Integer value = 56; // Integer | 
    try {
      apiInstance.cacheValueGet(value);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseInspectionApi#cacheValueGet");
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
| **value** | **Integer**|  | |

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
| **200** | Cache control set |  -  |

<a id="etagEtagGet"></a>
# **etagEtagGet**
> etagEtagGet(etag, ifNoneMatch, ifMatch)

Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseInspectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseInspectionApi apiInstance = new ResponseInspectionApi(defaultClient);
    String etag = "etag_example"; // String | Automatically added
    String ifNoneMatch = "ifNoneMatch_example"; // String | 
    String ifMatch = "ifMatch_example"; // String | 
    try {
      apiInstance.etagEtagGet(etag, ifNoneMatch, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseInspectionApi#etagEtagGet");
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
| **etag** | **String**| Automatically added | |
| **ifNoneMatch** | **String**|  | [optional] |
| **ifMatch** | **String**|  | [optional] |

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
| **200** | Normal response |  -  |
| **412** | match |  -  |

<a id="responseHeadersGet"></a>
# **responseHeadersGet**
> responseHeadersGet(freeform)

Returns a set of response headers from the query string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseInspectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseInspectionApi apiInstance = new ResponseInspectionApi(defaultClient);
    Map<String, String> freeform = new HashMap(); // Map<String, String> | 
    try {
      apiInstance.responseHeadersGet(freeform);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseInspectionApi#responseHeadersGet");
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
| **freeform** | [**Map&lt;String, String&gt;**](String.md)|  | [optional] |

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
| **200** | Response headers |  -  |

<a id="responseHeadersPost"></a>
# **responseHeadersPost**
> responseHeadersPost(freeform)

Returns a set of response headers from the query string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseInspectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseInspectionApi apiInstance = new ResponseInspectionApi(defaultClient);
    Map<String, String> freeform = new HashMap(); // Map<String, String> | 
    try {
      apiInstance.responseHeadersPost(freeform);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseInspectionApi#responseHeadersPost");
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
| **freeform** | [**Map&lt;String, String&gt;**](String.md)|  | [optional] |

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
| **200** | Response headers |  -  |

