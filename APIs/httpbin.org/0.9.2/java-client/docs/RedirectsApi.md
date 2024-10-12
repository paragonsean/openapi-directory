# RedirectsApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**absoluteRedirectNGet**](RedirectsApi.md#absoluteRedirectNGet) | **GET** /absolute-redirect/{n} | Absolutely 302 Redirects n times. |
| [**redirectNGet**](RedirectsApi.md#redirectNGet) | **GET** /redirect/{n} | 302 Redirects n times. |
| [**redirectToDelete**](RedirectsApi.md#redirectToDelete) | **DELETE** /redirect-to | 302/3XX Redirects to the given URL. |
| [**redirectToGet**](RedirectsApi.md#redirectToGet) | **GET** /redirect-to | 302/3XX Redirects to the given URL. |
| [**redirectToPatch**](RedirectsApi.md#redirectToPatch) | **PATCH** /redirect-to | 302/3XX Redirects to the given URL. |
| [**redirectToPost**](RedirectsApi.md#redirectToPost) | **POST** /redirect-to | 302/3XX Redirects to the given URL. |
| [**redirectToPut**](RedirectsApi.md#redirectToPut) | **PUT** /redirect-to | 302/3XX Redirects to the given URL. |
| [**redirectToTrace**](RedirectsApi.md#redirectToTrace) | **TRACE** /redirect-to | 302/3XX Redirects to the given URL. |
| [**relativeRedirectNGet**](RedirectsApi.md#relativeRedirectNGet) | **GET** /relative-redirect/{n} | Relatively 302 Redirects n times. |


<a id="absoluteRedirectNGet"></a>
# **absoluteRedirectNGet**
> absoluteRedirectNGet(n)

Absolutely 302 Redirects n times.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedirectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RedirectsApi apiInstance = new RedirectsApi(defaultClient);
    Integer n = 56; // Integer | 
    try {
      apiInstance.absoluteRedirectNGet(n);
    } catch (ApiException e) {
      System.err.println("Exception when calling RedirectsApi#absoluteRedirectNGet");
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
| **302** | A redirection. |  -  |

<a id="redirectNGet"></a>
# **redirectNGet**
> redirectNGet(n)

302 Redirects n times.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedirectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RedirectsApi apiInstance = new RedirectsApi(defaultClient);
    Integer n = 56; // Integer | 
    try {
      apiInstance.redirectNGet(n);
    } catch (ApiException e) {
      System.err.println("Exception when calling RedirectsApi#redirectNGet");
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
| **302** | A redirection. |  -  |

<a id="redirectToDelete"></a>
# **redirectToDelete**
> redirectToDelete()

302/3XX Redirects to the given URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedirectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RedirectsApi apiInstance = new RedirectsApi(defaultClient);
    try {
      apiInstance.redirectToDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling RedirectsApi#redirectToDelete");
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
| **302** | A redirection. |  -  |

<a id="redirectToGet"></a>
# **redirectToGet**
> redirectToGet(url, statusCode)

302/3XX Redirects to the given URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedirectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RedirectsApi apiInstance = new RedirectsApi(defaultClient);
    String url = "url_example"; // String | 
    Integer statusCode = 56; // Integer | 
    try {
      apiInstance.redirectToGet(url, statusCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling RedirectsApi#redirectToGet");
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
| **url** | **String**|  | |
| **statusCode** | **Integer**|  | [optional] |

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
| **302** | A redirection. |  -  |

<a id="redirectToPatch"></a>
# **redirectToPatch**
> redirectToPatch()

302/3XX Redirects to the given URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedirectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RedirectsApi apiInstance = new RedirectsApi(defaultClient);
    try {
      apiInstance.redirectToPatch();
    } catch (ApiException e) {
      System.err.println("Exception when calling RedirectsApi#redirectToPatch");
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
| **302** | A redirection. |  -  |

<a id="redirectToPost"></a>
# **redirectToPost**
> redirectToPost(url, statusCode)

302/3XX Redirects to the given URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedirectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RedirectsApi apiInstance = new RedirectsApi(defaultClient);
    String url = "url_example"; // String | 
    Integer statusCode = 56; // Integer | 
    try {
      apiInstance.redirectToPost(url, statusCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling RedirectsApi#redirectToPost");
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
| **url** | **String**|  | |
| **statusCode** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | A redirection. |  -  |

<a id="redirectToPut"></a>
# **redirectToPut**
> redirectToPut(url, statusCode)

302/3XX Redirects to the given URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedirectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RedirectsApi apiInstance = new RedirectsApi(defaultClient);
    String url = "url_example"; // String | 
    Integer statusCode = 56; // Integer | 
    try {
      apiInstance.redirectToPut(url, statusCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling RedirectsApi#redirectToPut");
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
| **url** | **String**|  | |
| **statusCode** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | A redirection. |  -  |

<a id="redirectToTrace"></a>
# **redirectToTrace**
> redirectToTrace()

302/3XX Redirects to the given URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedirectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RedirectsApi apiInstance = new RedirectsApi(defaultClient);
    try {
      apiInstance.redirectToTrace();
    } catch (ApiException e) {
      System.err.println("Exception when calling RedirectsApi#redirectToTrace");
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
| **302** | A redirection. |  -  |

<a id="relativeRedirectNGet"></a>
# **relativeRedirectNGet**
> relativeRedirectNGet(n)

Relatively 302 Redirects n times.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedirectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RedirectsApi apiInstance = new RedirectsApi(defaultClient);
    Integer n = 56; // Integer | 
    try {
      apiInstance.relativeRedirectNGet(n);
    } catch (ApiException e) {
      System.err.println("Exception when calling RedirectsApi#relativeRedirectNGet");
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
| **302** | A redirection. |  -  |

