# ChatApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chatDelete**](ChatApi.md#chatDelete) | **POST** /chat.delete |  |
| [**chatDeleteScheduledMessage**](ChatApi.md#chatDeleteScheduledMessage) | **POST** /chat.deleteScheduledMessage |  |
| [**chatGetPermalink**](ChatApi.md#chatGetPermalink) | **GET** /chat.getPermalink |  |
| [**chatMeMessage**](ChatApi.md#chatMeMessage) | **POST** /chat.meMessage |  |
| [**chatPostEphemeral**](ChatApi.md#chatPostEphemeral) | **POST** /chat.postEphemeral |  |
| [**chatPostMessage**](ChatApi.md#chatPostMessage) | **POST** /chat.postMessage |  |
| [**chatScheduleMessage**](ChatApi.md#chatScheduleMessage) | **POST** /chat.scheduleMessage |  |
| [**chatScheduledMessagesList_0**](ChatApi.md#chatScheduledMessagesList_0) | **GET** /chat.scheduledMessages.list |  |
| [**chatUnfurl**](ChatApi.md#chatUnfurl) | **POST** /chat.unfurl |  |
| [**chatUpdate**](ChatApi.md#chatUpdate) | **POST** /chat.update |  |


<a id="chatDelete"></a>
# **chatDelete**
> ChatDeleteSuccessSchema chatDelete(token, asUser, channel, ts)



Deletes a message.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatApi apiInstance = new ChatApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `chat:write`
    Boolean asUser = true; // Boolean | Pass true to delete the message as the authed user with `chat:write:user` scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with `chat:write:bot` scope.
    String channel = "channel_example"; // String | Channel containing the message to be deleted.
    BigDecimal ts = new BigDecimal(78); // BigDecimal | Timestamp of the message to be deleted.
    try {
      ChatDeleteSuccessSchema result = apiInstance.chatDelete(token, asUser, channel, ts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatApi#chatDelete");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;chat:write&#x60; | [optional] |
| **asUser** | **Boolean**| Pass true to delete the message as the authed user with &#x60;chat:write:user&#x60; scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with &#x60;chat:write:bot&#x60; scope. | [optional] |
| **channel** | **String**| Channel containing the message to be deleted. | [optional] |
| **ts** | **BigDecimal**| Timestamp of the message to be deleted. | [optional] |

### Return type

[**ChatDeleteSuccessSchema**](ChatDeleteSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="chatDeleteScheduledMessage"></a>
# **chatDeleteScheduledMessage**
> ChatDeleteScheduledMessageSchema chatDeleteScheduledMessage(token, channel, scheduledMessageId, asUser)



Deletes a pending scheduled message from the queue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatApi apiInstance = new ChatApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `chat:write`
    String channel = "channel_example"; // String | The channel the scheduled_message is posting to
    String scheduledMessageId = "scheduledMessageId_example"; // String | `scheduled_message_id` returned from call to chat.scheduleMessage
    Boolean asUser = true; // Boolean | Pass true to delete the message as the authed user with `chat:write:user` scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with `chat:write:bot` scope.
    try {
      ChatDeleteScheduledMessageSchema result = apiInstance.chatDeleteScheduledMessage(token, channel, scheduledMessageId, asUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatApi#chatDeleteScheduledMessage");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;chat:write&#x60; | |
| **channel** | **String**| The channel the scheduled_message is posting to | |
| **scheduledMessageId** | **String**| &#x60;scheduled_message_id&#x60; returned from call to chat.scheduleMessage | |
| **asUser** | **Boolean**| Pass true to delete the message as the authed user with &#x60;chat:write:user&#x60; scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with &#x60;chat:write:bot&#x60; scope. | [optional] |

### Return type

[**ChatDeleteScheduledMessageSchema**](ChatDeleteScheduledMessageSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response if no message is found |  -  |

<a id="chatGetPermalink"></a>
# **chatGetPermalink**
> ChatGetPermalinkSuccessSchema chatGetPermalink(token, channel, messageTs)



Retrieve a permalink URL for a specific extant message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatApi apiInstance = new ChatApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String channel = "channel_example"; // String | The ID of the conversation or channel containing the message
    String messageTs = "messageTs_example"; // String | A message's `ts` value, uniquely identifying it within a channel
    try {
      ChatGetPermalinkSuccessSchema result = apiInstance.chatGetPermalink(token, channel, messageTs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatApi#chatGetPermalink");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | |
| **channel** | **String**| The ID of the conversation or channel containing the message | |
| **messageTs** | **String**| A message&#39;s &#x60;ts&#x60; value, uniquely identifying it within a channel | |

### Return type

[**ChatGetPermalinkSuccessSchema**](ChatGetPermalinkSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standard success response |  -  |
| **0** | Error response when channel cannot be found |  -  |

<a id="chatMeMessage"></a>
# **chatMeMessage**
> ChatMeMessageSchema chatMeMessage(token, channel, text)



Share a me message into a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatApi apiInstance = new ChatApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `chat:write`
    String channel = "channel_example"; // String | Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded ID, or a name.
    String text = "text_example"; // String | Text of the message to send.
    try {
      ChatMeMessageSchema result = apiInstance.chatMeMessage(token, channel, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatApi#chatMeMessage");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;chat:write&#x60; | [optional] |
| **channel** | **String**| Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded ID, or a name. | [optional] |
| **text** | **String**| Text of the message to send. | [optional] |

### Return type

[**ChatMeMessageSchema**](ChatMeMessageSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="chatPostEphemeral"></a>
# **chatPostEphemeral**
> ChatPostEphemeralSuccessSchema chatPostEphemeral(token, channel, user, asUser, attachments, blocks, iconEmoji, iconUrl, linkNames, parse, text, threadTs, username)



Sends an ephemeral message to a user in a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatApi apiInstance = new ChatApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `chat:write`
    String channel = "channel_example"; // String | Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.
    String user = "user_example"; // String | `id` of the user who will receive the ephemeral message. The user should be in the channel specified by the `channel` argument.
    Boolean asUser = true; // Boolean | Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is not included. Otherwise, defaults to false.
    String attachments = "attachments_example"; // String | A JSON-based array of structured attachments, presented as a URL-encoded string.
    String blocks = "blocks_example"; // String | A JSON-based array of structured blocks, presented as a URL-encoded string.
    String iconEmoji = "iconEmoji_example"; // String | Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](#authorship) below.
    String iconUrl = "iconUrl_example"; // String | URL to an image to use as the icon for this message. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.
    Boolean linkNames = true; // Boolean | Find and link channel names and usernames.
    String parse = "parse_example"; // String | Change how messages are treated. Defaults to `none`. See [below](#formatting).
    String text = "text_example"; // String | How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.
    String threadTs = "threadTs_example"; // String | Provide another message's `ts` value to post this message in a thread. Avoid using a reply's `ts` value; use its parent's value instead. Ephemeral messages in threads are only shown if there is already an active thread.
    String username = "username_example"; // String | Set your bot's user name. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.
    try {
      ChatPostEphemeralSuccessSchema result = apiInstance.chatPostEphemeral(token, channel, user, asUser, attachments, blocks, iconEmoji, iconUrl, linkNames, parse, text, threadTs, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatApi#chatPostEphemeral");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;chat:write&#x60; | |
| **channel** | **String**| Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. | |
| **user** | **String**| &#x60;id&#x60; of the user who will receive the ephemeral message. The user should be in the channel specified by the &#x60;channel&#x60; argument. | |
| **asUser** | **Boolean**| Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is not included. Otherwise, defaults to false. | [optional] |
| **attachments** | **String**| A JSON-based array of structured attachments, presented as a URL-encoded string. | [optional] |
| **blocks** | **String**| A JSON-based array of structured blocks, presented as a URL-encoded string. | [optional] |
| **iconEmoji** | **String**| Emoji to use as the icon for this message. Overrides &#x60;icon_url&#x60;. Must be used in conjunction with &#x60;as_user&#x60; set to &#x60;false&#x60;, otherwise ignored. See [authorship](#authorship) below. | [optional] |
| **iconUrl** | **String**| URL to an image to use as the icon for this message. Must be used in conjunction with &#x60;as_user&#x60; set to false, otherwise ignored. See [authorship](#authorship) below. | [optional] |
| **linkNames** | **Boolean**| Find and link channel names and usernames. | [optional] |
| **parse** | **String**| Change how messages are treated. Defaults to &#x60;none&#x60;. See [below](#formatting). | [optional] |
| **text** | **String**| How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail. | [optional] |
| **threadTs** | **String**| Provide another message&#39;s &#x60;ts&#x60; value to post this message in a thread. Avoid using a reply&#39;s &#x60;ts&#x60; value; use its parent&#39;s value instead. Ephemeral messages in threads are only shown if there is already an active thread. | [optional] |
| **username** | **String**| Set your bot&#39;s user name. Must be used in conjunction with &#x60;as_user&#x60; set to false, otherwise ignored. See [authorship](#authorship) below. | [optional] |

### Return type

[**ChatPostEphemeralSuccessSchema**](ChatPostEphemeralSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="chatPostMessage"></a>
# **chatPostMessage**
> ChatPostMessageSuccessSchema chatPostMessage(token, channel, asUser, attachments, blocks, iconEmoji, iconUrl, linkNames, mrkdwn, parse, replyBroadcast, text, threadTs, unfurlLinks, unfurlMedia, username)



Sends a message to a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatApi apiInstance = new ChatApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `chat:write`
    String channel = "channel_example"; // String | Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details.
    String asUser = "asUser_example"; // String | Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [authorship](#authorship) below.
    String attachments = "attachments_example"; // String | A JSON-based array of structured attachments, presented as a URL-encoded string.
    String blocks = "blocks_example"; // String | A JSON-based array of structured blocks, presented as a URL-encoded string.
    String iconEmoji = "iconEmoji_example"; // String | Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](#authorship) below.
    String iconUrl = "iconUrl_example"; // String | URL to an image to use as the icon for this message. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.
    Boolean linkNames = true; // Boolean | Find and link channel names and usernames.
    Boolean mrkdwn = true; // Boolean | Disable Slack markup parsing by setting to `false`. Enabled by default.
    String parse = "parse_example"; // String | Change how messages are treated. Defaults to `none`. See [below](#formatting).
    Boolean replyBroadcast = true; // Boolean | Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.
    String text = "text_example"; // String | How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.
    String threadTs = "threadTs_example"; // String | Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.
    Boolean unfurlLinks = true; // Boolean | Pass true to enable unfurling of primarily text-based content.
    Boolean unfurlMedia = true; // Boolean | Pass false to disable unfurling of media content.
    String username = "username_example"; // String | Set your bot's user name. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.
    try {
      ChatPostMessageSuccessSchema result = apiInstance.chatPostMessage(token, channel, asUser, attachments, blocks, iconEmoji, iconUrl, linkNames, mrkdwn, parse, replyBroadcast, text, threadTs, unfurlLinks, unfurlMedia, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatApi#chatPostMessage");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;chat:write&#x60; | |
| **channel** | **String**| Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details. | |
| **asUser** | **String**| Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [authorship](#authorship) below. | [optional] |
| **attachments** | **String**| A JSON-based array of structured attachments, presented as a URL-encoded string. | [optional] |
| **blocks** | **String**| A JSON-based array of structured blocks, presented as a URL-encoded string. | [optional] |
| **iconEmoji** | **String**| Emoji to use as the icon for this message. Overrides &#x60;icon_url&#x60;. Must be used in conjunction with &#x60;as_user&#x60; set to &#x60;false&#x60;, otherwise ignored. See [authorship](#authorship) below. | [optional] |
| **iconUrl** | **String**| URL to an image to use as the icon for this message. Must be used in conjunction with &#x60;as_user&#x60; set to false, otherwise ignored. See [authorship](#authorship) below. | [optional] |
| **linkNames** | **Boolean**| Find and link channel names and usernames. | [optional] |
| **mrkdwn** | **Boolean**| Disable Slack markup parsing by setting to &#x60;false&#x60;. Enabled by default. | [optional] |
| **parse** | **String**| Change how messages are treated. Defaults to &#x60;none&#x60;. See [below](#formatting). | [optional] |
| **replyBroadcast** | **Boolean**| Used in conjunction with &#x60;thread_ts&#x60; and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to &#x60;false&#x60;. | [optional] |
| **text** | **String**| How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail. | [optional] |
| **threadTs** | **String**| Provide another message&#39;s &#x60;ts&#x60; value to make this message a reply. Avoid using a reply&#39;s &#x60;ts&#x60; value; use its parent instead. | [optional] |
| **unfurlLinks** | **Boolean**| Pass true to enable unfurling of primarily text-based content. | [optional] |
| **unfurlMedia** | **Boolean**| Pass false to disable unfurling of media content. | [optional] |
| **username** | **String**| Set your bot&#39;s user name. Must be used in conjunction with &#x60;as_user&#x60; set to false, otherwise ignored. See [authorship](#authorship) below. | [optional] |

### Return type

[**ChatPostMessageSuccessSchema**](ChatPostMessageSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response if too many attachments are included |  -  |

<a id="chatScheduleMessage"></a>
# **chatScheduleMessage**
> ChatScheduleMessageSuccessSchema chatScheduleMessage(token, asUser, attachments, blocks, channel, linkNames, parse, postAt, replyBroadcast, text, threadTs, unfurlLinks, unfurlMedia)



Schedules a message to be sent to a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatApi apiInstance = new ChatApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `chat:write`
    Boolean asUser = true; // Boolean | Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [chat.postMessage](chat.postMessage#authorship).
    String attachments = "attachments_example"; // String | A JSON-based array of structured attachments, presented as a URL-encoded string.
    String blocks = "blocks_example"; // String | A JSON-based array of structured blocks, presented as a URL-encoded string.
    String channel = "channel_example"; // String | Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details.
    Boolean linkNames = true; // Boolean | Find and link channel names and usernames.
    String parse = "parse_example"; // String | Change how messages are treated. Defaults to `none`. See [chat.postMessage](chat.postMessage#formatting).
    String postAt = "postAt_example"; // String | Unix EPOCH timestamp of time in future to send the message.
    Boolean replyBroadcast = true; // Boolean | Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.
    String text = "text_example"; // String | How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.
    BigDecimal threadTs = new BigDecimal(78); // BigDecimal | Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.
    Boolean unfurlLinks = true; // Boolean | Pass true to enable unfurling of primarily text-based content.
    Boolean unfurlMedia = true; // Boolean | Pass false to disable unfurling of media content.
    try {
      ChatScheduleMessageSuccessSchema result = apiInstance.chatScheduleMessage(token, asUser, attachments, blocks, channel, linkNames, parse, postAt, replyBroadcast, text, threadTs, unfurlLinks, unfurlMedia);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatApi#chatScheduleMessage");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;chat:write&#x60; | [optional] |
| **asUser** | **Boolean**| Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [chat.postMessage](chat.postMessage#authorship). | [optional] |
| **attachments** | **String**| A JSON-based array of structured attachments, presented as a URL-encoded string. | [optional] |
| **blocks** | **String**| A JSON-based array of structured blocks, presented as a URL-encoded string. | [optional] |
| **channel** | **String**| Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details. | [optional] |
| **linkNames** | **Boolean**| Find and link channel names and usernames. | [optional] |
| **parse** | **String**| Change how messages are treated. Defaults to &#x60;none&#x60;. See [chat.postMessage](chat.postMessage#formatting). | [optional] |
| **postAt** | **String**| Unix EPOCH timestamp of time in future to send the message. | [optional] |
| **replyBroadcast** | **Boolean**| Used in conjunction with &#x60;thread_ts&#x60; and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to &#x60;false&#x60;. | [optional] |
| **text** | **String**| How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail. | [optional] |
| **threadTs** | **BigDecimal**| Provide another message&#39;s &#x60;ts&#x60; value to make this message a reply. Avoid using a reply&#39;s &#x60;ts&#x60; value; use its parent instead. | [optional] |
| **unfurlLinks** | **Boolean**| Pass true to enable unfurling of primarily text-based content. | [optional] |
| **unfurlMedia** | **Boolean**| Pass false to disable unfurling of media content. | [optional] |

### Return type

[**ChatScheduleMessageSuccessSchema**](ChatScheduleMessageSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response if the &#x60;post_at&#x60; is invalid (ex. in the past or too far into the future) |  -  |

<a id="chatScheduledMessagesList_0"></a>
# **chatScheduledMessagesList_0**
> ChatScheduledMessagesListSchema chatScheduledMessagesList_0(token, channel, latest, oldest, limit, cursor)



Returns a list of scheduled messages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatApi apiInstance = new ChatApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String channel = "channel_example"; // String | The channel of the scheduled messages
    BigDecimal latest = new BigDecimal(78); // BigDecimal | A UNIX timestamp of the latest value in the time range
    BigDecimal oldest = new BigDecimal(78); // BigDecimal | A UNIX timestamp of the oldest value in the time range
    Integer limit = 56; // Integer | Maximum number of original entries to return.
    String cursor = "cursor_example"; // String | For pagination purposes, this is the `cursor` value returned from a previous call to `chat.scheduledmessages.list` indicating where you want to start this call from.
    try {
      ChatScheduledMessagesListSchema result = apiInstance.chatScheduledMessagesList_0(token, channel, latest, oldest, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatApi#chatScheduledMessagesList_0");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | [optional] |
| **channel** | **String**| The channel of the scheduled messages | [optional] |
| **latest** | **BigDecimal**| A UNIX timestamp of the latest value in the time range | [optional] |
| **oldest** | **BigDecimal**| A UNIX timestamp of the oldest value in the time range | [optional] |
| **limit** | **Integer**| Maximum number of original entries to return. | [optional] |
| **cursor** | **String**| For pagination purposes, this is the &#x60;cursor&#x60; value returned from a previous call to &#x60;chat.scheduledmessages.list&#x60; indicating where you want to start this call from. | [optional] |

### Return type

[**ChatScheduledMessagesListSchema**](ChatScheduledMessagesListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response if the channel passed is invalid |  -  |

<a id="chatUnfurl"></a>
# **chatUnfurl**
> ChatUnfurlSuccessSchema chatUnfurl(token, channel, ts, unfurls, userAuthMessage, userAuthRequired, userAuthUrl)



Provide custom unfurl behavior for user-posted URLs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatApi apiInstance = new ChatApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `links:write`
    String channel = "channel_example"; // String | Channel ID of the message
    String ts = "ts_example"; // String | Timestamp of the message to add unfurl behavior to.
    String unfurls = "unfurls_example"; // String | URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl blocks or message attachments.
    String userAuthMessage = "userAuthMessage_example"; // String | Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior
    Boolean userAuthRequired = true; // Boolean | Set to `true` or `1` to indicate the user must install your Slack app to trigger unfurls for this domain
    String userAuthUrl = "userAuthUrl_example"; // String | Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded.
    try {
      ChatUnfurlSuccessSchema result = apiInstance.chatUnfurl(token, channel, ts, unfurls, userAuthMessage, userAuthRequired, userAuthUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatApi#chatUnfurl");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;links:write&#x60; | |
| **channel** | **String**| Channel ID of the message | |
| **ts** | **String**| Timestamp of the message to add unfurl behavior to. | |
| **unfurls** | **String**| URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl blocks or message attachments. | [optional] |
| **userAuthMessage** | **String**| Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior | [optional] |
| **userAuthRequired** | **Boolean**| Set to &#x60;true&#x60; or &#x60;1&#x60; to indicate the user must install your Slack app to trigger unfurls for this domain | [optional] |
| **userAuthUrl** | **String**| Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded. | [optional] |

### Return type

[**ChatUnfurlSuccessSchema**](ChatUnfurlSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical, minimal success response |  -  |
| **0** | Typical error response |  -  |

<a id="chatUpdate"></a>
# **chatUpdate**
> ChatUpdateSuccessSchema chatUpdate(token, channel, ts, asUser, attachments, blocks, linkNames, parse, text)



Updates a message.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatApi apiInstance = new ChatApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `chat:write`
    String channel = "channel_example"; // String | Channel containing the message to be updated.
    String ts = "ts_example"; // String | Timestamp of the message to be updated.
    String asUser = "asUser_example"; // String | Pass true to update the message as the authed user. [Bot users](/bot-users) in this context are considered authed users.
    String attachments = "attachments_example"; // String | A JSON-based array of structured attachments, presented as a URL-encoded string. This field is required when not presenting `text`. If you don't include this field, the message's previous `attachments` will be retained. To remove previous `attachments`, include an empty array for this field.
    String blocks = "blocks_example"; // String | A JSON-based array of [structured blocks](/block-kit/building), presented as a URL-encoded string. If you don't include this field, the message's previous `blocks` will be retained. To remove previous `blocks`, include an empty array for this field.
    String linkNames = "linkNames_example"; // String | Find and link channel names and usernames. Defaults to `none`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `none`.
    String parse = "parse_example"; // String | Change how messages are treated. Defaults to `client`, unlike `chat.postMessage`. Accepts either `none` or `full`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `client`.
    String text = "text_example"; // String | New text for the message, using the [default formatting rules](/reference/surfaces/formatting). It's not required when presenting `blocks` or `attachments`.
    try {
      ChatUpdateSuccessSchema result = apiInstance.chatUpdate(token, channel, ts, asUser, attachments, blocks, linkNames, parse, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatApi#chatUpdate");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;chat:write&#x60; | |
| **channel** | **String**| Channel containing the message to be updated. | |
| **ts** | **String**| Timestamp of the message to be updated. | |
| **asUser** | **String**| Pass true to update the message as the authed user. [Bot users](/bot-users) in this context are considered authed users. | [optional] |
| **attachments** | **String**| A JSON-based array of structured attachments, presented as a URL-encoded string. This field is required when not presenting &#x60;text&#x60;. If you don&#39;t include this field, the message&#39;s previous &#x60;attachments&#x60; will be retained. To remove previous &#x60;attachments&#x60;, include an empty array for this field. | [optional] |
| **blocks** | **String**| A JSON-based array of [structured blocks](/block-kit/building), presented as a URL-encoded string. If you don&#39;t include this field, the message&#39;s previous &#x60;blocks&#x60; will be retained. To remove previous &#x60;blocks&#x60;, include an empty array for this field. | [optional] |
| **linkNames** | **String**| Find and link channel names and usernames. Defaults to &#x60;none&#x60;. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, &#x60;none&#x60;. | [optional] |
| **parse** | **String**| Change how messages are treated. Defaults to &#x60;client&#x60;, unlike &#x60;chat.postMessage&#x60;. Accepts either &#x60;none&#x60; or &#x60;full&#x60;. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, &#x60;client&#x60;. | [optional] |
| **text** | **String**| New text for the message, using the [default formatting rules](/reference/surfaces/formatting). It&#39;s not required when presenting &#x60;blocks&#x60; or &#x60;attachments&#x60;. | [optional] |

### Return type

[**ChatUpdateSuccessSchema**](ChatUpdateSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

