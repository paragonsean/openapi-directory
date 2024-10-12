# DeviceTypeGroupPoliciesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkWirelessSsidDeviceTypeGroupPolicies_2**](DeviceTypeGroupPoliciesApi.md#getNetworkWirelessSsidDeviceTypeGroupPolicies_2) | **GET** /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies | List the device type group policies for the SSID |
| [**updateNetworkWirelessSsidDeviceTypeGroupPolicies_2**](DeviceTypeGroupPoliciesApi.md#updateNetworkWirelessSsidDeviceTypeGroupPolicies_2) | **PUT** /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies | Update the device type group policies for the SSID |


<a id="getNetworkWirelessSsidDeviceTypeGroupPolicies_2"></a>
# **getNetworkWirelessSsidDeviceTypeGroupPolicies_2**
> Object getNetworkWirelessSsidDeviceTypeGroupPolicies_2(networkId, number)

List the device type group policies for the SSID

List the device type group policies for the SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceTypeGroupPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DeviceTypeGroupPoliciesApi apiInstance = new DeviceTypeGroupPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidDeviceTypeGroupPolicies_2(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceTypeGroupPoliciesApi#getNetworkWirelessSsidDeviceTypeGroupPolicies_2");
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
| **number** | **String**|  | |

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

<a id="updateNetworkWirelessSsidDeviceTypeGroupPolicies_2"></a>
# **updateNetworkWirelessSsidDeviceTypeGroupPolicies_2**
> Object updateNetworkWirelessSsidDeviceTypeGroupPolicies_2(networkId, number, updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest)

Update the device type group policies for the SSID

Update the device type group policies for the SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceTypeGroupPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DeviceTypeGroupPoliciesApi apiInstance = new DeviceTypeGroupPoliciesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest = new UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest(); // UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidDeviceTypeGroupPolicies_2(networkId, number, updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceTypeGroupPoliciesApi#updateNetworkWirelessSsidDeviceTypeGroupPolicies_2");
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
| **number** | **String**|  | |
| **updateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest** | [**UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest**](UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest.md)|  | [optional] |

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

