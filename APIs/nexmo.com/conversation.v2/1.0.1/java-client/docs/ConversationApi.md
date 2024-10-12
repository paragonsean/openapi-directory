# ConversationApi

All URIs are relative to *https://api.nexmo.com/v0.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConversations**](ConversationApi.md#getConversations) | **GET** /conversations | List Conversations |


<a id="getConversations"></a>
# **getConversations**
> GetConversations200Response getConversations(pageSize, order, cursor, dateStart, dateEnd)

List Conversations

Please note that not all data is available in the list endpoint. Once  you&#39;ve identified the conversation you need to work with, use the  [GET /conversations/:id](#get-conversation) endpoint to fetch all of the conversation details 

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
    defaultClient.setBasePath("https://api.nexmo.com/v0.2");

    ConversationApi apiInstance = new ConversationApi(defaultClient);
    Integer pageSize = 10; // Integer | The number of results returned per page.   The default value is `10`. The maximum value is `100`.
    String order = "asc"; // String | Show the most (`desc`) / least (`asc`) recently created entries first
    String cursor = "cursor_example"; // String | The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in `_links.next.href` in the response which contains a `cursor` value 
    String dateStart = "dateStart_example"; // String | Search for conversations created after this ISO8601 date
    String dateEnd = "dateEnd_example"; // String | Search for conversations created before this ISO8601 date
    try {
      GetConversations200Response result = apiInstance.getConversations(pageSize, order, cursor, dateStart, dateEnd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationApi#getConversations");
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
| **pageSize** | **Integer**| The number of results returned per page.   The default value is &#x60;10&#x60;. The maximum value is &#x60;100&#x60;. | [optional] [default to 10] |
| **order** | **String**| Show the most (&#x60;desc&#x60;) / least (&#x60;asc&#x60;) recently created entries first | [optional] [default to asc] [enum: asc, desc] |
| **cursor** | **String**| The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in &#x60;_links.next.href&#x60; in the response which contains a &#x60;cursor&#x60; value  | [optional] |
| **dateStart** | **String**| Search for conversations created after this ISO8601 date | [optional] |
| **dateEnd** | **String**| Search for conversations created before this ISO8601 date | [optional] |

### Return type

[**GetConversations200Response**](GetConversations200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

