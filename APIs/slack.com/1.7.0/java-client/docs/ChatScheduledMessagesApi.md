# ChatScheduledMessagesApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chatScheduledMessagesList**](ChatScheduledMessagesApi.md#chatScheduledMessagesList) | **GET** /chat.scheduledMessages.list |  |


<a id="chatScheduledMessagesList"></a>
# **chatScheduledMessagesList**
> ChatScheduledMessagesListSchema chatScheduledMessagesList(token, channel, latest, oldest, limit, cursor)



Returns a list of scheduled messages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatScheduledMessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ChatScheduledMessagesApi apiInstance = new ChatScheduledMessagesApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `none`
    String channel = "channel_example"; // String | The channel of the scheduled messages
    BigDecimal latest = new BigDecimal(78); // BigDecimal | A UNIX timestamp of the latest value in the time range
    BigDecimal oldest = new BigDecimal(78); // BigDecimal | A UNIX timestamp of the oldest value in the time range
    Integer limit = 56; // Integer | Maximum number of original entries to return.
    String cursor = "cursor_example"; // String | For pagination purposes, this is the `cursor` value returned from a previous call to `chat.scheduledmessages.list` indicating where you want to start this call from.
    try {
      ChatScheduledMessagesListSchema result = apiInstance.chatScheduledMessagesList(token, channel, latest, oldest, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatScheduledMessagesApi#chatScheduledMessagesList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | [optional] |
| **channel** | **String**| The channel of the scheduled messages | [optional] |
| **latest** | **BigDecimal**| A UNIX timestamp of the latest value in the time range | [optional] |
| **oldest** | **BigDecimal**| A UNIX timestamp of the oldest value in the time range | [optional] |
| **limit** | **Integer**| Maximum number of original entries to return. | [optional] |
| **cursor** | **String**| For pagination purposes, this is the &#x60;cursor&#x60; value returned from a previous call to &#x60;chat.scheduledmessages.list&#x60; indicating where you want to start this call from. | [optional] |

### Return type

[**ChatScheduledMessagesListSchema**](ChatScheduledMessagesListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response if the channel passed is invalid |  -  |

