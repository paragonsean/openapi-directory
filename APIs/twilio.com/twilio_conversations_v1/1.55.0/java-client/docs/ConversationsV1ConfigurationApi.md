# ConversationsV1ConfigurationApi

All URIs are relative to *https://conversations.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchConfiguration**](ConversationsV1ConfigurationApi.md#fetchConfiguration) | **GET** /v1/Configuration |  |
| [**fetchServiceConfiguration**](ConversationsV1ConfigurationApi.md#fetchServiceConfiguration) | **GET** /v1/Services/{ChatServiceSid}/Configuration |  |
| [**updateConfiguration**](ConversationsV1ConfigurationApi.md#updateConfiguration) | **POST** /v1/Configuration |  |
| [**updateServiceConfiguration**](ConversationsV1ConfigurationApi.md#updateServiceConfiguration) | **POST** /v1/Services/{ChatServiceSid}/Configuration |  |


<a id="fetchConfiguration"></a>
# **fetchConfiguration**
> ConversationsV1Configuration fetchConfiguration()



Fetch the global configuration of conversations on your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConfigurationApi apiInstance = new ConversationsV1ConfigurationApi(defaultClient);
    try {
      ConversationsV1Configuration result = apiInstance.fetchConfiguration();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConfigurationApi#fetchConfiguration");
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

[**ConversationsV1Configuration**](ConversationsV1Configuration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchServiceConfiguration"></a>
# **fetchServiceConfiguration**
> ConversationsV1ServiceServiceConfiguration fetchServiceConfiguration(chatServiceSid)



Fetch the configuration of a conversation service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConfigurationApi apiInstance = new ConversationsV1ConfigurationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the Service configuration resource to fetch.
    try {
      ConversationsV1ServiceServiceConfiguration result = apiInstance.fetchServiceConfiguration(chatServiceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConfigurationApi#fetchServiceConfiguration");
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
| **chatServiceSid** | **String**| The SID of the Service configuration resource to fetch. | |

### Return type

[**ConversationsV1ServiceServiceConfiguration**](ConversationsV1ServiceServiceConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateConfiguration"></a>
# **updateConfiguration**
> ConversationsV1Configuration updateConfiguration(defaultChatServiceSid, defaultClosedTimer, defaultInactiveTimer, defaultMessagingServiceSid)



Update the global configuration of conversations on your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConfigurationApi apiInstance = new ConversationsV1ConfigurationApi(defaultClient);
    String defaultChatServiceSid = "defaultChatServiceSid_example"; // String | The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to use when creating a conversation.
    String defaultClosedTimer = "defaultClosedTimer_example"; // String | Default ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
    String defaultInactiveTimer = "defaultInactiveTimer_example"; // String | Default ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
    String defaultMessagingServiceSid = "defaultMessagingServiceSid_example"; // String | The SID of the default [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to use when creating a conversation.
    try {
      ConversationsV1Configuration result = apiInstance.updateConfiguration(defaultChatServiceSid, defaultClosedTimer, defaultInactiveTimer, defaultMessagingServiceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConfigurationApi#updateConfiguration");
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
| **defaultChatServiceSid** | **String**| The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to use when creating a conversation. | [optional] |
| **defaultClosedTimer** | **String**| Default ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] |
| **defaultInactiveTimer** | **String**| Default ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] |
| **defaultMessagingServiceSid** | **String**| The SID of the default [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to use when creating a conversation. | [optional] |

### Return type

[**ConversationsV1Configuration**](ConversationsV1Configuration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateServiceConfiguration"></a>
# **updateServiceConfiguration**
> ConversationsV1ServiceServiceConfiguration updateServiceConfiguration(chatServiceSid, defaultChatServiceRoleSid, defaultConversationCreatorRoleSid, defaultConversationRoleSid, reachabilityEnabled)



Update configuration settings of a conversation service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1ConfigurationApi apiInstance = new ConversationsV1ConfigurationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the Service configuration resource to update.
    String defaultChatServiceRoleSid = "defaultChatServiceRoleSid_example"; // String | The service-level role assigned to users when they are added to the service. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
    String defaultConversationCreatorRoleSid = "defaultConversationCreatorRoleSid_example"; // String | The conversation-level role assigned to a conversation creator when they join a new conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
    String defaultConversationRoleSid = "defaultConversationRoleSid_example"; // String | The conversation-level role assigned to users when they are added to a conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
    Boolean reachabilityEnabled = true; // Boolean | Whether the [Reachability Indicator](https://www.twilio.com/docs/conversations/reachability) is enabled for this Conversations Service. The default is `false`.
    try {
      ConversationsV1ServiceServiceConfiguration result = apiInstance.updateServiceConfiguration(chatServiceSid, defaultChatServiceRoleSid, defaultConversationCreatorRoleSid, defaultConversationRoleSid, reachabilityEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1ConfigurationApi#updateServiceConfiguration");
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
| **chatServiceSid** | **String**| The SID of the Service configuration resource to update. | |
| **defaultChatServiceRoleSid** | **String**| The service-level role assigned to users when they are added to the service. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles. | [optional] |
| **defaultConversationCreatorRoleSid** | **String**| The conversation-level role assigned to a conversation creator when they join a new conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles. | [optional] |
| **defaultConversationRoleSid** | **String**| The conversation-level role assigned to users when they are added to a conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles. | [optional] |
| **reachabilityEnabled** | **Boolean**| Whether the [Reachability Indicator](https://www.twilio.com/docs/conversations/reachability) is enabled for this Conversations Service. The default is &#x60;false&#x60;. | [optional] |

### Return type

[**ConversationsV1ServiceServiceConfiguration**](ConversationsV1ServiceServiceConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

