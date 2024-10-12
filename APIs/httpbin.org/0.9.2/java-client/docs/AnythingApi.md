# AnythingApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**anythingAnythingDelete**](AnythingApi.md#anythingAnythingDelete) | **DELETE** /anything/{anything} | Returns anything passed in request data. |
| [**anythingAnythingGet**](AnythingApi.md#anythingAnythingGet) | **GET** /anything/{anything} | Returns anything passed in request data. |
| [**anythingAnythingPatch**](AnythingApi.md#anythingAnythingPatch) | **PATCH** /anything/{anything} | Returns anything passed in request data. |
| [**anythingAnythingPost**](AnythingApi.md#anythingAnythingPost) | **POST** /anything/{anything} | Returns anything passed in request data. |
| [**anythingAnythingPut**](AnythingApi.md#anythingAnythingPut) | **PUT** /anything/{anything} | Returns anything passed in request data. |
| [**anythingAnythingTrace**](AnythingApi.md#anythingAnythingTrace) | **TRACE** /anything/{anything} | Returns anything passed in request data. |
| [**anythingDelete**](AnythingApi.md#anythingDelete) | **DELETE** /anything | Returns anything passed in request data. |
| [**anythingGet**](AnythingApi.md#anythingGet) | **GET** /anything | Returns anything passed in request data. |
| [**anythingPatch**](AnythingApi.md#anythingPatch) | **PATCH** /anything | Returns anything passed in request data. |
| [**anythingPost**](AnythingApi.md#anythingPost) | **POST** /anything | Returns anything passed in request data. |
| [**anythingPut**](AnythingApi.md#anythingPut) | **PUT** /anything | Returns anything passed in request data. |
| [**anythingTrace**](AnythingApi.md#anythingTrace) | **TRACE** /anything | Returns anything passed in request data. |


<a id="anythingAnythingDelete"></a>
# **anythingAnythingDelete**
> anythingAnythingDelete(anything)

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    String anything = "anything_example"; // String | Automatically added
    try {
      apiInstance.anythingAnythingDelete(anything);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingAnythingDelete");
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
| **anything** | **String**| Automatically added | |

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
| **200** | Anything passed in request |  -  |

<a id="anythingAnythingGet"></a>
# **anythingAnythingGet**
> anythingAnythingGet(anything)

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    String anything = "anything_example"; // String | Automatically added
    try {
      apiInstance.anythingAnythingGet(anything);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingAnythingGet");
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
| **anything** | **String**| Automatically added | |

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
| **200** | Anything passed in request |  -  |

<a id="anythingAnythingPatch"></a>
# **anythingAnythingPatch**
> anythingAnythingPatch(anything)

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    String anything = "anything_example"; // String | Automatically added
    try {
      apiInstance.anythingAnythingPatch(anything);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingAnythingPatch");
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
| **anything** | **String**| Automatically added | |

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
| **200** | Anything passed in request |  -  |

<a id="anythingAnythingPost"></a>
# **anythingAnythingPost**
> anythingAnythingPost(anything)

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    String anything = "anything_example"; // String | Automatically added
    try {
      apiInstance.anythingAnythingPost(anything);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingAnythingPost");
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
| **anything** | **String**| Automatically added | |

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
| **200** | Anything passed in request |  -  |

<a id="anythingAnythingPut"></a>
# **anythingAnythingPut**
> anythingAnythingPut(anything)

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    String anything = "anything_example"; // String | Automatically added
    try {
      apiInstance.anythingAnythingPut(anything);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingAnythingPut");
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
| **anything** | **String**| Automatically added | |

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
| **200** | Anything passed in request |  -  |

<a id="anythingAnythingTrace"></a>
# **anythingAnythingTrace**
> anythingAnythingTrace(anything)

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    String anything = "anything_example"; // String | Automatically added
    try {
      apiInstance.anythingAnythingTrace(anything);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingAnythingTrace");
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
| **anything** | **String**| Automatically added | |

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
| **200** | Anything passed in request |  -  |

<a id="anythingDelete"></a>
# **anythingDelete**
> anythingDelete()

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    try {
      apiInstance.anythingDelete();
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingDelete");
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
| **200** | Anything passed in request |  -  |

<a id="anythingGet"></a>
# **anythingGet**
> anythingGet()

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    try {
      apiInstance.anythingGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingGet");
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
| **200** | Anything passed in request |  -  |

<a id="anythingPatch"></a>
# **anythingPatch**
> anythingPatch()

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    try {
      apiInstance.anythingPatch();
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingPatch");
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
| **200** | Anything passed in request |  -  |

<a id="anythingPost"></a>
# **anythingPost**
> anythingPost()

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    try {
      apiInstance.anythingPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingPost");
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
| **200** | Anything passed in request |  -  |

<a id="anythingPut"></a>
# **anythingPut**
> anythingPut()

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    try {
      apiInstance.anythingPut();
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingPut");
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
| **200** | Anything passed in request |  -  |

<a id="anythingTrace"></a>
# **anythingTrace**
> anythingTrace()

Returns anything passed in request data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnythingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AnythingApi apiInstance = new AnythingApi(defaultClient);
    try {
      apiInstance.anythingTrace();
    } catch (ApiException e) {
      System.err.println("Exception when calling AnythingApi#anythingTrace");
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
| **200** | Anything passed in request |  -  |

