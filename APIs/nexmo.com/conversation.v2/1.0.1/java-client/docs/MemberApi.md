# MemberApi

All URIs are relative to *https://api.nexmo.com/v0.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMembers**](MemberApi.md#getMembers) | **GET** /conversations/{conversation_id}/members | List Members |


<a id="getMembers"></a>
# **getMembers**
> GetMembers200Response getMembers(conversationId, pageSize, order, cursor)

List Members

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.2");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String conversationId = "CON-afe887d8-d587-4280-9aae-dfa4c9227d5e"; // String | The ID of the conversation
    Integer pageSize = 10; // Integer | The number of results returned per page.   The default value is `10`. The maximum value is `100`.
    String order = "asc"; // String | Show the most (`desc`) / least (`asc`) recently created entries first
    String cursor = "cursor_example"; // String | The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in `_links.next.href` in the response which contains a `cursor` value 
    try {
      GetMembers200Response result = apiInstance.getMembers(conversationId, pageSize, order, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getMembers");
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
| **conversationId** | **String**| The ID of the conversation | |
| **pageSize** | **Integer**| The number of results returned per page.   The default value is &#x60;10&#x60;. The maximum value is &#x60;100&#x60;. | [optional] [default to 10] |
| **order** | **String**| Show the most (&#x60;desc&#x60;) / least (&#x60;asc&#x60;) recently created entries first | [optional] [default to asc] [enum: asc, desc] |
| **cursor** | **String**| The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in &#x60;_links.next.href&#x60; in the response which contains a &#x60;cursor&#x60; value  | [optional] |

### Return type

[**GetMembers200Response**](GetMembers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

