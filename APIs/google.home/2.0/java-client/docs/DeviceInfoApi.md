# DeviceInfoApi

All URIs are relative to *http://example.com/setup*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appDeviceID**](DeviceInfoApi.md#appDeviceID) | **POST** /get_app_device_id | App Device ID |
| [**checkReadyStatus**](DeviceInfoApi.md#checkReadyStatus) | **POST** /assistant/check_ready_status | Check Ready Status |
| [**eurekaInfo**](DeviceInfoApi.md#eurekaInfo) | **GET** /eureka_info | Eureka Info |
| [**locales**](DeviceInfoApi.md#locales) | **GET** /supported_locales | Locales |
| [**offer**](DeviceInfoApi.md#offer) | **GET** /offer | Offer |
| [**testInternetDownloadSpeed**](DeviceInfoApi.md#testInternetDownloadSpeed) | **POST** /test_internet_download_speed | Test Internet Download Speed |
| [**timezones**](DeviceInfoApi.md#timezones) | **GET** /supported_timezones | Timezones |


<a id="appDeviceID"></a>
# **appDeviceID**
> Example11 appDeviceID(appDeviceIDRequest)

App Device ID

This gives \&quot;app device id\&quot;, \&quot;certificate\&quot; and \&quot;signed data\&quot;.   The &#x60;app_id&#x60; in the request is mandatory and refers to Chromecast backdrop/screensaver app. It has to be set to &#x60;E8C28D3C&#x60;.    The certificate is valid and issued by &#x60;Chromecast ICA 6 (Audio Assist), Google Inc&#x60;.  Not sure what the other two are.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    DeviceInfoApi apiInstance = new DeviceInfoApi(defaultClient);
    AppDeviceIDRequest appDeviceIDRequest = new AppDeviceIDRequest(); // AppDeviceIDRequest | 
    try {
      Example11 result = apiInstance.appDeviceID(appDeviceIDRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceInfoApi#appDeviceID");
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
| **appDeviceIDRequest** | [**AppDeviceIDRequest**](AppDeviceIDRequest.md)|  | |

### Return type

[**Example11**](Example11.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Not Found |  -  |

<a id="checkReadyStatus"></a>
# **checkReadyStatus**
> Example13 checkReadyStatus(checkReadyStatusRequest)

Check Ready Status

**Update:** This seems to have changed now and is no longer possible. The error is also new.  Setting &#x60;play_ready_message&#x60; to true plays a welcome message on the device saying \&quot;Hi, I&#39;m your Google Assistant. I&#39;m here to help. To learn a few things you can do, continue in the Google Home app.\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    DeviceInfoApi apiInstance = new DeviceInfoApi(defaultClient);
    CheckReadyStatusRequest checkReadyStatusRequest = new CheckReadyStatusRequest(); // CheckReadyStatusRequest | 
    try {
      Example13 result = apiInstance.checkReadyStatus(checkReadyStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceInfoApi#checkReadyStatus");
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
| **checkReadyStatusRequest** | [**CheckReadyStatusRequest**](CheckReadyStatusRequest.md)|  | |

### Return type

[**Example13**](Example13.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="eurekaInfo"></a>
# **eurekaInfo**
> Example1 eurekaInfo(params, options, nonce)

Eureka Info

This gives most of the device info. The GET parameter &#x60;param&#x60; is a comma separated list of json keys to fetch. Currently, these params are known: &#x60;version,audio,name,build_info,detail,device_info,net,wifi,setup,settings,opt_in,opencast,multizone,proxy,night_mode_params,user_eq,room_equalizer,sign,aogh,ultrasound,mesh&#x60;  Nested items can also be filtered using the dot notation. Example: &#x60;audio.digital&#x60;  The &#x60;options&#x60; GET parameter is always set to &#x60;detail&#x60; or &#x60;detail,sign&#x60;. &#x60;sign&#x60; signs the &#x60;nonce&#x60; and returns some value.  The &#x60;nonce&#x60; GET parameter is an integer value signed with needed (see &#x60;option&#x60; parameter above).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    DeviceInfoApi apiInstance = new DeviceInfoApi(defaultClient);
    String params = "version,audio,name,build_info,detail,device_info,net,wifi,setup,settings,opt_in,opencast,multizone,proxy,night_mode_params,user_eq,room_equalizer,sign,aogh,ultrasound,mesh"; // String | 
    String options = "detail,sign"; // String | 
    Integer nonce = 1234512345; // Integer | 
    try {
      Example1 result = apiInstance.eurekaInfo(params, options, nonce);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceInfoApi#eurekaInfo");
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
| **params** | **String**|  | |
| **options** | **String**|  | |
| **nonce** | **Integer**|  | |

### Return type

[**Example1**](Example1.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="locales"></a>
# **locales**
> List&lt;Example15&gt; locales()

Locales

Simply returns a list of all supported locales.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    DeviceInfoApi apiInstance = new DeviceInfoApi(defaultClient);
    try {
      List<Example15> result = apiInstance.locales();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceInfoApi#locales");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Example15&gt;**](Example15.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="offer"></a>
# **offer**
> Example12 offer()

Offer

This gives a token which is used by the Home app to get offers. The offers themselves are not stored on the device.   A new token is generated for every request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    DeviceInfoApi apiInstance = new DeviceInfoApi(defaultClient);
    try {
      Example12 result = apiInstance.offer();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceInfoApi#offer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Example12**](Example12.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="testInternetDownloadSpeed"></a>
# **testInternetDownloadSpeed**
> Example16 testInternetDownloadSpeed(testInternetDownloadSpeedRequest)

Test Internet Download Speed

**Update:** This seems to have been removed. Returns 404 Not Found.  This endpoint tests internet download speed. Any sample file URL can be provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    DeviceInfoApi apiInstance = new DeviceInfoApi(defaultClient);
    TestInternetDownloadSpeedRequest testInternetDownloadSpeedRequest = new TestInternetDownloadSpeedRequest(); // TestInternetDownloadSpeedRequest | 
    try {
      Example16 result = apiInstance.testInternetDownloadSpeed(testInternetDownloadSpeedRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceInfoApi#testInternetDownloadSpeed");
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
| **testInternetDownloadSpeedRequest** | [**TestInternetDownloadSpeedRequest**](TestInternetDownloadSpeedRequest.md)|  | |

### Return type

[**Example16**](Example16.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="timezones"></a>
# **timezones**
> List&lt;Example14&gt; timezones()

Timezones

Simply returns a list of all supported timezones.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    DeviceInfoApi apiInstance = new DeviceInfoApi(defaultClient);
    try {
      List<Example14> result = apiInstance.timezones();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceInfoApi#timezones");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Example14&gt;**](Example14.md)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

