# MicrovisorV1DeviceConfigApi

All URIs are relative to *https://microvisor.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeviceConfig**](MicrovisorV1DeviceConfigApi.md#createDeviceConfig) | **POST** /v1/Devices/{DeviceSid}/Configs |  |
| [**deleteDeviceConfig**](MicrovisorV1DeviceConfigApi.md#deleteDeviceConfig) | **DELETE** /v1/Devices/{DeviceSid}/Configs/{Key} |  |
| [**fetchDeviceConfig**](MicrovisorV1DeviceConfigApi.md#fetchDeviceConfig) | **GET** /v1/Devices/{DeviceSid}/Configs/{Key} |  |
| [**listDeviceConfig**](MicrovisorV1DeviceConfigApi.md#listDeviceConfig) | **GET** /v1/Devices/{DeviceSid}/Configs |  |
| [**updateDeviceConfig**](MicrovisorV1DeviceConfigApi.md#updateDeviceConfig) | **POST** /v1/Devices/{DeviceSid}/Configs/{Key} |  |


<a id="createDeviceConfig"></a>
# **createDeviceConfig**
> MicrovisorV1DeviceDeviceConfig createDeviceConfig(deviceSid, key, value)



Create a config for a Microvisor Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceConfigApi apiInstance = new MicrovisorV1DeviceConfigApi(defaultClient);
    String deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
    String key = "key_example"; // String | The config key; up to 100 characters.
    String value = "value_example"; // String | The config value; up to 4096 characters.
    try {
      MicrovisorV1DeviceDeviceConfig result = apiInstance.createDeviceConfig(deviceSid, key, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceConfigApi#createDeviceConfig");
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
| **deviceSid** | **String**| A 34-character string that uniquely identifies the Device. | |
| **key** | **String**| The config key; up to 100 characters. | |
| **value** | **String**| The config value; up to 4096 characters. | |

### Return type

[**MicrovisorV1DeviceDeviceConfig**](MicrovisorV1DeviceDeviceConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteDeviceConfig"></a>
# **deleteDeviceConfig**
> deleteDeviceConfig(deviceSid, key)



Delete a config for a Microvisor Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceConfigApi apiInstance = new MicrovisorV1DeviceConfigApi(defaultClient);
    String deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
    String key = "key_example"; // String | The config key; up to 100 characters.
    try {
      apiInstance.deleteDeviceConfig(deviceSid, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceConfigApi#deleteDeviceConfig");
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
| **deviceSid** | **String**| A 34-character string that uniquely identifies the Device. | |
| **key** | **String**| The config key; up to 100 characters. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchDeviceConfig"></a>
# **fetchDeviceConfig**
> MicrovisorV1DeviceDeviceConfig fetchDeviceConfig(deviceSid, key)



Retrieve a Config for a Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceConfigApi apiInstance = new MicrovisorV1DeviceConfigApi(defaultClient);
    String deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
    String key = "key_example"; // String | The config key; up to 100 characters.
    try {
      MicrovisorV1DeviceDeviceConfig result = apiInstance.fetchDeviceConfig(deviceSid, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceConfigApi#fetchDeviceConfig");
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
| **deviceSid** | **String**| A 34-character string that uniquely identifies the Device. | |
| **key** | **String**| The config key; up to 100 characters. | |

### Return type

[**MicrovisorV1DeviceDeviceConfig**](MicrovisorV1DeviceDeviceConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDeviceConfig"></a>
# **listDeviceConfig**
> ListDeviceConfigResponse listDeviceConfig(deviceSid, pageSize, page, pageToken)



Retrieve a list of all Configs for a Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceConfigApi apiInstance = new MicrovisorV1DeviceConfigApi(defaultClient);
    String deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDeviceConfigResponse result = apiInstance.listDeviceConfig(deviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceConfigApi#listDeviceConfig");
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
| **deviceSid** | **String**| A 34-character string that uniquely identifies the Device. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDeviceConfigResponse**](ListDeviceConfigResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDeviceConfig"></a>
# **updateDeviceConfig**
> MicrovisorV1DeviceDeviceConfig updateDeviceConfig(deviceSid, key, value)



Update a config for a Microvisor Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceConfigApi apiInstance = new MicrovisorV1DeviceConfigApi(defaultClient);
    String deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
    String key = "key_example"; // String | The config key; up to 100 characters.
    String value = "value_example"; // String | The config value; up to 4096 characters.
    try {
      MicrovisorV1DeviceDeviceConfig result = apiInstance.updateDeviceConfig(deviceSid, key, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceConfigApi#updateDeviceConfig");
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
| **deviceSid** | **String**| A 34-character string that uniquely identifies the Device. | |
| **key** | **String**| The config key; up to 100 characters. | |
| **value** | **String**| The config value; up to 4096 characters. | |

### Return type

[**MicrovisorV1DeviceDeviceConfig**](MicrovisorV1DeviceDeviceConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

