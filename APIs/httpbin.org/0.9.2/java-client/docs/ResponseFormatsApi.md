# ResponseFormatsApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**brotliGet**](ResponseFormatsApi.md#brotliGet) | **GET** /brotli | Returns Brotli-encoded data. |
| [**deflateGet**](ResponseFormatsApi.md#deflateGet) | **GET** /deflate | Returns Deflate-encoded data. |
| [**denyGet**](ResponseFormatsApi.md#denyGet) | **GET** /deny | Returns page denied by robots.txt rules. |
| [**encodingUtf8Get**](ResponseFormatsApi.md#encodingUtf8Get) | **GET** /encoding/utf8 | Returns a UTF-8 encoded body. |
| [**gzipGet**](ResponseFormatsApi.md#gzipGet) | **GET** /gzip | Returns GZip-encoded data. |
| [**htmlGet**](ResponseFormatsApi.md#htmlGet) | **GET** /html | Returns a simple HTML document. |
| [**jsonGet**](ResponseFormatsApi.md#jsonGet) | **GET** /json | Returns a simple JSON document. |
| [**robotsTxtGet**](ResponseFormatsApi.md#robotsTxtGet) | **GET** /robots.txt | Returns some robots.txt rules. |
| [**xmlGet**](ResponseFormatsApi.md#xmlGet) | **GET** /xml | Returns a simple XML document. |


<a id="brotliGet"></a>
# **brotliGet**
> brotliGet()

Returns Brotli-encoded data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseFormatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseFormatsApi apiInstance = new ResponseFormatsApi(defaultClient);
    try {
      apiInstance.brotliGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseFormatsApi#brotliGet");
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
| **200** | Brotli-encoded data. |  -  |

<a id="deflateGet"></a>
# **deflateGet**
> deflateGet()

Returns Deflate-encoded data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseFormatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseFormatsApi apiInstance = new ResponseFormatsApi(defaultClient);
    try {
      apiInstance.deflateGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseFormatsApi#deflateGet");
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
| **200** | Defalte-encoded data. |  -  |

<a id="denyGet"></a>
# **denyGet**
> denyGet()

Returns page denied by robots.txt rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseFormatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseFormatsApi apiInstance = new ResponseFormatsApi(defaultClient);
    try {
      apiInstance.denyGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseFormatsApi#denyGet");
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
| **200** | Denied message |  -  |

<a id="encodingUtf8Get"></a>
# **encodingUtf8Get**
> encodingUtf8Get()

Returns a UTF-8 encoded body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseFormatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseFormatsApi apiInstance = new ResponseFormatsApi(defaultClient);
    try {
      apiInstance.encodingUtf8Get();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseFormatsApi#encodingUtf8Get");
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
| **200** | Encoded UTF-8 content. |  -  |

<a id="gzipGet"></a>
# **gzipGet**
> gzipGet()

Returns GZip-encoded data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseFormatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseFormatsApi apiInstance = new ResponseFormatsApi(defaultClient);
    try {
      apiInstance.gzipGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseFormatsApi#gzipGet");
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
| **200** | GZip-encoded data. |  -  |

<a id="htmlGet"></a>
# **htmlGet**
> htmlGet()

Returns a simple HTML document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseFormatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseFormatsApi apiInstance = new ResponseFormatsApi(defaultClient);
    try {
      apiInstance.htmlGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseFormatsApi#htmlGet");
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
| **200** | An HTML page. |  -  |

<a id="jsonGet"></a>
# **jsonGet**
> jsonGet()

Returns a simple JSON document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseFormatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseFormatsApi apiInstance = new ResponseFormatsApi(defaultClient);
    try {
      apiInstance.jsonGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseFormatsApi#jsonGet");
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
| **200** | An JSON document. |  -  |

<a id="robotsTxtGet"></a>
# **robotsTxtGet**
> robotsTxtGet()

Returns some robots.txt rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseFormatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseFormatsApi apiInstance = new ResponseFormatsApi(defaultClient);
    try {
      apiInstance.robotsTxtGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseFormatsApi#robotsTxtGet");
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
| **200** | Robots file |  -  |

<a id="xmlGet"></a>
# **xmlGet**
> xmlGet()

Returns a simple XML document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponseFormatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ResponseFormatsApi apiInstance = new ResponseFormatsApi(defaultClient);
    try {
      apiInstance.xmlGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponseFormatsApi#xmlGet");
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
| **200** | An XML document. |  -  |

