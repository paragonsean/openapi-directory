# ChatV2MessageApi

All URIs are relative to *https://chat.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMessage**](ChatV2MessageApi.md#createMessage) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages |  |
| [**deleteMessage**](ChatV2MessageApi.md#deleteMessage) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} |  |
| [**fetchMessage**](ChatV2MessageApi.md#fetchMessage) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} |  |
| [**listMessage**](ChatV2MessageApi.md#listMessage) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages |  |
| [**updateMessage**](ChatV2MessageApi.md#updateMessage) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} |  |


<a id="createMessage"></a>
# **createMessage**
> ChatV2ServiceChannelMessage createMessage(serviceSid, channelSid, xTwilioWebhookEnabled, attributes, body, dateCreated, dateUpdated, from, lastUpdatedBy, mediaSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2MessageApi apiInstance = new ChatV2MessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Message resource under.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Message resource belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    MessageEnumWebhookEnabledType xTwilioWebhookEnabled = MessageEnumWebhookEnabledType.fromValue("true"); // MessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | A valid JSON string that contains application-specific data.
    String body = "body_example"; // String | The message to send to the channel. Can be an empty string or `null`, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat's history is being recreated from a backup/separate source.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
    String from = "from_example"; // String | The [Identity](https://www.twilio.com/docs/chat/identity) of the new message's author. The default value is `system`.
    String lastUpdatedBy = "lastUpdatedBy_example"; // String | The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable.
    String mediaSid = "mediaSid_example"; // String | The SID of the [Media](https://www.twilio.com/docs/chat/rest/media) to attach to the new Message.
    try {
      ChatV2ServiceChannelMessage result = apiInstance.createMessage(serviceSid, channelSid, xTwilioWebhookEnabled, attributes, body, dateCreated, dateUpdated, from, lastUpdatedBy, mediaSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2MessageApi#createMessage");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Message resource under. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Message resource belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **xTwilioWebhookEnabled** | **MessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] |
| **body** | **String**| The message to send to the channel. Can be an empty string or &#x60;null&#x60;, which sets the value as an empty string. You can send structured data in the body by serializing it as a string. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat&#39;s history is being recreated from a backup/separate source. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. | [optional] |
| **from** | **String**| The [Identity](https://www.twilio.com/docs/chat/identity) of the new message&#39;s author. The default value is &#x60;system&#x60;. | [optional] |
| **lastUpdatedBy** | **String**| The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable. | [optional] |
| **mediaSid** | **String**| The SID of the [Media](https://www.twilio.com/docs/chat/rest/media) to attach to the new Message. | [optional] |

### Return type

[**ChatV2ServiceChannelMessage**](ChatV2ServiceChannelMessage.md)

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
> deleteMessage(serviceSid, channelSid, sid, xTwilioWebhookEnabled)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2MessageApi apiInstance = new ChatV2MessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Message resource from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to delete belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Message resource to delete.
    MessageEnumWebhookEnabledType xTwilioWebhookEnabled = MessageEnumWebhookEnabledType.fromValue("true"); // MessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteMessage(serviceSid, channelSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2MessageApi#deleteMessage");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Message resource from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to delete belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Message resource to delete. | |
| **xTwilioWebhookEnabled** | **MessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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
> ChatV2ServiceChannelMessage fetchMessage(serviceSid, channelSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2MessageApi apiInstance = new ChatV2MessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Message resource from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to fetch belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Message resource to fetch.
    try {
      ChatV2ServiceChannelMessage result = apiInstance.fetchMessage(serviceSid, channelSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2MessageApi#fetchMessage");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Message resource from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to fetch belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Message resource to fetch. | |

### Return type

[**ChatV2ServiceChannelMessage**](ChatV2ServiceChannelMessage.md)

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
import org.openapitools.client.api.ChatV2MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2MessageApi apiInstance = new ChatV2MessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Message resources from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to read belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    MessageEnumOrderType order = MessageEnumOrderType.fromValue("asc"); // MessageEnumOrderType | The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending) with `asc` as the default.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMessageResponse result = apiInstance.listMessage(serviceSid, channelSid, order, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2MessageApi#listMessage");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Message resources from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to read belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **order** | **MessageEnumOrderType**| The sort order of the returned messages. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;asc&#x60; as the default. | [optional] [enum: asc, desc] |
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
> ChatV2ServiceChannelMessage updateMessage(serviceSid, channelSid, sid, xTwilioWebhookEnabled, attributes, body, dateCreated, dateUpdated, from, lastUpdatedBy)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2MessageApi apiInstance = new ChatV2MessageApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Message resource in.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to update belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Message resource to update.
    MessageEnumWebhookEnabledType xTwilioWebhookEnabled = MessageEnumWebhookEnabledType.fromValue("true"); // MessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | A valid JSON string that contains application-specific data.
    String body = "body_example"; // String | The message to send to the channel. Can be an empty string or `null`, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat's history is being recreated from a backup/separate source.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
    String from = "from_example"; // String | The [Identity](https://www.twilio.com/docs/chat/identity) of the message's author.
    String lastUpdatedBy = "lastUpdatedBy_example"; // String | The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable.
    try {
      ChatV2ServiceChannelMessage result = apiInstance.updateMessage(serviceSid, channelSid, sid, xTwilioWebhookEnabled, attributes, body, dateCreated, dateUpdated, from, lastUpdatedBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2MessageApi#updateMessage");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Message resource in. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to update belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Message resource to update. | |
| **xTwilioWebhookEnabled** | **MessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] |
| **body** | **String**| The message to send to the channel. Can be an empty string or &#x60;null&#x60;, which sets the value as an empty string. You can send structured data in the body by serializing it as a string. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat&#39;s history is being recreated from a backup/separate source. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. | [optional] |
| **from** | **String**| The [Identity](https://www.twilio.com/docs/chat/identity) of the message&#39;s author. | [optional] |
| **lastUpdatedBy** | **String**| The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable. | [optional] |

### Return type

[**ChatV2ServiceChannelMessage**](ChatV2ServiceChannelMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

