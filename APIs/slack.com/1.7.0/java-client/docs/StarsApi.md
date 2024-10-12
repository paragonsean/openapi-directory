# StarsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**starsAdd**](StarsApi.md#starsAdd) | **POST** /stars.add |  |
| [**starsList**](StarsApi.md#starsList) | **GET** /stars.list |  |
| [**starsRemove**](StarsApi.md#starsRemove) | **POST** /stars.remove |  |


<a id="starsAdd"></a>
# **starsAdd**
> StarsAddSchema starsAdd(token, channel, _file, fileComment, timestamp)



Adds a star to an item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    StarsApi apiInstance = new StarsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `stars:write`
    String channel = "channel_example"; // String | Channel to add star to, or channel where the message to add star to was posted (used with `timestamp`).
    String _file = "_file_example"; // String | File to add star to.
    String fileComment = "fileComment_example"; // String | File comment to add star to.
    String timestamp = "timestamp_example"; // String | Timestamp of the message to add star to.
    try {
      StarsAddSchema result = apiInstance.starsAdd(token, channel, _file, fileComment, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StarsApi#starsAdd");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;stars:write&#x60; | |
| **channel** | **String**| Channel to add star to, or channel where the message to add star to was posted (used with &#x60;timestamp&#x60;). | [optional] |
| **_file** | **String**| File to add star to. | [optional] |
| **fileComment** | **String**| File comment to add star to. | [optional] |
| **timestamp** | **String**| Timestamp of the message to add star to. | [optional] |

### Return type

[**StarsAddSchema**](StarsAddSchema.md)

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

<a id="starsList"></a>
# **starsList**
> StarsListSchema starsList(token, count, page, cursor, limit)



Lists stars for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    StarsApi apiInstance = new StarsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `stars:read`
    String count = "count_example"; // String | 
    String page = "page_example"; // String | 
    String cursor = "cursor_example"; // String | Parameter for pagination. Set `cursor` equal to the `next_cursor` attribute returned by the previous request's `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more details.
    Integer limit = 56; // Integer | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.
    try {
      StarsListSchema result = apiInstance.starsList(token, count, page, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StarsApi#starsList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;stars:read&#x60; | [optional] |
| **count** | **String**|  | [optional] |
| **page** | **String**|  | [optional] |
| **cursor** | **String**| Parameter for pagination. Set &#x60;cursor&#x60; equal to the &#x60;next_cursor&#x60; attribute returned by the previous request&#39;s &#x60;response_metadata&#x60;. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more details. | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. | [optional] |

### Return type

[**StarsListSchema**](StarsListSchema.md)

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

<a id="starsRemove"></a>
# **starsRemove**
> StarsRemoveSchema starsRemove(token, channel, _file, fileComment, timestamp)



Removes a star from an item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    StarsApi apiInstance = new StarsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `stars:write`
    String channel = "channel_example"; // String | Channel to remove star from, or channel where the message to remove star from was posted (used with `timestamp`).
    String _file = "_file_example"; // String | File to remove star from.
    String fileComment = "fileComment_example"; // String | File comment to remove star from.
    String timestamp = "timestamp_example"; // String | Timestamp of the message to remove star from.
    try {
      StarsRemoveSchema result = apiInstance.starsRemove(token, channel, _file, fileComment, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StarsApi#starsRemove");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;stars:write&#x60; | |
| **channel** | **String**| Channel to remove star from, or channel where the message to remove star from was posted (used with &#x60;timestamp&#x60;). | [optional] |
| **_file** | **String**| File to remove star from. | [optional] |
| **fileComment** | **String**| File comment to remove star from. | [optional] |
| **timestamp** | **String**| Timestamp of the message to remove star from. | [optional] |

### Return type

[**StarsRemoveSchema**](StarsRemoveSchema.md)

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

