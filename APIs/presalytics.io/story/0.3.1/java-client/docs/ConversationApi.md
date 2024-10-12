# ConversationApi

All URIs are relative to */story*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storyIdMessagesGet**](ConversationApi.md#storyIdMessagesGet) | **GET** /{id}/messages | Conversation: List Conversation Messages |
| [**storyIdMessagesPost**](ConversationApi.md#storyIdMessagesPost) | **POST** /{id}/messages | Conversation: Send a Message |


<a id="storyIdMessagesGet"></a>
# **storyIdMessagesGet**
> List&lt;Message&gt; storyIdMessagesGet(id)

Conversation: List Conversation Messages

Get a list of messages that have been send in this story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    ConversationApi apiInstance = new ConversationApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    try {
      List<Message> result = apiInstance.storyIdMessagesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationApi#storyIdMessagesGet");
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
| **id** | **UUID**| the id from the story object | |

### Return type

[**List&lt;Message&gt;**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Array of conversation messages |  -  |
| **401** | Unauthorized |  -  |

<a id="storyIdMessagesPost"></a>
# **storyIdMessagesPost**
> storyIdMessagesPost(id, body)

Conversation: Send a Message

Add a message to the Story&#39;s conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    ConversationApi apiInstance = new ConversationApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    String body = "body_example"; // String | The message text
    try {
      apiInstance.storyIdMessagesPost(id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationApi#storyIdMessagesPost");
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
| **id** | **UUID**| the id from the story object | |
| **body** | **String**| The message text | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

