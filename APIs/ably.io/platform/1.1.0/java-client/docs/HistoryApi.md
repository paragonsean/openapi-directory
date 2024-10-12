# HistoryApi

All URIs are relative to *https://rest.ably.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMessagesByChannel**](HistoryApi.md#getMessagesByChannel) | **GET** /channels/{channel_id}/messages | Get message history for a channel |
| [**getPresenceHistoryOfChannel**](HistoryApi.md#getPresenceHistoryOfChannel) | **GET** /channels/{channel_id}/presence/history | Get presence history of a channel |


<a id="getMessagesByChannel"></a>
# **getMessagesByChannel**
> List&lt;Message&gt; getMessagesByChannel(channelId, xAblyVersion, format, start, limit, end, direction)

Get message history for a channel

Get message history for a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String channelId = "channelId_example"; // String | The [Channel's ID](https://www.ably.io/documentation/rest/channels).
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    String start = "start_example"; // String | 
    Integer limit = 56; // Integer | 
    String end = "now"; // String | 
    String direction = "forwards"; // String | 
    try {
      List<Message> result = apiInstance.getMessagesByChannel(channelId, xAblyVersion, format, start, limit, end, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#getMessagesByChannel");
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
| **channelId** | **String**| The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels). | |
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **start** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **end** | **String**|  | [optional] [default to now] |
| **direction** | **String**|  | [optional] [default to backwards] [enum: forwards, backwards] |

### Return type

[**List&lt;Message&gt;**](Message.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  * link -  <br>  * x-ably-serverid -  <br>  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="getPresenceHistoryOfChannel"></a>
# **getPresenceHistoryOfChannel**
> List&lt;PresenceMessage&gt; getPresenceHistoryOfChannel(channelId, xAblyVersion, format, start, limit, end, direction)

Get presence history of a channel

Get presence on a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String channelId = "channelId_example"; // String | The [Channel's ID](https://www.ably.io/documentation/rest/channels).
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    String start = "start_example"; // String | 
    Integer limit = 56; // Integer | 
    String end = "now"; // String | 
    String direction = "forwards"; // String | 
    try {
      List<PresenceMessage> result = apiInstance.getPresenceHistoryOfChannel(channelId, xAblyVersion, format, start, limit, end, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#getPresenceHistoryOfChannel");
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
| **channelId** | **String**| The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels). | |
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **start** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |
| **end** | **String**|  | [optional] [default to now] |
| **direction** | **String**|  | [optional] [default to backwards] [enum: forwards, backwards] |

### Return type

[**List&lt;PresenceMessage&gt;**](PresenceMessage.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  * link -  <br>  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

