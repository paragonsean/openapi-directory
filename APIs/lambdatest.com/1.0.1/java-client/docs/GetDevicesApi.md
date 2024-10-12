# GetDevicesApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**devices**](GetDevicesApi.md#devices) | **GET** /devices | Fetch all available device combinations. |


<a id="devices"></a>
# **devices**
> OsDevices devices(os)

Fetch all available device combinations.

Fetch all os devices combinations available on lambdatest platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetDevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lambdatest.com/screenshots/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    GetDevicesApi apiInstance = new GetDevicesApi(defaultClient);
    String os = "os_example"; // String | Fetch details for a particular OS
    try {
      OsDevices result = apiInstance.devices(os);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetDevicesApi#devices");
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
| **os** | **String**| Fetch details for a particular OS | [optional] |

### Return type

[**OsDevices**](OsDevices.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **401** | Access denied. Auth error. |  -  |

