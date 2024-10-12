# DefaultApi

All URIs are relative to *http://openaq.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**favicoFaviconIcoGet**](DefaultApi.md#favicoFaviconIcoGet) | **GET** /favicon.ico | Favico |
| [**pongPingGet**](DefaultApi.md#pongPingGet) | **GET** /ping | Pong |


<a id="favicoFaviconIcoGet"></a>
# **favicoFaviconIcoGet**
> Object favicoFaviconIcoGet()

Favico

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Object result = apiInstance.favicoFaviconIcoGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#favicoFaviconIcoGet");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="pongPingGet"></a>
# **pongPingGet**
> Object pongPingGet()

Pong

Sanity check. This will let the user know that the service is operational. And this path operation will: * show a lifesign

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openaq.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      Object result = apiInstance.pongPingGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#pongPingGet");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

