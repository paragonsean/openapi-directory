# SlackApi

All URIs are relative to *http://botschaft.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**slackGetSlackGet**](SlackApi.md#slackGetSlackGet) | **GET** /slack | Slack Get |
| [**slackPostSlackPost**](SlackApi.md#slackPostSlackPost) | **POST** /slack | Slack Post |


<a id="slackGetSlackGet"></a>
# **slackGetSlackGet**
> Object slackGetSlackGet(channel, message, base64Message, authorization)

Slack Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://botschaft.local");

    SlackApi apiInstance = new SlackApi(defaultClient);
    String channel = "channel_example"; // String | 
    String message = "message_example"; // String | 
    String base64Message = "base64Message_example"; // String | 
    String authorization = "authorization_example"; // String | 
    try {
      Object result = apiInstance.slackGetSlackGet(channel, message, base64Message, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlackApi#slackGetSlackGet");
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
| **channel** | **String**|  | |
| **message** | **String**|  | [optional] |
| **base64Message** | **String**|  | [optional] |
| **authorization** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="slackPostSlackPost"></a>
# **slackPostSlackPost**
> Object slackPostSlackPost(slackMessageRequest, authorization)

Slack Post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SlackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://botschaft.local");

    SlackApi apiInstance = new SlackApi(defaultClient);
    SlackMessageRequest slackMessageRequest = new SlackMessageRequest(); // SlackMessageRequest | 
    String authorization = "authorization_example"; // String | 
    try {
      Object result = apiInstance.slackPostSlackPost(slackMessageRequest, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SlackApi#slackPostSlackPost");
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
| **slackMessageRequest** | [**SlackMessageRequest**](SlackMessageRequest.md)|  | |
| **authorization** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

