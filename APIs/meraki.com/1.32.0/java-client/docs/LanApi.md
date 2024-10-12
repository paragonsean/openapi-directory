# LanApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceCellularGatewayLan_1**](LanApi.md#getDeviceCellularGatewayLan_1) | **GET** /devices/{serial}/cellularGateway/lan | Show the LAN Settings of a MG |
| [**updateDeviceCellularGatewayLan_1**](LanApi.md#updateDeviceCellularGatewayLan_1) | **PUT** /devices/{serial}/cellularGateway/lan | Update the LAN Settings for a single MG. |


<a id="getDeviceCellularGatewayLan_1"></a>
# **getDeviceCellularGatewayLan_1**
> Object getDeviceCellularGatewayLan_1(serial)

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
import org.openapitools.client.api.LanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LanApi apiInstance = new LanApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCellularGatewayLan_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanApi#getDeviceCellularGatewayLan_1");
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

<a id="updateDeviceCellularGatewayLan_1"></a>
# **updateDeviceCellularGatewayLan_1**
> Object updateDeviceCellularGatewayLan_1(serial, updateDeviceCellularGatewayLanRequest)

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
import org.openapitools.client.api.LanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LanApi apiInstance = new LanApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCellularGatewayLanRequest updateDeviceCellularGatewayLanRequest = new UpdateDeviceCellularGatewayLanRequest(); // UpdateDeviceCellularGatewayLanRequest | 
    try {
      Object result = apiInstance.updateDeviceCellularGatewayLan_1(serial, updateDeviceCellularGatewayLanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanApi#updateDeviceCellularGatewayLan_1");
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
| **updateDeviceCellularGatewayLanRequest** | [**UpdateDeviceCellularGatewayLanRequest**](UpdateDeviceCellularGatewayLanRequest.md)|  | [optional] |

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

