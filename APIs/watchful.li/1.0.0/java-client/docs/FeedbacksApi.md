# FeedbacksApi

All URIs are relative to *https://watchful.li/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFeedbacks**](FeedbacksApi.md#createFeedbacks) | **POST** /feedbacks | Create a feedback |
| [**getFeedbacks**](FeedbacksApi.md#getFeedbacks) | **GET** /feedbacks | Get feedbacks |
| [**getFieldsFeedbacks**](FeedbacksApi.md#getFieldsFeedbacks) | **GET** /feedbacks/metadata | Get the list of fields |


<a id="createFeedbacks"></a>
# **createFeedbacks**
> Audit createFeedbacks(body)

Create a feedback

Create a feedback

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedbacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    FeedbacksApi apiInstance = new FeedbacksApi(defaultClient);
    Feedback body = new Feedback(); // Feedback | JSON object Feedback
    try {
      Audit result = apiInstance.createFeedbacks(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedbacksApi#createFeedbacks");
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
| **body** | [**Feedback**](Feedback.md)| JSON object Feedback | |

### Return type

[**Audit**](Audit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **201** | Saved successfully |  -  |
| **400** | Invalid data |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Not saved |  -  |

<a id="getFeedbacks"></a>
# **getFeedbacks**
> Feedback getFeedbacks(fields)

Get feedbacks

Returns a list of feedbacks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedbacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    FeedbacksApi apiInstance = new FeedbacksApi(defaultClient);
    String fields = "fields_example"; // String | Fields to return separate by comas (es. name,id)
    try {
      Feedback result = apiInstance.getFeedbacks(fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedbacksApi#getFeedbacks");
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
| **fields** | **String**| Fields to return separate by comas (es. name,id) | [optional] |

### Return type

[**Feedback**](Feedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |

<a id="getFieldsFeedbacks"></a>
# **getFieldsFeedbacks**
> String getFieldsFeedbacks()

Get the list of fields

Returns a list of fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedbacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://watchful.li/api/v1");

    FeedbacksApi apiInstance = new FeedbacksApi(defaultClient);
    try {
      String result = apiInstance.getFieldsFeedbacks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedbacksApi#getFieldsFeedbacks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

