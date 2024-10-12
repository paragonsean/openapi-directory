# RealtimeApi

All URIs are relative to *http://api.edrv.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRealtime**](RealtimeApi.md#getRealtime) | **GET** /v1/realtime |  |


<a id="getRealtime"></a>
# **getRealtime**
> getRealtime(secWebsocketProtocol)



Use to request a Websockets handshake

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealtimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.edrv.io");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RealtimeApi apiInstance = new RealtimeApi(defaultClient);
    String secWebsocketProtocol = "secWebsocketProtocol_example"; // String | The JWT token to use for auth
    try {
      apiInstance.getRealtime(secWebsocketProtocol);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealtimeApi#getRealtime");
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
| **secWebsocketProtocol** | **String**| The JWT token to use for auth | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **101** | Upgrade connection |  -  |

