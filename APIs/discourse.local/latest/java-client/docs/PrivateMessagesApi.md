# PrivateMessagesApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTopicPostPM_1**](PrivateMessagesApi.md#createTopicPostPM_1) | **POST** /posts.json | Creates a new topic, a new post, or a private message |
| [**getUserSentPrivateMessages**](PrivateMessagesApi.md#getUserSentPrivateMessages) | **GET** /topics/private-messages-sent/{username}.json | Get a list of private messages sent for a user |
| [**listUserPrivateMessages**](PrivateMessagesApi.md#listUserPrivateMessages) | **GET** /topics/private-messages/{username}.json | Get a list of private messages for a user |


<a id="createTopicPostPM_1"></a>
# **createTopicPostPM_1**
> CreateTopicPostPM200Response createTopicPostPM_1(createTopicPostPMRequest)

Creates a new topic, a new post, or a private message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateMessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PrivateMessagesApi apiInstance = new PrivateMessagesApi(defaultClient);
    CreateTopicPostPMRequest createTopicPostPMRequest = new CreateTopicPostPMRequest(); // CreateTopicPostPMRequest | 
    try {
      CreateTopicPostPM200Response result = apiInstance.createTopicPostPM_1(createTopicPostPMRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateMessagesApi#createTopicPostPM_1");
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
| **createTopicPostPMRequest** | [**CreateTopicPostPMRequest**](CreateTopicPostPMRequest.md)|  | [optional] |

### Return type

[**CreateTopicPostPM200Response**](CreateTopicPostPM200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | post created |  -  |

<a id="getUserSentPrivateMessages"></a>
# **getUserSentPrivateMessages**
> GetUserSentPrivateMessages200Response getUserSentPrivateMessages(username)

Get a list of private messages sent for a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateMessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PrivateMessagesApi apiInstance = new PrivateMessagesApi(defaultClient);
    String username = "username_example"; // String | 
    try {
      GetUserSentPrivateMessages200Response result = apiInstance.getUserSentPrivateMessages(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateMessagesApi#getUserSentPrivateMessages");
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
| **username** | **String**|  | |

### Return type

[**GetUserSentPrivateMessages200Response**](GetUserSentPrivateMessages200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | private messages |  -  |

<a id="listUserPrivateMessages"></a>
# **listUserPrivateMessages**
> ListUserPrivateMessages200Response listUserPrivateMessages(username)

Get a list of private messages for a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateMessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://discourse.local");

    PrivateMessagesApi apiInstance = new PrivateMessagesApi(defaultClient);
    String username = "username_example"; // String | 
    try {
      ListUserPrivateMessages200Response result = apiInstance.listUserPrivateMessages(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateMessagesApi#listUserPrivateMessages");
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
| **username** | **String**|  | |

### Return type

[**ListUserPrivateMessages200Response**](ListUserPrivateMessages200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | private messages |  -  |

