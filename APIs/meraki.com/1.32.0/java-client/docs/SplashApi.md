# SplashApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkWirelessSsidSplashSettings_2**](SplashApi.md#getNetworkWirelessSsidSplashSettings_2) | **GET** /networks/{networkId}/wireless/ssids/{number}/splash/settings | Display the splash page settings for the given SSID |
| [**updateNetworkWirelessSsidSplashSettings_2**](SplashApi.md#updateNetworkWirelessSsidSplashSettings_2) | **PUT** /networks/{networkId}/wireless/ssids/{number}/splash/settings | Modify the splash page settings for the given SSID |


<a id="getNetworkWirelessSsidSplashSettings_2"></a>
# **getNetworkWirelessSsidSplashSettings_2**
> GetNetworkWirelessSsidSplashSettings200Response getNetworkWirelessSsidSplashSettings_2(networkId, number)

Display the splash page settings for the given SSID

Display the splash page settings for the given SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SplashApi apiInstance = new SplashApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      GetNetworkWirelessSsidSplashSettings200Response result = apiInstance.getNetworkWirelessSsidSplashSettings_2(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplashApi#getNetworkWirelessSsidSplashSettings_2");
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

[**GetNetworkWirelessSsidSplashSettings200Response**](GetNetworkWirelessSsidSplashSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWirelessSsidSplashSettings_2"></a>
# **updateNetworkWirelessSsidSplashSettings_2**
> GetNetworkWirelessSsidSplashSettings200Response updateNetworkWirelessSsidSplashSettings_2(networkId, number, updateNetworkWirelessSsidSplashSettingsRequest)

Modify the splash page settings for the given SSID

Modify the splash page settings for the given SSID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SplashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SplashApi apiInstance = new SplashApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidSplashSettingsRequest updateNetworkWirelessSsidSplashSettingsRequest = new UpdateNetworkWirelessSsidSplashSettingsRequest(); // UpdateNetworkWirelessSsidSplashSettingsRequest | 
    try {
      GetNetworkWirelessSsidSplashSettings200Response result = apiInstance.updateNetworkWirelessSsidSplashSettings_2(networkId, number, updateNetworkWirelessSsidSplashSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplashApi#updateNetworkWirelessSsidSplashSettings_2");
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
| **updateNetworkWirelessSsidSplashSettingsRequest** | [**UpdateNetworkWirelessSsidSplashSettingsRequest**](UpdateNetworkWirelessSsidSplashSettingsRequest.md)|  | [optional] |

### Return type

[**GetNetworkWirelessSsidSplashSettings200Response**](GetNetworkWirelessSsidSplashSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

