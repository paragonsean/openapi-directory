# DeviceSettingsApi

All URIs are relative to *http://example.com/setup*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**nightModesettings**](DeviceSettingsApi.md#nightModesettings) | **POST** /assistant/set_night_mode_params | Night Mode settings |
| [**rebootandFactoryReset**](DeviceSettingsApi.md#rebootandFactoryReset) | **POST** /reboot | Reboot and Factory Reset |
| [**setEurekaInfo**](DeviceSettingsApi.md#setEurekaInfo) | **POST** /set_eureka_info | Set Eureka Info |


<a id="nightModesettings"></a>
# **nightModesettings**
> Example17 nightModesettings(nightModesettingsRequest)

Night Mode settings

This sets night mode options.   To view currently set values, use /setup/eureka_info.   If &#x60;enabled&#x60; is set to false, night mode is disabled and the other values do not matter.   &#x60;led_brightness&#x60; and &#x60;volume&#x60; refer to the maximum LED Brightness and Volume that is set during night mode.   &#x60;demo_to_user&#x60; is always set to &#x60;true&#x60; so change in values will be visible in realtime (like brightness).   &#x60;windows&#x60;: A combination of &#x60;length_hours&#x60; and &#x60;start_hour&#x60; is used to define start and end times for night mode. In this example, night mode starts at 10 PM (22) and ends at 6 AM (8 hours later). &#x60;windows.days&#x60; is an array of days of week when night mode will be enabled. Example: 0-&gt;Sunday, 1-&gt; Monday, ..., 6-&gt;Saturday.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    DeviceSettingsApi apiInstance = new DeviceSettingsApi(defaultClient);
    NightModesettingsRequest nightModesettingsRequest = new NightModesettingsRequest(); // NightModesettingsRequest | 
    try {
      Example17 result = apiInstance.nightModesettings(nightModesettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceSettingsApi#nightModesettings");
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
| **nightModesettingsRequest** | [**NightModesettingsRequest**](NightModesettingsRequest.md)|  | |

### Return type

[**Example17**](Example17.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="rebootandFactoryReset"></a>
# **rebootandFactoryReset**
> Object rebootandFactoryReset(rebootandFactoryResetRequest)

Reboot and Factory Reset

This can simply reboot the device (&#x60;params: \&quot;now\&quot;&#x60;) or factory reset the device (&#x60;params: \&quot;fdr\&quot;&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    DeviceSettingsApi apiInstance = new DeviceSettingsApi(defaultClient);
    RebootandFactoryResetRequest rebootandFactoryResetRequest = new RebootandFactoryResetRequest(); // RebootandFactoryResetRequest | 
    try {
      Object result = apiInstance.rebootandFactoryReset(rebootandFactoryResetRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceSettingsApi#rebootandFactoryReset");
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
| **rebootandFactoryResetRequest** | [**RebootandFactoryResetRequest**](RebootandFactoryResetRequest.md)|  | |

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="setEurekaInfo"></a>
# **setEurekaInfo**
> Object setEurekaInfo(setEurekaInfoRequest)

Set Eureka Info

This can set custom values to some options.  Only fields to be modified need to be sent, not all. The example has some modifiable fields.  TODO: List all modifiable fields.  Sending non-existant fields will still return a 200 OK, but they are not saved.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    DeviceSettingsApi apiInstance = new DeviceSettingsApi(defaultClient);
    SetEurekaInfoRequest setEurekaInfoRequest = new SetEurekaInfoRequest(); // SetEurekaInfoRequest | 
    try {
      Object result = apiInstance.setEurekaInfo(setEurekaInfoRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceSettingsApi#setEurekaInfo");
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
| **setEurekaInfoRequest** | [**SetEurekaInfoRequest**](SetEurekaInfoRequest.md)|  | |

### Return type

**Object**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

