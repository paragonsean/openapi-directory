# MgPortForwardingRulesApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceCellularGatewaySettingsPortForwardingRules**](MgPortForwardingRulesApi.md#getDeviceCellularGatewaySettingsPortForwardingRules) | **GET** /devices/{serial}/cellularGateway/settings/portForwardingRules | Returns the port forwarding rules for a single MG. |
| [**updateDeviceCellularGatewaySettingsPortForwardingRules**](MgPortForwardingRulesApi.md#updateDeviceCellularGatewaySettingsPortForwardingRules) | **PUT** /devices/{serial}/cellularGateway/settings/portForwardingRules | Updates the port forwarding rules for a single MG. |


<a id="getDeviceCellularGatewaySettingsPortForwardingRules"></a>
# **getDeviceCellularGatewaySettingsPortForwardingRules**
> Object getDeviceCellularGatewaySettingsPortForwardingRules(serial)

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
import org.openapitools.client.api.MgPortForwardingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MgPortForwardingRulesApi apiInstance = new MgPortForwardingRulesApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCellularGatewaySettingsPortForwardingRules(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MgPortForwardingRulesApi#getDeviceCellularGatewaySettingsPortForwardingRules");
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

<a id="updateDeviceCellularGatewaySettingsPortForwardingRules"></a>
# **updateDeviceCellularGatewaySettingsPortForwardingRules**
> Object updateDeviceCellularGatewaySettingsPortForwardingRules(serial, updateDeviceCellularGatewaySettingsPortForwardingRulesRequest)

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
import org.openapitools.client.api.MgPortForwardingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MgPortForwardingRulesApi apiInstance = new MgPortForwardingRulesApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest updateDeviceCellularGatewaySettingsPortForwardingRulesRequest = new UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest(); // UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest | 
    try {
      Object result = apiInstance.updateDeviceCellularGatewaySettingsPortForwardingRules(serial, updateDeviceCellularGatewaySettingsPortForwardingRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MgPortForwardingRulesApi#updateDeviceCellularGatewaySettingsPortForwardingRules");
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
| **updateDeviceCellularGatewaySettingsPortForwardingRulesRequest** | [**UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest**](UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest.md)|  | [optional] |

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

