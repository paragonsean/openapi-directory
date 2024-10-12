# StormControlApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSwitchStormControl_1**](StormControlApi.md#getNetworkSwitchStormControl_1) | **GET** /networks/{networkId}/switch/stormControl | Return the storm control configuration for a switch network |
| [**updateNetworkSwitchStormControl_1**](StormControlApi.md#updateNetworkSwitchStormControl_1) | **PUT** /networks/{networkId}/switch/stormControl | Update the storm control configuration for a switch network |


<a id="getNetworkSwitchStormControl_1"></a>
# **getNetworkSwitchStormControl_1**
> GetNetworkSwitchStormControl200Response getNetworkSwitchStormControl_1(networkId)

Return the storm control configuration for a switch network

Return the storm control configuration for a switch network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StormControlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StormControlApi apiInstance = new StormControlApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSwitchStormControl200Response result = apiInstance.getNetworkSwitchStormControl_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StormControlApi#getNetworkSwitchStormControl_1");
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

### Return type

[**GetNetworkSwitchStormControl200Response**](GetNetworkSwitchStormControl200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStormControl_1"></a>
# **updateNetworkSwitchStormControl_1**
> Object updateNetworkSwitchStormControl_1(networkId, updateNetworkSwitchStormControlRequest)

Update the storm control configuration for a switch network

Update the storm control configuration for a switch network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StormControlApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StormControlApi apiInstance = new StormControlApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchStormControlRequest updateNetworkSwitchStormControlRequest = new UpdateNetworkSwitchStormControlRequest(); // UpdateNetworkSwitchStormControlRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStormControl_1(networkId, updateNetworkSwitchStormControlRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StormControlApi#updateNetworkSwitchStormControl_1");
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
| **updateNetworkSwitchStormControlRequest** | [**UpdateNetworkSwitchStormControlRequest**](UpdateNetworkSwitchStormControlRequest.md)|  | [optional] |

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

