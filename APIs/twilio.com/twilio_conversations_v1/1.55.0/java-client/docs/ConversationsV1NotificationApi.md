# ConversationsV1NotificationApi

All URIs are relative to *https://conversations.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchServiceNotification**](ConversationsV1NotificationApi.md#fetchServiceNotification) | **GET** /v1/Services/{ChatServiceSid}/Configuration/Notifications |  |
| [**updateServiceNotification**](ConversationsV1NotificationApi.md#updateServiceNotification) | **POST** /v1/Services/{ChatServiceSid}/Configuration/Notifications |  |


<a id="fetchServiceNotification"></a>
# **fetchServiceNotification**
> ConversationsV1ServiceServiceConfigurationServiceNotification fetchServiceNotification(chatServiceSid)



Fetch push notification service settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1NotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1NotificationApi apiInstance = new ConversationsV1NotificationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to.
    try {
      ConversationsV1ServiceServiceConfigurationServiceNotification result = apiInstance.fetchServiceNotification(chatServiceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1NotificationApi#fetchServiceNotification");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to. | |

### Return type

[**ConversationsV1ServiceServiceConfigurationServiceNotification**](ConversationsV1ServiceServiceConfigurationServiceNotification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateServiceNotification"></a>
# **updateServiceNotification**
> ConversationsV1ServiceServiceConfigurationServiceNotification updateServiceNotification(chatServiceSid, addedToConversationEnabled, addedToConversationSound, addedToConversationTemplate, logEnabled, newMessageBadgeCountEnabled, newMessageEnabled, newMessageSound, newMessageTemplate, newMessageWithMediaEnabled, newMessageWithMediaTemplate, removedFromConversationEnabled, removedFromConversationSound, removedFromConversationTemplate)



Update push notification service settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1NotificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1NotificationApi apiInstance = new ConversationsV1NotificationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to.
    Boolean addedToConversationEnabled = true; // Boolean | Whether to send a notification when a participant is added to a conversation. The default is `false`.
    String addedToConversationSound = "addedToConversationSound_example"; // String | The name of the sound to play when a participant is added to a conversation and `added_to_conversation.enabled` is `true`.
    String addedToConversationTemplate = "addedToConversationTemplate_example"; // String | The template to use to create the notification text displayed when a participant is added to a conversation and `added_to_conversation.enabled` is `true`.
    Boolean logEnabled = true; // Boolean | Weather the notification logging is enabled.
    Boolean newMessageBadgeCountEnabled = true; // Boolean | Whether the new message badge is enabled. The default is `false`.
    Boolean newMessageEnabled = true; // Boolean | Whether to send a notification when a new message is added to a conversation. The default is `false`.
    String newMessageSound = "newMessageSound_example"; // String | The name of the sound to play when a new message is added to a conversation and `new_message.enabled` is `true`.
    String newMessageTemplate = "newMessageTemplate_example"; // String | The template to use to create the notification text displayed when a new message is added to a conversation and `new_message.enabled` is `true`.
    Boolean newMessageWithMediaEnabled = true; // Boolean | Whether to send a notification when a new message with media/file attachments is added to a conversation. The default is `false`.
    String newMessageWithMediaTemplate = "newMessageWithMediaTemplate_example"; // String | The template to use to create the notification text displayed when a new message with media/file attachments is added to a conversation and `new_message.attachments.enabled` is `true`.
    Boolean removedFromConversationEnabled = true; // Boolean | Whether to send a notification to a user when they are removed from a conversation. The default is `false`.
    String removedFromConversationSound = "removedFromConversationSound_example"; // String | The name of the sound to play to a user when they are removed from a conversation and `removed_from_conversation.enabled` is `true`.
    String removedFromConversationTemplate = "removedFromConversationTemplate_example"; // String | The template to use to create the notification text displayed to a user when they are removed from a conversation and `removed_from_conversation.enabled` is `true`.
    try {
      ConversationsV1ServiceServiceConfigurationServiceNotification result = apiInstance.updateServiceNotification(chatServiceSid, addedToConversationEnabled, addedToConversationSound, addedToConversationTemplate, logEnabled, newMessageBadgeCountEnabled, newMessageEnabled, newMessageSound, newMessageTemplate, newMessageWithMediaEnabled, newMessageWithMediaTemplate, removedFromConversationEnabled, removedFromConversationSound, removedFromConversationTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1NotificationApi#updateServiceNotification");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to. | |
| **addedToConversationEnabled** | **Boolean**| Whether to send a notification when a participant is added to a conversation. The default is &#x60;false&#x60;. | [optional] |
| **addedToConversationSound** | **String**| The name of the sound to play when a participant is added to a conversation and &#x60;added_to_conversation.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **addedToConversationTemplate** | **String**| The template to use to create the notification text displayed when a participant is added to a conversation and &#x60;added_to_conversation.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **logEnabled** | **Boolean**| Weather the notification logging is enabled. | [optional] |
| **newMessageBadgeCountEnabled** | **Boolean**| Whether the new message badge is enabled. The default is &#x60;false&#x60;. | [optional] |
| **newMessageEnabled** | **Boolean**| Whether to send a notification when a new message is added to a conversation. The default is &#x60;false&#x60;. | [optional] |
| **newMessageSound** | **String**| The name of the sound to play when a new message is added to a conversation and &#x60;new_message.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **newMessageTemplate** | **String**| The template to use to create the notification text displayed when a new message is added to a conversation and &#x60;new_message.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **newMessageWithMediaEnabled** | **Boolean**| Whether to send a notification when a new message with media/file attachments is added to a conversation. The default is &#x60;false&#x60;. | [optional] |
| **newMessageWithMediaTemplate** | **String**| The template to use to create the notification text displayed when a new message with media/file attachments is added to a conversation and &#x60;new_message.attachments.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **removedFromConversationEnabled** | **Boolean**| Whether to send a notification to a user when they are removed from a conversation. The default is &#x60;false&#x60;. | [optional] |
| **removedFromConversationSound** | **String**| The name of the sound to play to a user when they are removed from a conversation and &#x60;removed_from_conversation.enabled&#x60; is &#x60;true&#x60;. | [optional] |
| **removedFromConversationTemplate** | **String**| The template to use to create the notification text displayed to a user when they are removed from a conversation and &#x60;removed_from_conversation.enabled&#x60; is &#x60;true&#x60;. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConfigurationServiceNotification**](ConversationsV1ServiceServiceConfigurationServiceNotification.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

