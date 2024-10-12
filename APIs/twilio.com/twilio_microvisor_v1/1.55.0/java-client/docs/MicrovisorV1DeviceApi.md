# MicrovisorV1DeviceApi

All URIs are relative to *https://microvisor.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchDevice**](MicrovisorV1DeviceApi.md#fetchDevice) | **GET** /v1/Devices/{Sid} |  |
| [**listDevice**](MicrovisorV1DeviceApi.md#listDevice) | **GET** /v1/Devices |  |
| [**updateDevice**](MicrovisorV1DeviceApi.md#updateDevice) | **POST** /v1/Devices/{Sid} |  |


<a id="fetchDevice"></a>
# **fetchDevice**
> MicrovisorV1Device fetchDevice(sid)



Fetch a specific Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceApi apiInstance = new MicrovisorV1DeviceApi(defaultClient);
    String sid = "sid_example"; // String | A 34-character string that uniquely identifies this Device.
    try {
      MicrovisorV1Device result = apiInstance.fetchDevice(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceApi#fetchDevice");
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
| **sid** | **String**| A 34-character string that uniquely identifies this Device. | |

### Return type

[**MicrovisorV1Device**](MicrovisorV1Device.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDevice"></a>
# **listDevice**
> ListDeviceResponse listDevice(pageSize, page, pageToken)



Retrieve a list of all Devices registered with the Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceApi apiInstance = new MicrovisorV1DeviceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDeviceResponse result = apiInstance.listDevice(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceApi#listDevice");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDeviceResponse**](ListDeviceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDevice"></a>
# **updateDevice**
> MicrovisorV1Device updateDevice(sid, loggingEnabled, restartApp, targetApp, uniqueName)



Update a specific Device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1DeviceApi apiInstance = new MicrovisorV1DeviceApi(defaultClient);
    String sid = "sid_example"; // String | A 34-character string that uniquely identifies this Device.
    Boolean loggingEnabled = true; // Boolean | A Boolean flag specifying whether to enable application logging. Logs will be enabled or extended for 24 hours.
    Boolean restartApp = true; // Boolean | Set to true to restart the App running on the Device.
    String targetApp = "targetApp_example"; // String | The SID or unique name of the App to be targeted to the Device.
    String uniqueName = "uniqueName_example"; // String | A unique and addressable name to be assigned to this Device by the developer. It may be used in place of the Device SID.
    try {
      MicrovisorV1Device result = apiInstance.updateDevice(sid, loggingEnabled, restartApp, targetApp, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1DeviceApi#updateDevice");
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
| **sid** | **String**| A 34-character string that uniquely identifies this Device. | |
| **loggingEnabled** | **Boolean**| A Boolean flag specifying whether to enable application logging. Logs will be enabled or extended for 24 hours. | [optional] |
| **restartApp** | **Boolean**| Set to true to restart the App running on the Device. | [optional] |
| **targetApp** | **String**| The SID or unique name of the App to be targeted to the Device. | [optional] |
| **uniqueName** | **String**| A unique and addressable name to be assigned to this Device by the developer. It may be used in place of the Device SID. | [optional] |

### Return type

[**MicrovisorV1Device**](MicrovisorV1Device.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

