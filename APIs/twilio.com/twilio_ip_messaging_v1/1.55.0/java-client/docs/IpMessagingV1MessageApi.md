# IpMessagingV1MessageApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMessage**](IpMessagingV1MessageApi.md#createMessage) | **POST** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Messages |  |
| [**deleteMessage**](IpMessagingV1MessageApi.md#deleteMessage) | **DELETE** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} |  |
| [**fetchMessage**](IpMessagingV1MessageApi.md#fetchMessage) | **GET** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} |  |
| [**listMessage**](IpMessagingV1MessageApi.md#listMessage) | **GET** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Messages |  |
| [**updateMessage**](IpMessagingV1MessageApi.md#updateMessage) | **POST** /v1/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} |  |


<a id="createMessage"></a>
# **createMessage**
> IpMessagingV1ServiceChannelMessage createMessage(serviceSid, channelSid, body, attributes, from)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1MessageApi apiInstance = new IpMessagingV1MessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String body = "body_example"; // String | 
    String attributes = "attributes_example"; // String | 
    String from = "from_example"; // String | 
    try {
      IpMessagingV1ServiceChannelMessage result = apiInstance.createMessage(serviceSid, channelSid, body, attributes, from);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1MessageApi#createMessage");
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
| **body** | **String**|  | |
| **attributes** | **String**|  | [optional] |
| **from** | **String**|  | [optional] |

### Return type

[**IpMessagingV1ServiceChannelMessage**](IpMessagingV1ServiceChannelMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteMessage"></a>
# **deleteMessage**
> deleteMessage(serviceSid, channelSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1MessageApi apiInstance = new IpMessagingV1MessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteMessage(serviceSid, channelSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1MessageApi#deleteMessage");
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

<a id="fetchMessage"></a>
# **fetchMessage**
> IpMessagingV1ServiceChannelMessage fetchMessage(serviceSid, channelSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1MessageApi apiInstance = new IpMessagingV1MessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV1ServiceChannelMessage result = apiInstance.fetchMessage(serviceSid, channelSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1MessageApi#fetchMessage");
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

[**IpMessagingV1ServiceChannelMessage**](IpMessagingV1ServiceChannelMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMessage"></a>
# **listMessage**
> ListMessageResponse listMessage(serviceSid, channelSid, order, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1MessageApi apiInstance = new IpMessagingV1MessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    MessageEnumOrderType order = MessageEnumOrderType.fromValue("asc"); // MessageEnumOrderType | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMessageResponse result = apiInstance.listMessage(serviceSid, channelSid, order, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1MessageApi#listMessage");
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
| **order** | **MessageEnumOrderType**|  | [optional] [enum: asc, desc] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListMessageResponse**](ListMessageResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateMessage"></a>
# **updateMessage**
> IpMessagingV1ServiceChannelMessage updateMessage(serviceSid, channelSid, sid, attributes, body)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1MessageApi apiInstance = new IpMessagingV1MessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String sid = "sid_example"; // String | 
    String attributes = "attributes_example"; // String | 
    String body = "body_example"; // String | 
    try {
      IpMessagingV1ServiceChannelMessage result = apiInstance.updateMessage(serviceSid, channelSid, sid, attributes, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1MessageApi#updateMessage");
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
| **attributes** | **String**|  | [optional] |
| **body** | **String**|  | [optional] |

### Return type

[**IpMessagingV1ServiceChannelMessage**](IpMessagingV1ServiceChannelMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

