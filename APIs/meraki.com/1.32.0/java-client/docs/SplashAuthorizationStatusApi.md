# SplashAuthorizationStatusApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkClientSplashAuthorizationStatus_2**](SplashAuthorizationStatusApi.md#getNetworkClientSplashAuthorizationStatus_2) | **GET** /networks/{networkId}/clients/{clientId}/splashAuthorizationStatus | Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash |
| [**updateNetworkClientSplashAuthorizationStatus_2**](SplashAuthorizationStatusApi.md#updateNetworkClientSplashAuthorizationStatus_2) | **PUT** /networks/{networkId}/clients/{clientId}/splashAuthorizationStatus | Update a client&#39;s splash authorization |


<a id="getNetworkClientSplashAuthorizationStatus_2"></a>
# **getNetworkClientSplashAuthorizationStatus_2**
> Object getNetworkClientSplashAuthorizationStatus_2(networkId, clientId)

Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash

Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplashAuthorizationStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SplashAuthorizationStatusApi apiInstance = new SplashAuthorizationStatusApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkClientSplashAuthorizationStatus_2(networkId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplashAuthorizationStatusApi#getNetworkClientSplashAuthorizationStatus_2");
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
| **networkId** | **String**|  | |
| **clientId** | **String**|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkClientSplashAuthorizationStatus_2"></a>
# **updateNetworkClientSplashAuthorizationStatus_2**
> Object updateNetworkClientSplashAuthorizationStatus_2(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest)

Update a client&#39;s splash authorization

Update a client&#39;s splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplashAuthorizationStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SplashAuthorizationStatusApi apiInstance = new SplashAuthorizationStatusApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    UpdateNetworkClientSplashAuthorizationStatusRequest updateNetworkClientSplashAuthorizationStatusRequest = new UpdateNetworkClientSplashAuthorizationStatusRequest(); // UpdateNetworkClientSplashAuthorizationStatusRequest | 
    try {
      Object result = apiInstance.updateNetworkClientSplashAuthorizationStatus_2(networkId, clientId, updateNetworkClientSplashAuthorizationStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplashAuthorizationStatusApi#updateNetworkClientSplashAuthorizationStatus_2");
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
| **networkId** | **String**|  | |
| **clientId** | **String**|  | |
| **updateNetworkClientSplashAuthorizationStatusRequest** | [**UpdateNetworkClientSplashAuthorizationStatusRequest**](UpdateNetworkClientSplashAuthorizationStatusRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

