# ChatV2ServiceApi

All URIs are relative to *https://chat.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createService**](ChatV2ServiceApi.md#createService) | **POST** /v2/Services |  |
| [**deleteService**](ChatV2ServiceApi.md#deleteService) | **DELETE** /v2/Services/{Sid} |  |
| [**fetchService**](ChatV2ServiceApi.md#fetchService) | **GET** /v2/Services/{Sid} |  |
| [**listService**](ChatV2ServiceApi.md#listService) | **GET** /v2/Services |  |
| [**updateService**](ChatV2ServiceApi.md#updateService) | **POST** /v2/Services/{Sid} |  |


<a id="createService"></a>
# **createService**
> ChatV2Service createService(friendlyName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2ServiceApi apiInstance = new ChatV2ServiceApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new resource.
    try {
      ChatV2Service result = apiInstance.createService(friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2ServiceApi#createService");
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
| **friendlyName** | **String**| A descriptive string that you create to describe the new resource. | |

### Return type

[**ChatV2Service**](ChatV2Service.md)

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
import org.openapitools.client.api.ChatV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2ServiceApi apiInstance = new ChatV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Service resource to delete.
    try {
      apiInstance.deleteService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2ServiceApi#deleteService");
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
| **sid** | **String**| The SID of the Service resource to delete. | |

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
> ChatV2Service fetchService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2ServiceApi apiInstance = new ChatV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Service resource to fetch.
    try {
      ChatV2Service result = apiInstance.fetchService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2ServiceApi#fetchService");
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
| **sid** | **String**| The SID of the Service resource to fetch. | |

### Return type

[**ChatV2Service**](ChatV2Service.md)

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
import org.openapitools.client.api.ChatV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2ServiceApi apiInstance = new ChatV2ServiceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceResponse result = apiInstance.listService(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2ServiceApi#listService");
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
> ChatV2Service updateService(sid, consumptionReportInterval, defaultChannelCreatorRoleSid, defaultChannelRoleSid, defaultServiceRoleSid, friendlyName, limitsChannelMembers, limitsUserChannels, mediaCompatibilityMessage, notificationsAddedToChannelEnabled, notificationsAddedToChannelSound, notificationsAddedToChannelTemplate, notificationsInvitedToChannelEnabled, notificationsInvitedToChannelSound, notificationsInvitedToChannelTemplate, notificationsLogEnabled, notificationsNewMessageBadgeCountEnabled, notificationsNewMessageEnabled, notificationsNewMessageSound, notificationsNewMessageTemplate, notificationsRemovedFromChannelEnabled, notificationsRemovedFromChannelSound, notificationsRemovedFromChannelTemplate, postWebhookRetryCount, postWebhookUrl, preWebhookRetryCount, preWebhookUrl, reachabilityEnabled, readStatusEnabled, typingIndicatorTimeout, webhookFilters, webhookMethod)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2ServiceApi apiInstance = new ChatV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Service resource to update.
    Integer consumptionReportInterval = 56; // Integer | DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints.
    String defaultChannelCreatorRoleSid = "defaultChannelCreatorRoleSid_example"; // String | The channel role assigned to a channel creator when they join a new channel. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles.
    String defaultChannelRoleSid = "defaultChannelRoleSid_example"; // String | The channel role assigned to users when they are added to a channel. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles.
    String defaultServiceRoleSid = "defaultServiceRoleSid_example"; // String | The service role assigned to users when they are added to the service. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource.
    Integer limitsChannelMembers = 56; // Integer | The maximum number of Members that can be added to Channels within this Service. Can be up to 1,000.
    Integer limitsUserChannels = 56; // Integer | The maximum number of Channels Users can be a Member of within this Service. Can be up to 1,000.
    String mediaCompatibilityMessage = "mediaCompatibilityMessage_example"; // String | The message to send when a media message has no text. Can be used as placeholder message.
    Boolean notificationsAddedToChannelEnabled = true; // Boolean | Whether to send a notification when a member is added to a channel. The default is `false`.
    String notificationsAddedToChannelSound = "notificationsAddedToChannelSound_example"; // String | The name of the sound to play when a member is added to a channel and `notifications.added_to_channel.enabled` is `true`.
    String notificationsAddedToChannelTemplate = "notificationsAddedToChannelTemplate_example"; // String | The template to use to create the notification text displayed when a member is added to a channel and `notifications.added_to_channel.enabled` is `true`.
    Boolean notificationsInvitedToChannelEnabled = true; // Boolean | Whether to send a notification when a user is invited to a channel. The default is `false`.
    String notificationsInvitedToChannelSound = "notificationsInvitedToChannelSound_example"; // String | The name of the sound to play when a user is invited to a channel and `notifications.invited_to_channel.enabled` is `true`.
    String notificationsInvitedToChannelTemplate = "notificationsInvitedToChannelTemplate_example"; // String | The template to use to create the notification text displayed when a user is invited to a channel and `notifications.invited_to_channel.enabled` is `true`.
    Boolean notificationsLogEnabled = true; // Boolean | Whether to log notifications. The default is `false`.
    Boolean notificationsNewMessageBadgeCountEnabled = true; // Boolean | Whether the new message badge is enabled. The default is `false`.
    Boolean notificationsNewMessageEnabled = true; // Boolean | Whether to send a notification when a new message is added to a channel. The default is `false`.
    String notificationsNewMessageSound = "notificationsNewMessageSound_example"; // String | The name of the sound to play when a new message is added to a channel and `notifications.new_message.enabled` is `true`.
    String notificationsNewMessageTemplate = "notificationsNewMessageTemplate_example"; // String | The template to use to create the notification text displayed when a new message is added to a channel and `notifications.new_message.enabled` is `true`.
    Boolean notificationsRemovedFromChannelEnabled = true; // Boolean | Whether to send a notification to a user when they are removed from a channel. The default is `false`.
    String notificationsRemovedFromChannelSound = "notificationsRemovedFromChannelSound_example"; // String | The name of the sound to play to a user when they are removed from a channel and `notifications.removed_from_channel.enabled` is `true`.
    String notificationsRemovedFromChannelTemplate = "notificationsRemovedFromChannelTemplate_example"; // String | The template to use to create the notification text displayed to a user when they are removed from a channel and `notifications.removed_from_channel.enabled` is `true`.
    Integer postWebhookRetryCount = 56; // Integer | The number of times to retry a call to the `post_webhook_url` if the request times out (after 5 seconds) or it receives a 429, 503, or 504 HTTP response. The default is 0, which means the call won't be retried.
    URI postWebhookUrl = new URI(); // URI | The URL for post-event webhooks, which are called by using the `webhook_method`. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    Integer preWebhookRetryCount = 56; // Integer | The number of times to retry a call to the `pre_webhook_url` if the request times out (after 5 seconds) or it receives a 429, 503, or 504 HTTP response. Default retry count is 0 times, which means the call won't be retried.
    URI preWebhookUrl = new URI(); // URI | The URL for pre-event webhooks, which are called by using the `webhook_method`. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    Boolean reachabilityEnabled = true; // Boolean | Whether to enable the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) for this Service instance. The default is `false`.
    Boolean readStatusEnabled = true; // Boolean | Whether to enable the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature. The default is `true`.
    Integer typingIndicatorTimeout = 56; // Integer | How long in seconds after a `started typing` event until clients should assume that user is no longer typing, even if no `ended typing` message was received.  The default is 5 seconds.
    List<String> webhookFilters = Arrays.asList(); // List<String> | The list of webhook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    String webhookMethod = "HEAD"; // String | The HTTP method to use for calls to the `pre_webhook_url` and `post_webhook_url` webhooks.  Can be: `POST` or `GET` and the default is `POST`. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
    try {
      ChatV2Service result = apiInstance.updateService(sid, consumptionReportInterval, defaultChannelCreatorRoleSid, defaultChannelRoleSid, defaultServiceRoleSid, friendlyName, limitsChannelMembers, limitsUserChannels, mediaCompatibilityMessage, notificationsAddedToChannelEnabled, notificationsAddedToChannelSound, notificationsAddedToChannelTemplate, notificationsInvitedToChannelEnabled, notificationsInvitedToChannelSound, notificationsInvitedToChannelTemplate, notificationsLogEnabled, notificationsNewMessageBadgeCountEnabled, notificationsNewMessageEnabled, notificationsNewMessageSound, notificationsNewMessageTemplate, notificationsRemovedFromChannelEnabled, notificationsRemovedFromChannelSound, notificationsRemovedFromChannelTemplate, postWebhookRetryCount, postWebhookUrl, preWebhookRetryCount, preWebhookUrl, reachabilityEnabled, readStatusEnabled, typingIndicatorTimeout, webhookFilters, webhookMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2ServiceApi#updateService");
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
| **sid** | **String**| The SID of the Service resource to update. | |
| **consumptionReportInterval** | **Integer**| DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints. | [optional] |
| **defaultChannelCreatorRoleSid** | **String**| The channel role assigned to a channel creator when they join a new channel. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles. | [optional] |
| **defaultChannelRoleSid** | **String**| The channel role assigned to users when they are added to a channel. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles. | [optional] |
| **defaultServiceRoleSid** | **String**| The service role assigned to users when they are added to the service. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. | [optional] |
| **limitsChannelMembers** | **Integer**| The maximum number of Members that can be added to Channels within this Service. Can be up to 1,000. | [optional] |
| **limitsUserChannels** | **Integer**| The maximum number of Channels Users can be a Member of within this Service. Can be up to 1,000. | [optional] |
| **mediaCompatibilityMessage** | **String**| The message to send when a media message has no text. Can be used as placeholder message. | [optional] |
| **notificationsAddedToChannelEnabled** | **Boolean**| Whether to send a notification when a member is added to a channel. The default is &#x60;false&#x60;. | [optional] |
| **notificationsAddedToChannelSound** | **String**| The name of the sound to play when a member is added to a channel and &#x60;notifications.added_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **notificationsAddedToChannelTemplate** | **String**| The template to use to create the notification text displayed when a member is added to a channel and &#x60;notifications.added_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **notificationsInvitedToChannelEnabled** | **Boolean**| Whether to send a notification when a user is invited to a channel. The default is &#x60;false&#x60;. | [optional] |
| **notificationsInvitedToChannelSound** | **String**| The name of the sound to play when a user is invited to a channel and &#x60;notifications.invited_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **notificationsInvitedToChannelTemplate** | **String**| The template to use to create the notification text displayed when a user is invited to a channel and &#x60;notifications.invited_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **notificationsLogEnabled** | **Boolean**| Whether to log notifications. The default is &#x60;false&#x60;. | [optional] |
| **notificationsNewMessageBadgeCountEnabled** | **Boolean**| Whether the new message badge is enabled. The default is &#x60;false&#x60;. | [optional] |
| **notificationsNewMessageEnabled** | **Boolean**| Whether to send a notification when a new message is added to a channel. The default is &#x60;false&#x60;. | [optional] |
| **notificationsNewMessageSound** | **String**| The name of the sound to play when a new message is added to a channel and &#x60;notifications.new_message.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **notificationsNewMessageTemplate** | **String**| The template to use to create the notification text displayed when a new message is added to a channel and &#x60;notifications.new_message.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **notificationsRemovedFromChannelEnabled** | **Boolean**| Whether to send a notification to a user when they are removed from a channel. The default is &#x60;false&#x60;. | [optional] |
| **notificationsRemovedFromChannelSound** | **String**| The name of the sound to play to a user when they are removed from a channel and &#x60;notifications.removed_from_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **notificationsRemovedFromChannelTemplate** | **String**| The template to use to create the notification text displayed to a user when they are removed from a channel and &#x60;notifications.removed_from_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **postWebhookRetryCount** | **Integer**| The number of times to retry a call to the &#x60;post_webhook_url&#x60; if the request times out (after 5 seconds) or it receives a 429, 503, or 504 HTTP response. The default is 0, which means the call won&#39;t be retried. | [optional] |
| **postWebhookUrl** | **URI**| The URL for post-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] |
| **preWebhookRetryCount** | **Integer**| The number of times to retry a call to the &#x60;pre_webhook_url&#x60; if the request times out (after 5 seconds) or it receives a 429, 503, or 504 HTTP response. Default retry count is 0 times, which means the call won&#39;t be retried. | [optional] |
| **preWebhookUrl** | **URI**| The URL for pre-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] |
| **reachabilityEnabled** | **Boolean**| Whether to enable the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) for this Service instance. The default is &#x60;false&#x60;. | [optional] |
| **readStatusEnabled** | **Boolean**| Whether to enable the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature. The default is &#x60;true&#x60;. | [optional] |
| **typingIndicatorTimeout** | **Integer**| How long in seconds after a &#x60;started typing&#x60; event until clients should assume that user is no longer typing, even if no &#x60;ended typing&#x60; message was received.  The default is 5 seconds. | [optional] |
| **webhookFilters** | [**List&lt;String&gt;**](String.md)| The list of webhook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] |
| **webhookMethod** | **String**| The HTTP method to use for calls to the &#x60;pre_webhook_url&#x60; and &#x60;post_webhook_url&#x60; webhooks.  Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |

### Return type

[**ChatV2Service**](ChatV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

