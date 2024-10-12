# DefaultApi

All URIs are relative to *https://api.nexmo.com/v0.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUsers**](DefaultApi.md#getUsers) | **GET** /users | List Users |


<a id="getUsers"></a>
# **getUsers**
> GetUsers200Response getUsers(pageSize, order, cursor)

List Users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v0.2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer pageSize = 10; // Integer | The number of results returned per page.   The default value is `10`. The maximum value is `100`.
    String order = "asc"; // String | Show the most (`desc`) / least (`asc`) recently created entries first
    String cursor = "cursor_example"; // String | The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in `_links.next.href` in the response which contains a `cursor` value 
    try {
      GetUsers200Response result = apiInstance.getUsers(pageSize, order, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUsers");
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

### Return type

[**GetUsers200Response**](GetUsers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

