# DiscordApi

All URIs are relative to *http://botschaft.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**discordGetDiscordGet**](DiscordApi.md#discordGetDiscordGet) | **GET** /discord | Discord Get |
| [**discordPostDiscordPost**](DiscordApi.md#discordPostDiscordPost) | **POST** /discord | Discord Post |


<a id="discordGetDiscordGet"></a>
# **discordGetDiscordGet**
> Object discordGetDiscordGet(channel, message, base64Message, authorization)

Discord Get

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://botschaft.local");

    DiscordApi apiInstance = new DiscordApi(defaultClient);
    String channel = "channel_example"; // String | 
    String message = "message_example"; // String | 
    String base64Message = "base64Message_example"; // String | 
    String authorization = "authorization_example"; // String | 
    try {
      Object result = apiInstance.discordGetDiscordGet(channel, message, base64Message, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscordApi#discordGetDiscordGet");
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

<a id="discordPostDiscordPost"></a>
# **discordPostDiscordPost**
> Object discordPostDiscordPost(discordMessageRequest, authorization)

Discord Post

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://botschaft.local");

    DiscordApi apiInstance = new DiscordApi(defaultClient);
    DiscordMessageRequest discordMessageRequest = new DiscordMessageRequest(); // DiscordMessageRequest | 
    String authorization = "authorization_example"; // String | 
    try {
      Object result = apiInstance.discordPostDiscordPost(discordMessageRequest, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscordApi#discordPostDiscordPost");
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
| **discordMessageRequest** | [**DiscordMessageRequest**](DiscordMessageRequest.md)|  | |
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

