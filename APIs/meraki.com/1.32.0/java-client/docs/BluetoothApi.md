# BluetoothApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceWirelessBluetoothSettings_1**](BluetoothApi.md#getDeviceWirelessBluetoothSettings_1) | **GET** /devices/{serial}/wireless/bluetooth/settings | Return the bluetooth settings for a wireless device |
| [**getNetworkWirelessBluetoothSettings_1**](BluetoothApi.md#getNetworkWirelessBluetoothSettings_1) | **GET** /networks/{networkId}/wireless/bluetooth/settings | Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network. |
| [**updateDeviceWirelessBluetoothSettings_1**](BluetoothApi.md#updateDeviceWirelessBluetoothSettings_1) | **PUT** /devices/{serial}/wireless/bluetooth/settings | Update the bluetooth settings for a wireless device |
| [**updateNetworkWirelessBluetoothSettings_1**](BluetoothApi.md#updateNetworkWirelessBluetoothSettings_1) | **PUT** /networks/{networkId}/wireless/bluetooth/settings | Update the Bluetooth settings for a network |


<a id="getDeviceWirelessBluetoothSettings_1"></a>
# **getDeviceWirelessBluetoothSettings_1**
> GetDeviceWirelessBluetoothSettings200Response getDeviceWirelessBluetoothSettings_1(serial)

Return the bluetooth settings for a wireless device

Return the bluetooth settings for a wireless device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      GetDeviceWirelessBluetoothSettings200Response result = apiInstance.getDeviceWirelessBluetoothSettings_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#getDeviceWirelessBluetoothSettings_1");
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

[**GetDeviceWirelessBluetoothSettings200Response**](GetDeviceWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessBluetoothSettings_1"></a>
# **getNetworkWirelessBluetoothSettings_1**
> GetNetworkWirelessBluetoothSettings200Response getNetworkWirelessBluetoothSettings_1(networkId)

Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkWirelessBluetoothSettings200Response result = apiInstance.getNetworkWirelessBluetoothSettings_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#getNetworkWirelessBluetoothSettings_1");
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

[**GetNetworkWirelessBluetoothSettings200Response**](GetNetworkWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceWirelessBluetoothSettings_1"></a>
# **updateDeviceWirelessBluetoothSettings_1**
> GetDeviceWirelessBluetoothSettings200Response updateDeviceWirelessBluetoothSettings_1(serial, updateDeviceWirelessBluetoothSettingsRequest)

Update the bluetooth settings for a wireless device

Update the bluetooth settings for a wireless device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceWirelessBluetoothSettingsRequest updateDeviceWirelessBluetoothSettingsRequest = new UpdateDeviceWirelessBluetoothSettingsRequest(); // UpdateDeviceWirelessBluetoothSettingsRequest | 
    try {
      GetDeviceWirelessBluetoothSettings200Response result = apiInstance.updateDeviceWirelessBluetoothSettings_1(serial, updateDeviceWirelessBluetoothSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#updateDeviceWirelessBluetoothSettings_1");
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
| **updateDeviceWirelessBluetoothSettingsRequest** | [**UpdateDeviceWirelessBluetoothSettingsRequest**](UpdateDeviceWirelessBluetoothSettingsRequest.md)|  | [optional] |

### Return type

[**GetDeviceWirelessBluetoothSettings200Response**](GetDeviceWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWirelessBluetoothSettings_1"></a>
# **updateNetworkWirelessBluetoothSettings_1**
> GetNetworkWirelessBluetoothSettings200Response updateNetworkWirelessBluetoothSettings_1(networkId, updateNetworkWirelessBluetoothSettingsRequest)

Update the Bluetooth settings for a network

Update the Bluetooth settings for a network. See the docs page for &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BluetoothApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BluetoothApi apiInstance = new BluetoothApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkWirelessBluetoothSettingsRequest updateNetworkWirelessBluetoothSettingsRequest = new UpdateNetworkWirelessBluetoothSettingsRequest(); // UpdateNetworkWirelessBluetoothSettingsRequest | 
    try {
      GetNetworkWirelessBluetoothSettings200Response result = apiInstance.updateNetworkWirelessBluetoothSettings_1(networkId, updateNetworkWirelessBluetoothSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothApi#updateNetworkWirelessBluetoothSettings_1");
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
| **updateNetworkWirelessBluetoothSettingsRequest** | [**UpdateNetworkWirelessBluetoothSettingsRequest**](UpdateNetworkWirelessBluetoothSettingsRequest.md)|  | [optional] |

### Return type

[**GetNetworkWirelessBluetoothSettings200Response**](GetNetworkWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

