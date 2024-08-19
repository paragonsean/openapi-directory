# BackgroundTasksApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBackgroundTaskApiV1BackgroundTaskTaskIdGet**](BackgroundTasksApi.md#getBackgroundTaskApiV1BackgroundTaskTaskIdGet) | **GET** /api/v1/background-task/{task_id}/ | Get Background Task |
| [**listBackgroundTasksApiV1BackgroundTaskGet**](BackgroundTasksApi.md#listBackgroundTasksApiV1BackgroundTaskGet) | **GET** /api/v1/background-task/ | List Background Tasks |


<a id="getBackgroundTaskApiV1BackgroundTaskTaskIdGet"></a>
# **getBackgroundTaskApiV1BackgroundTaskTaskIdGet**
> BackgroundTaskOut getBackgroundTaskApiV1BackgroundTaskTaskIdGet(taskId, idempotencyKey)

Get Background Task

Get a background task by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackgroundTasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    BackgroundTasksApi apiInstance = new BackgroundTasksApi(defaultClient);
    String taskId = "qtask_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      BackgroundTaskOut result = apiInstance.getBackgroundTaskApiV1BackgroundTaskTaskIdGet(taskId, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackgroundTasksApi#getBackgroundTaskApiV1BackgroundTaskTaskIdGet");
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
| **taskId** | **String**|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**BackgroundTaskOut**](BackgroundTaskOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="listBackgroundTasksApiV1BackgroundTaskGet"></a>
# **listBackgroundTasksApiV1BackgroundTaskGet**
> ListResponseBackgroundTaskOut listBackgroundTasksApiV1BackgroundTaskGet(iterator, limit, order, idempotencyKey)

List Background Tasks

List background tasks executed in the past 90 days.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackgroundTasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    BackgroundTasksApi apiInstance = new BackgroundTasksApi(defaultClient);
    String iterator = "qtask_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
    Integer limit = 50; // Integer | 
    Ordering order = Ordering.fromValue("ascending"); // Ordering | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseBackgroundTaskOut result = apiInstance.listBackgroundTasksApiV1BackgroundTaskGet(iterator, limit, order, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackgroundTasksApi#listBackgroundTasksApiV1BackgroundTaskGet");
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
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **order** | [**Ordering**](.md)|  | [optional] [default to descending] [enum: ascending, descending] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseBackgroundTaskOut**](ListResponseBackgroundTaskOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

