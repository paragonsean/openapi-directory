# ConversationsV1ConversationApi

All URIs are relative to *https://conversations.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createConversation**](ConversationsV1ConversationApi.md#createConversation) | **POST** /v1/Conversations |  |
| [**createServiceConversation**](ConversationsV1ConversationApi.md#createServiceConversation) | **POST** /v1/Services/{ChatServiceSid}/Conversations |  |
| [**deleteConversation**](ConversationsV1ConversationApi.md#deleteConversation) | **DELETE** /v1/Conversations/{Sid} |  |
| [**deleteServiceConversation**](ConversationsV1ConversationApi.md#deleteServiceConversation) | **DELETE** /v1/Services/{ChatServiceSid}/Conversations/{Sid} |  |
| [**fetchConversation**](ConversationsV1ConversationApi.md#fetchConversation) | **GET** /v1/Conversations/{Sid} |  |
| [**fetchServiceConversation**](ConversationsV1ConversationApi.md#fetchServiceConversation) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{Sid} |  |
| [**listConversation**](ConversationsV1ConversationApi.md#listConversation) | **GET** /v1/Conversations |  |
| [**listServiceConversation**](ConversationsV1ConversationApi.md#listServiceConversation) | **GET** /v1/Services/{ChatServiceSid}/Conversations |  |
| [**updateConversation**](ConversationsV1ConversationApi.md#updateConversation) | **POST** /v1/Conversations/{Sid} |  |
| [**updateServiceConversation**](ConversationsV1ConversationApi.md#updateServiceConversation) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{Sid} |  |


<a id="createConversation"></a>
# **createConversation**
> ConversationsV1Conversation createConversation(xTwilioWebhookEnabled, attributes, bindingsEmailAddress, bindingsEmailName, dateCreated, dateUpdated, friendlyName, messagingServiceSid, state, timersClosed, timersInactive, uniqueName)



Create a new conversation in your account&#39;s default service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConversationApi apiInstance = new ConversationsV1ConversationApi(defaultClient);
    ConversationEnumWebhookEnabledType xTwilioWebhookEnabled = ConversationEnumWebhookEnabledType.fromValue("true"); // ConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
    String bindingsEmailAddress = "bindingsEmailAddress_example"; // String | The default email address that will be used when sending outbound emails in this conversation.
    String bindingsEmailName = "bindingsEmailName_example"; // String | The default name that will be used when sending outbound emails in this conversation.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was last updated.
    String friendlyName = "friendlyName_example"; // String | The human-readable name of this conversation, limited to 256 characters. Optional.
    String messagingServiceSid = "messagingServiceSid_example"; // String | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
    ConversationEnumState state = ConversationEnumState.fromValue("inactive"); // ConversationEnumState | 
    String timersClosed = "timersClosed_example"; // String | ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
    String timersInactive = "timersInactive_example"; // String | ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
    try {
      ConversationsV1Conversation result = apiInstance.createConversation(xTwilioWebhookEnabled, attributes, bindingsEmailAddress, bindingsEmailName, dateCreated, dateUpdated, friendlyName, messagingServiceSid, state, timersClosed, timersInactive, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConversationApi#createConversation");
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
| **xTwilioWebhookEnabled** | **ConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] |
| **bindingsEmailAddress** | **String**| The default email address that will be used when sending outbound emails in this conversation. | [optional] |
| **bindingsEmailName** | **String**| The default name that will be used when sending outbound emails in this conversation. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date that this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date that this resource was last updated. | [optional] |
| **friendlyName** | **String**| The human-readable name of this conversation, limited to 256 characters. Optional. | [optional] |
| **messagingServiceSid** | **String**| The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to. | [optional] |
| **state** | **ConversationEnumState**|  | [optional] [enum: inactive, active, closed] |
| **timersClosed** | **String**| ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] |
| **timersInactive** | **String**| ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. | [optional] |

### Return type

[**ConversationsV1Conversation**](ConversationsV1Conversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="createServiceConversation"></a>
# **createServiceConversation**
> ConversationsV1ServiceServiceConversation createServiceConversation(chatServiceSid, xTwilioWebhookEnabled, attributes, bindingsEmailAddress, bindingsEmailName, dateCreated, dateUpdated, friendlyName, messagingServiceSid, state, timersClosed, timersInactive, uniqueName)



Create a new conversation in your service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConversationApi apiInstance = new ConversationsV1ConversationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    ServiceConversationEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceConversationEnumWebhookEnabledType.fromValue("true"); // ServiceConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
    String bindingsEmailAddress = "bindingsEmailAddress_example"; // String | The default email address that will be used when sending outbound emails in this conversation.
    String bindingsEmailName = "bindingsEmailName_example"; // String | The default name that will be used when sending outbound emails in this conversation.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was last updated.
    String friendlyName = "friendlyName_example"; // String | The human-readable name of this conversation, limited to 256 characters. Optional.
    String messagingServiceSid = "messagingServiceSid_example"; // String | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
    ServiceConversationEnumState state = ServiceConversationEnumState.fromValue("inactive"); // ServiceConversationEnumState | 
    String timersClosed = "timersClosed_example"; // String | ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
    String timersInactive = "timersInactive_example"; // String | ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
    try {
      ConversationsV1ServiceServiceConversation result = apiInstance.createServiceConversation(chatServiceSid, xTwilioWebhookEnabled, attributes, bindingsEmailAddress, bindingsEmailName, dateCreated, dateUpdated, friendlyName, messagingServiceSid, state, timersClosed, timersInactive, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConversationApi#createServiceConversation");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with. | |
| **xTwilioWebhookEnabled** | **ServiceConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] |
| **bindingsEmailAddress** | **String**| The default email address that will be used when sending outbound emails in this conversation. | [optional] |
| **bindingsEmailName** | **String**| The default name that will be used when sending outbound emails in this conversation. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date that this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date that this resource was last updated. | [optional] |
| **friendlyName** | **String**| The human-readable name of this conversation, limited to 256 characters. Optional. | [optional] |
| **messagingServiceSid** | **String**| The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to. | [optional] |
| **state** | **ServiceConversationEnumState**|  | [optional] [enum: inactive, active, closed] |
| **timersClosed** | **String**| ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] |
| **timersInactive** | **String**| ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConversation**](ConversationsV1ServiceServiceConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteConversation"></a>
# **deleteConversation**
> deleteConversation(sid, xTwilioWebhookEnabled)



Remove a conversation from your account&#39;s default service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConversationApi apiInstance = new ConversationsV1ConversationApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
    ConversationEnumWebhookEnabledType xTwilioWebhookEnabled = ConversationEnumWebhookEnabledType.fromValue("true"); // ConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteConversation(sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConversationApi#deleteConversation");
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
| **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | |
| **xTwilioWebhookEnabled** | **ConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="deleteServiceConversation"></a>
# **deleteServiceConversation**
> deleteServiceConversation(chatServiceSid, sid, xTwilioWebhookEnabled)



Remove a conversation from your service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConversationApi apiInstance = new ConversationsV1ConversationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
    ServiceConversationEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceConversationEnumWebhookEnabledType.fromValue("true"); // ServiceConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteServiceConversation(chatServiceSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConversationApi#deleteServiceConversation");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | |
| **xTwilioWebhookEnabled** | **ServiceConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="fetchConversation"></a>
# **fetchConversation**
> ConversationsV1Conversation fetchConversation(sid)



Fetch a conversation from your account&#39;s default service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConversationApi apiInstance = new ConversationsV1ConversationApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
    try {
      ConversationsV1Conversation result = apiInstance.fetchConversation(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConversationApi#fetchConversation");
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
| **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | |

### Return type

[**ConversationsV1Conversation**](ConversationsV1Conversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchServiceConversation"></a>
# **fetchServiceConversation**
> ConversationsV1ServiceServiceConversation fetchServiceConversation(chatServiceSid, sid)



Fetch a conversation from your service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConversationApi apiInstance = new ConversationsV1ConversationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
    try {
      ConversationsV1ServiceServiceConversation result = apiInstance.fetchServiceConversation(chatServiceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConversationApi#fetchServiceConversation");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | |

### Return type

[**ConversationsV1ServiceServiceConversation**](ConversationsV1ServiceServiceConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listConversation"></a>
# **listConversation**
> ListConversationResponse listConversation(startDate, endDate, state, pageSize, page, pageToken)



Retrieve a list of conversations in your account&#39;s default service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConversationApi apiInstance = new ConversationsV1ConversationApi(defaultClient);
    String startDate = "startDate_example"; // String | Start date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the start time of the date is used (YYYY-MM-DDT00:00:00Z). Can be combined with other filters.
    String endDate = "endDate_example"; // String | End date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the end time of the date is used (YYYY-MM-DDT23:59:59Z). Can be combined with other filters.
    ConversationEnumState state = ConversationEnumState.fromValue("inactive"); // ConversationEnumState | State for sorting and filtering list of Conversations. Can be `active`, `inactive` or `closed`
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListConversationResponse result = apiInstance.listConversation(startDate, endDate, state, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConversationApi#listConversation");
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
| **startDate** | **String**| Start date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the start time of the date is used (YYYY-MM-DDT00:00:00Z). Can be combined with other filters. | [optional] |
| **endDate** | **String**| End date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the end time of the date is used (YYYY-MM-DDT23:59:59Z). Can be combined with other filters. | [optional] |
| **state** | **ConversationEnumState**| State for sorting and filtering list of Conversations. Can be &#x60;active&#x60;, &#x60;inactive&#x60; or &#x60;closed&#x60; | [optional] [enum: inactive, active, closed] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListConversationResponse**](ListConversationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listServiceConversation"></a>
# **listServiceConversation**
> ListServiceConversationResponse listServiceConversation(chatServiceSid, startDate, endDate, state, pageSize, page, pageToken)



Retrieve a list of conversations in your service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConversationApi apiInstance = new ConversationsV1ConversationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    String startDate = "startDate_example"; // String | Start date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the start time of the date is used (YYYY-MM-DDT00:00:00Z). Can be combined with other filters.
    String endDate = "endDate_example"; // String | End date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the end time of the date is used (YYYY-MM-DDT23:59:59Z). Can be combined with other filters.
    ServiceConversationEnumState state = ServiceConversationEnumState.fromValue("inactive"); // ServiceConversationEnumState | State for sorting and filtering list of Conversations. Can be `active`, `inactive` or `closed`
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceConversationResponse result = apiInstance.listServiceConversation(chatServiceSid, startDate, endDate, state, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConversationApi#listServiceConversation");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with. | |
| **startDate** | **String**| Start date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the start time of the date is used (YYYY-MM-DDT00:00:00Z). Can be combined with other filters. | [optional] |
| **endDate** | **String**| End date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the end time of the date is used (YYYY-MM-DDT23:59:59Z). Can be combined with other filters. | [optional] |
| **state** | **ServiceConversationEnumState**| State for sorting and filtering list of Conversations. Can be &#x60;active&#x60;, &#x60;inactive&#x60; or &#x60;closed&#x60; | [optional] [enum: inactive, active, closed] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceConversationResponse**](ListServiceConversationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateConversation"></a>
# **updateConversation**
> ConversationsV1Conversation updateConversation(sid, xTwilioWebhookEnabled, attributes, bindingsEmailAddress, bindingsEmailName, dateCreated, dateUpdated, friendlyName, messagingServiceSid, state, timersClosed, timersInactive, uniqueName)



Update an existing conversation in your account&#39;s default service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConversationApi apiInstance = new ConversationsV1ConversationApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
    ConversationEnumWebhookEnabledType xTwilioWebhookEnabled = ConversationEnumWebhookEnabledType.fromValue("true"); // ConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
    String bindingsEmailAddress = "bindingsEmailAddress_example"; // String | The default email address that will be used when sending outbound emails in this conversation.
    String bindingsEmailName = "bindingsEmailName_example"; // String | The default name that will be used when sending outbound emails in this conversation.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was last updated.
    String friendlyName = "friendlyName_example"; // String | The human-readable name of this conversation, limited to 256 characters. Optional.
    String messagingServiceSid = "messagingServiceSid_example"; // String | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
    ConversationEnumState state = ConversationEnumState.fromValue("inactive"); // ConversationEnumState | 
    String timersClosed = "timersClosed_example"; // String | ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
    String timersInactive = "timersInactive_example"; // String | ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
    try {
      ConversationsV1Conversation result = apiInstance.updateConversation(sid, xTwilioWebhookEnabled, attributes, bindingsEmailAddress, bindingsEmailName, dateCreated, dateUpdated, friendlyName, messagingServiceSid, state, timersClosed, timersInactive, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConversationApi#updateConversation");
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
| **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | |
| **xTwilioWebhookEnabled** | **ConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] |
| **bindingsEmailAddress** | **String**| The default email address that will be used when sending outbound emails in this conversation. | [optional] |
| **bindingsEmailName** | **String**| The default name that will be used when sending outbound emails in this conversation. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date that this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date that this resource was last updated. | [optional] |
| **friendlyName** | **String**| The human-readable name of this conversation, limited to 256 characters. Optional. | [optional] |
| **messagingServiceSid** | **String**| The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to. | [optional] |
| **state** | **ConversationEnumState**|  | [optional] [enum: inactive, active, closed] |
| **timersClosed** | **String**| ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] |
| **timersInactive** | **String**| ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. | [optional] |

### Return type

[**ConversationsV1Conversation**](ConversationsV1Conversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateServiceConversation"></a>
# **updateServiceConversation**
> ConversationsV1ServiceServiceConversation updateServiceConversation(chatServiceSid, sid, xTwilioWebhookEnabled, attributes, bindingsEmailAddress, bindingsEmailName, dateCreated, dateUpdated, friendlyName, messagingServiceSid, state, timersClosed, timersInactive, uniqueName)



Update an existing conversation in your service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConversationApi apiInstance = new ConversationsV1ConversationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
    ServiceConversationEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceConversationEnumWebhookEnabledType.fromValue("true"); // ServiceConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
    String bindingsEmailAddress = "bindingsEmailAddress_example"; // String | The default email address that will be used when sending outbound emails in this conversation.
    String bindingsEmailName = "bindingsEmailName_example"; // String | The default name that will be used when sending outbound emails in this conversation.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was created.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date that this resource was last updated.
    String friendlyName = "friendlyName_example"; // String | The human-readable name of this conversation, limited to 256 characters. Optional.
    String messagingServiceSid = "messagingServiceSid_example"; // String | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
    ServiceConversationEnumState state = ServiceConversationEnumState.fromValue("inactive"); // ServiceConversationEnumState | 
    String timersClosed = "timersClosed_example"; // String | ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
    String timersInactive = "timersInactive_example"; // String | ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
    try {
      ConversationsV1ServiceServiceConversation result = apiInstance.updateServiceConversation(chatServiceSid, sid, xTwilioWebhookEnabled, attributes, bindingsEmailAddress, bindingsEmailName, dateCreated, dateUpdated, friendlyName, messagingServiceSid, state, timersClosed, timersInactive, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConversationApi#updateServiceConversation");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | |
| **xTwilioWebhookEnabled** | **ServiceConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] |
| **bindingsEmailAddress** | **String**| The default email address that will be used when sending outbound emails in this conversation. | [optional] |
| **bindingsEmailName** | **String**| The default name that will be used when sending outbound emails in this conversation. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date that this resource was created. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date that this resource was last updated. | [optional] |
| **friendlyName** | **String**| The human-readable name of this conversation, limited to 256 characters. Optional. | [optional] |
| **messagingServiceSid** | **String**| The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to. | [optional] |
| **state** | **ServiceConversationEnumState**|  | [optional] [enum: inactive, active, closed] |
| **timersClosed** | **String**| ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] |
| **timersInactive** | **String**| ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConversation**](ConversationsV1ServiceServiceConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

