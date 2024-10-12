# PreviewWirelessSimApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchWirelessSim**](PreviewWirelessSimApi.md#fetchWirelessSim) | **GET** /wireless/Sims/{Sid} |  |
| [**listWirelessSim**](PreviewWirelessSimApi.md#listWirelessSim) | **GET** /wireless/Sims |  |
| [**updateWirelessSim**](PreviewWirelessSimApi.md#updateWirelessSim) | **POST** /wireless/Sims/{Sid} |  |


<a id="fetchWirelessSim"></a>
# **fetchWirelessSim**
> PreviewWirelessSim fetchWirelessSim(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessSimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessSimApi apiInstance = new PreviewWirelessSimApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      PreviewWirelessSim result = apiInstance.fetchWirelessSim(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessSimApi#fetchWirelessSim");
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

[**PreviewWirelessSim**](PreviewWirelessSim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listWirelessSim"></a>
# **listWirelessSim**
> ListWirelessSimResponse listWirelessSim(status, iccid, ratePlan, eid, simRegistrationCode, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessSimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessSimApi apiInstance = new PreviewWirelessSimApi(defaultClient);
    String status = "status_example"; // String | 
    String iccid = "iccid_example"; // String | 
    String ratePlan = "ratePlan_example"; // String | 
    String eid = "eid_example"; // String | 
    String simRegistrationCode = "simRegistrationCode_example"; // String | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListWirelessSimResponse result = apiInstance.listWirelessSim(status, iccid, ratePlan, eid, simRegistrationCode, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessSimApi#listWirelessSim");
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
| **status** | **String**|  | [optional] |
| **iccid** | **String**|  | [optional] |
| **ratePlan** | **String**|  | [optional] |
| **eid** | **String**|  | [optional] |
| **simRegistrationCode** | **String**|  | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListWirelessSimResponse**](ListWirelessSimResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateWirelessSim"></a>
# **updateWirelessSim**
> PreviewWirelessSim updateWirelessSim(sid, callbackMethod, callbackUrl, commandsCallbackMethod, commandsCallbackUrl, friendlyName, ratePlan, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, status, uniqueName, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessSimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessSimApi apiInstance = new PreviewWirelessSimApi(defaultClient);
    String sid = "sid_example"; // String | 
    String callbackMethod = "callbackMethod_example"; // String | 
    URI callbackUrl = new URI(); // URI | 
    String commandsCallbackMethod = "HEAD"; // String | 
    URI commandsCallbackUrl = new URI(); // URI | 
    String friendlyName = "friendlyName_example"; // String | 
    String ratePlan = "ratePlan_example"; // String | 
    String smsFallbackMethod = "HEAD"; // String | 
    URI smsFallbackUrl = new URI(); // URI | 
    String smsMethod = "HEAD"; // String | 
    URI smsUrl = new URI(); // URI | 
    String status = "status_example"; // String | 
    String uniqueName = "uniqueName_example"; // String | 
    String voiceFallbackMethod = "HEAD"; // String | 
    URI voiceFallbackUrl = new URI(); // URI | 
    String voiceMethod = "HEAD"; // String | 
    URI voiceUrl = new URI(); // URI | 
    try {
      PreviewWirelessSim result = apiInstance.updateWirelessSim(sid, callbackMethod, callbackUrl, commandsCallbackMethod, commandsCallbackUrl, friendlyName, ratePlan, smsFallbackMethod, smsFallbackUrl, smsMethod, smsUrl, status, uniqueName, voiceFallbackMethod, voiceFallbackUrl, voiceMethod, voiceUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessSimApi#updateWirelessSim");
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
| **callbackMethod** | **String**|  | [optional] |
| **callbackUrl** | **URI**|  | [optional] |
| **commandsCallbackMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **commandsCallbackUrl** | **URI**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **ratePlan** | **String**|  | [optional] |
| **smsFallbackMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsFallbackUrl** | **URI**|  | [optional] |
| **smsMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **smsUrl** | **URI**|  | [optional] |
| **status** | **String**|  | [optional] |
| **uniqueName** | **String**|  | [optional] |
| **voiceFallbackMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceFallbackUrl** | **URI**|  | [optional] |
| **voiceMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **voiceUrl** | **URI**|  | [optional] |

### Return type

[**PreviewWirelessSim**](PreviewWirelessSim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

