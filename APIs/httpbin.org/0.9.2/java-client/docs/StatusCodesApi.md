# StatusCodesApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statusCodesDelete**](StatusCodesApi.md#statusCodesDelete) | **DELETE** /status/{codes} | Return status code or random status code if more than one are given |
| [**statusCodesGet**](StatusCodesApi.md#statusCodesGet) | **GET** /status/{codes} | Return status code or random status code if more than one are given |
| [**statusCodesPatch**](StatusCodesApi.md#statusCodesPatch) | **PATCH** /status/{codes} | Return status code or random status code if more than one are given |
| [**statusCodesPost**](StatusCodesApi.md#statusCodesPost) | **POST** /status/{codes} | Return status code or random status code if more than one are given |
| [**statusCodesPut**](StatusCodesApi.md#statusCodesPut) | **PUT** /status/{codes} | Return status code or random status code if more than one are given |
| [**statusCodesTrace**](StatusCodesApi.md#statusCodesTrace) | **TRACE** /status/{codes} | Return status code or random status code if more than one are given |


<a id="statusCodesDelete"></a>
# **statusCodesDelete**
> statusCodesDelete(codes)

Return status code or random status code if more than one are given

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    StatusCodesApi apiInstance = new StatusCodesApi(defaultClient);
    String codes = "codes_example"; // String | 
    try {
      apiInstance.statusCodesDelete(codes);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusCodesApi#statusCodesDelete");
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
| **codes** | **String**|  | |

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
| **100** | Informational responses |  -  |
| **200** | Success |  -  |
| **300** | Redirection |  -  |
| **400** | Client Errors |  -  |
| **500** | Server Errors |  -  |

<a id="statusCodesGet"></a>
# **statusCodesGet**
> statusCodesGet(codes)

Return status code or random status code if more than one are given

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    StatusCodesApi apiInstance = new StatusCodesApi(defaultClient);
    String codes = "codes_example"; // String | 
    try {
      apiInstance.statusCodesGet(codes);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusCodesApi#statusCodesGet");
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
| **codes** | **String**|  | |

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
| **100** | Informational responses |  -  |
| **200** | Success |  -  |
| **300** | Redirection |  -  |
| **400** | Client Errors |  -  |
| **500** | Server Errors |  -  |

<a id="statusCodesPatch"></a>
# **statusCodesPatch**
> statusCodesPatch(codes)

Return status code or random status code if more than one are given

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    StatusCodesApi apiInstance = new StatusCodesApi(defaultClient);
    String codes = "codes_example"; // String | 
    try {
      apiInstance.statusCodesPatch(codes);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusCodesApi#statusCodesPatch");
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
| **codes** | **String**|  | |

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
| **100** | Informational responses |  -  |
| **200** | Success |  -  |
| **300** | Redirection |  -  |
| **400** | Client Errors |  -  |
| **500** | Server Errors |  -  |

<a id="statusCodesPost"></a>
# **statusCodesPost**
> statusCodesPost(codes)

Return status code or random status code if more than one are given

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    StatusCodesApi apiInstance = new StatusCodesApi(defaultClient);
    String codes = "codes_example"; // String | 
    try {
      apiInstance.statusCodesPost(codes);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusCodesApi#statusCodesPost");
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
| **codes** | **String**|  | |

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
| **100** | Informational responses |  -  |
| **200** | Success |  -  |
| **300** | Redirection |  -  |
| **400** | Client Errors |  -  |
| **500** | Server Errors |  -  |

<a id="statusCodesPut"></a>
# **statusCodesPut**
> statusCodesPut(codes)

Return status code or random status code if more than one are given

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    StatusCodesApi apiInstance = new StatusCodesApi(defaultClient);
    String codes = "codes_example"; // String | 
    try {
      apiInstance.statusCodesPut(codes);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusCodesApi#statusCodesPut");
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
| **codes** | **String**|  | |

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
| **100** | Informational responses |  -  |
| **200** | Success |  -  |
| **300** | Redirection |  -  |
| **400** | Client Errors |  -  |
| **500** | Server Errors |  -  |

<a id="statusCodesTrace"></a>
# **statusCodesTrace**
> statusCodesTrace(codes)

Return status code or random status code if more than one are given

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    StatusCodesApi apiInstance = new StatusCodesApi(defaultClient);
    String codes = "codes_example"; // String | 
    try {
      apiInstance.statusCodesTrace(codes);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusCodesApi#statusCodesTrace");
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
| **codes** | **String**|  | |

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
| **100** | Informational responses |  -  |
| **200** | Success |  -  |
| **300** | Redirection |  -  |
| **400** | Client Errors |  -  |
| **500** | Server Errors |  -  |

