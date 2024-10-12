# SplashSettingsApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSsidSplashSettings**](SplashSettingsApi.md#getNetworkSsidSplashSettings) | **GET** /networks/{networkId}/ssids/{number}/splashSettings | Display the splash page settings for the given SSID |
| [**updateNetworkSsidSplashSettings**](SplashSettingsApi.md#updateNetworkSsidSplashSettings) | **PUT** /networks/{networkId}/ssids/{number}/splashSettings | Modify the splash page settings for the given SSID |


<a id="getNetworkSsidSplashSettings"></a>
# **getNetworkSsidSplashSettings**
> Object getNetworkSsidSplashSettings(networkId, number)

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
import org.openapitools.client.api.SplashSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SplashSettingsApi apiInstance = new SplashSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSsidSplashSettings(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplashSettingsApi#getNetworkSsidSplashSettings");
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

<a id="updateNetworkSsidSplashSettings"></a>
# **updateNetworkSsidSplashSettings**
> Object updateNetworkSsidSplashSettings(networkId, number, updateNetworkSsidSplashSettingsRequest)

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
import org.openapitools.client.api.SplashSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SplashSettingsApi apiInstance = new SplashSettingsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkSsidSplashSettingsRequest updateNetworkSsidSplashSettingsRequest = new UpdateNetworkSsidSplashSettingsRequest(); // UpdateNetworkSsidSplashSettingsRequest | 
    try {
      Object result = apiInstance.updateNetworkSsidSplashSettings(networkId, number, updateNetworkSsidSplashSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SplashSettingsApi#updateNetworkSsidSplashSettings");
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
| **updateNetworkSsidSplashSettingsRequest** | [**UpdateNetworkSsidSplashSettingsRequest**](UpdateNetworkSsidSplashSettingsRequest.md)|  | [optional] |

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

