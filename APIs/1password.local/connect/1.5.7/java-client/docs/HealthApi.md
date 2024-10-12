# HealthApi

All URIs are relative to *http://1password.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHeartbeat**](HealthApi.md#getHeartbeat) | **GET** /heartbeat | Ping the server for liveness |
| [**getServerHealth**](HealthApi.md#getServerHealth) | **GET** /health | Get state of the server and its dependencies. |


<a id="getHeartbeat"></a>
# **getHeartbeat**
> String getHeartbeat()

Ping the server for liveness

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      String result = apiInstance.getHeartbeat();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#getHeartbeat");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getServerHealth"></a>
# **getServerHealth**
> GetServerHealth200Response getServerHealth()

Get state of the server and its dependencies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      GetServerHealth200Response result = apiInstance.getServerHealth();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#getServerHealth");
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

[**GetServerHealth200Response**](GetServerHealth200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

