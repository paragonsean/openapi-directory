# DaemonApi

All URIs are relative to *https://api.mailscript.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDaemonToken**](DaemonApi.md#getDaemonToken) | **GET** /daemons/{daemon}/token | Get a token for opening a daemon connection |


<a id="getDaemonToken"></a>
# **getDaemonToken**
> GetDaemonToken200Response getDaemonToken(daemon)

Get a token for opening a daemon connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DaemonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DaemonApi apiInstance = new DaemonApi(defaultClient);
    String daemon = "daemon_example"; // String | name of Daemon
    try {
      GetDaemonToken200Response result = apiInstance.getDaemonToken(daemon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DaemonApi#getDaemonToken");
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
| **daemon** | **String**| name of Daemon | |

### Return type

[**GetDaemonToken200Response**](GetDaemonToken200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful get operation |  -  |
| **400** | Failure |  -  |
| **403** | Bad credentials |  -  |

