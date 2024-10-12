# FeedbackApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**feedbackFeedbackIdGet**](FeedbackApi.md#feedbackFeedbackIdGet) | **GET** /feedback/{feedback_id} | Feedback details |


<a id="feedbackFeedbackIdGet"></a>
# **feedbackFeedbackIdGet**
> feedbackFeedbackIdGet(feedbackId)

Feedback details

Feedback details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedbackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    FeedbackApi apiInstance = new FeedbackApi(defaultClient);
    String feedbackId = "feedbackId_example"; // String | 
    try {
      apiInstance.feedbackFeedbackIdGet(feedbackId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedbackApi#feedbackFeedbackIdGet");
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
| **0** | Unexpected error |  -  |

