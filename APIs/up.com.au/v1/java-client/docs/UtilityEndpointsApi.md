# UtilityEndpointsApi

All URIs are relative to *https://api.up.com.au/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**utilPingGet**](UtilityEndpointsApi.md#utilPingGet) | **GET** /util/ping | Ping |


<a id="utilPingGet"></a>
# **utilPingGet**
> PingResponse utilPingGet()

Ping

Make a basic ping request to the API. This is useful to verify that authentication is functioning correctly. On authentication success an HTTP &#x60;200&#x60; status is returned. On failure an HTTP &#x60;401&#x60; error response is returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilityEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.up.com.au/api/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    UtilityEndpointsApi apiInstance = new UtilityEndpointsApi(defaultClient);
    try {
      PingResponse result = apiInstance.utilPingGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilityEndpointsApi#utilPingGet");
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

[**PingResponse**](PingResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Not Authorized |  -  |

