# StatusApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceWirelessStatus_1**](StatusApi.md#getDeviceWirelessStatus_1) | **GET** /devices/{serial}/wireless/status | Return the SSID statuses of an access point |


<a id="getDeviceWirelessStatus_1"></a>
# **getDeviceWirelessStatus_1**
> Object getDeviceWirelessStatus_1(serial)

Return the SSID statuses of an access point

Return the SSID statuses of an access point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceWirelessStatus_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getDeviceWirelessStatus_1");
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

