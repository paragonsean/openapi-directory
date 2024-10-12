# IpMessagingV2ChannelApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createChannel**](IpMessagingV2ChannelApi.md#createChannel) | **POST** /v2/Services/{ServiceSid}/Channels |  |
| [**deleteChannel**](IpMessagingV2ChannelApi.md#deleteChannel) | **DELETE** /v2/Services/{ServiceSid}/Channels/{Sid} |  |
| [**fetchChannel**](IpMessagingV2ChannelApi.md#fetchChannel) | **GET** /v2/Services/{ServiceSid}/Channels/{Sid} |  |
| [**listChannel**](IpMessagingV2ChannelApi.md#listChannel) | **GET** /v2/Services/{ServiceSid}/Channels |  |
| [**updateChannel**](IpMessagingV2ChannelApi.md#updateChannel) | **POST** /v2/Services/{ServiceSid}/Channels/{Sid} |  |


<a id="createChannel"></a>
# **createChannel**
> IpMessagingV2ServiceChannel createChannel(serviceSid, xTwilioWebhookEnabled, attributes, createdBy, dateCreated, dateUpdated, friendlyName, type, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2ChannelApi apiInstance = new IpMessagingV2ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    ChannelEnumWebhookEnabledType xTwilioWebhookEnabled = ChannelEnumWebhookEnabledType.fromValue("true"); // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | 
    String createdBy = "createdBy_example"; // String | 
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | 
    String friendlyName = "friendlyName_example"; // String | 
    ChannelEnumChannelType type = ChannelEnumChannelType.fromValue("public"); // ChannelEnumChannelType | 
    String uniqueName = "uniqueName_example"; // String | 
    try {
      IpMessagingV2ServiceChannel result = apiInstance.createChannel(serviceSid, xTwilioWebhookEnabled, attributes, createdBy, dateCreated, dateUpdated, friendlyName, type, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2ChannelApi#createChannel");
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
| **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**|  | [optional] |
| **createdBy** | **String**|  | [optional] |
| **dateCreated** | **OffsetDateTime**|  | [optional] |
| **dateUpdated** | **OffsetDateTime**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **type** | **ChannelEnumChannelType**|  | [optional] [enum: public, private] |
| **uniqueName** | **String**|  | [optional] |

### Return type

[**IpMessagingV2ServiceChannel**](IpMessagingV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteChannel"></a>
# **deleteChannel**
> deleteChannel(serviceSid, sid, xTwilioWebhookEnabled)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2ChannelApi apiInstance = new IpMessagingV2ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    ChannelEnumWebhookEnabledType xTwilioWebhookEnabled = ChannelEnumWebhookEnabledType.fromValue("true"); // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteChannel(serviceSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2ChannelApi#deleteChannel");
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
| **sid** | **String**|  | |
| **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="fetchChannel"></a>
# **fetchChannel**
> IpMessagingV2ServiceChannel fetchChannel(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2ChannelApi apiInstance = new IpMessagingV2ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV2ServiceChannel result = apiInstance.fetchChannel(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2ChannelApi#fetchChannel");
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
| **sid** | **String**|  | |

### Return type

[**IpMessagingV2ServiceChannel**](IpMessagingV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listChannel"></a>
# **listChannel**
> ListChannelResponse listChannel(serviceSid, type, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2ChannelApi apiInstance = new IpMessagingV2ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    List<ChannelEnumChannelType> type = Arrays.asList(); // List<ChannelEnumChannelType> | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListChannelResponse result = apiInstance.listChannel(serviceSid, type, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2ChannelApi#listChannel");
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
| **type** | [**List&lt;ChannelEnumChannelType&gt;**](ChannelEnumChannelType.md)|  | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListChannelResponse**](ListChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateChannel"></a>
# **updateChannel**
> IpMessagingV2ServiceChannel updateChannel(serviceSid, sid, xTwilioWebhookEnabled, attributes, createdBy, dateCreated, dateUpdated, friendlyName, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2ChannelApi apiInstance = new IpMessagingV2ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    ChannelEnumWebhookEnabledType xTwilioWebhookEnabled = ChannelEnumWebhookEnabledType.fromValue("true"); // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | 
    String createdBy = "createdBy_example"; // String | 
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | 
    String friendlyName = "friendlyName_example"; // String | 
    String uniqueName = "uniqueName_example"; // String | 
    try {
      IpMessagingV2ServiceChannel result = apiInstance.updateChannel(serviceSid, sid, xTwilioWebhookEnabled, attributes, createdBy, dateCreated, dateUpdated, friendlyName, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2ChannelApi#updateChannel");
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
| **sid** | **String**|  | |
| **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**|  | [optional] |
| **createdBy** | **String**|  | [optional] |
| **dateCreated** | **OffsetDateTime**|  | [optional] |
| **dateUpdated** | **OffsetDateTime**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **uniqueName** | **String**|  | [optional] |

### Return type

[**IpMessagingV2ServiceChannel**](IpMessagingV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

