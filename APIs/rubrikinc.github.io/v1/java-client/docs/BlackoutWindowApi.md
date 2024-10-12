# BlackoutWindowApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBlackoutWindowStatus**](BlackoutWindowApi.md#getBlackoutWindowStatus) | **GET** /blackout_window | Get current status of global blackout window |
| [**toggleBlackoutWindow**](BlackoutWindowApi.md#toggleBlackoutWindow) | **PATCH** /blackout_window | Starts or stops the global blackout window in local Rubrik cluster |


<a id="getBlackoutWindowStatus"></a>
# **getBlackoutWindowStatus**
> GlobalBlackoutWindowStatus getBlackoutWindowStatus()

Get current status of global blackout window

Determine whether global blackout window is currently active.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlackoutWindowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    BlackoutWindowApi apiInstance = new BlackoutWindowApi(defaultClient);
    try {
      GlobalBlackoutWindowStatus result = apiInstance.getBlackoutWindowStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlackoutWindowApi#getBlackoutWindowStatus");
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

[**GlobalBlackoutWindowStatus**](GlobalBlackoutWindowStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current status of blackout window. |  -  |

<a id="toggleBlackoutWindow"></a>
# **toggleBlackoutWindow**
> GlobalBlackoutWindowStatus toggleBlackoutWindow(globalBlackoutWindowStatus)

Starts or stops the global blackout window in local Rubrik cluster

Returns whether or not the system is in a blackout window.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlackoutWindowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    BlackoutWindowApi apiInstance = new BlackoutWindowApi(defaultClient);
    GlobalBlackoutWindowStatus globalBlackoutWindowStatus = new GlobalBlackoutWindowStatus(); // GlobalBlackoutWindowStatus | Whether to start or stop the global blackout window.
    try {
      GlobalBlackoutWindowStatus result = apiInstance.toggleBlackoutWindow(globalBlackoutWindowStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlackoutWindowApi#toggleBlackoutWindow");
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
| **globalBlackoutWindowStatus** | [**GlobalBlackoutWindowStatus**](GlobalBlackoutWindowStatus.md)| Whether to start or stop the global blackout window. | |

### Return type

[**GlobalBlackoutWindowStatus**](GlobalBlackoutWindowStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned the updated blackout window status. |  -  |

