# ConversationsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**conversationsArchive**](ConversationsApi.md#conversationsArchive) | **POST** /conversations.archive |  |
| [**conversationsClose**](ConversationsApi.md#conversationsClose) | **POST** /conversations.close |  |
| [**conversationsCreate**](ConversationsApi.md#conversationsCreate) | **POST** /conversations.create |  |
| [**conversationsHistory**](ConversationsApi.md#conversationsHistory) | **GET** /conversations.history |  |
| [**conversationsInfo**](ConversationsApi.md#conversationsInfo) | **GET** /conversations.info |  |
| [**conversationsInvite**](ConversationsApi.md#conversationsInvite) | **POST** /conversations.invite |  |
| [**conversationsJoin**](ConversationsApi.md#conversationsJoin) | **POST** /conversations.join |  |
| [**conversationsKick**](ConversationsApi.md#conversationsKick) | **POST** /conversations.kick |  |
| [**conversationsLeave**](ConversationsApi.md#conversationsLeave) | **POST** /conversations.leave |  |
| [**conversationsList**](ConversationsApi.md#conversationsList) | **GET** /conversations.list |  |
| [**conversationsMark**](ConversationsApi.md#conversationsMark) | **POST** /conversations.mark |  |
| [**conversationsMembers**](ConversationsApi.md#conversationsMembers) | **GET** /conversations.members |  |
| [**conversationsOpen**](ConversationsApi.md#conversationsOpen) | **POST** /conversations.open |  |
| [**conversationsRename**](ConversationsApi.md#conversationsRename) | **POST** /conversations.rename |  |
| [**conversationsReplies**](ConversationsApi.md#conversationsReplies) | **GET** /conversations.replies |  |
| [**conversationsSetPurpose**](ConversationsApi.md#conversationsSetPurpose) | **POST** /conversations.setPurpose |  |
| [**conversationsSetTopic**](ConversationsApi.md#conversationsSetTopic) | **POST** /conversations.setTopic |  |
| [**conversationsUnarchive**](ConversationsApi.md#conversationsUnarchive) | **POST** /conversations.unarchive |  |


<a id="conversationsArchive"></a>
# **conversationsArchive**
> ConversationsArchiveSuccessSchema conversationsArchive(token, channel)



Archives a conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | ID of conversation to archive
    try {
      ConversationsArchiveSuccessSchema result = apiInstance.conversationsArchive(token, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsArchive");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| ID of conversation to archive | [optional] |

### Return type

[**ConversationsArchiveSuccessSchema**](ConversationsArchiveSuccessSchema.md)

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

<a id="conversationsClose"></a>
# **conversationsClose**
> ConversationsCloseSuccessSchema conversationsClose(token, channel)



Closes a direct message or multi-person direct message.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | Conversation to close.
    try {
      ConversationsCloseSuccessSchema result = apiInstance.conversationsClose(token, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsClose");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| Conversation to close. | [optional] |

### Return type

[**ConversationsCloseSuccessSchema**](ConversationsCloseSuccessSchema.md)

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

<a id="conversationsCreate"></a>
# **conversationsCreate**
> ConversationsCreateSuccessSchema conversationsCreate(token, isPrivate, name)



Initiates a public or private channel-based conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    Boolean isPrivate = true; // Boolean | Create a private channel instead of a public one
    String name = "name_example"; // String | Name of the public or private channel to create
    try {
      ConversationsCreateSuccessSchema result = apiInstance.conversationsCreate(token, isPrivate, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsCreate");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **isPrivate** | **Boolean**| Create a private channel instead of a public one | [optional] |
| **name** | **String**| Name of the public or private channel to create | [optional] |

### Return type

[**ConversationsCreateSuccessSchema**](ConversationsCreateSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If successful, the command returns a rather stark [conversation object](/types/conversation) |  -  |
| **0** | Typical error response when name already in use |  -  |

<a id="conversationsHistory"></a>
# **conversationsHistory**
> ConversationsHistorySuccessSchema conversationsHistory(token, channel, latest, oldest, inclusive, limit, cursor)



Fetches a conversation&#39;s history of messages and events.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:history`
    String channel = "channel_example"; // String | Conversation ID to fetch history for.
    BigDecimal latest = new BigDecimal(78); // BigDecimal | End of time range of messages to include in results.
    BigDecimal oldest = new BigDecimal(78); // BigDecimal | Start of time range of messages to include in results.
    Boolean inclusive = true; // Boolean | Include messages with latest or oldest timestamp in results only when either timestamp is specified.
    Integer limit = 56; // Integer | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    try {
      ConversationsHistorySuccessSchema result = apiInstance.conversationsHistory(token, channel, latest, oldest, inclusive, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsHistory");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:history&#x60; | [optional] |
| **channel** | **String**| Conversation ID to fetch history for. | [optional] |
| **latest** | **BigDecimal**| End of time range of messages to include in results. | [optional] |
| **oldest** | **BigDecimal**| Start of time range of messages to include in results. | [optional] |
| **inclusive** | **Boolean**| Include messages with latest or oldest timestamp in results only when either timestamp is specified. | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached. | [optional] |
| **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] |

### Return type

[**ConversationsHistorySuccessSchema**](ConversationsHistorySuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response containing a channel&#39;s messages |  -  |
| **0** | Typical error response |  -  |

<a id="conversationsInfo"></a>
# **conversationsInfo**
> ConversationsInfoSuccessSchema conversationsInfo(token, channel, includeLocale, includeNumMembers)



Retrieve information about a conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:read`
    String channel = "channel_example"; // String | Conversation ID to learn more about
    Boolean includeLocale = true; // Boolean | Set this to `true` to receive the locale for this conversation. Defaults to `false`
    Boolean includeNumMembers = true; // Boolean | Set to `true` to include the member count for the specified conversation. Defaults to `false`
    try {
      ConversationsInfoSuccessSchema result = apiInstance.conversationsInfo(token, channel, includeLocale, includeNumMembers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:read&#x60; | [optional] |
| **channel** | **String**| Conversation ID to learn more about | [optional] |
| **includeLocale** | **Boolean**| Set this to &#x60;true&#x60; to receive the locale for this conversation. Defaults to &#x60;false&#x60; | [optional] |
| **includeNumMembers** | **Boolean**| Set to &#x60;true&#x60; to include the member count for the specified conversation. Defaults to &#x60;false&#x60; | [optional] |

### Return type

[**ConversationsInfoSuccessSchema**](ConversationsInfoSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response for a public channel. (Also, a response from a private channel and a multi-party IM is very similar to this example.) |  -  |
| **0** | Typical error response when a channel cannot be found |  -  |

<a id="conversationsInvite"></a>
# **conversationsInvite**
> ConversationsInviteErrorSchema conversationsInvite(token, channel, users)



Invites users to a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | The ID of the public or private channel to invite user(s) to.
    String users = "users_example"; // String | A comma separated list of user IDs. Up to 1000 users may be listed.
    try {
      ConversationsInviteErrorSchema result = apiInstance.conversationsInvite(token, channel, users);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsInvite");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| The ID of the public or private channel to invite user(s) to. | [optional] |
| **users** | **String**| A comma separated list of user IDs. Up to 1000 users may be listed. | [optional] |

### Return type

[**ConversationsInviteErrorSchema**](ConversationsInviteErrorSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response when an invitation is extended |  -  |
| **0** | Typical error response when an invite is attempted on a conversation type that does not support it |  -  |

<a id="conversationsJoin"></a>
# **conversationsJoin**
> ConversationsJoinSuccessSchema conversationsJoin(token, channel)



Joins an existing conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `channels:write`
    String channel = "channel_example"; // String | ID of conversation to join
    try {
      ConversationsJoinSuccessSchema result = apiInstance.conversationsJoin(token, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsJoin");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;channels:write&#x60; | [optional] |
| **channel** | **String**| ID of conversation to join | [optional] |

### Return type

[**ConversationsJoinSuccessSchema**](ConversationsJoinSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response if the conversation is archived and cannot be joined |  -  |

<a id="conversationsKick"></a>
# **conversationsKick**
> ConversationsKickSuccessSchema conversationsKick(token, channel, user)



Removes a user from a conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | ID of conversation to remove user from.
    String user = "user_example"; // String | User ID to be removed.
    try {
      ConversationsKickSuccessSchema result = apiInstance.conversationsKick(token, channel, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsKick");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| ID of conversation to remove user from. | [optional] |
| **user** | **String**| User ID to be removed. | [optional] |

### Return type

[**ConversationsKickSuccessSchema**](ConversationsKickSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response when you attempt to kick yourself from a channel |  -  |

<a id="conversationsLeave"></a>
# **conversationsLeave**
> ConversationsLeaveSuccessSchema conversationsLeave(token, channel)



Leaves a conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | Conversation to leave
    try {
      ConversationsLeaveSuccessSchema result = apiInstance.conversationsLeave(token, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsLeave");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| Conversation to leave | [optional] |

### Return type

[**ConversationsLeaveSuccessSchema**](ConversationsLeaveSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response when attempting to leave a workspace&#39;s \&quot;general\&quot; channel |  -  |

<a id="conversationsList"></a>
# **conversationsList**
> ConversationsListSuccessSchema conversationsList(token, excludeArchived, types, limit, cursor)



Lists all channels in a Slack team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:read`
    Boolean excludeArchived = true; // Boolean | Set to `true` to exclude archived channels from the list
    String types = "types_example"; // String | Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`
    Integer limit = 56; // Integer | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000.
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    try {
      ConversationsListSuccessSchema result = apiInstance.conversationsList(token, excludeArchived, types, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:read&#x60; | [optional] |
| **excludeArchived** | **Boolean**| Set to &#x60;true&#x60; to exclude archived channels from the list | [optional] |
| **types** | **String**| Mix and match channel types by providing a comma-separated list of any combination of &#x60;public_channel&#x60;, &#x60;private_channel&#x60;, &#x60;mpim&#x60;, &#x60;im&#x60; | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. Must be an integer no larger than 1000. | [optional] |
| **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] |

### Return type

[**ConversationsListSuccessSchema**](ConversationsListSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response with only public channels |  -  |
| **0** | Typical error response |  -  |

<a id="conversationsMark"></a>
# **conversationsMark**
> ConversationsMarkSuccessSchema conversationsMark(token, channel, ts)



Sets the read cursor in a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | Channel or conversation to set the read cursor for.
    BigDecimal ts = new BigDecimal(78); // BigDecimal | Unique identifier of message you want marked as most recently seen in this conversation.
    try {
      ConversationsMarkSuccessSchema result = apiInstance.conversationsMark(token, channel, ts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsMark");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| Channel or conversation to set the read cursor for. | [optional] |
| **ts** | **BigDecimal**| Unique identifier of message you want marked as most recently seen in this conversation. | [optional] |

### Return type

[**ConversationsMarkSuccessSchema**](ConversationsMarkSuccessSchema.md)

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

<a id="conversationsMembers"></a>
# **conversationsMembers**
> ConversationsMembersSuccessSchema conversationsMembers(token, channel, limit, cursor)



Retrieve members of a conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:read`
    String channel = "channel_example"; // String | ID of the conversation to retrieve members for
    Integer limit = 56; // Integer | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    try {
      ConversationsMembersSuccessSchema result = apiInstance.conversationsMembers(token, channel, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsMembers");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:read&#x60; | [optional] |
| **channel** | **String**| ID of the conversation to retrieve members for | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached. | [optional] |
| **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] |

### Return type

[**ConversationsMembersSuccessSchema**](ConversationsMembersSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical paginated success response |  -  |
| **0** | Typical error response when an invalid cursor is provided |  -  |

<a id="conversationsOpen"></a>
# **conversationsOpen**
> ConversationsOpenSuccessSchema conversationsOpen(token, channel, returnIm, users)



Opens or resumes a direct message or multi-person direct message.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | Resume a conversation by supplying an `im` or `mpim`'s ID. Or provide the `users` field instead.
    Boolean returnIm = true; // Boolean | Boolean, indicates you want the full IM channel definition in the response.
    String users = "users_example"; // String | Comma separated lists of users. If only one user is included, this creates a 1:1 DM.  The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a `channel` when not supplying `users`.
    try {
      ConversationsOpenSuccessSchema result = apiInstance.conversationsOpen(token, channel, returnIm, users);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsOpen");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| Resume a conversation by supplying an &#x60;im&#x60; or &#x60;mpim&#x60;&#39;s ID. Or provide the &#x60;users&#x60; field instead. | [optional] |
| **returnIm** | **Boolean**| Boolean, indicates you want the full IM channel definition in the response. | [optional] |
| **users** | **String**| Comma separated lists of users. If only one user is included, this creates a 1:1 DM.  The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a &#x60;channel&#x60; when not supplying &#x60;users&#x60;. | [optional] |

### Return type

[**ConversationsOpenSuccessSchema**](ConversationsOpenSuccessSchema.md)

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

<a id="conversationsRename"></a>
# **conversationsRename**
> ConversationsRenameSuccessSchema conversationsRename(token, channel, name)



Renames a conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | ID of conversation to rename
    String name = "name_example"; // String | New name for conversation.
    try {
      ConversationsRenameSuccessSchema result = apiInstance.conversationsRename(token, channel, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsRename");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| ID of conversation to rename | [optional] |
| **name** | **String**| New name for conversation. | [optional] |

### Return type

[**ConversationsRenameSuccessSchema**](ConversationsRenameSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response when the calling user is not a member of the conversation |  -  |

<a id="conversationsReplies"></a>
# **conversationsReplies**
> ConversationsRepliesSuccessSchema conversationsReplies(token, channel, ts, latest, oldest, inclusive, limit, cursor)



Retrieve a thread of messages posted to a conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:history`
    String channel = "channel_example"; // String | Conversation ID to fetch thread from.
    BigDecimal ts = new BigDecimal(78); // BigDecimal | Unique identifier of a thread's parent message. `ts` must be the timestamp of an existing message with 0 or more replies. If there are no replies then just the single message referenced by `ts` will return - it is just an ordinary, unthreaded message.
    BigDecimal latest = new BigDecimal(78); // BigDecimal | End of time range of messages to include in results.
    BigDecimal oldest = new BigDecimal(78); // BigDecimal | Start of time range of messages to include in results.
    Boolean inclusive = true; // Boolean | Include messages with latest or oldest timestamp in results only when either timestamp is specified.
    Integer limit = 56; // Integer | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    try {
      ConversationsRepliesSuccessSchema result = apiInstance.conversationsReplies(token, channel, ts, latest, oldest, inclusive, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsReplies");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:history&#x60; | [optional] |
| **channel** | **String**| Conversation ID to fetch thread from. | [optional] |
| **ts** | **BigDecimal**| Unique identifier of a thread&#39;s parent message. &#x60;ts&#x60; must be the timestamp of an existing message with 0 or more replies. If there are no replies then just the single message referenced by &#x60;ts&#x60; will return - it is just an ordinary, unthreaded message. | [optional] |
| **latest** | **BigDecimal**| End of time range of messages to include in results. | [optional] |
| **oldest** | **BigDecimal**| Start of time range of messages to include in results. | [optional] |
| **inclusive** | **Boolean**| Include messages with latest or oldest timestamp in results only when either timestamp is specified. | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached. | [optional] |
| **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] |

### Return type

[**ConversationsRepliesSuccessSchema**](ConversationsRepliesSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="conversationsSetPurpose"></a>
# **conversationsSetPurpose**
> ConversationsSetPurposeSuccessSchema conversationsSetPurpose(token, channel, purpose)



Sets the purpose for a conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | Conversation to set the purpose of
    String purpose = "purpose_example"; // String | A new, specialer purpose
    try {
      ConversationsSetPurposeSuccessSchema result = apiInstance.conversationsSetPurpose(token, channel, purpose);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsSetPurpose");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| Conversation to set the purpose of | [optional] |
| **purpose** | **String**| A new, specialer purpose | [optional] |

### Return type

[**ConversationsSetPurposeSuccessSchema**](ConversationsSetPurposeSuccessSchema.md)

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

<a id="conversationsSetTopic"></a>
# **conversationsSetTopic**
> ConversationsSetTopicSuccessSchema conversationsSetTopic(token, channel, topic)



Sets the topic for a conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | Conversation to set the topic of
    String topic = "topic_example"; // String | The new topic string. Does not support formatting or linkification.
    try {
      ConversationsSetTopicSuccessSchema result = apiInstance.conversationsSetTopic(token, channel, topic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsSetTopic");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| Conversation to set the topic of | [optional] |
| **topic** | **String**| The new topic string. Does not support formatting or linkification. | [optional] |

### Return type

[**ConversationsSetTopicSuccessSchema**](ConversationsSetTopicSuccessSchema.md)

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

<a id="conversationsUnarchive"></a>
# **conversationsUnarchive**
> ConversationsUnarchiveSuccessSchema conversationsUnarchive(token, channel)



Reverses conversation archival.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:write`
    String channel = "channel_example"; // String | ID of conversation to unarchive
    try {
      ConversationsUnarchiveSuccessSchema result = apiInstance.conversationsUnarchive(token, channel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#conversationsUnarchive");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] |
| **channel** | **String**| ID of conversation to unarchive | [optional] |

### Return type

[**ConversationsUnarchiveSuccessSchema**](ConversationsUnarchiveSuccessSchema.md)

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

