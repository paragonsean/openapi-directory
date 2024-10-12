# TrafficShapingUplinkSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkUplinkSettings**](TrafficShapingUplinkSettingsApi.md#getNetworkUplinkSettings) | **GET** /networks/{networkId}/uplinkSettings | Returns the uplink settings for your MX network. |
| [**updateNetworkUplinkSettings**](TrafficShapingUplinkSettingsApi.md#updateNetworkUplinkSettings) | **PUT** /networks/{networkId}/uplinkSettings | Updates the uplink settings for your MX network. |


<a id="getNetworkUplinkSettings"></a>
# **getNetworkUplinkSettings**
> Object getNetworkUplinkSettings(networkId)

Returns the uplink settings for your MX network.

Returns the uplink settings for your MX network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingUplinkSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingUplinkSettingsApi apiInstance = new TrafficShapingUplinkSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkUplinkSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingUplinkSettingsApi#getNetworkUplinkSettings");
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

<a id="updateNetworkUplinkSettings"></a>
# **updateNetworkUplinkSettings**
> Object updateNetworkUplinkSettings(networkId, updateNetworkUplinkSettingsRequest)

Updates the uplink settings for your MX network.

Updates the uplink settings for your MX network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrafficShapingUplinkSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrafficShapingUplinkSettingsApi apiInstance = new TrafficShapingUplinkSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkUplinkSettingsRequest updateNetworkUplinkSettingsRequest = new UpdateNetworkUplinkSettingsRequest(); // UpdateNetworkUplinkSettingsRequest | 
    try {
      Object result = apiInstance.updateNetworkUplinkSettings(networkId, updateNetworkUplinkSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrafficShapingUplinkSettingsApi#updateNetworkUplinkSettings");
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
| **updateNetworkUplinkSettingsRequest** | [**UpdateNetworkUplinkSettingsRequest**](UpdateNetworkUplinkSettingsRequest.md)|  | [optional] |

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

