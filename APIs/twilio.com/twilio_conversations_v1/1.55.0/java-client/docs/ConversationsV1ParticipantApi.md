# ConversationsV1ParticipantApi

All URIs are relative to *https://conversations.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createConversationParticipant**](ConversationsV1ParticipantApi.md#createConversationParticipant) | **POST** /v1/Conversations/{ConversationSid}/Participants |  |
| [**createServiceConversationParticipant**](ConversationsV1ParticipantApi.md#createServiceConversationParticipant) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants |  |
| [**deleteConversationParticipant**](ConversationsV1ParticipantApi.md#deleteConversationParticipant) | **DELETE** /v1/Conversations/{ConversationSid}/Participants/{Sid} |  |
| [**deleteServiceConversationParticipant**](ConversationsV1ParticipantApi.md#deleteServiceConversationParticipant) | **DELETE** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid} |  |
| [**fetchConversationParticipant**](ConversationsV1ParticipantApi.md#fetchConversationParticipant) | **GET** /v1/Conversations/{ConversationSid}/Participants/{Sid} |  |
| [**fetchServiceConversationParticipant**](ConversationsV1ParticipantApi.md#fetchServiceConversationParticipant) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid} |  |
| [**listConversationParticipant**](ConversationsV1ParticipantApi.md#listConversationParticipant) | **GET** /v1/Conversations/{ConversationSid}/Participants |  |
| [**listServiceConversationParticipant**](ConversationsV1ParticipantApi.md#listServiceConversationParticipant) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants |  |
| [**updateConversationParticipant**](ConversationsV1ParticipantApi.md#updateConversationParticipant) | **POST** /v1/Conversations/{ConversationSid}/Participants/{Sid} |  |
| [**updateServiceConversationParticipant**](ConversationsV1ParticipantApi.md#updateServiceConversationParticipant) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid} |  |


<a id="createConversationParticipant"></a>
# **createConversationParticipant**
> ConversationsV1ConversationConversationParticipant createConversationParticipant(conversationSid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, identity, messagingBindingAddress, messagingBindingProjectedAddress, messagingBindingProxyAddress, roleSid)



Add a new participant to the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ParticipantApi apiInstance = new ConversationsV1ParticipantApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    ConversationParticipantEnumWebhookEnabledType xTwilioWebhookEnabled = ConversationParticipantEnumWebhookEnabledType.fromValue("true"); // ConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was last updated.
    String identity = "identity_example"; // String | A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
    String messagingBindingAddress = "messagingBindingAddress_example"; // String | The address of the participant's device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address) is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).
    String messagingBindingProjectedAddress = "messagingBindingProjectedAddress_example"; // String | The address of the Twilio phone number that is used in Group MMS. Communication mask for the Conversation participant with Identity.
    String messagingBindingProxyAddress = "messagingBindingProxyAddress_example"; // String | The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).
    String roleSid = "roleSid_example"; // String | The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
    try {
      ConversationsV1ConversationConversationParticipant result = apiInstance.createConversationParticipant(conversationSid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, identity, messagingBindingAddress, messagingBindingProjectedAddress, messagingBindingProxyAddress, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ParticipantApi#createConversationParticipant");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | |
| **xTwilioWebhookEnabled** | **ConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date that this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date that this resource was last updated. | [optional] |
| **identity** | **String**| A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters. | [optional] |
| **messagingBindingAddress** | **String**| The address of the participant&#39;s device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address) is only null when the participant is interacting from an SDK endpoint (see the &#39;identity&#39; field). | [optional] |
| **messagingBindingProjectedAddress** | **String**| The address of the Twilio phone number that is used in Group MMS. Communication mask for the Conversation participant with Identity. | [optional] |
| **messagingBindingProxyAddress** | **String**| The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the &#39;identity&#39; field). | [optional] |
| **roleSid** | **String**| The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant. | [optional] |

### Return type

[**ConversationsV1ConversationConversationParticipant**](ConversationsV1ConversationConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="createServiceConversationParticipant"></a>
# **createServiceConversationParticipant**
> ConversationsV1ServiceServiceConversationServiceConversationParticipant createServiceConversationParticipant(chatServiceSid, conversationSid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, identity, messagingBindingAddress, messagingBindingProjectedAddress, messagingBindingProxyAddress, roleSid)



Add a new participant to the conversation in a specific service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ParticipantApi apiInstance = new ConversationsV1ParticipantApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    ServiceConversationParticipantEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceConversationParticipantEnumWebhookEnabledType.fromValue("true"); // ServiceConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set `{}` will be returned.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date on which this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date on which this resource was last updated.
    String identity = "identity_example"; // String | A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](https://www.twilio.com/docs/conversations/sdk-overview) to communicate. Limited to 256 characters.
    String messagingBindingAddress = "messagingBindingAddress_example"; // String | The address of the participant's device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with `proxy_address`) is only null when the participant is interacting from an SDK endpoint (see the `identity` field).
    String messagingBindingProjectedAddress = "messagingBindingProjectedAddress_example"; // String | The address of the Twilio phone number that is used in Group MMS.
    String messagingBindingProxyAddress = "messagingBindingProxyAddress_example"; // String | The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the `identity` field).
    String roleSid = "roleSid_example"; // String | The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
    try {
      ConversationsV1ServiceServiceConversationServiceConversationParticipant result = apiInstance.createServiceConversationParticipant(chatServiceSid, conversationSid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, identity, messagingBindingAddress, messagingBindingProjectedAddress, messagingBindingProxyAddress, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ParticipantApi#createServiceConversationParticipant");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | |
| **xTwilioWebhookEnabled** | **ServiceConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set &#x60;{}&#x60; will be returned. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date on which this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date on which this resource was last updated. | [optional] |
| **identity** | **String**| A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](https://www.twilio.com/docs/conversations/sdk-overview) to communicate. Limited to 256 characters. | [optional] |
| **messagingBindingAddress** | **String**| The address of the participant&#39;s device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with &#x60;proxy_address&#x60;) is only null when the participant is interacting from an SDK endpoint (see the &#x60;identity&#x60; field). | [optional] |
| **messagingBindingProjectedAddress** | **String**| The address of the Twilio phone number that is used in Group MMS. | [optional] |
| **messagingBindingProxyAddress** | **String**| The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the &#x60;identity&#x60; field). | [optional] |
| **roleSid** | **String**| The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationParticipant**](ConversationsV1ServiceServiceConversationServiceConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteConversationParticipant"></a>
# **deleteConversationParticipant**
> deleteConversationParticipant(conversationSid, sid, xTwilioWebhookEnabled)



Remove a participant from the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ParticipantApi apiInstance = new ConversationsV1ParticipantApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    ConversationParticipantEnumWebhookEnabledType xTwilioWebhookEnabled = ConversationParticipantEnumWebhookEnabledType.fromValue("true"); // ConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteConversationParticipant(conversationSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ParticipantApi#deleteConversationParticipant");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **xTwilioWebhookEnabled** | **ConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="deleteServiceConversationParticipant"></a>
# **deleteServiceConversationParticipant**
> deleteServiceConversationParticipant(chatServiceSid, conversationSid, sid, xTwilioWebhookEnabled)



Remove a participant from the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ParticipantApi apiInstance = new ConversationsV1ParticipantApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    ServiceConversationParticipantEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceConversationParticipantEnumWebhookEnabledType.fromValue("true"); // ServiceConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteServiceConversationParticipant(chatServiceSid, conversationSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ParticipantApi#deleteServiceConversationParticipant");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **xTwilioWebhookEnabled** | **ServiceConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="fetchConversationParticipant"></a>
# **fetchConversationParticipant**
> ConversationsV1ConversationConversationParticipant fetchConversationParticipant(conversationSid, sid)



Fetch a participant of the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ParticipantApi apiInstance = new ConversationsV1ParticipantApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant's `identity` rather than the SID.
    try {
      ConversationsV1ConversationConversationParticipant result = apiInstance.fetchConversationParticipant(conversationSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ParticipantApi#fetchConversationParticipant");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant&#39;s &#x60;identity&#x60; rather than the SID. | |

### Return type

[**ConversationsV1ConversationConversationParticipant**](ConversationsV1ConversationConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchServiceConversationParticipant"></a>
# **fetchServiceConversationParticipant**
> ConversationsV1ServiceServiceConversationServiceConversationParticipant fetchServiceConversationParticipant(chatServiceSid, conversationSid, sid)



Fetch a participant of the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ParticipantApi apiInstance = new ConversationsV1ParticipantApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant's `identity` rather than the SID.
    try {
      ConversationsV1ServiceServiceConversationServiceConversationParticipant result = apiInstance.fetchServiceConversationParticipant(chatServiceSid, conversationSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ParticipantApi#fetchServiceConversationParticipant");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant&#39;s &#x60;identity&#x60; rather than the SID. | |

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationParticipant**](ConversationsV1ServiceServiceConversationServiceConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listConversationParticipant"></a>
# **listConversationParticipant**
> ListConversationParticipantResponse listConversationParticipant(conversationSid, pageSize, page, pageToken)



Retrieve a list of all participants of the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ParticipantApi apiInstance = new ConversationsV1ParticipantApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListConversationParticipantResponse result = apiInstance.listConversationParticipant(conversationSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ParticipantApi#listConversationParticipant");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListConversationParticipantResponse**](ListConversationParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listServiceConversationParticipant"></a>
# **listServiceConversationParticipant**
> ListServiceConversationParticipantResponse listServiceConversationParticipant(chatServiceSid, conversationSid, pageSize, page, pageToken)



Retrieve a list of all participants of the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ParticipantApi apiInstance = new ConversationsV1ParticipantApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceConversationParticipantResponse result = apiInstance.listServiceConversationParticipant(chatServiceSid, conversationSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ParticipantApi#listServiceConversationParticipant");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceConversationParticipantResponse**](ListServiceConversationParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateConversationParticipant"></a>
# **updateConversationParticipant**
> ConversationsV1ConversationConversationParticipant updateConversationParticipant(conversationSid, sid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, identity, lastReadMessageIndex, lastReadTimestamp, messagingBindingProjectedAddress, messagingBindingProxyAddress, roleSid)



Update an existing participant in the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ParticipantApi apiInstance = new ConversationsV1ParticipantApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    ConversationParticipantEnumWebhookEnabledType xTwilioWebhookEnabled = ConversationParticipantEnumWebhookEnabledType.fromValue("true"); // ConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was last updated.
    String identity = "identity_example"; // String | A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
    Integer lastReadMessageIndex = 56; // Integer | Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
    String lastReadTimestamp = "lastReadTimestamp_example"; // String | Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
    String messagingBindingProjectedAddress = "messagingBindingProjectedAddress_example"; // String | The address of the Twilio phone number that is used in Group MMS. 'null' value will remove it.
    String messagingBindingProxyAddress = "messagingBindingProxyAddress_example"; // String | The address of the Twilio phone number that the participant is in contact with. 'null' value will remove it.
    String roleSid = "roleSid_example"; // String | The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
    try {
      ConversationsV1ConversationConversationParticipant result = apiInstance.updateConversationParticipant(conversationSid, sid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, identity, lastReadMessageIndex, lastReadTimestamp, messagingBindingProjectedAddress, messagingBindingProxyAddress, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ParticipantApi#updateConversationParticipant");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **xTwilioWebhookEnabled** | **ConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date that this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date that this resource was last updated. | [optional] |
| **identity** | **String**| A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters. | [optional] |
| **lastReadMessageIndex** | **Integer**| Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant. | [optional] |
| **lastReadTimestamp** | **String**| Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant. | [optional] |
| **messagingBindingProjectedAddress** | **String**| The address of the Twilio phone number that is used in Group MMS. &#39;null&#39; value will remove it. | [optional] |
| **messagingBindingProxyAddress** | **String**| The address of the Twilio phone number that the participant is in contact with. &#39;null&#39; value will remove it. | [optional] |
| **roleSid** | **String**| The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant. | [optional] |

### Return type

[**ConversationsV1ConversationConversationParticipant**](ConversationsV1ConversationConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateServiceConversationParticipant"></a>
# **updateServiceConversationParticipant**
> ConversationsV1ServiceServiceConversationServiceConversationParticipant updateServiceConversationParticipant(chatServiceSid, conversationSid, sid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, identity, lastReadMessageIndex, lastReadTimestamp, messagingBindingProjectedAddress, messagingBindingProxyAddress, roleSid)



Update an existing participant in the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ParticipantApi apiInstance = new ConversationsV1ParticipantApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    ServiceConversationParticipantEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceConversationParticipantEnumWebhookEnabledType.fromValue("true"); // ServiceConversationParticipantEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set `{}` will be returned.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date on which this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date on which this resource was last updated.
    String identity = "identity_example"; // String | A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](https://www.twilio.com/docs/conversations/sdk-overview) to communicate. Limited to 256 characters.
    Integer lastReadMessageIndex = 56; // Integer | Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
    String lastReadTimestamp = "lastReadTimestamp_example"; // String | Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
    String messagingBindingProjectedAddress = "messagingBindingProjectedAddress_example"; // String | The address of the Twilio phone number that is used in Group MMS. 'null' value will remove it.
    String messagingBindingProxyAddress = "messagingBindingProxyAddress_example"; // String | The address of the Twilio phone number that the participant is in contact with. 'null' value will remove it.
    String roleSid = "roleSid_example"; // String | The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
    try {
      ConversationsV1ServiceServiceConversationServiceConversationParticipant result = apiInstance.updateServiceConversationParticipant(chatServiceSid, conversationSid, sid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, identity, lastReadMessageIndex, lastReadTimestamp, messagingBindingProjectedAddress, messagingBindingProxyAddress, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ParticipantApi#updateServiceConversationParticipant");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **xTwilioWebhookEnabled** | **ServiceConversationParticipantEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set &#x60;{}&#x60; will be returned. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date on which this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date on which this resource was last updated. | [optional] |
| **identity** | **String**| A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](https://www.twilio.com/docs/conversations/sdk-overview) to communicate. Limited to 256 characters. | [optional] |
| **lastReadMessageIndex** | **Integer**| Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant. | [optional] |
| **lastReadTimestamp** | **String**| Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant. | [optional] |
| **messagingBindingProjectedAddress** | **String**| The address of the Twilio phone number that is used in Group MMS. &#39;null&#39; value will remove it. | [optional] |
| **messagingBindingProxyAddress** | **String**| The address of the Twilio phone number that the participant is in contact with. &#39;null&#39; value will remove it. | [optional] |
| **roleSid** | **String**| The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationParticipant**](ConversationsV1ServiceServiceConversationServiceConversationParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

