# IpMessagingV2WebhookApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createChannelWebhook**](IpMessagingV2WebhookApi.md#createChannelWebhook) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks |  |
| [**deleteChannelWebhook**](IpMessagingV2WebhookApi.md#deleteChannelWebhook) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} |  |
| [**fetchChannelWebhook**](IpMessagingV2WebhookApi.md#fetchChannelWebhook) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} |  |
| [**listChannelWebhook**](IpMessagingV2WebhookApi.md#listChannelWebhook) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks |  |
| [**updateChannelWebhook**](IpMessagingV2WebhookApi.md#updateChannelWebhook) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} |  |


<a id="createChannelWebhook"></a>
# **createChannelWebhook**
> IpMessagingV2ServiceChannelChannelWebhook createChannelWebhook(serviceSid, channelSid, type, configurationFilters, configurationFlowSid, configurationMethod, configurationRetryCount, configurationTriggers, configurationUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2WebhookApi apiInstance = new IpMessagingV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    ChannelWebhookEnumType type = ChannelWebhookEnumType.fromValue("webhook"); // ChannelWebhookEnumType | 
    List<String> configurationFilters = Arrays.asList(); // List<String> | 
    String configurationFlowSid = "configurationFlowSid_example"; // String | 
    ChannelWebhookEnumMethod configurationMethod = ChannelWebhookEnumMethod.fromValue("GET"); // ChannelWebhookEnumMethod | 
    Integer configurationRetryCount = 56; // Integer | 
    List<String> configurationTriggers = Arrays.asList(); // List<String> | 
    String configurationUrl = "configurationUrl_example"; // String | 
    try {
      IpMessagingV2ServiceChannelChannelWebhook result = apiInstance.createChannelWebhook(serviceSid, channelSid, type, configurationFilters, configurationFlowSid, configurationMethod, configurationRetryCount, configurationTriggers, configurationUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2WebhookApi#createChannelWebhook");
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
| **serviceSid** | **String**|  | |
| **channelSid** | **String**|  | |
| **type** | **ChannelWebhookEnumType**|  | [enum: webhook, trigger, studio] |
| **configurationFilters** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **configurationFlowSid** | **String**|  | [optional] |
| **configurationMethod** | **ChannelWebhookEnumMethod**|  | [optional] [enum: GET, POST] |
| **configurationRetryCount** | **Integer**|  | [optional] |
| **configurationTriggers** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **configurationUrl** | **String**|  | [optional] |

### Return type

[**IpMessagingV2ServiceChannelChannelWebhook**](IpMessagingV2ServiceChannelChannelWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteChannelWebhook"></a>
# **deleteChannelWebhook**
> deleteChannelWebhook(serviceSid, channelSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2WebhookApi apiInstance = new IpMessagingV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteChannelWebhook(serviceSid, channelSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2WebhookApi#deleteChannelWebhook");
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
| **serviceSid** | **String**|  | |
| **channelSid** | **String**|  | |
| **sid** | **String**|  | |

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

<a id="fetchChannelWebhook"></a>
# **fetchChannelWebhook**
> IpMessagingV2ServiceChannelChannelWebhook fetchChannelWebhook(serviceSid, channelSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2WebhookApi apiInstance = new IpMessagingV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV2ServiceChannelChannelWebhook result = apiInstance.fetchChannelWebhook(serviceSid, channelSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2WebhookApi#fetchChannelWebhook");
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
| **serviceSid** | **String**|  | |
| **channelSid** | **String**|  | |
| **sid** | **String**|  | |

### Return type

[**IpMessagingV2ServiceChannelChannelWebhook**](IpMessagingV2ServiceChannelChannelWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listChannelWebhook"></a>
# **listChannelWebhook**
> ListChannelWebhookResponse listChannelWebhook(serviceSid, channelSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2WebhookApi apiInstance = new IpMessagingV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListChannelWebhookResponse result = apiInstance.listChannelWebhook(serviceSid, channelSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2WebhookApi#listChannelWebhook");
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
| **serviceSid** | **String**|  | |
| **channelSid** | **String**|  | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListChannelWebhookResponse**](ListChannelWebhookResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateChannelWebhook"></a>
# **updateChannelWebhook**
> IpMessagingV2ServiceChannelChannelWebhook updateChannelWebhook(serviceSid, channelSid, sid, configurationFilters, configurationFlowSid, configurationMethod, configurationRetryCount, configurationTriggers, configurationUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2WebhookApi apiInstance = new IpMessagingV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String sid = "sid_example"; // String | 
    List<String> configurationFilters = Arrays.asList(); // List<String> | 
    String configurationFlowSid = "configurationFlowSid_example"; // String | 
    ChannelWebhookEnumMethod configurationMethod = ChannelWebhookEnumMethod.fromValue("GET"); // ChannelWebhookEnumMethod | 
    Integer configurationRetryCount = 56; // Integer | 
    List<String> configurationTriggers = Arrays.asList(); // List<String> | 
    String configurationUrl = "configurationUrl_example"; // String | 
    try {
      IpMessagingV2ServiceChannelChannelWebhook result = apiInstance.updateChannelWebhook(serviceSid, channelSid, sid, configurationFilters, configurationFlowSid, configurationMethod, configurationRetryCount, configurationTriggers, configurationUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2WebhookApi#updateChannelWebhook");
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
| **serviceSid** | **String**|  | |
| **channelSid** | **String**|  | |
| **sid** | **String**|  | |
| **configurationFilters** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **configurationFlowSid** | **String**|  | [optional] |
| **configurationMethod** | **ChannelWebhookEnumMethod**|  | [optional] [enum: GET, POST] |
| **configurationRetryCount** | **Integer**|  | [optional] |
| **configurationTriggers** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **configurationUrl** | **String**|  | [optional] |

### Return type

[**IpMessagingV2ServiceChannelChannelWebhook**](IpMessagingV2ServiceChannelChannelWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

