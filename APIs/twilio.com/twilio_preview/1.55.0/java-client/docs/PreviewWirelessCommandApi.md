# PreviewWirelessCommandApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWirelessCommand**](PreviewWirelessCommandApi.md#createWirelessCommand) | **POST** /wireless/Commands |  |
| [**fetchWirelessCommand**](PreviewWirelessCommandApi.md#fetchWirelessCommand) | **GET** /wireless/Commands/{Sid} |  |
| [**listWirelessCommand**](PreviewWirelessCommandApi.md#listWirelessCommand) | **GET** /wireless/Commands |  |


<a id="createWirelessCommand"></a>
# **createWirelessCommand**
> PreviewWirelessCommand createWirelessCommand(command, callbackMethod, callbackUrl, commandMode, device, includeSid, sim)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessCommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessCommandApi apiInstance = new PreviewWirelessCommandApi(defaultClient);
    String command = "command_example"; // String | 
    String callbackMethod = "callbackMethod_example"; // String | 
    URI callbackUrl = new URI(); // URI | 
    String commandMode = "commandMode_example"; // String | 
    String device = "device_example"; // String | 
    String includeSid = "includeSid_example"; // String | 
    String sim = "sim_example"; // String | 
    try {
      PreviewWirelessCommand result = apiInstance.createWirelessCommand(command, callbackMethod, callbackUrl, commandMode, device, includeSid, sim);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessCommandApi#createWirelessCommand");
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
| **command** | **String**|  | |
| **callbackMethod** | **String**|  | [optional] |
| **callbackUrl** | **URI**|  | [optional] |
| **commandMode** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **includeSid** | **String**|  | [optional] |
| **sim** | **String**|  | [optional] |

### Return type

[**PreviewWirelessCommand**](PreviewWirelessCommand.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchWirelessCommand"></a>
# **fetchWirelessCommand**
> PreviewWirelessCommand fetchWirelessCommand(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessCommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessCommandApi apiInstance = new PreviewWirelessCommandApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      PreviewWirelessCommand result = apiInstance.fetchWirelessCommand(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessCommandApi#fetchWirelessCommand");
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
| **sid** | **String**|  | |

### Return type

[**PreviewWirelessCommand**](PreviewWirelessCommand.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listWirelessCommand"></a>
# **listWirelessCommand**
> ListWirelessCommandResponse listWirelessCommand(device, sim, status, direction, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessCommandApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessCommandApi apiInstance = new PreviewWirelessCommandApi(defaultClient);
    String device = "device_example"; // String | 
    String sim = "sim_example"; // String | 
    String status = "status_example"; // String | 
    String direction = "direction_example"; // String | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListWirelessCommandResponse result = apiInstance.listWirelessCommand(device, sim, status, direction, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessCommandApi#listWirelessCommand");
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
| **device** | **String**|  | [optional] |
| **sim** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **direction** | **String**|  | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListWirelessCommandResponse**](ListWirelessCommandResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

