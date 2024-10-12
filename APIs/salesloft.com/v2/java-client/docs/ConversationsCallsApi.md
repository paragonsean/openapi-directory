# ConversationsCallsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2ConversationsCallsPost**](ConversationsCallsApi.md#v2ConversationsCallsPost) | **POST** /v2/conversations/calls | Create Conversations Call |


<a id="v2ConversationsCallsPost"></a>
# **v2ConversationsCallsPost**
> ConversationsCall v2ConversationsCallsPost(duration, from, recording, to, callCreatedAt, direction, userGuid)

Create Conversations Call

Enqueue a Conversations Call for processing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsCallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ConversationsCallsApi apiInstance = new ConversationsCallsApi(defaultClient);
    BigDecimal duration = new BigDecimal(78); // BigDecimal | Duration of call in seconds
    String from = "from_example"; // String | Phone number that call was made from
    Object recording = null; // Object | Object containing recording info including the audio file (.mp3, .wav, .ogg, .m4a)
    String to = "to_example"; // String |  Phone number that was called
    String callCreatedAt = "callCreatedAt_example"; // String | Timestamp for when the call started. If not provided, will default to the time the request was received
    String direction = "direction_example"; // String | Call direction
    String userGuid = "userGuid_example"; // String | Guid of the Salesloft User to assign the call to. If not provided, will default to the user within the authentication token
    try {
      ConversationsCall result = apiInstance.v2ConversationsCallsPost(duration, from, recording, to, callCreatedAt, direction, userGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsCallsApi#v2ConversationsCallsPost");
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
| **duration** | **BigDecimal**| Duration of call in seconds | |
| **from** | **String**| Phone number that call was made from | |
| **recording** | [**Object**](Object.md)| Object containing recording info including the audio file (.mp3, .wav, .ogg, .m4a) | |
| **to** | **String**|  Phone number that was called | |
| **callCreatedAt** | **String**| Timestamp for when the call started. If not provided, will default to the time the request was received | [optional] |
| **direction** | **String**| Call direction | [optional] |
| **userGuid** | **String**| Guid of the Salesloft User to assign the call to. If not provided, will default to the user within the authentication token | [optional] |

### Return type

[**ConversationsCall**](ConversationsCall.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |

