# RadioApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceWirelessRadioSettings_1**](RadioApi.md#getDeviceWirelessRadioSettings_1) | **GET** /devices/{serial}/wireless/radio/settings | Return the radio settings of a device |
| [**updateDeviceWirelessRadioSettings_1**](RadioApi.md#updateDeviceWirelessRadioSettings_1) | **PUT** /devices/{serial}/wireless/radio/settings | Update the radio settings of a device |


<a id="getDeviceWirelessRadioSettings_1"></a>
# **getDeviceWirelessRadioSettings_1**
> Object getDeviceWirelessRadioSettings_1(serial)

Return the radio settings of a device

Return the radio settings of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceWirelessRadioSettings_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#getDeviceWirelessRadioSettings_1");
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

<a id="updateDeviceWirelessRadioSettings_1"></a>
# **updateDeviceWirelessRadioSettings_1**
> Object updateDeviceWirelessRadioSettings_1(serial, updateDeviceWirelessRadioSettingsRequest)

Update the radio settings of a device

Update the radio settings of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RadioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RadioApi apiInstance = new RadioApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceWirelessRadioSettingsRequest updateDeviceWirelessRadioSettingsRequest = new UpdateDeviceWirelessRadioSettingsRequest(); // UpdateDeviceWirelessRadioSettingsRequest | 
    try {
      Object result = apiInstance.updateDeviceWirelessRadioSettings_1(serial, updateDeviceWirelessRadioSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RadioApi#updateDeviceWirelessRadioSettings_1");
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
| **updateDeviceWirelessRadioSettingsRequest** | [**UpdateDeviceWirelessRadioSettingsRequest**](UpdateDeviceWirelessRadioSettingsRequest.md)|  | [optional] |

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

