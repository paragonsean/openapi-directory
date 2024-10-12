# RequestInspectionApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**headersGet**](RequestInspectionApi.md#headersGet) | **GET** /headers | Return the incoming request&#39;s HTTP headers. |
| [**ipGet**](RequestInspectionApi.md#ipGet) | **GET** /ip | Returns the requester&#39;s IP Address. |
| [**userAgentGet**](RequestInspectionApi.md#userAgentGet) | **GET** /user-agent | Return the incoming requests&#39;s User-Agent header. |


<a id="headersGet"></a>
# **headersGet**
> headersGet()

Return the incoming request&#39;s HTTP headers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestInspectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RequestInspectionApi apiInstance = new RequestInspectionApi(defaultClient);
    try {
      apiInstance.headersGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestInspectionApi#headersGet");
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
| **200** | The request&#39;s headers. |  -  |

<a id="ipGet"></a>
# **ipGet**
> ipGet()

Returns the requester&#39;s IP Address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestInspectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RequestInspectionApi apiInstance = new RequestInspectionApi(defaultClient);
    try {
      apiInstance.ipGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestInspectionApi#ipGet");
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
| **200** | The Requester&#39;s IP Address. |  -  |

<a id="userAgentGet"></a>
# **userAgentGet**
> userAgentGet()

Return the incoming requests&#39;s User-Agent header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestInspectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    RequestInspectionApi apiInstance = new RequestInspectionApi(defaultClient);
    try {
      apiInstance.userAgentGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestInspectionApi#userAgentGet");
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
| **200** | The request&#39;s User-Agent header. |  -  |

