# ConversationsV1WebhookApi

All URIs are relative to *https://conversations.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createConversationScopedWebhook**](ConversationsV1WebhookApi.md#createConversationScopedWebhook) | **POST** /v1/Conversations/{ConversationSid}/Webhooks |  |
| [**createServiceConversationScopedWebhook**](ConversationsV1WebhookApi.md#createServiceConversationScopedWebhook) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks |  |
| [**deleteConversationScopedWebhook**](ConversationsV1WebhookApi.md#deleteConversationScopedWebhook) | **DELETE** /v1/Conversations/{ConversationSid}/Webhooks/{Sid} |  |
| [**deleteServiceConversationScopedWebhook**](ConversationsV1WebhookApi.md#deleteServiceConversationScopedWebhook) | **DELETE** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid} |  |
| [**fetchConfigurationWebhook**](ConversationsV1WebhookApi.md#fetchConfigurationWebhook) | **GET** /v1/Configuration/Webhooks |  |
| [**fetchConversationScopedWebhook**](ConversationsV1WebhookApi.md#fetchConversationScopedWebhook) | **GET** /v1/Conversations/{ConversationSid}/Webhooks/{Sid} |  |
| [**fetchServiceConversationScopedWebhook**](ConversationsV1WebhookApi.md#fetchServiceConversationScopedWebhook) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid} |  |
| [**fetchServiceWebhookConfiguration**](ConversationsV1WebhookApi.md#fetchServiceWebhookConfiguration) | **GET** /v1/Services/{ChatServiceSid}/Configuration/Webhooks |  |
| [**listConversationScopedWebhook**](ConversationsV1WebhookApi.md#listConversationScopedWebhook) | **GET** /v1/Conversations/{ConversationSid}/Webhooks |  |
| [**listServiceConversationScopedWebhook**](ConversationsV1WebhookApi.md#listServiceConversationScopedWebhook) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks |  |
| [**updateConfigurationWebhook**](ConversationsV1WebhookApi.md#updateConfigurationWebhook) | **POST** /v1/Configuration/Webhooks |  |
| [**updateConversationScopedWebhook**](ConversationsV1WebhookApi.md#updateConversationScopedWebhook) | **POST** /v1/Conversations/{ConversationSid}/Webhooks/{Sid} |  |
| [**updateServiceConversationScopedWebhook**](ConversationsV1WebhookApi.md#updateServiceConversationScopedWebhook) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid} |  |
| [**updateServiceWebhookConfiguration**](ConversationsV1WebhookApi.md#updateServiceWebhookConfiguration) | **POST** /v1/Services/{ChatServiceSid}/Configuration/Webhooks |  |


<a id="createConversationScopedWebhook"></a>
# **createConversationScopedWebhook**
> ConversationsV1ConversationConversationScopedWebhook createConversationScopedWebhook(conversationSid, target, configurationFilters, configurationFlowSid, configurationMethod, configurationReplayAfter, configurationTriggers, configurationUrl)



Create a new webhook scoped to the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    ConversationScopedWebhookEnumTarget target = ConversationScopedWebhookEnumTarget.fromValue("webhook"); // ConversationScopedWebhookEnumTarget | 
    List<String> configurationFilters = Arrays.asList(); // List<String> | The list of events, firing webhook event for this Conversation.
    String configurationFlowSid = "configurationFlowSid_example"; // String | The studio flow SID, where the webhook should be sent to.
    ConversationScopedWebhookEnumMethod configurationMethod = ConversationScopedWebhookEnumMethod.fromValue("GET"); // ConversationScopedWebhookEnumMethod | 
    Integer configurationReplayAfter = 56; // Integer | The message index for which and it's successors the webhook will be replayed. Not set by default
    List<String> configurationTriggers = Arrays.asList(); // List<String> | The list of keywords, firing webhook event for this Conversation.
    String configurationUrl = "configurationUrl_example"; // String | The absolute url the webhook request should be sent to.
    try {
      ConversationsV1ConversationConversationScopedWebhook result = apiInstance.createConversationScopedWebhook(conversationSid, target, configurationFilters, configurationFlowSid, configurationMethod, configurationReplayAfter, configurationTriggers, configurationUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#createConversationScopedWebhook");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | |
| **target** | **ConversationScopedWebhookEnumTarget**|  | [enum: webhook, trigger, studio] |
| **configurationFilters** | [**List&lt;String&gt;**](String.md)| The list of events, firing webhook event for this Conversation. | [optional] |
| **configurationFlowSid** | **String**| The studio flow SID, where the webhook should be sent to. | [optional] |
| **configurationMethod** | **ConversationScopedWebhookEnumMethod**|  | [optional] [enum: GET, POST] |
| **configurationReplayAfter** | **Integer**| The message index for which and it&#39;s successors the webhook will be replayed. Not set by default | [optional] |
| **configurationTriggers** | [**List&lt;String&gt;**](String.md)| The list of keywords, firing webhook event for this Conversation. | [optional] |
| **configurationUrl** | **String**| The absolute url the webhook request should be sent to. | [optional] |

### Return type

[**ConversationsV1ConversationConversationScopedWebhook**](ConversationsV1ConversationConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="createServiceConversationScopedWebhook"></a>
# **createServiceConversationScopedWebhook**
> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook createServiceConversationScopedWebhook(chatServiceSid, conversationSid, target, configurationFilters, configurationFlowSid, configurationMethod, configurationReplayAfter, configurationTriggers, configurationUrl)



Create a new webhook scoped to the conversation in a specific service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    ServiceConversationScopedWebhookEnumTarget target = ServiceConversationScopedWebhookEnumTarget.fromValue("webhook"); // ServiceConversationScopedWebhookEnumTarget | 
    List<String> configurationFilters = Arrays.asList(); // List<String> | The list of events, firing webhook event for this Conversation.
    String configurationFlowSid = "configurationFlowSid_example"; // String | The studio flow SID, where the webhook should be sent to.
    ServiceConversationScopedWebhookEnumMethod configurationMethod = ServiceConversationScopedWebhookEnumMethod.fromValue("GET"); // ServiceConversationScopedWebhookEnumMethod | 
    Integer configurationReplayAfter = 56; // Integer | The message index for which and it's successors the webhook will be replayed. Not set by default
    List<String> configurationTriggers = Arrays.asList(); // List<String> | The list of keywords, firing webhook event for this Conversation.
    String configurationUrl = "configurationUrl_example"; // String | The absolute url the webhook request should be sent to.
    try {
      ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook result = apiInstance.createServiceConversationScopedWebhook(chatServiceSid, conversationSid, target, configurationFilters, configurationFlowSid, configurationMethod, configurationReplayAfter, configurationTriggers, configurationUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#createServiceConversationScopedWebhook");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | |
| **target** | **ServiceConversationScopedWebhookEnumTarget**|  | [enum: webhook, trigger, studio] |
| **configurationFilters** | [**List&lt;String&gt;**](String.md)| The list of events, firing webhook event for this Conversation. | [optional] |
| **configurationFlowSid** | **String**| The studio flow SID, where the webhook should be sent to. | [optional] |
| **configurationMethod** | **ServiceConversationScopedWebhookEnumMethod**|  | [optional] [enum: GET, POST] |
| **configurationReplayAfter** | **Integer**| The message index for which and it&#39;s successors the webhook will be replayed. Not set by default | [optional] |
| **configurationTriggers** | [**List&lt;String&gt;**](String.md)| The list of keywords, firing webhook event for this Conversation. | [optional] |
| **configurationUrl** | **String**| The absolute url the webhook request should be sent to. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook**](ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteConversationScopedWebhook"></a>
# **deleteConversationScopedWebhook**
> deleteConversationScopedWebhook(conversationSid, sid)



Remove an existing webhook scoped to the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    try {
      apiInstance.deleteConversationScopedWebhook(conversationSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#deleteConversationScopedWebhook");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |

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

<a id="deleteServiceConversationScopedWebhook"></a>
# **deleteServiceConversationScopedWebhook**
> deleteServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid)



Remove an existing webhook scoped to the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    try {
      apiInstance.deleteServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#deleteServiceConversationScopedWebhook");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |

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

<a id="fetchConfigurationWebhook"></a>
# **fetchConfigurationWebhook**
> ConversationsV1ConfigurationConfigurationWebhook fetchConfigurationWebhook()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    try {
      ConversationsV1ConfigurationConfigurationWebhook result = apiInstance.fetchConfigurationWebhook();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#fetchConfigurationWebhook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConversationsV1ConfigurationConfigurationWebhook**](ConversationsV1ConfigurationConfigurationWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchConversationScopedWebhook"></a>
# **fetchConversationScopedWebhook**
> ConversationsV1ConversationConversationScopedWebhook fetchConversationScopedWebhook(conversationSid, sid)



Fetch the configuration of a conversation-scoped webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    try {
      ConversationsV1ConversationConversationScopedWebhook result = apiInstance.fetchConversationScopedWebhook(conversationSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#fetchConversationScopedWebhook");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |

### Return type

[**ConversationsV1ConversationConversationScopedWebhook**](ConversationsV1ConversationConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchServiceConversationScopedWebhook"></a>
# **fetchServiceConversationScopedWebhook**
> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook fetchServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid)



Fetch the configuration of a conversation-scoped webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    try {
      ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook result = apiInstance.fetchServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#fetchServiceConversationScopedWebhook");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook**](ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchServiceWebhookConfiguration"></a>
# **fetchServiceWebhookConfiguration**
> ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration fetchServiceWebhookConfiguration(chatServiceSid)



Fetch a specific service webhook configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
    try {
      ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration result = apiInstance.fetchServiceWebhookConfiguration(chatServiceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#fetchServiceWebhookConfiguration");
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
| **chatServiceSid** | **String**| The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to. | |

### Return type

[**ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration**](ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listConversationScopedWebhook"></a>
# **listConversationScopedWebhook**
> ListConversationScopedWebhookResponse listConversationScopedWebhook(conversationSid, pageSize, page, pageToken)



Retrieve a list of all webhooks scoped to the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListConversationScopedWebhookResponse result = apiInstance.listConversationScopedWebhook(conversationSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#listConversationScopedWebhook");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListConversationScopedWebhookResponse**](ListConversationScopedWebhookResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listServiceConversationScopedWebhook"></a>
# **listServiceConversationScopedWebhook**
> ListServiceConversationScopedWebhookResponse listServiceConversationScopedWebhook(chatServiceSid, conversationSid, pageSize, page, pageToken)



Retrieve a list of all webhooks scoped to the conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceConversationScopedWebhookResponse result = apiInstance.listServiceConversationScopedWebhook(chatServiceSid, conversationSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#listServiceConversationScopedWebhook");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceConversationScopedWebhookResponse**](ListServiceConversationScopedWebhookResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateConfigurationWebhook"></a>
# **updateConfigurationWebhook**
> ConversationsV1ConfigurationConfigurationWebhook updateConfigurationWebhook(filters, method, postWebhookUrl, preWebhookUrl, target)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    List<String> filters = Arrays.asList(); // List<String> | The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
    String method = "method_example"; // String | The HTTP method to be used when sending a webhook request.
    String postWebhookUrl = "postWebhookUrl_example"; // String | The absolute url the post-event webhook request should be sent to.
    String preWebhookUrl = "preWebhookUrl_example"; // String | The absolute url the pre-event webhook request should be sent to.
    ConfigurationWebhookEnumTarget target = ConfigurationWebhookEnumTarget.fromValue("webhook"); // ConfigurationWebhookEnumTarget | 
    try {
      ConversationsV1ConfigurationConfigurationWebhook result = apiInstance.updateConfigurationWebhook(filters, method, postWebhookUrl, preWebhookUrl, target);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#updateConfigurationWebhook");
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
| **filters** | [**List&lt;String&gt;**](String.md)| The list of webhook event triggers that are enabled for this Service: &#x60;onMessageAdded&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onParticipantRemoved&#x60; | [optional] |
| **method** | **String**| The HTTP method to be used when sending a webhook request. | [optional] |
| **postWebhookUrl** | **String**| The absolute url the post-event webhook request should be sent to. | [optional] |
| **preWebhookUrl** | **String**| The absolute url the pre-event webhook request should be sent to. | [optional] |
| **target** | **ConfigurationWebhookEnumTarget**|  | [optional] [enum: webhook, flex] |

### Return type

[**ConversationsV1ConfigurationConfigurationWebhook**](ConversationsV1ConfigurationConfigurationWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateConversationScopedWebhook"></a>
# **updateConversationScopedWebhook**
> ConversationsV1ConversationConversationScopedWebhook updateConversationScopedWebhook(conversationSid, sid, configurationFilters, configurationFlowSid, configurationMethod, configurationTriggers, configurationUrl)



Update an existing conversation-scoped webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    List<String> configurationFilters = Arrays.asList(); // List<String> | The list of events, firing webhook event for this Conversation.
    String configurationFlowSid = "configurationFlowSid_example"; // String | The studio flow SID, where the webhook should be sent to.
    ConversationScopedWebhookEnumMethod configurationMethod = ConversationScopedWebhookEnumMethod.fromValue("GET"); // ConversationScopedWebhookEnumMethod | 
    List<String> configurationTriggers = Arrays.asList(); // List<String> | The list of keywords, firing webhook event for this Conversation.
    String configurationUrl = "configurationUrl_example"; // String | The absolute url the webhook request should be sent to.
    try {
      ConversationsV1ConversationConversationScopedWebhook result = apiInstance.updateConversationScopedWebhook(conversationSid, sid, configurationFilters, configurationFlowSid, configurationMethod, configurationTriggers, configurationUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#updateConversationScopedWebhook");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **configurationFilters** | [**List&lt;String&gt;**](String.md)| The list of events, firing webhook event for this Conversation. | [optional] |
| **configurationFlowSid** | **String**| The studio flow SID, where the webhook should be sent to. | [optional] |
| **configurationMethod** | **ConversationScopedWebhookEnumMethod**|  | [optional] [enum: GET, POST] |
| **configurationTriggers** | [**List&lt;String&gt;**](String.md)| The list of keywords, firing webhook event for this Conversation. | [optional] |
| **configurationUrl** | **String**| The absolute url the webhook request should be sent to. | [optional] |

### Return type

[**ConversationsV1ConversationConversationScopedWebhook**](ConversationsV1ConversationConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateServiceConversationScopedWebhook"></a>
# **updateServiceConversationScopedWebhook**
> ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook updateServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid, configurationFilters, configurationFlowSid, configurationMethod, configurationTriggers, configurationUrl)



Update an existing conversation-scoped webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
    String conversationSid = "conversationSid_example"; // String | The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource.
    List<String> configurationFilters = Arrays.asList(); // List<String> | The list of events, firing webhook event for this Conversation.
    String configurationFlowSid = "configurationFlowSid_example"; // String | The studio flow SID, where the webhook should be sent to.
    ServiceConversationScopedWebhookEnumMethod configurationMethod = ServiceConversationScopedWebhookEnumMethod.fromValue("GET"); // ServiceConversationScopedWebhookEnumMethod | 
    List<String> configurationTriggers = Arrays.asList(); // List<String> | The list of keywords, firing webhook event for this Conversation.
    String configurationUrl = "configurationUrl_example"; // String | The absolute url the webhook request should be sent to.
    try {
      ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook result = apiInstance.updateServiceConversationScopedWebhook(chatServiceSid, conversationSid, sid, configurationFilters, configurationFlowSid, configurationMethod, configurationTriggers, configurationUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#updateServiceConversationScopedWebhook");
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
| **conversationSid** | **String**| The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this webhook. | |
| **sid** | **String**| A 34 character string that uniquely identifies this resource. | |
| **configurationFilters** | [**List&lt;String&gt;**](String.md)| The list of events, firing webhook event for this Conversation. | [optional] |
| **configurationFlowSid** | **String**| The studio flow SID, where the webhook should be sent to. | [optional] |
| **configurationMethod** | **ServiceConversationScopedWebhookEnumMethod**|  | [optional] [enum: GET, POST] |
| **configurationTriggers** | [**List&lt;String&gt;**](String.md)| The list of keywords, firing webhook event for this Conversation. | [optional] |
| **configurationUrl** | **String**| The absolute url the webhook request should be sent to. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook**](ConversationsV1ServiceServiceConversationServiceConversationScopedWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateServiceWebhookConfiguration"></a>
# **updateServiceWebhookConfiguration**
> ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration updateServiceWebhookConfiguration(chatServiceSid, filters, method, postWebhookUrl, preWebhookUrl)



Update a specific Webhook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1WebhookApi apiInstance = new ConversationsV1WebhookApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
    List<String> filters = Arrays.asList(); // List<String> | The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are `onParticipantAdd`, `onParticipantAdded`, `onDeliveryUpdated`, `onConversationUpdated`, `onConversationRemove`, `onParticipantRemove`, `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`, `onParticipantUpdated`, `onConversationAdded`, `onMessageAdded`, `onConversationAdd`, `onConversationRemoved`, `onParticipantUpdate`, `onMessageRemove`, `onMessageUpdated`, `onParticipantRemoved`, `onMessageUpdate` or `onConversationStateUpdated`.
    String method = "method_example"; // String | The HTTP method to be used when sending a webhook request. One of `GET` or `POST`.
    URI postWebhookUrl = new URI(); // URI | The absolute url the post-event webhook request should be sent to.
    URI preWebhookUrl = new URI(); // URI | The absolute url the pre-event webhook request should be sent to.
    try {
      ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration result = apiInstance.updateServiceWebhookConfiguration(chatServiceSid, filters, method, postWebhookUrl, preWebhookUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1WebhookApi#updateServiceWebhookConfiguration");
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
| **chatServiceSid** | **String**| The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to. | |
| **filters** | [**List&lt;String&gt;**](String.md)| The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are &#x60;onParticipantAdd&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onDeliveryUpdated&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationRemove&#x60;, &#x60;onParticipantRemove&#x60;, &#x60;onConversationUpdate&#x60;, &#x60;onMessageAdd&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onConversationAdded&#x60;, &#x60;onMessageAdded&#x60;, &#x60;onConversationAdd&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantUpdate&#x60;, &#x60;onMessageRemove&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onParticipantRemoved&#x60;, &#x60;onMessageUpdate&#x60; or &#x60;onConversationStateUpdated&#x60;. | [optional] |
| **method** | **String**| The HTTP method to be used when sending a webhook request. One of &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] |
| **postWebhookUrl** | **URI**| The absolute url the post-event webhook request should be sent to. | [optional] |
| **preWebhookUrl** | **URI**| The absolute url the pre-event webhook request should be sent to. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration**](ConversationsV1ServiceServiceConfigurationServiceWebhookConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

