# ConversationsV1UserConversationApi

All URIs are relative to *https://conversations.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteServiceUserConversation**](ConversationsV1UserConversationApi.md#deleteServiceUserConversation) | **DELETE** /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid} |  |
| [**deleteUserConversation**](ConversationsV1UserConversationApi.md#deleteUserConversation) | **DELETE** /v1/Users/{UserSid}/Conversations/{ConversationSid} |  |
| [**fetchServiceUserConversation**](ConversationsV1UserConversationApi.md#fetchServiceUserConversation) | **GET** /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid} |  |
| [**fetchUserConversation**](ConversationsV1UserConversationApi.md#fetchUserConversation) | **GET** /v1/Users/{UserSid}/Conversations/{ConversationSid} |  |
| [**listServiceUserConversation**](ConversationsV1UserConversationApi.md#listServiceUserConversation) | **GET** /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations |  |
| [**listUserConversation**](ConversationsV1UserConversationApi.md#listUserConversation) | **GET** /v1/Users/{UserSid}/Conversations |  |
| [**updateServiceUserConversation**](ConversationsV1UserConversationApi.md#updateServiceUserConversation) | **POST** /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid} |  |
| [**updateUserConversation**](ConversationsV1UserConversationApi.md#updateUserConversation) | **POST** /v1/Users/{UserSid}/Conversations/{ConversationSid} |  |


<a id="deleteServiceUserConversation"></a>
# **deleteServiceUserConversation**
> deleteServiceUserConversation(chatServiceSid, userSid, conversationSid)



Delete a specific User Conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserConversationApi apiInstance = new ConversationsV1UserConversationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    String userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
    String conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    try {
      apiInstance.deleteServiceUserConversation(chatServiceSid, userSid, conversationSid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserConversationApi#deleteServiceUserConversation");
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
| **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | |
| **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | |

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

<a id="deleteUserConversation"></a>
# **deleteUserConversation**
> deleteUserConversation(userSid, conversationSid)



Delete a specific User Conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserConversationApi apiInstance = new ConversationsV1UserConversationApi(defaultClient);
    String userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
    String conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    try {
      apiInstance.deleteUserConversation(userSid, conversationSid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserConversationApi#deleteUserConversation");
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
| **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | |
| **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | |

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

<a id="fetchServiceUserConversation"></a>
# **fetchServiceUserConversation**
> ConversationsV1ServiceServiceUserServiceUserConversation fetchServiceUserConversation(chatServiceSid, userSid, conversationSid)



Fetch a specific User Conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserConversationApi apiInstance = new ConversationsV1UserConversationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    String userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
    String conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    try {
      ConversationsV1ServiceServiceUserServiceUserConversation result = apiInstance.fetchServiceUserConversation(chatServiceSid, userSid, conversationSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserConversationApi#fetchServiceUserConversation");
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
| **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | |
| **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | |

### Return type

[**ConversationsV1ServiceServiceUserServiceUserConversation**](ConversationsV1ServiceServiceUserServiceUserConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchUserConversation"></a>
# **fetchUserConversation**
> ConversationsV1UserUserConversation fetchUserConversation(userSid, conversationSid)



Fetch a specific User Conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserConversationApi apiInstance = new ConversationsV1UserConversationApi(defaultClient);
    String userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
    String conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    try {
      ConversationsV1UserUserConversation result = apiInstance.fetchUserConversation(userSid, conversationSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserConversationApi#fetchUserConversation");
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
| **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | |
| **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | |

### Return type

[**ConversationsV1UserUserConversation**](ConversationsV1UserUserConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listServiceUserConversation"></a>
# **listServiceUserConversation**
> ListServiceUserConversationResponse listServiceUserConversation(chatServiceSid, userSid, pageSize, page, pageToken)



Retrieve a list of all User Conversations for the User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserConversationApi apiInstance = new ConversationsV1UserConversationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    String userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceUserConversationResponse result = apiInstance.listServiceUserConversation(chatServiceSid, userSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserConversationApi#listServiceUserConversation");
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
| **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceUserConversationResponse**](ListServiceUserConversationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listUserConversation"></a>
# **listUserConversation**
> ListUserConversationResponse listUserConversation(userSid, pageSize, page, pageToken)



Retrieve a list of all User Conversations for the User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserConversationApi apiInstance = new ConversationsV1UserConversationApi(defaultClient);
    String userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListUserConversationResponse result = apiInstance.listUserConversation(userSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserConversationApi#listUserConversation");
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
| **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListUserConversationResponse**](ListUserConversationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateServiceUserConversation"></a>
# **updateServiceUserConversation**
> ConversationsV1ServiceServiceUserServiceUserConversation updateServiceUserConversation(chatServiceSid, userSid, conversationSid, lastReadMessageIndex, lastReadTimestamp, notificationLevel)



Update a specific User Conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserConversationApi apiInstance = new ConversationsV1UserConversationApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
    String userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
    String conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    Integer lastReadMessageIndex = 56; // Integer | The index of the last Message in the Conversation that the Participant has read.
    OffsetDateTime lastReadTimestamp = OffsetDateTime.now(); // OffsetDateTime | The date of the last message read in conversation by the user, given in ISO 8601 format.
    ServiceUserConversationEnumNotificationLevel notificationLevel = ServiceUserConversationEnumNotificationLevel.fromValue("default"); // ServiceUserConversationEnumNotificationLevel | 
    try {
      ConversationsV1ServiceServiceUserServiceUserConversation result = apiInstance.updateServiceUserConversation(chatServiceSid, userSid, conversationSid, lastReadMessageIndex, lastReadTimestamp, notificationLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserConversationApi#updateServiceUserConversation");
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
| **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | |
| **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | |
| **lastReadMessageIndex** | **Integer**| The index of the last Message in the Conversation that the Participant has read. | [optional] |
| **lastReadTimestamp** | **OffsetDateTime**| The date of the last message read in conversation by the user, given in ISO 8601 format. | [optional] |
| **notificationLevel** | **ServiceUserConversationEnumNotificationLevel**|  | [optional] [enum: default, muted] |

### Return type

[**ConversationsV1ServiceServiceUserServiceUserConversation**](ConversationsV1ServiceServiceUserServiceUserConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateUserConversation"></a>
# **updateUserConversation**
> ConversationsV1UserUserConversation updateUserConversation(userSid, conversationSid, lastReadMessageIndex, lastReadTimestamp, notificationLevel)



Update a specific User Conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserConversationApi apiInstance = new ConversationsV1UserConversationApi(defaultClient);
    String userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
    String conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
    Integer lastReadMessageIndex = 56; // Integer | The index of the last Message in the Conversation that the Participant has read.
    OffsetDateTime lastReadTimestamp = OffsetDateTime.now(); // OffsetDateTime | The date of the last message read in conversation by the user, given in ISO 8601 format.
    UserConversationEnumNotificationLevel notificationLevel = UserConversationEnumNotificationLevel.fromValue("default"); // UserConversationEnumNotificationLevel | 
    try {
      ConversationsV1UserUserConversation result = apiInstance.updateUserConversation(userSid, conversationSid, lastReadMessageIndex, lastReadTimestamp, notificationLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserConversationApi#updateUserConversation");
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
| **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | |
| **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | |
| **lastReadMessageIndex** | **Integer**| The index of the last Message in the Conversation that the Participant has read. | [optional] |
| **lastReadTimestamp** | **OffsetDateTime**| The date of the last message read in conversation by the user, given in ISO 8601 format. | [optional] |
| **notificationLevel** | **UserConversationEnumNotificationLevel**|  | [optional] [enum: default, muted] |

### Return type

[**ConversationsV1UserUserConversation**](ConversationsV1UserUserConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

