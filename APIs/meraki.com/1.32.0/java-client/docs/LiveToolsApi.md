# LiveToolsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blinkDeviceLeds_0**](LiveToolsApi.md#blinkDeviceLeds_0) | **POST** /devices/{serial}/blinkLeds | Blink the LEDs on a device |
| [**createDeviceLiveToolsPingDevice_0**](LiveToolsApi.md#createDeviceLiveToolsPingDevice_0) | **POST** /devices/{serial}/liveTools/pingDevice | Enqueue a job to check connectivity status to the device |
| [**createDeviceLiveToolsPing_0**](LiveToolsApi.md#createDeviceLiveToolsPing_0) | **POST** /devices/{serial}/liveTools/ping | Enqueue a job to ping a target host from the device |
| [**cycleDeviceSwitchPorts_0**](LiveToolsApi.md#cycleDeviceSwitchPorts_0) | **POST** /devices/{serial}/switch/ports/cycle | Cycle a set of switch ports |
| [**getDeviceLiveToolsPingDevice_0**](LiveToolsApi.md#getDeviceLiveToolsPingDevice_0) | **GET** /devices/{serial}/liveTools/pingDevice/{id} | Return a ping device job |
| [**getDeviceLiveToolsPing_0**](LiveToolsApi.md#getDeviceLiveToolsPing_0) | **GET** /devices/{serial}/liveTools/ping/{id} | Return a ping job |
| [**rebootDevice_0**](LiveToolsApi.md#rebootDevice_0) | **POST** /devices/{serial}/reboot | Reboot a device |


<a id="blinkDeviceLeds_0"></a>
# **blinkDeviceLeds_0**
> Object blinkDeviceLeds_0(serial, blinkDeviceLedsRequest)

Blink the LEDs on a device

Blink the LEDs on a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LiveToolsApi apiInstance = new LiveToolsApi(defaultClient);
    String serial = "serial_example"; // String | 
    BlinkDeviceLedsRequest blinkDeviceLedsRequest = new BlinkDeviceLedsRequest(); // BlinkDeviceLedsRequest | 
    try {
      Object result = apiInstance.blinkDeviceLeds_0(serial, blinkDeviceLedsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveToolsApi#blinkDeviceLeds_0");
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
| **blinkDeviceLedsRequest** | [**BlinkDeviceLedsRequest**](BlinkDeviceLedsRequest.md)|  | [optional] |

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
| **202** | Successful operation |  -  |

<a id="createDeviceLiveToolsPingDevice_0"></a>
# **createDeviceLiveToolsPingDevice_0**
> CreateDeviceLiveToolsPing201Response createDeviceLiveToolsPingDevice_0(serial, createDeviceLiveToolsPingDeviceRequest)

Enqueue a job to check connectivity status to the device

Enqueue a job to check connectivity status to the device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LiveToolsApi apiInstance = new LiveToolsApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceLiveToolsPingDeviceRequest createDeviceLiveToolsPingDeviceRequest = new CreateDeviceLiveToolsPingDeviceRequest(); // CreateDeviceLiveToolsPingDeviceRequest | 
    try {
      CreateDeviceLiveToolsPing201Response result = apiInstance.createDeviceLiveToolsPingDevice_0(serial, createDeviceLiveToolsPingDeviceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveToolsApi#createDeviceLiveToolsPingDevice_0");
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
| **createDeviceLiveToolsPingDeviceRequest** | [**CreateDeviceLiveToolsPingDeviceRequest**](CreateDeviceLiveToolsPingDeviceRequest.md)|  | [optional] |

### Return type

[**CreateDeviceLiveToolsPing201Response**](CreateDeviceLiveToolsPing201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createDeviceLiveToolsPing_0"></a>
# **createDeviceLiveToolsPing_0**
> CreateDeviceLiveToolsPing201Response createDeviceLiveToolsPing_0(serial, createDeviceLiveToolsPingRequest)

Enqueue a job to ping a target host from the device

Enqueue a job to ping a target host from the device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LiveToolsApi apiInstance = new LiveToolsApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceLiveToolsPingRequest createDeviceLiveToolsPingRequest = new CreateDeviceLiveToolsPingRequest(); // CreateDeviceLiveToolsPingRequest | 
    try {
      CreateDeviceLiveToolsPing201Response result = apiInstance.createDeviceLiveToolsPing_0(serial, createDeviceLiveToolsPingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveToolsApi#createDeviceLiveToolsPing_0");
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
| **createDeviceLiveToolsPingRequest** | [**CreateDeviceLiveToolsPingRequest**](CreateDeviceLiveToolsPingRequest.md)|  | |

### Return type

[**CreateDeviceLiveToolsPing201Response**](CreateDeviceLiveToolsPing201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="cycleDeviceSwitchPorts_0"></a>
# **cycleDeviceSwitchPorts_0**
> Object cycleDeviceSwitchPorts_0(serial, cycleDeviceSwitchPortsRequest)

Cycle a set of switch ports

Cycle a set of switch ports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LiveToolsApi apiInstance = new LiveToolsApi(defaultClient);
    String serial = "serial_example"; // String | 
    CycleDeviceSwitchPortsRequest cycleDeviceSwitchPortsRequest = new CycleDeviceSwitchPortsRequest(); // CycleDeviceSwitchPortsRequest | 
    try {
      Object result = apiInstance.cycleDeviceSwitchPorts_0(serial, cycleDeviceSwitchPortsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveToolsApi#cycleDeviceSwitchPorts_0");
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
| **cycleDeviceSwitchPortsRequest** | [**CycleDeviceSwitchPortsRequest**](CycleDeviceSwitchPortsRequest.md)|  | |

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

<a id="getDeviceLiveToolsPingDevice_0"></a>
# **getDeviceLiveToolsPingDevice_0**
> GetDeviceLiveToolsPing200Response getDeviceLiveToolsPingDevice_0(serial, id)

Return a ping device job

Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LiveToolsApi apiInstance = new LiveToolsApi(defaultClient);
    String serial = "serial_example"; // String | 
    String id = "id_example"; // String | 
    try {
      GetDeviceLiveToolsPing200Response result = apiInstance.getDeviceLiveToolsPingDevice_0(serial, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveToolsApi#getDeviceLiveToolsPingDevice_0");
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
| **id** | **String**|  | |

### Return type

[**GetDeviceLiveToolsPing200Response**](GetDeviceLiveToolsPing200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceLiveToolsPing_0"></a>
# **getDeviceLiveToolsPing_0**
> GetDeviceLiveToolsPing200Response getDeviceLiveToolsPing_0(serial, id)

Return a ping job

Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LiveToolsApi apiInstance = new LiveToolsApi(defaultClient);
    String serial = "serial_example"; // String | 
    String id = "id_example"; // String | 
    try {
      GetDeviceLiveToolsPing200Response result = apiInstance.getDeviceLiveToolsPing_0(serial, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveToolsApi#getDeviceLiveToolsPing_0");
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
| **id** | **String**|  | |

### Return type

[**GetDeviceLiveToolsPing200Response**](GetDeviceLiveToolsPing200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="rebootDevice_0"></a>
# **rebootDevice_0**
> Object rebootDevice_0(serial)

Reboot a device

Reboot a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LiveToolsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LiveToolsApi apiInstance = new LiveToolsApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.rebootDevice_0(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LiveToolsApi#rebootDevice_0");
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
| **202** | Successful operation |  -  |

