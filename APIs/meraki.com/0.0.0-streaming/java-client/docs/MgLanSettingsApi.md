# MgLanSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceCellularGatewaySettings**](MgLanSettingsApi.md#getDeviceCellularGatewaySettings) | **GET** /devices/{serial}/cellularGateway/settings | Show the LAN Settings of a MG |
| [**updateDeviceCellularGatewaySettings**](MgLanSettingsApi.md#updateDeviceCellularGatewaySettings) | **PUT** /devices/{serial}/cellularGateway/settings | Update the LAN Settings for a single MG. |


<a id="getDeviceCellularGatewaySettings"></a>
# **getDeviceCellularGatewaySettings**
> Object getDeviceCellularGatewaySettings(serial)

Show the LAN Settings of a MG

Show the LAN Settings of a MG

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MgLanSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MgLanSettingsApi apiInstance = new MgLanSettingsApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCellularGatewaySettings(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MgLanSettingsApi#getDeviceCellularGatewaySettings");
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

<a id="updateDeviceCellularGatewaySettings"></a>
# **updateDeviceCellularGatewaySettings**
> Object updateDeviceCellularGatewaySettings(serial, updateDeviceCellularGatewaySettingsRequest)

Update the LAN Settings for a single MG.

Update the LAN Settings for a single MG.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MgLanSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MgLanSettingsApi apiInstance = new MgLanSettingsApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCellularGatewaySettingsRequest updateDeviceCellularGatewaySettingsRequest = new UpdateDeviceCellularGatewaySettingsRequest(); // UpdateDeviceCellularGatewaySettingsRequest | 
    try {
      Object result = apiInstance.updateDeviceCellularGatewaySettings(serial, updateDeviceCellularGatewaySettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MgLanSettingsApi#updateDeviceCellularGatewaySettings");
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
| **updateDeviceCellularGatewaySettingsRequest** | [**UpdateDeviceCellularGatewaySettingsRequest**](UpdateDeviceCellularGatewaySettingsRequest.md)|  | [optional] |

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

