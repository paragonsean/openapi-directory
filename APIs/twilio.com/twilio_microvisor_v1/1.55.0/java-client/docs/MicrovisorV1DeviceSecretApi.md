# MicrovisorV1DeviceSecretApi

All URIs are relative to *https://microvisor.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeviceSecret**](MicrovisorV1DeviceSecretApi.md#createDeviceSecret) | **POST** /v1/Devices/{DeviceSid}/Secrets |  |
| [**deleteDeviceSecret**](MicrovisorV1DeviceSecretApi.md#deleteDeviceSecret) | **DELETE** /v1/Devices/{DeviceSid}/Secrets/{Key} |  |
| [**fetchDeviceSecret**](MicrovisorV1DeviceSecretApi.md#fetchDeviceSecret) | **GET** /v1/Devices/{DeviceSid}/Secrets/{Key} |  |
| [**listDeviceSecret**](MicrovisorV1DeviceSecretApi.md#listDeviceSecret) | **GET** /v1/Devices/{DeviceSid}/Secrets |  |
| [**updateDeviceSecret**](MicrovisorV1DeviceSecretApi.md#updateDeviceSecret) | **POST** /v1/Devices/{DeviceSid}/Secrets/{Key} |  |


<a id="createDeviceSecret"></a>
# **createDeviceSecret**
> MicrovisorV1DeviceDeviceSecret createDeviceSecret(deviceSid, key, value)



Create a secret for a Microvisor Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceSecretApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceSecretApi apiInstance = new MicrovisorV1DeviceSecretApi(defaultClient);
    String deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
    String key = "key_example"; // String | The secret key; up to 100 characters.
    String value = "value_example"; // String | The secret value; up to 4096 characters.
    try {
      MicrovisorV1DeviceDeviceSecret result = apiInstance.createDeviceSecret(deviceSid, key, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceSecretApi#createDeviceSecret");
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
| **key** | **String**| The secret key; up to 100 characters. | |
| **value** | **String**| The secret value; up to 4096 characters. | |

### Return type

[**MicrovisorV1DeviceDeviceSecret**](MicrovisorV1DeviceDeviceSecret.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteDeviceSecret"></a>
# **deleteDeviceSecret**
> deleteDeviceSecret(deviceSid, key)



Delete a secret for a Microvisor Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceSecretApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceSecretApi apiInstance = new MicrovisorV1DeviceSecretApi(defaultClient);
    String deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
    String key = "key_example"; // String | The secret key; up to 100 characters.
    try {
      apiInstance.deleteDeviceSecret(deviceSid, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceSecretApi#deleteDeviceSecret");
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
| **key** | **String**| The secret key; up to 100 characters. | |

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

<a id="fetchDeviceSecret"></a>
# **fetchDeviceSecret**
> MicrovisorV1DeviceDeviceSecret fetchDeviceSecret(deviceSid, key)



Retrieve a Secret for a Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceSecretApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceSecretApi apiInstance = new MicrovisorV1DeviceSecretApi(defaultClient);
    String deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
    String key = "key_example"; // String | The secret key; up to 100 characters.
    try {
      MicrovisorV1DeviceDeviceSecret result = apiInstance.fetchDeviceSecret(deviceSid, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceSecretApi#fetchDeviceSecret");
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
| **key** | **String**| The secret key; up to 100 characters. | |

### Return type

[**MicrovisorV1DeviceDeviceSecret**](MicrovisorV1DeviceDeviceSecret.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDeviceSecret"></a>
# **listDeviceSecret**
> ListDeviceSecretResponse listDeviceSecret(deviceSid, pageSize, page, pageToken)



Retrieve a list of all Secrets for a Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceSecretApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceSecretApi apiInstance = new MicrovisorV1DeviceSecretApi(defaultClient);
    String deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDeviceSecretResponse result = apiInstance.listDeviceSecret(deviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceSecretApi#listDeviceSecret");
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

[**ListDeviceSecretResponse**](ListDeviceSecretResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDeviceSecret"></a>
# **updateDeviceSecret**
> MicrovisorV1DeviceDeviceSecret updateDeviceSecret(deviceSid, key, value)



Update a secret for a Microvisor Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceSecretApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceSecretApi apiInstance = new MicrovisorV1DeviceSecretApi(defaultClient);
    String deviceSid = "deviceSid_example"; // String | A 34-character string that uniquely identifies the Device.
    String key = "key_example"; // String | The secret key; up to 100 characters.
    String value = "value_example"; // String | The secret value; up to 4096 characters.
    try {
      MicrovisorV1DeviceDeviceSecret result = apiInstance.updateDeviceSecret(deviceSid, key, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceSecretApi#updateDeviceSecret");
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
| **key** | **String**| The secret key; up to 100 characters. | |
| **value** | **String**| The secret value; up to 4096 characters. | |

### Return type

[**MicrovisorV1DeviceDeviceSecret**](MicrovisorV1DeviceDeviceSecret.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

