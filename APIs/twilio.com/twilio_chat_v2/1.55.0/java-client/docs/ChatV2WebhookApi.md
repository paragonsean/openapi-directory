# ChatV2WebhookApi

All URIs are relative to *https://chat.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createChannelWebhook**](ChatV2WebhookApi.md#createChannelWebhook) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks |  |
| [**deleteChannelWebhook**](ChatV2WebhookApi.md#deleteChannelWebhook) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} |  |
| [**fetchChannelWebhook**](ChatV2WebhookApi.md#fetchChannelWebhook) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} |  |
| [**listChannelWebhook**](ChatV2WebhookApi.md#listChannelWebhook) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks |  |
| [**updateChannelWebhook**](ChatV2WebhookApi.md#updateChannelWebhook) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} |  |


<a id="createChannelWebhook"></a>
# **createChannelWebhook**
> ChatV2ServiceChannelChannelWebhook createChannelWebhook(serviceSid, channelSid, type, configurationFilters, configurationFlowSid, configurationMethod, configurationRetryCount, configurationTriggers, configurationUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2WebhookApi apiInstance = new ChatV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to create the Webhook resource under.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Channel Webhook resource belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    ChannelWebhookEnumType type = ChannelWebhookEnumType.fromValue("webhook"); // ChannelWebhookEnumType | 
    List<String> configurationFilters = Arrays.asList(); // List<String> | The events that cause us to call the Channel Webhook. Used when `type` is `webhook`. This parameter takes only one event. To specify more than one event, repeat this parameter for each event. For the list of possible events, see [Webhook Event Triggers](https://www.twilio.com/docs/chat/webhook-events#webhook-event-trigger).
    String configurationFlowSid = "configurationFlowSid_example"; // String | The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-api/flow) to call when an event in `configuration.filters` occurs. Used only when `type` is `studio`.
    ChannelWebhookEnumMethod configurationMethod = ChannelWebhookEnumMethod.fromValue("GET"); // ChannelWebhookEnumMethod | 
    Integer configurationRetryCount = 56; // Integer | The number of times to retry the webhook if the first attempt fails. Can be an integer between 0 and 3, inclusive, and the default is 0.
    List<String> configurationTriggers = Arrays.asList(); // List<String> | A string that will cause us to call the webhook when it is present in a message body. This parameter takes only one trigger string. To specify more than one, repeat this parameter for each trigger string up to a total of 5 trigger strings. Used only when `type` = `trigger`.
    String configurationUrl = "configurationUrl_example"; // String | The URL of the webhook to call using the `configuration.method`.
    try {
      ChatV2ServiceChannelChannelWebhook result = apiInstance.createChannelWebhook(serviceSid, channelSid, type, configurationFilters, configurationFlowSid, configurationMethod, configurationRetryCount, configurationTriggers, configurationUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2WebhookApi#createChannelWebhook");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to create the Webhook resource under. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Channel Webhook resource belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **type** | **ChannelWebhookEnumType**|  | [enum: webhook, trigger, studio] |
| **configurationFilters** | [**List&lt;String&gt;**](String.md)| The events that cause us to call the Channel Webhook. Used when &#x60;type&#x60; is &#x60;webhook&#x60;. This parameter takes only one event. To specify more than one event, repeat this parameter for each event. For the list of possible events, see [Webhook Event Triggers](https://www.twilio.com/docs/chat/webhook-events#webhook-event-trigger). | [optional] |
| **configurationFlowSid** | **String**| The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-api/flow) to call when an event in &#x60;configuration.filters&#x60; occurs. Used only when &#x60;type&#x60; is &#x60;studio&#x60;. | [optional] |
| **configurationMethod** | **ChannelWebhookEnumMethod**|  | [optional] [enum: GET, POST] |
| **configurationRetryCount** | **Integer**| The number of times to retry the webhook if the first attempt fails. Can be an integer between 0 and 3, inclusive, and the default is 0. | [optional] |
| **configurationTriggers** | [**List&lt;String&gt;**](String.md)| A string that will cause us to call the webhook when it is present in a message body. This parameter takes only one trigger string. To specify more than one, repeat this parameter for each trigger string up to a total of 5 trigger strings. Used only when &#x60;type&#x60; &#x3D; &#x60;trigger&#x60;. | [optional] |
| **configurationUrl** | **String**| The URL of the webhook to call using the &#x60;configuration.method&#x60;. | [optional] |

### Return type

[**ChatV2ServiceChannelChannelWebhook**](ChatV2ServiceChannelChannelWebhook.md)

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
import org.openapitools.client.api.ChatV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2WebhookApi apiInstance = new ChatV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to delete the Webhook resource from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to delete belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Channel Webhook resource to delete.
    try {
      apiInstance.deleteChannelWebhook(serviceSid, channelSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2WebhookApi#deleteChannelWebhook");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to delete the Webhook resource from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to delete belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Channel Webhook resource to delete. | |

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
> ChatV2ServiceChannelChannelWebhook fetchChannelWebhook(serviceSid, channelSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2WebhookApi apiInstance = new ChatV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to fetch the Webhook resource from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to fetch belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Channel Webhook resource to fetch.
    try {
      ChatV2ServiceChannelChannelWebhook result = apiInstance.fetchChannelWebhook(serviceSid, channelSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2WebhookApi#fetchChannelWebhook");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to fetch the Webhook resource from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to fetch belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Channel Webhook resource to fetch. | |

### Return type

[**ChatV2ServiceChannelChannelWebhook**](ChatV2ServiceChannelChannelWebhook.md)

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
import org.openapitools.client.api.ChatV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2WebhookApi apiInstance = new ChatV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to read the resources from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resources to read belong to. This value can be the Channel resource's `sid` or `unique_name`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListChannelWebhookResponse result = apiInstance.listChannelWebhook(serviceSid, channelSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2WebhookApi#listChannelWebhook");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to read the resources from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resources to read belong to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
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
> ChatV2ServiceChannelChannelWebhook updateChannelWebhook(serviceSid, channelSid, sid, configurationFilters, configurationFlowSid, configurationMethod, configurationRetryCount, configurationTriggers, configurationUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2WebhookApi apiInstance = new ChatV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel that has the Webhook resource to update.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to update belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Channel Webhook resource to update.
    List<String> configurationFilters = Arrays.asList(); // List<String> | The events that cause us to call the Channel Webhook. Used when `type` is `webhook`. This parameter takes only one event. To specify more than one event, repeat this parameter for each event. For the list of possible events, see [Webhook Event Triggers](https://www.twilio.com/docs/chat/webhook-events#webhook-event-trigger).
    String configurationFlowSid = "configurationFlowSid_example"; // String | The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-api/flow) to call when an event in `configuration.filters` occurs. Used only when `type` = `studio`.
    ChannelWebhookEnumMethod configurationMethod = ChannelWebhookEnumMethod.fromValue("GET"); // ChannelWebhookEnumMethod | 
    Integer configurationRetryCount = 56; // Integer | The number of times to retry the webhook if the first attempt fails. Can be an integer between 0 and 3, inclusive, and the default is 0.
    List<String> configurationTriggers = Arrays.asList(); // List<String> | A string that will cause us to call the webhook when it is present in a message body. This parameter takes only one trigger string. To specify more than one, repeat this parameter for each trigger string up to a total of 5 trigger strings. Used only when `type` = `trigger`.
    String configurationUrl = "configurationUrl_example"; // String | The URL of the webhook to call using the `configuration.method`.
    try {
      ChatV2ServiceChannelChannelWebhook result = apiInstance.updateChannelWebhook(serviceSid, channelSid, sid, configurationFilters, configurationFlowSid, configurationMethod, configurationRetryCount, configurationTriggers, configurationUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2WebhookApi#updateChannelWebhook");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel that has the Webhook resource to update. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to update belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Channel Webhook resource to update. | |
| **configurationFilters** | [**List&lt;String&gt;**](String.md)| The events that cause us to call the Channel Webhook. Used when &#x60;type&#x60; is &#x60;webhook&#x60;. This parameter takes only one event. To specify more than one event, repeat this parameter for each event. For the list of possible events, see [Webhook Event Triggers](https://www.twilio.com/docs/chat/webhook-events#webhook-event-trigger). | [optional] |
| **configurationFlowSid** | **String**| The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-api/flow) to call when an event in &#x60;configuration.filters&#x60; occurs. Used only when &#x60;type&#x60; &#x3D; &#x60;studio&#x60;. | [optional] |
| **configurationMethod** | **ChannelWebhookEnumMethod**|  | [optional] [enum: GET, POST] |
| **configurationRetryCount** | **Integer**| The number of times to retry the webhook if the first attempt fails. Can be an integer between 0 and 3, inclusive, and the default is 0. | [optional] |
| **configurationTriggers** | [**List&lt;String&gt;**](String.md)| A string that will cause us to call the webhook when it is present in a message body. This parameter takes only one trigger string. To specify more than one, repeat this parameter for each trigger string up to a total of 5 trigger strings. Used only when &#x60;type&#x60; &#x3D; &#x60;trigger&#x60;. | [optional] |
| **configurationUrl** | **String**| The URL of the webhook to call using the &#x60;configuration.method&#x60;. | [optional] |

### Return type

[**ChatV2ServiceChannelChannelWebhook**](ChatV2ServiceChannelChannelWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

