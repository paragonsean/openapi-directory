# HttpMethodsApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDelete**](HttpMethodsApi.md#deleteDelete) | **DELETE** /delete | The request&#39;s DELETE parameters. |
| [**getGet**](HttpMethodsApi.md#getGet) | **GET** /get | The request&#39;s query parameters. |
| [**patchPatch**](HttpMethodsApi.md#patchPatch) | **PATCH** /patch | The request&#39;s PATCH parameters. |
| [**postPost**](HttpMethodsApi.md#postPost) | **POST** /post | The request&#39;s POST parameters. |
| [**putPut**](HttpMethodsApi.md#putPut) | **PUT** /put | The request&#39;s PUT parameters. |


<a id="deleteDelete"></a>
# **deleteDelete**
> deleteDelete()

The request&#39;s DELETE parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HttpMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    HttpMethodsApi apiInstance = new HttpMethodsApi(defaultClient);
    try {
      apiInstance.deleteDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling HttpMethodsApi#deleteDelete");
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
| **200** | The request&#39;s DELETE parameters. |  -  |

<a id="getGet"></a>
# **getGet**
> getGet()

The request&#39;s query parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HttpMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    HttpMethodsApi apiInstance = new HttpMethodsApi(defaultClient);
    try {
      apiInstance.getGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling HttpMethodsApi#getGet");
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
| **200** | The request&#39;s query parameters. |  -  |

<a id="patchPatch"></a>
# **patchPatch**
> patchPatch()

The request&#39;s PATCH parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HttpMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    HttpMethodsApi apiInstance = new HttpMethodsApi(defaultClient);
    try {
      apiInstance.patchPatch();
    } catch (ApiException e) {
      System.err.println("Exception when calling HttpMethodsApi#patchPatch");
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
| **200** | The request&#39;s PATCH parameters. |  -  |

<a id="postPost"></a>
# **postPost**
> postPost()

The request&#39;s POST parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HttpMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    HttpMethodsApi apiInstance = new HttpMethodsApi(defaultClient);
    try {
      apiInstance.postPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling HttpMethodsApi#postPost");
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
| **200** | The request&#39;s POST parameters. |  -  |

<a id="putPut"></a>
# **putPut**
> putPut()

The request&#39;s PUT parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HttpMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    HttpMethodsApi apiInstance = new HttpMethodsApi(defaultClient);
    try {
      apiInstance.putPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling HttpMethodsApi#putPut");
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
| **200** | The request&#39;s PUT parameters. |  -  |

