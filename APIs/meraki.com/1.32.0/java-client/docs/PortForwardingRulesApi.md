# PortForwardingRulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceCellularGatewayPortForwardingRules_1**](PortForwardingRulesApi.md#getDeviceCellularGatewayPortForwardingRules_1) | **GET** /devices/{serial}/cellularGateway/portForwardingRules | Returns the port forwarding rules for a single MG. |
| [**getNetworkApplianceFirewallPortForwardingRules_2**](PortForwardingRulesApi.md#getNetworkApplianceFirewallPortForwardingRules_2) | **GET** /networks/{networkId}/appliance/firewall/portForwardingRules | Return the port forwarding rules for an MX network |
| [**updateDeviceCellularGatewayPortForwardingRules_1**](PortForwardingRulesApi.md#updateDeviceCellularGatewayPortForwardingRules_1) | **PUT** /devices/{serial}/cellularGateway/portForwardingRules | Updates the port forwarding rules for a single MG. |
| [**updateNetworkApplianceFirewallPortForwardingRules_2**](PortForwardingRulesApi.md#updateNetworkApplianceFirewallPortForwardingRules_2) | **PUT** /networks/{networkId}/appliance/firewall/portForwardingRules | Update the port forwarding rules for an MX network |


<a id="getDeviceCellularGatewayPortForwardingRules_1"></a>
# **getDeviceCellularGatewayPortForwardingRules_1**
> Object getDeviceCellularGatewayPortForwardingRules_1(serial)

Returns the port forwarding rules for a single MG.

Returns the port forwarding rules for a single MG.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortForwardingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PortForwardingRulesApi apiInstance = new PortForwardingRulesApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCellularGatewayPortForwardingRules_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortForwardingRulesApi#getDeviceCellularGatewayPortForwardingRules_1");
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
| **serial** | **String**|  | |

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

<a id="getNetworkApplianceFirewallPortForwardingRules_2"></a>
# **getNetworkApplianceFirewallPortForwardingRules_2**
> Object getNetworkApplianceFirewallPortForwardingRules_2(networkId)

Return the port forwarding rules for an MX network

Return the port forwarding rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortForwardingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PortForwardingRulesApi apiInstance = new PortForwardingRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallPortForwardingRules_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortForwardingRulesApi#getNetworkApplianceFirewallPortForwardingRules_2");
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

<a id="updateDeviceCellularGatewayPortForwardingRules_1"></a>
# **updateDeviceCellularGatewayPortForwardingRules_1**
> Object updateDeviceCellularGatewayPortForwardingRules_1(serial, updateDeviceCellularGatewayPortForwardingRulesRequest)

Updates the port forwarding rules for a single MG.

Updates the port forwarding rules for a single MG.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortForwardingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PortForwardingRulesApi apiInstance = new PortForwardingRulesApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCellularGatewayPortForwardingRulesRequest updateDeviceCellularGatewayPortForwardingRulesRequest = new UpdateDeviceCellularGatewayPortForwardingRulesRequest(); // UpdateDeviceCellularGatewayPortForwardingRulesRequest | 
    try {
      Object result = apiInstance.updateDeviceCellularGatewayPortForwardingRules_1(serial, updateDeviceCellularGatewayPortForwardingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortForwardingRulesApi#updateDeviceCellularGatewayPortForwardingRules_1");
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
| **serial** | **String**|  | |
| **updateDeviceCellularGatewayPortForwardingRulesRequest** | [**UpdateDeviceCellularGatewayPortForwardingRulesRequest**](UpdateDeviceCellularGatewayPortForwardingRulesRequest.md)|  | [optional] |

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

<a id="updateNetworkApplianceFirewallPortForwardingRules_2"></a>
# **updateNetworkApplianceFirewallPortForwardingRules_2**
> Object updateNetworkApplianceFirewallPortForwardingRules_2(networkId, updateNetworkApplianceFirewallPortForwardingRulesRequest)

Update the port forwarding rules for an MX network

Update the port forwarding rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortForwardingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PortForwardingRulesApi apiInstance = new PortForwardingRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallPortForwardingRulesRequest updateNetworkApplianceFirewallPortForwardingRulesRequest = new UpdateNetworkApplianceFirewallPortForwardingRulesRequest(); // UpdateNetworkApplianceFirewallPortForwardingRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallPortForwardingRules_2(networkId, updateNetworkApplianceFirewallPortForwardingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortForwardingRulesApi#updateNetworkApplianceFirewallPortForwardingRules_2");
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
| **updateNetworkApplianceFirewallPortForwardingRulesRequest** | [**UpdateNetworkApplianceFirewallPortForwardingRulesRequest**](UpdateNetworkApplianceFirewallPortForwardingRulesRequest.md)|  | |

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

