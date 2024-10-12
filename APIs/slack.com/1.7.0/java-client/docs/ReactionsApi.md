# ReactionsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reactionsAdd**](ReactionsApi.md#reactionsAdd) | **POST** /reactions.add |  |
| [**reactionsGet**](ReactionsApi.md#reactionsGet) | **GET** /reactions.get |  |
| [**reactionsList**](ReactionsApi.md#reactionsList) | **GET** /reactions.list |  |
| [**reactionsRemove**](ReactionsApi.md#reactionsRemove) | **POST** /reactions.remove |  |


<a id="reactionsAdd"></a>
# **reactionsAdd**
> ReactionsAddSchema reactionsAdd(token, channel, name, timestamp)



Adds a reaction to an item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `reactions:write`
    String channel = "channel_example"; // String | Channel where the message to add reaction to was posted.
    String name = "name_example"; // String | Reaction (emoji) name.
    String timestamp = "timestamp_example"; // String | Timestamp of the message to add reaction to.
    try {
      ReactionsAddSchema result = apiInstance.reactionsAdd(token, channel, name, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsAdd");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;reactions:write&#x60; | |
| **channel** | **String**| Channel where the message to add reaction to was posted. | |
| **name** | **String**| Reaction (emoji) name. | |
| **timestamp** | **String**| Timestamp of the message to add reaction to. | |

### Return type

[**ReactionsAddSchema**](ReactionsAddSchema.md)

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

<a id="reactionsGet"></a>
# **reactionsGet**
> List&lt;ReactionsGetSuccessSchemaInner&gt; reactionsGet(token, channel, _file, fileComment, full, timestamp)



Gets reactions for an item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `reactions:read`
    String channel = "channel_example"; // String | Channel where the message to get reactions for was posted.
    String _file = "_file_example"; // String | File to get reactions for.
    String fileComment = "fileComment_example"; // String | File comment to get reactions for.
    Boolean full = true; // Boolean | If true always return the complete reaction list.
    String timestamp = "timestamp_example"; // String | Timestamp of the message to get reactions for.
    try {
      List<ReactionsGetSuccessSchemaInner> result = apiInstance.reactionsGet(token, channel, _file, fileComment, full, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsGet");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;reactions:read&#x60; | |
| **channel** | **String**| Channel where the message to get reactions for was posted. | [optional] |
| **_file** | **String**| File to get reactions for. | [optional] |
| **fileComment** | **String**| File comment to get reactions for. | [optional] |
| **full** | **Boolean**| If true always return the complete reaction list. | [optional] |
| **timestamp** | **String**| Timestamp of the message to get reactions for. | [optional] |

### Return type

[**List&lt;ReactionsGetSuccessSchemaInner&gt;**](ReactionsGetSuccessSchemaInner.md)

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

<a id="reactionsList"></a>
# **reactionsList**
> ReactionsListSchema reactionsList(token, user, full, count, page, cursor, limit)



Lists reactions made by a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `reactions:read`
    String user = "user_example"; // String | Show reactions made by this user. Defaults to the authed user.
    Boolean full = true; // Boolean | If true always return the complete reaction list.
    Integer count = 56; // Integer | 
    Integer page = 56; // Integer | 
    String cursor = "cursor_example"; // String | Parameter for pagination. Set `cursor` equal to the `next_cursor` attribute returned by the previous request's `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more details.
    Integer limit = 56; // Integer | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.
    try {
      ReactionsListSchema result = apiInstance.reactionsList(token, user, full, count, page, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;reactions:read&#x60; | |
| **user** | **String**| Show reactions made by this user. Defaults to the authed user. | [optional] |
| **full** | **Boolean**| If true always return the complete reaction list. | [optional] |
| **count** | **Integer**|  | [optional] |
| **page** | **Integer**|  | [optional] |
| **cursor** | **String**| Parameter for pagination. Set &#x60;cursor&#x60; equal to the &#x60;next_cursor&#x60; attribute returned by the previous request&#39;s &#x60;response_metadata&#x60;. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more details. | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. | [optional] |

### Return type

[**ReactionsListSchema**](ReactionsListSchema.md)

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

<a id="reactionsRemove"></a>
# **reactionsRemove**
> ReactionsRemoveSchema reactionsRemove(token, name, channel, _file, fileComment, timestamp)



Removes a reaction from an item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `reactions:write`
    String name = "name_example"; // String | Reaction (emoji) name.
    String channel = "channel_example"; // String | Channel where the message to remove reaction from was posted.
    String _file = "_file_example"; // String | File to remove reaction from.
    String fileComment = "fileComment_example"; // String | File comment to remove reaction from.
    String timestamp = "timestamp_example"; // String | Timestamp of the message to remove reaction from.
    try {
      ReactionsRemoveSchema result = apiInstance.reactionsRemove(token, name, channel, _file, fileComment, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsRemove");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;reactions:write&#x60; | |
| **name** | **String**| Reaction (emoji) name. | |
| **channel** | **String**| Channel where the message to remove reaction from was posted. | [optional] |
| **_file** | **String**| File to remove reaction from. | [optional] |
| **fileComment** | **String**| File comment to remove reaction from. | [optional] |
| **timestamp** | **String**| Timestamp of the message to remove reaction from. | [optional] |

### Return type

[**ReactionsRemoveSchema**](ReactionsRemoveSchema.md)

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

