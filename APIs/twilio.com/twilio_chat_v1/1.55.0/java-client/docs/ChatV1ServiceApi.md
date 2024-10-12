# ChatV1ServiceApi

All URIs are relative to *https://chat.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createService**](ChatV1ServiceApi.md#createService) | **POST** /v1/Services |  |
| [**deleteService**](ChatV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} |  |
| [**fetchService**](ChatV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} |  |
| [**listService**](ChatV1ServiceApi.md#listService) | **GET** /v1/Services |  |
| [**updateService**](ChatV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} |  |


<a id="createService"></a>
# **createService**
> ChatV1Service createService(friendlyName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV1ServiceApi apiInstance = new ChatV1ServiceApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    try {
      ChatV1Service result = apiInstance.createService(friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV1ServiceApi#createService");
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
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | |

### Return type

[**ChatV1Service**](ChatV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteService"></a>
# **deleteService**
> deleteService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV1ServiceApi apiInstance = new ChatV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to delete.
    try {
      apiInstance.deleteService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV1ServiceApi#deleteService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to delete. | |

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

<a id="fetchService"></a>
# **fetchService**
> ChatV1Service fetchService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV1ServiceApi apiInstance = new ChatV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to fetch.
    try {
      ChatV1Service result = apiInstance.fetchService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV1ServiceApi#fetchService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to fetch. | |

### Return type

[**ChatV1Service**](ChatV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listService"></a>
# **listService**
> ListServiceResponse listService(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV1ServiceApi apiInstance = new ChatV1ServiceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceResponse result = apiInstance.listService(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV1ServiceApi#listService");
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

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateService"></a>
# **updateService**
> ChatV1Service updateService(sid, consumptionReportInterval, defaultChannelCreatorRoleSid, defaultChannelRoleSid, defaultServiceRoleSid, friendlyName, limitsChannelMembers, limitsUserChannels, notificationsAddedToChannelEnabled, notificationsAddedToChannelTemplate, notificationsInvitedToChannelEnabled, notificationsInvitedToChannelTemplate, notificationsNewMessageEnabled, notificationsNewMessageTemplate, notificationsRemovedFromChannelEnabled, notificationsRemovedFromChannelTemplate, postWebhookUrl, preWebhookUrl, reachabilityEnabled, readStatusEnabled, typingIndicatorTimeout, webhookFilters, webhookMethod, webhooksOnChannelAddMethod, webhooksOnChannelAddUrl, webhooksOnChannelAddedMethod, webhooksOnChannelAddedUrl, webhooksOnChannelDestroyMethod, webhooksOnChannelDestroyUrl, webhooksOnChannelDestroyedMethod, webhooksOnChannelDestroyedUrl, webhooksOnChannelUpdateMethod, webhooksOnChannelUpdateUrl, webhooksOnChannelUpdatedMethod, webhooksOnChannelUpdatedUrl, webhooksOnMemberAddMethod, webhooksOnMemberAddUrl, webhooksOnMemberAddedMethod, webhooksOnMemberAddedUrl, webhooksOnMemberRemoveMethod, webhooksOnMemberRemoveUrl, webhooksOnMemberRemovedMethod, webhooksOnMemberRemovedUrl, webhooksOnMessageRemoveMethod, webhooksOnMessageRemoveUrl, webhooksOnMessageRemovedMethod, webhooksOnMessageRemovedUrl, webhooksOnMessageSendMethod, webhooksOnMessageSendUrl, webhooksOnMessageSentMethod, webhooksOnMessageSentUrl, webhooksOnMessageUpdateMethod, webhooksOnMessageUpdateUrl, webhooksOnMessageUpdatedMethod, webhooksOnMessageUpdatedUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV1ServiceApi apiInstance = new ChatV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to update.
    Integer consumptionReportInterval = 56; // Integer | DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints.
    String defaultChannelCreatorRoleSid = "defaultChannelCreatorRoleSid_example"; // String | The channel role assigned to a channel creator when they join a new channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details.
    String defaultChannelRoleSid = "defaultChannelRoleSid_example"; // String | The channel role assigned to users when they are added to a channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details.
    String defaultServiceRoleSid = "defaultServiceRoleSid_example"; // String | The service role assigned to users when they are added to the service. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    Integer limitsChannelMembers = 56; // Integer | The maximum number of Members that can be added to Channels within this Service. Can be up to 1,000.
    Integer limitsUserChannels = 56; // Integer | The maximum number of Channels Users can be a Member of within this Service. Can be up to 1,000.
    Boolean notificationsAddedToChannelEnabled = true; // Boolean | Whether to send a notification when a member is added to a channel. Can be: `true` or `false` and the default is `false`.
    String notificationsAddedToChannelTemplate = "notificationsAddedToChannelTemplate_example"; // String | The template to use to create the notification text displayed when a member is added to a channel and `notifications.added_to_channel.enabled` is `true`.
    Boolean notificationsInvitedToChannelEnabled = true; // Boolean | Whether to send a notification when a user is invited to a channel. Can be: `true` or `false` and the default is `false`.
    String notificationsInvitedToChannelTemplate = "notificationsInvitedToChannelTemplate_example"; // String | The template to use to create the notification text displayed when a user is invited to a channel and `notifications.invited_to_channel.enabled` is `true`.
    Boolean notificationsNewMessageEnabled = true; // Boolean | Whether to send a notification when a new message is added to a channel. Can be: `true` or `false` and the default is `false`.
    String notificationsNewMessageTemplate = "notificationsNewMessageTemplate_example"; // String | The template to use to create the notification text displayed when a new message is added to a channel and `notifications.new_message.enabled` is `true`.
    Boolean notificationsRemovedFromChannelEnabled = true; // Boolean | Whether to send a notification to a user when they are removed from a channel. Can be: `true` or `false` and the default is `false`.
    String notificationsRemovedFromChannelTemplate = "notificationsRemovedFromChannelTemplate_example"; // String | The template to use to create the notification text displayed to a user when they are removed from a channel and `notifications.removed_from_channel.enabled` is `true`.
    URI postWebhookUrl = new URI(); // URI | The URL for post-event webhooks, which are called by using the `webhook_method`. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details.
    URI preWebhookUrl = new URI(); // URI | The URL for pre-event webhooks, which are called by using the `webhook_method`. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details.
    Boolean reachabilityEnabled = true; // Boolean | Whether to enable the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) for this Service instance. The default is `false`.
    Boolean readStatusEnabled = true; // Boolean | Whether to enable the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature. The default is `true`.
    Integer typingIndicatorTimeout = 56; // Integer | How long in seconds after a `started typing` event until clients should assume that user is no longer typing, even if no `ended typing` message was received.  The default is 5 seconds.
    List<String> webhookFilters = Arrays.asList(); // List<String> | The list of WebHook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    String webhookMethod = "HEAD"; // String | The HTTP method to use for calls to the `pre_webhook_url` and `post_webhook_url` webhooks.  Can be: `POST` or `GET` and the default is `POST`. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    String webhooksOnChannelAddMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_channel_add.url`.
    URI webhooksOnChannelAddUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_channel_add` event using the `webhooks.on_channel_add.method` HTTP method.
    String webhooksOnChannelAddedMethod = "HEAD"; // String | The URL of the webhook to call in response to the `on_channel_added` event`.
    URI webhooksOnChannelAddedUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_channel_added` event using the `webhooks.on_channel_added.method` HTTP method.
    String webhooksOnChannelDestroyMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_channel_destroy.url`.
    URI webhooksOnChannelDestroyUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_channel_destroy` event using the `webhooks.on_channel_destroy.method` HTTP method.
    String webhooksOnChannelDestroyedMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_channel_destroyed.url`.
    URI webhooksOnChannelDestroyedUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_channel_added` event using the `webhooks.on_channel_destroyed.method` HTTP method.
    String webhooksOnChannelUpdateMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_channel_update.url`.
    URI webhooksOnChannelUpdateUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_channel_update` event using the `webhooks.on_channel_update.method` HTTP method.
    String webhooksOnChannelUpdatedMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_channel_updated.url`.
    URI webhooksOnChannelUpdatedUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_channel_updated` event using the `webhooks.on_channel_updated.method` HTTP method.
    String webhooksOnMemberAddMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_member_add.url`.
    URI webhooksOnMemberAddUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_member_add` event using the `webhooks.on_member_add.method` HTTP method.
    String webhooksOnMemberAddedMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_channel_updated.url`.
    URI webhooksOnMemberAddedUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_channel_updated` event using the `webhooks.on_channel_updated.method` HTTP method.
    String webhooksOnMemberRemoveMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_member_remove.url`.
    URI webhooksOnMemberRemoveUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_member_remove` event using the `webhooks.on_member_remove.method` HTTP method.
    String webhooksOnMemberRemovedMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_member_removed.url`.
    URI webhooksOnMemberRemovedUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_member_removed` event using the `webhooks.on_member_removed.method` HTTP method.
    String webhooksOnMessageRemoveMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_message_remove.url`.
    URI webhooksOnMessageRemoveUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_message_remove` event using the `webhooks.on_message_remove.method` HTTP method.
    String webhooksOnMessageRemovedMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_message_removed.url`.
    URI webhooksOnMessageRemovedUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_message_removed` event using the `webhooks.on_message_removed.method` HTTP method.
    String webhooksOnMessageSendMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_message_send.url`.
    URI webhooksOnMessageSendUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_message_send` event using the `webhooks.on_message_send.method` HTTP method.
    String webhooksOnMessageSentMethod = "HEAD"; // String | The URL of the webhook to call in response to the `on_message_sent` event`.
    URI webhooksOnMessageSentUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_message_sent` event using the `webhooks.on_message_sent.method` HTTP method.
    String webhooksOnMessageUpdateMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_message_update.url`.
    URI webhooksOnMessageUpdateUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_message_update` event using the `webhooks.on_message_update.method` HTTP method.
    String webhooksOnMessageUpdatedMethod = "HEAD"; // String | The HTTP method to use when calling the `webhooks.on_message_updated.url`.
    URI webhooksOnMessageUpdatedUrl = new URI(); // URI | The URL of the webhook to call in response to the `on_message_updated` event using the `webhooks.on_message_updated.method` HTTP method.
    try {
      ChatV1Service result = apiInstance.updateService(sid, consumptionReportInterval, defaultChannelCreatorRoleSid, defaultChannelRoleSid, defaultServiceRoleSid, friendlyName, limitsChannelMembers, limitsUserChannels, notificationsAddedToChannelEnabled, notificationsAddedToChannelTemplate, notificationsInvitedToChannelEnabled, notificationsInvitedToChannelTemplate, notificationsNewMessageEnabled, notificationsNewMessageTemplate, notificationsRemovedFromChannelEnabled, notificationsRemovedFromChannelTemplate, postWebhookUrl, preWebhookUrl, reachabilityEnabled, readStatusEnabled, typingIndicatorTimeout, webhookFilters, webhookMethod, webhooksOnChannelAddMethod, webhooksOnChannelAddUrl, webhooksOnChannelAddedMethod, webhooksOnChannelAddedUrl, webhooksOnChannelDestroyMethod, webhooksOnChannelDestroyUrl, webhooksOnChannelDestroyedMethod, webhooksOnChannelDestroyedUrl, webhooksOnChannelUpdateMethod, webhooksOnChannelUpdateUrl, webhooksOnChannelUpdatedMethod, webhooksOnChannelUpdatedUrl, webhooksOnMemberAddMethod, webhooksOnMemberAddUrl, webhooksOnMemberAddedMethod, webhooksOnMemberAddedUrl, webhooksOnMemberRemoveMethod, webhooksOnMemberRemoveUrl, webhooksOnMemberRemovedMethod, webhooksOnMemberRemovedUrl, webhooksOnMessageRemoveMethod, webhooksOnMessageRemoveUrl, webhooksOnMessageRemovedMethod, webhooksOnMessageRemovedUrl, webhooksOnMessageSendMethod, webhooksOnMessageSendUrl, webhooksOnMessageSentMethod, webhooksOnMessageSentUrl, webhooksOnMessageUpdateMethod, webhooksOnMessageUpdateUrl, webhooksOnMessageUpdatedMethod, webhooksOnMessageUpdatedUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV1ServiceApi#updateService");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to update. | |
| **consumptionReportInterval** | **Integer**| DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints. | [optional] |
| **defaultChannelCreatorRoleSid** | **String**| The channel role assigned to a channel creator when they join a new channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details. | [optional] |
| **defaultChannelRoleSid** | **String**| The channel role assigned to users when they are added to a channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details. | [optional] |
| **defaultServiceRoleSid** | **String**| The service role assigned to users when they are added to the service. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] |
| **limitsChannelMembers** | **Integer**| The maximum number of Members that can be added to Channels within this Service. Can be up to 1,000. | [optional] |
| **limitsUserChannels** | **Integer**| The maximum number of Channels Users can be a Member of within this Service. Can be up to 1,000. | [optional] |
| **notificationsAddedToChannelEnabled** | **Boolean**| Whether to send a notification when a member is added to a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] |
| **notificationsAddedToChannelTemplate** | **String**| The template to use to create the notification text displayed when a member is added to a channel and &#x60;notifications.added_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **notificationsInvitedToChannelEnabled** | **Boolean**| Whether to send a notification when a user is invited to a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] |
| **notificationsInvitedToChannelTemplate** | **String**| The template to use to create the notification text displayed when a user is invited to a channel and &#x60;notifications.invited_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **notificationsNewMessageEnabled** | **Boolean**| Whether to send a notification when a new message is added to a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] |
| **notificationsNewMessageTemplate** | **String**| The template to use to create the notification text displayed when a new message is added to a channel and &#x60;notifications.new_message.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **notificationsRemovedFromChannelEnabled** | **Boolean**| Whether to send a notification to a user when they are removed from a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] |
| **notificationsRemovedFromChannelTemplate** | **String**| The template to use to create the notification text displayed to a user when they are removed from a channel and &#x60;notifications.removed_from_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **postWebhookUrl** | **URI**| The URL for post-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details. | [optional] |
| **preWebhookUrl** | **URI**| The URL for pre-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details. | [optional] |
| **reachabilityEnabled** | **Boolean**| Whether to enable the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) for this Service instance. The default is &#x60;false&#x60;. | [optional] |
| **readStatusEnabled** | **Boolean**| Whether to enable the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature. The default is &#x60;true&#x60;. | [optional] |
| **typingIndicatorTimeout** | **Integer**| How long in seconds after a &#x60;started typing&#x60; event until clients should assume that user is no longer typing, even if no &#x60;ended typing&#x60; message was received.  The default is 5 seconds. | [optional] |
| **webhookFilters** | [**List&lt;String&gt;**](String.md)| The list of WebHook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] |
| **webhookMethod** | **String**| The HTTP method to use for calls to the &#x60;pre_webhook_url&#x60; and &#x60;post_webhook_url&#x60; webhooks.  Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelAddMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_add.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelAddUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_channel_add&#x60; event using the &#x60;webhooks.on_channel_add.method&#x60; HTTP method. | [optional] |
| **webhooksOnChannelAddedMethod** | **String**| The URL of the webhook to call in response to the &#x60;on_channel_added&#x60; event&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelAddedUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_channel_added&#x60; event using the &#x60;webhooks.on_channel_added.method&#x60; HTTP method. | [optional] |
| **webhooksOnChannelDestroyMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_destroy.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelDestroyUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_channel_destroy&#x60; event using the &#x60;webhooks.on_channel_destroy.method&#x60; HTTP method. | [optional] |
| **webhooksOnChannelDestroyedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_destroyed.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelDestroyedUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_channel_added&#x60; event using the &#x60;webhooks.on_channel_destroyed.method&#x60; HTTP method. | [optional] |
| **webhooksOnChannelUpdateMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_update.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelUpdateUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_channel_update&#x60; event using the &#x60;webhooks.on_channel_update.method&#x60; HTTP method. | [optional] |
| **webhooksOnChannelUpdatedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_updated.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelUpdatedUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_channel_updated&#x60; event using the &#x60;webhooks.on_channel_updated.method&#x60; HTTP method. | [optional] |
| **webhooksOnMemberAddMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_member_add.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMemberAddUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_member_add&#x60; event using the &#x60;webhooks.on_member_add.method&#x60; HTTP method. | [optional] |
| **webhooksOnMemberAddedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_updated.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMemberAddedUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_channel_updated&#x60; event using the &#x60;webhooks.on_channel_updated.method&#x60; HTTP method. | [optional] |
| **webhooksOnMemberRemoveMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_member_remove.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMemberRemoveUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_member_remove&#x60; event using the &#x60;webhooks.on_member_remove.method&#x60; HTTP method. | [optional] |
| **webhooksOnMemberRemovedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_member_removed.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMemberRemovedUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_member_removed&#x60; event using the &#x60;webhooks.on_member_removed.method&#x60; HTTP method. | [optional] |
| **webhooksOnMessageRemoveMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_message_remove.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageRemoveUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_message_remove&#x60; event using the &#x60;webhooks.on_message_remove.method&#x60; HTTP method. | [optional] |
| **webhooksOnMessageRemovedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_message_removed.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageRemovedUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_message_removed&#x60; event using the &#x60;webhooks.on_message_removed.method&#x60; HTTP method. | [optional] |
| **webhooksOnMessageSendMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_message_send.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageSendUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_message_send&#x60; event using the &#x60;webhooks.on_message_send.method&#x60; HTTP method. | [optional] |
| **webhooksOnMessageSentMethod** | **String**| The URL of the webhook to call in response to the &#x60;on_message_sent&#x60; event&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageSentUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_message_sent&#x60; event using the &#x60;webhooks.on_message_sent.method&#x60; HTTP method. | [optional] |
| **webhooksOnMessageUpdateMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_message_update.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageUpdateUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_message_update&#x60; event using the &#x60;webhooks.on_message_update.method&#x60; HTTP method. | [optional] |
| **webhooksOnMessageUpdatedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_message_updated.url&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageUpdatedUrl** | **URI**| The URL of the webhook to call in response to the &#x60;on_message_updated&#x60; event using the &#x60;webhooks.on_message_updated.method&#x60; HTTP method. | [optional] |

### Return type

[**ChatV1Service**](ChatV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

