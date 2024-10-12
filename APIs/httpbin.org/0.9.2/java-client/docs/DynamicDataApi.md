# DynamicDataApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**base64ValueGet**](DynamicDataApi.md#base64ValueGet) | **GET** /base64/{value} | Decodes base64url-encoded string. |
| [**bytesNGet**](DynamicDataApi.md#bytesNGet) | **GET** /bytes/{n} | Returns n random bytes generated with given seed |
| [**delayDelayDelete**](DynamicDataApi.md#delayDelayDelete) | **DELETE** /delay/{delay} | Returns a delayed response (max of 10 seconds). |
| [**delayDelayGet**](DynamicDataApi.md#delayDelayGet) | **GET** /delay/{delay} | Returns a delayed response (max of 10 seconds). |
| [**delayDelayPatch**](DynamicDataApi.md#delayDelayPatch) | **PATCH** /delay/{delay} | Returns a delayed response (max of 10 seconds). |
| [**delayDelayPost**](DynamicDataApi.md#delayDelayPost) | **POST** /delay/{delay} | Returns a delayed response (max of 10 seconds). |
| [**delayDelayPut**](DynamicDataApi.md#delayDelayPut) | **PUT** /delay/{delay} | Returns a delayed response (max of 10 seconds). |
| [**delayDelayTrace**](DynamicDataApi.md#delayDelayTrace) | **TRACE** /delay/{delay} | Returns a delayed response (max of 10 seconds). |
| [**dripGet**](DynamicDataApi.md#dripGet) | **GET** /drip | Drips data over a duration after an optional initial delay. |
| [**linksNOffsetGet**](DynamicDataApi.md#linksNOffsetGet) | **GET** /links/{n}/{offset} | Generate a page containing n links to other pages which do the same. |
| [**rangeNumbytesGet**](DynamicDataApi.md#rangeNumbytesGet) | **GET** /range/{numbytes} | Streams n random bytes generated with given seed, at given chunk size per packet. |
| [**streamBytesNGet**](DynamicDataApi.md#streamBytesNGet) | **GET** /stream-bytes/{n} | Streams n random bytes generated with given seed, at given chunk size per packet. |
| [**streamNGet**](DynamicDataApi.md#streamNGet) | **GET** /stream/{n} | Stream n JSON responses |
| [**uuidGet**](DynamicDataApi.md#uuidGet) | **GET** /uuid | Return a UUID4. |


<a id="base64ValueGet"></a>
# **base64ValueGet**
> base64ValueGet(value)

Decodes base64url-encoded string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    String value = "SFRUUEJJTiBpcyBhd2Vzb21l"; // String | 
    try {
      apiInstance.base64ValueGet(value);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#base64ValueGet");
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
| **value** | **String**|  | [default to SFRUUEJJTiBpcyBhd2Vzb21l] |

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
| **200** | Decoded base64 content. |  -  |

<a id="bytesNGet"></a>
# **bytesNGet**
> bytesNGet(n)

Returns n random bytes generated with given seed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer n = 56; // Integer | 
    try {
      apiInstance.bytesNGet(n);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#bytesNGet");
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
| **n** | **Integer**|  | |

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
| **200** | Bytes. |  -  |

<a id="delayDelayDelete"></a>
# **delayDelayDelete**
> delayDelayDelete(delay)

Returns a delayed response (max of 10 seconds).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer delay = 56; // Integer | 
    try {
      apiInstance.delayDelayDelete(delay);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#delayDelayDelete");
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
| **delay** | **Integer**|  | |

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
| **200** | A delayed response. |  -  |

<a id="delayDelayGet"></a>
# **delayDelayGet**
> delayDelayGet(delay)

Returns a delayed response (max of 10 seconds).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer delay = 56; // Integer | 
    try {
      apiInstance.delayDelayGet(delay);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#delayDelayGet");
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
| **delay** | **Integer**|  | |

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
| **200** | A delayed response. |  -  |

<a id="delayDelayPatch"></a>
# **delayDelayPatch**
> delayDelayPatch(delay)

Returns a delayed response (max of 10 seconds).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer delay = 56; // Integer | 
    try {
      apiInstance.delayDelayPatch(delay);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#delayDelayPatch");
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
| **delay** | **Integer**|  | |

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
| **200** | A delayed response. |  -  |

<a id="delayDelayPost"></a>
# **delayDelayPost**
> delayDelayPost(delay)

Returns a delayed response (max of 10 seconds).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer delay = 56; // Integer | 
    try {
      apiInstance.delayDelayPost(delay);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#delayDelayPost");
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
| **delay** | **Integer**|  | |

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
| **200** | A delayed response. |  -  |

<a id="delayDelayPut"></a>
# **delayDelayPut**
> delayDelayPut(delay)

Returns a delayed response (max of 10 seconds).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer delay = 56; // Integer | 
    try {
      apiInstance.delayDelayPut(delay);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#delayDelayPut");
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
| **delay** | **Integer**|  | |

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
| **200** | A delayed response. |  -  |

<a id="delayDelayTrace"></a>
# **delayDelayTrace**
> delayDelayTrace(delay)

Returns a delayed response (max of 10 seconds).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer delay = 56; // Integer | 
    try {
      apiInstance.delayDelayTrace(delay);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#delayDelayTrace");
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
| **delay** | **Integer**|  | |

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
| **200** | A delayed response. |  -  |

<a id="dripGet"></a>
# **dripGet**
> dripGet(duration, numbytes, code, delay)

Drips data over a duration after an optional initial delay.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    BigDecimal duration = new BigDecimal("2"); // BigDecimal | The amount of time (in seconds) over which to drip each byte
    Integer numbytes = 10; // Integer | The number of bytes to respond with
    Integer code = 200; // Integer | The response code that will be returned
    BigDecimal delay = new BigDecimal("2"); // BigDecimal | The amount of time (in seconds) to delay before responding
    try {
      apiInstance.dripGet(duration, numbytes, code, delay);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#dripGet");
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
| **duration** | **BigDecimal**| The amount of time (in seconds) over which to drip each byte | [optional] [default to 2] |
| **numbytes** | **Integer**| The number of bytes to respond with | [optional] [default to 10] |
| **code** | **Integer**| The response code that will be returned | [optional] [default to 200] |
| **delay** | **BigDecimal**| The amount of time (in seconds) to delay before responding | [optional] [default to 2] |

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
| **200** | A dripped response. |  -  |

<a id="linksNOffsetGet"></a>
# **linksNOffsetGet**
> linksNOffsetGet(n, offset)

Generate a page containing n links to other pages which do the same.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer n = 56; // Integer | 
    Integer offset = 56; // Integer | 
    try {
      apiInstance.linksNOffsetGet(n, offset);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#linksNOffsetGet");
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
| **n** | **Integer**|  | |
| **offset** | **Integer**|  | |

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
| **200** | HTML links. |  -  |

<a id="rangeNumbytesGet"></a>
# **rangeNumbytesGet**
> rangeNumbytesGet(numbytes)

Streams n random bytes generated with given seed, at given chunk size per packet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer numbytes = 56; // Integer | 
    try {
      apiInstance.rangeNumbytesGet(numbytes);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#rangeNumbytesGet");
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
| **numbytes** | **Integer**|  | |

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
| **200** | Bytes. |  -  |

<a id="streamBytesNGet"></a>
# **streamBytesNGet**
> streamBytesNGet(n)

Streams n random bytes generated with given seed, at given chunk size per packet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer n = 56; // Integer | 
    try {
      apiInstance.streamBytesNGet(n);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#streamBytesNGet");
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
| **n** | **Integer**|  | |

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
| **200** | Bytes. |  -  |

<a id="streamNGet"></a>
# **streamNGet**
> streamNGet(n)

Stream n JSON responses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    Integer n = 56; // Integer | 
    try {
      apiInstance.streamNGet(n);
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#streamNGet");
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
| **n** | **Integer**|  | |

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
| **200** | Streamed JSON responses. |  -  |

<a id="uuidGet"></a>
# **uuidGet**
> uuidGet()

Return a UUID4.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DynamicDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    DynamicDataApi apiInstance = new DynamicDataApi(defaultClient);
    try {
      apiInstance.uuidGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DynamicDataApi#uuidGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | A UUID4. |  -  |

