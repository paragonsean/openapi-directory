# BluetoothSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkBluetoothSettings**](BluetoothSettingsApi.md#getNetworkBluetoothSettings) | **GET** /networks/{networkId}/bluetoothSettings | Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network. |
| [**updateDeviceWirelessBluetoothSettings**](BluetoothSettingsApi.md#updateDeviceWirelessBluetoothSettings) | **PUT** /devices/{serial}/wireless/bluetooth/settings | Update the bluetooth settings for a wireless device |
| [**updateNetworkBluetoothSettings**](BluetoothSettingsApi.md#updateNetworkBluetoothSettings) | **PUT** /networks/{networkId}/bluetoothSettings | Update the Bluetooth settings for a network |


<a id="getNetworkBluetoothSettings"></a>
# **getNetworkBluetoothSettings**
> GetNetworkBluetoothSettings200Response getNetworkBluetoothSettings(networkId)

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
import org.openapitools.client.api.BluetoothSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BluetoothSettingsApi apiInstance = new BluetoothSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkBluetoothSettings200Response result = apiInstance.getNetworkBluetoothSettings(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothSettingsApi#getNetworkBluetoothSettings");
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

[**GetNetworkBluetoothSettings200Response**](GetNetworkBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceWirelessBluetoothSettings"></a>
# **updateDeviceWirelessBluetoothSettings**
> UpdateDeviceWirelessBluetoothSettings200Response updateDeviceWirelessBluetoothSettings(serial, updateDeviceWirelessBluetoothSettingsRequest)

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
import org.openapitools.client.api.BluetoothSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BluetoothSettingsApi apiInstance = new BluetoothSettingsApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceWirelessBluetoothSettingsRequest updateDeviceWirelessBluetoothSettingsRequest = new UpdateDeviceWirelessBluetoothSettingsRequest(); // UpdateDeviceWirelessBluetoothSettingsRequest | 
    try {
      UpdateDeviceWirelessBluetoothSettings200Response result = apiInstance.updateDeviceWirelessBluetoothSettings(serial, updateDeviceWirelessBluetoothSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothSettingsApi#updateDeviceWirelessBluetoothSettings");
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

[**UpdateDeviceWirelessBluetoothSettings200Response**](UpdateDeviceWirelessBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkBluetoothSettings"></a>
# **updateNetworkBluetoothSettings**
> GetNetworkBluetoothSettings200Response updateNetworkBluetoothSettings(networkId, updateNetworkBluetoothSettingsRequest)

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
import org.openapitools.client.api.BluetoothSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BluetoothSettingsApi apiInstance = new BluetoothSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkBluetoothSettingsRequest updateNetworkBluetoothSettingsRequest = new UpdateNetworkBluetoothSettingsRequest(); // UpdateNetworkBluetoothSettingsRequest | 
    try {
      GetNetworkBluetoothSettings200Response result = apiInstance.updateNetworkBluetoothSettings(networkId, updateNetworkBluetoothSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BluetoothSettingsApi#updateNetworkBluetoothSettings");
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
| **updateNetworkBluetoothSettingsRequest** | [**UpdateNetworkBluetoothSettingsRequest**](UpdateNetworkBluetoothSettingsRequest.md)|  | [optional] |

### Return type

[**GetNetworkBluetoothSettings200Response**](GetNetworkBluetoothSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

