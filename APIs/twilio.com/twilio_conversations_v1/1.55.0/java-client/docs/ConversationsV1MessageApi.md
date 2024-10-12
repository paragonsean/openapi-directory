# ConversationsV1MessageApi

All URIs are relative to *https://conversations.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createConversationMessage**](ConversationsV1MessageApi.md#createConversationMessage) | **POST** /v1/Conversations/{ConversationSid}/Messages |  |
| [**createServiceConversationMessage**](ConversationsV1MessageApi.md#createServiceConversationMessage) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages |  |
| [**deleteConversationMessage**](ConversationsV1MessageApi.md#deleteConversationMessage) | **DELETE** /v1/Conversations/{ConversationSid}/Messages/{Sid} |  |
| [**deleteServiceConversationMessage**](ConversationsV1MessageApi.md#deleteServiceConversationMessage) | **DELETE** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid} |  |
| [**fetchConversationMessage**](ConversationsV1MessageApi.md#fetchConversationMessage) | **GET** /v1/Conversations/{ConversationSid}/Messages/{Sid} |  |
| [**fetchServiceConversationMessage**](ConversationsV1MessageApi.md#fetchServiceConversationMessage) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid} |  |
| [**listConversationMessage**](ConversationsV1MessageApi.md#listConversationMessage) | **GET** /v1/Conversations/{ConversationSid}/Messages |  |
| [**listServiceConversationMessage**](ConversationsV1MessageApi.md#listServiceConversationMessage) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages |  |
| [**updateConversationMessage**](ConversationsV1MessageApi.md#updateConversationMessage) | **POST** /v1/Conversations/{ConversationSid}/Messages/{Sid} |  |
| [**updateServiceConversationMessage**](ConversationsV1MessageApi.md#updateServiceConversationMessage) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid} |  |


<a id="createConversationMessage"></a>
# **createConversationMessage**
> ConversationsV1ConversationConversationMessage createConversationMessage(conversationSid, xTwilioWebhookEnabled, attributes, author, body, contentSid, contentVariables, dateCreated, dateUpdated, mediaSid, subject)



Add a new message to the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1MessageApi apiInstance = new ConversationsV1MessageApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    ConversationMessageEnumWebhookEnabledType xTwilioWebhookEnabled = ConversationMessageEnumWebhookEnabledType.fromValue("true"); // ConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
    String author = "author_example"; // String | The channel specific identifier of the message's author. Defaults to `system`.
    String body = "body_example"; // String | The content of the message, can be up to 1,600 characters long.
    String contentSid = "contentSid_example"; // String | The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template, required for template-generated messages.  **Note** that if this field is set, `Body` and `MediaSid` parameters are ignored.
    String contentVariables = "contentVariables_example"; // String | A structurally valid JSON string that contains values to resolve Rich Content template variables.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was last updated. `null` if the message has not been edited.
    String mediaSid = "mediaSid_example"; // String | The Media SID to be attached to the new Message.
    String subject = "subject_example"; // String | The subject of the message, can be up to 256 characters long.
    try {
      ConversationsV1ConversationConversationMessage result = apiInstance.createConversationMessage(conversationSid, xTwilioWebhookEnabled, attributes, author, body, contentSid, contentVariables, dateCreated, dateUpdated, mediaSid, subject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1MessageApi#createConversationMessage");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | |
| **xTwilioWebhookEnabled** | **ConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] |
| **author** | **String**| The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;. | [optional] |
| **body** | **String**| The content of the message, can be up to 1,600 characters long. | [optional] |
| **contentSid** | **String**| The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template, required for template-generated messages.  **Note** that if this field is set, &#x60;Body&#x60; and &#x60;MediaSid&#x60; parameters are ignored. | [optional] |
| **contentVariables** | **String**| A structurally valid JSON string that contains values to resolve Rich Content template variables. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date that this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited. | [optional] |
| **mediaSid** | **String**| The Media SID to be attached to the new Message. | [optional] |
| **subject** | **String**| The subject of the message, can be up to 256 characters long. | [optional] |

### Return type

[**ConversationsV1ConversationConversationMessage**](ConversationsV1ConversationConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="createServiceConversationMessage"></a>
# **createServiceConversationMessage**
> ConversationsV1ServiceServiceConversationServiceConversationMessage createServiceConversationMessage(chatServiceSid, conversationSid, xTwilioWebhookEnabled, attributes, author, body, contentSid, contentVariables, dateCreated, dateUpdated, mediaSid, subject)



Add a new message to the conversation in a specific service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1MessageApi apiInstance = new ConversationsV1MessageApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    ServiceConversationMessageEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceConversationMessageEnumWebhookEnabledType.fromValue("true"); // ServiceConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
    String author = "author_example"; // String | The channel specific identifier of the message's author. Defaults to `system`.
    String body = "body_example"; // String | The content of the message, can be up to 1,600 characters long.
    String contentSid = "contentSid_example"; // String | The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template, required for template-generated messages.  **Note** that if this field is set, `Body` and `MediaSid` parameters are ignored.
    String contentVariables = "contentVariables_example"; // String | A structurally valid JSON string that contains values to resolve Rich Content template variables.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was last updated. `null` if the message has not been edited.
    String mediaSid = "mediaSid_example"; // String | The Media SID to be attached to the new Message.
    String subject = "subject_example"; // String | The subject of the message, can be up to 256 characters long.
    try {
      ConversationsV1ServiceServiceConversationServiceConversationMessage result = apiInstance.createServiceConversationMessage(chatServiceSid, conversationSid, xTwilioWebhookEnabled, attributes, author, body, contentSid, contentVariables, dateCreated, dateUpdated, mediaSid, subject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1MessageApi#createServiceConversationMessage");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | |
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | |
| **xTwilioWebhookEnabled** | **ServiceConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] |
| **author** | **String**| The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;. | [optional] |
| **body** | **String**| The content of the message, can be up to 1,600 characters long. | [optional] |
| **contentSid** | **String**| The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content) template, required for template-generated messages.  **Note** that if this field is set, &#x60;Body&#x60; and &#x60;MediaSid&#x60; parameters are ignored. | [optional] |
| **contentVariables** | **String**| A structurally valid JSON string that contains values to resolve Rich Content template variables. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date that this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited. | [optional] |
| **mediaSid** | **String**| The Media SID to be attached to the new Message. | [optional] |
| **subject** | **String**| The subject of the message, can be up to 256 characters long. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationMessage**](ConversationsV1ServiceServiceConversationServiceConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteConversationMessage"></a>
# **deleteConversationMessage**
> deleteConversationMessage(conversationSid, sid, xTwilioWebhookEnabled)



Remove a message from the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1MessageApi apiInstance = new ConversationsV1MessageApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    ConversationMessageEnumWebhookEnabledType xTwilioWebhookEnabled = ConversationMessageEnumWebhookEnabledType.fromValue("true"); // ConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteConversationMessage(conversationSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1MessageApi#deleteConversationMessage");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **xTwilioWebhookEnabled** | **ConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="deleteServiceConversationMessage"></a>
# **deleteServiceConversationMessage**
> deleteServiceConversationMessage(chatServiceSid, conversationSid, sid, xTwilioWebhookEnabled)



Remove a message from the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1MessageApi apiInstance = new ConversationsV1MessageApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    ServiceConversationMessageEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceConversationMessageEnumWebhookEnabledType.fromValue("true"); // ServiceConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteServiceConversationMessage(chatServiceSid, conversationSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1MessageApi#deleteServiceConversationMessage");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | |
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **xTwilioWebhookEnabled** | **ServiceConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="fetchConversationMessage"></a>
# **fetchConversationMessage**
> ConversationsV1ConversationConversationMessage fetchConversationMessage(conversationSid, sid)



Fetch a message from the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1MessageApi apiInstance = new ConversationsV1MessageApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    try {
      ConversationsV1ConversationConversationMessage result = apiInstance.fetchConversationMessage(conversationSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1MessageApi#fetchConversationMessage");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |

### Return type

[**ConversationsV1ConversationConversationMessage**](ConversationsV1ConversationConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchServiceConversationMessage"></a>
# **fetchServiceConversationMessage**
> ConversationsV1ServiceServiceConversationServiceConversationMessage fetchServiceConversationMessage(chatServiceSid, conversationSid, sid)



Fetch a message from the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1MessageApi apiInstance = new ConversationsV1MessageApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    try {
      ConversationsV1ServiceServiceConversationServiceConversationMessage result = apiInstance.fetchServiceConversationMessage(chatServiceSid, conversationSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1MessageApi#fetchServiceConversationMessage");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | |
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationMessage**](ConversationsV1ServiceServiceConversationServiceConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listConversationMessage"></a>
# **listConversationMessage**
> ListConversationMessageResponse listConversationMessage(conversationSid, order, pageSize, page, pageToken)



Retrieve a list of all messages in the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1MessageApi apiInstance = new ConversationsV1MessageApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages.
    ConversationMessageEnumOrderType order = ConversationMessageEnumOrderType.fromValue("asc"); // ConversationMessageEnumOrderType | The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListConversationMessageResponse result = apiInstance.listConversationMessage(conversationSid, order, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1MessageApi#listConversationMessage");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages. | |
| **order** | **ConversationMessageEnumOrderType**| The sort order of the returned messages. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending), with &#x60;asc&#x60; as the default. | [optional] [enum: asc, desc] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListConversationMessageResponse**](ListConversationMessageResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listServiceConversationMessage"></a>
# **listServiceConversationMessage**
> ListServiceConversationMessageResponse listServiceConversationMessage(chatServiceSid, conversationSid, order, pageSize, page, pageToken)



Retrieve a list of all messages in the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1MessageApi apiInstance = new ConversationsV1MessageApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages.
    ServiceConversationMessageEnumOrderType order = ServiceConversationMessageEnumOrderType.fromValue("asc"); // ServiceConversationMessageEnumOrderType | The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceConversationMessageResponse result = apiInstance.listServiceConversationMessage(chatServiceSid, conversationSid, order, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1MessageApi#listServiceConversationMessage");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | |
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages. | |
| **order** | **ServiceConversationMessageEnumOrderType**| The sort order of the returned messages. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending), with &#x60;asc&#x60; as the default. | [optional] [enum: asc, desc] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceConversationMessageResponse**](ListServiceConversationMessageResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateConversationMessage"></a>
# **updateConversationMessage**
> ConversationsV1ConversationConversationMessage updateConversationMessage(conversationSid, sid, xTwilioWebhookEnabled, attributes, author, body, dateCreated, dateUpdated, subject)



Update an existing message in the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1MessageApi apiInstance = new ConversationsV1MessageApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    ConversationMessageEnumWebhookEnabledType xTwilioWebhookEnabled = ConversationMessageEnumWebhookEnabledType.fromValue("true"); // ConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
    String author = "author_example"; // String | The channel specific identifier of the message's author. Defaults to `system`.
    String body = "body_example"; // String | The content of the message, can be up to 1,600 characters long.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was last updated. `null` if the message has not been edited.
    String subject = "subject_example"; // String | The subject of the message, can be up to 256 characters long.
    try {
      ConversationsV1ConversationConversationMessage result = apiInstance.updateConversationMessage(conversationSid, sid, xTwilioWebhookEnabled, attributes, author, body, dateCreated, dateUpdated, subject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1MessageApi#updateConversationMessage");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **xTwilioWebhookEnabled** | **ConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] |
| **author** | **String**| The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;. | [optional] |
| **body** | **String**| The content of the message, can be up to 1,600 characters long. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date that this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited. | [optional] |
| **subject** | **String**| The subject of the message, can be up to 256 characters long. | [optional] |

### Return type

[**ConversationsV1ConversationConversationMessage**](ConversationsV1ConversationConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateServiceConversationMessage"></a>
# **updateServiceConversationMessage**
> ConversationsV1ServiceServiceConversationServiceConversationMessage updateServiceConversationMessage(chatServiceSid, conversationSid, sid, xTwilioWebhookEnabled, attributes, author, body, dateCreated, dateUpdated, subject)



Update an existing message in the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1MessageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1MessageApi apiInstance = new ConversationsV1MessageApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    ServiceConversationMessageEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceConversationMessageEnumWebhookEnabledType.fromValue("true"); // ServiceConversationMessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
    String author = "author_example"; // String | The channel specific identifier of the message's author. Defaults to `system`.
    String body = "body_example"; // String | The content of the message, can be up to 1,600 characters long.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was last updated. `null` if the message has not been edited.
    String subject = "subject_example"; // String | The subject of the message, can be up to 256 characters long.
    try {
      ConversationsV1ServiceServiceConversationServiceConversationMessage result = apiInstance.updateServiceConversationMessage(chatServiceSid, conversationSid, sid, xTwilioWebhookEnabled, attributes, author, body, dateCreated, dateUpdated, subject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1MessageApi#updateServiceConversationMessage");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with. | |
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **xTwilioWebhookEnabled** | **ServiceConversationMessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] |
| **author** | **String**| The channel specific identifier of the message&#39;s author. Defaults to &#x60;system&#x60;. | [optional] |
| **body** | **String**| The content of the message, can be up to 1,600 characters long. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date that this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date that this resource was last updated. &#x60;null&#x60; if the message has not been edited. | [optional] |
| **subject** | **String**| The subject of the message, can be up to 256 characters long. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationMessage**](ConversationsV1ServiceServiceConversationServiceConversationMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

