# ImagesApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**imageGet**](ImagesApi.md#imageGet) | **GET** /image | Returns a simple image of the type suggest by the Accept header. |
| [**imageJpegGet**](ImagesApi.md#imageJpegGet) | **GET** /image/jpeg | Returns a simple JPEG image. |
| [**imagePngGet**](ImagesApi.md#imagePngGet) | **GET** /image/png | Returns a simple PNG image. |
| [**imageSvgGet**](ImagesApi.md#imageSvgGet) | **GET** /image/svg | Returns a simple SVG image. |
| [**imageWebpGet**](ImagesApi.md#imageWebpGet) | **GET** /image/webp | Returns a simple WEBP image. |


<a id="imageGet"></a>
# **imageGet**
> imageGet()

Returns a simple image of the type suggest by the Accept header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    try {
      apiInstance.imageGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imageGet");
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
| **200** | An image. |  -  |

<a id="imageJpegGet"></a>
# **imageJpegGet**
> imageJpegGet()

Returns a simple JPEG image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    try {
      apiInstance.imageJpegGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imageJpegGet");
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
| **200** | A JPEG image. |  -  |

<a id="imagePngGet"></a>
# **imagePngGet**
> imagePngGet()

Returns a simple PNG image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    try {
      apiInstance.imagePngGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imagePngGet");
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
| **200** | A PNG image. |  -  |

<a id="imageSvgGet"></a>
# **imageSvgGet**
> imageSvgGet()

Returns a simple SVG image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    try {
      apiInstance.imageSvgGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imageSvgGet");
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
| **200** | An SVG image. |  -  |

<a id="imageWebpGet"></a>
# **imageWebpGet**
> imageWebpGet()

Returns a simple WEBP image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    ImagesApi apiInstance = new ImagesApi(defaultClient);
    try {
      apiInstance.imageWebpGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ImagesApi#imageWebpGet");
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
| **200** | A WEBP image. |  -  |

