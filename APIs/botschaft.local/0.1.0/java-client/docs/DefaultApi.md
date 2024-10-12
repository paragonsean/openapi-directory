# DefaultApi

All URIs are relative to *http://botschaft.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configConfigGet**](DefaultApi.md#configConfigGet) | **GET** /config | Config |
| [**topicTopicTopicNameGet**](DefaultApi.md#topicTopicTopicNameGet) | **GET** /topic/{topic_name} | Topic |


<a id="configConfigGet"></a>
# **configConfigGet**
> Config configConfigGet(authorization)

Config

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
    defaultClient.setBasePath("http://botschaft.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String authorization = "authorization_example"; // String | 
    try {
      Config result = apiInstance.configConfigGet(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#configConfigGet");
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
| **authorization** | **String**|  | [optional] |

### Return type

[**Config**](Config.md)

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

<a id="topicTopicTopicNameGet"></a>
# **topicTopicTopicNameGet**
> Object topicTopicTopicNameGet(topicName, message, base64Message, authorization)

Topic

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
    defaultClient.setBasePath("http://botschaft.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String topicName = "topicName_example"; // String | 
    String message = "message_example"; // String | 
    String base64Message = "base64Message_example"; // String | 
    String authorization = "authorization_example"; // String | 
    try {
      Object result = apiInstance.topicTopicTopicNameGet(topicName, message, base64Message, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#topicTopicTopicNameGet");
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
| **topicName** | **String**|  | |
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

