# MessageCommentReactionsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteMessageCommentReactionsId**](MessageCommentReactionsApi.md#deleteMessageCommentReactionsId) | **DELETE** /message_comment_reactions/{id} | Delete Message Comment Reaction |
| [**getMessageCommentReactions**](MessageCommentReactionsApi.md#getMessageCommentReactions) | **GET** /message_comment_reactions | List Message Comment Reactions |
| [**getMessageCommentReactionsId**](MessageCommentReactionsApi.md#getMessageCommentReactionsId) | **GET** /message_comment_reactions/{id} | Show Message Comment Reaction |
| [**postMessageCommentReactions**](MessageCommentReactionsApi.md#postMessageCommentReactions) | **POST** /message_comment_reactions | Create Message Comment Reaction |


<a id="deleteMessageCommentReactionsId"></a>
# **deleteMessageCommentReactionsId**
> deleteMessageCommentReactionsId(id)

Delete Message Comment Reaction

Delete Message Comment Reaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageCommentReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    MessageCommentReactionsApi apiInstance = new MessageCommentReactionsApi(defaultClient);
    Integer id = 56; // Integer | Message Comment Reaction ID.
    try {
      apiInstance.deleteMessageCommentReactionsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageCommentReactionsApi#deleteMessageCommentReactionsId");
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
| **id** | **Integer**| Message Comment Reaction ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No body. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getMessageCommentReactions"></a>
# **getMessageCommentReactions**
> List&lt;MessageCommentReactionEntity&gt; getMessageCommentReactions(messageCommentId, userId, cursor, perPage)

List Message Comment Reactions

List Message Comment Reactions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageCommentReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    MessageCommentReactionsApi apiInstance = new MessageCommentReactionsApi(defaultClient);
    Integer messageCommentId = 56; // Integer | Message comment to return reactions for.
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<MessageCommentReactionEntity> result = apiInstance.getMessageCommentReactions(messageCommentId, userId, cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageCommentReactionsApi#getMessageCommentReactions");
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
| **messageCommentId** | **Integer**| Message comment to return reactions for. | |
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |

### Return type

[**List&lt;MessageCommentReactionEntity&gt;**](MessageCommentReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of MessageCommentReactions objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getMessageCommentReactionsId"></a>
# **getMessageCommentReactionsId**
> MessageCommentReactionEntity getMessageCommentReactionsId(id)

Show Message Comment Reaction

Show Message Comment Reaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageCommentReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    MessageCommentReactionsApi apiInstance = new MessageCommentReactionsApi(defaultClient);
    Integer id = 56; // Integer | Message Comment Reaction ID.
    try {
      MessageCommentReactionEntity result = apiInstance.getMessageCommentReactionsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageCommentReactionsApi#getMessageCommentReactionsId");
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
| **id** | **Integer**| Message Comment Reaction ID. | |

### Return type

[**MessageCommentReactionEntity**](MessageCommentReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The MessageCommentReactions object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postMessageCommentReactions"></a>
# **postMessageCommentReactions**
> MessageCommentReactionEntity postMessageCommentReactions(emoji, userId)

Create Message Comment Reaction

Create Message Comment Reaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessageCommentReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    MessageCommentReactionsApi apiInstance = new MessageCommentReactionsApi(defaultClient);
    String emoji = "emoji_example"; // String | Emoji to react with.
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    try {
      MessageCommentReactionEntity result = apiInstance.postMessageCommentReactions(emoji, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessageCommentReactionsApi#postMessageCommentReactions");
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
| **emoji** | **String**| Emoji to react with. | |
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |

### Return type

[**MessageCommentReactionEntity**](MessageCommentReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The MessageCommentReactions object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

