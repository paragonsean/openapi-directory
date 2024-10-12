# Class4FeedbackApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFeedback**](Class4FeedbackApi.md#getFeedback) | **GET** /feedback/{feedbackId} |  |
| [**sendFeedback**](Class4FeedbackApi.md#sendFeedback) | **POST** /feedback/submit |  |


<a id="getFeedback"></a>
# **getFeedback**
> getFeedback(authorization, feedbackId)



Retrieve feedback

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4FeedbackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class4FeedbackApi apiInstance = new Class4FeedbackApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
    String feedbackId = "feedbackId_example"; // String | 
    try {
      apiInstance.getFeedback(authorization, feedbackId);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4FeedbackApi#getFeedback");
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
| **authorization** | **String**| Authorization token (provided upon successful login) | |
| **feedbackId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad parameters: Please check provided values |  -  |
| **401** | Unauthorized request |  -  |
| **500** | Internal server error |  -  |

<a id="sendFeedback"></a>
# **sendFeedback**
> sendFeedback(body)



Submit feedback for the bank

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4FeedbackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class4FeedbackApi apiInstance = new Class4FeedbackApi(defaultClient);
    Feedback body = new Feedback(); // Feedback | Feedback details including name, email the subject and complete message
    try {
      apiInstance.sendFeedback(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4FeedbackApi#sendFeedback");
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
| **body** | [**Feedback**](Feedback.md)| Feedback details including name, email the subject and complete message | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **401** | Unauthorized request |  -  |
| **500** | Internal server error |  -  |

