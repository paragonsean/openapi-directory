# TasksApi

All URIs are relative to *http://localhost:7700*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelTasks**](TasksApi.md#cancelTasks) | **POST** /tasks/cancel | Cancel tasks |
| [**deleteTasks**](TasksApi.md#deleteTasks) | **DELETE** /tasks | Delete tasks |
| [**getAllTasks**](TasksApi.md#getAllTasks) | **GET** /tasks | Get all tasks |
| [**getOneTask**](TasksApi.md#getOneTask) | **GET** /tasks/0 | Get one task |


<a id="cancelTasks"></a>
# **cancelTasks**
> cancelTasks(uids, indexUids, types, statuses, beforeEnqueuedAt, afterEnqueuedAt, beforeStartedAt, afterStartedAt, beforeFinishedAt, afterFinishedAt, canceledBy, limit, from)

Cancel tasks

Cancel tasks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String uids = "uids_example"; // String | 
    String indexUids = "books"; // String | 
    String types = "documentAdditionOrUpdate"; // String | 
    String statuses = "failed"; // String | 
    String beforeEnqueuedAt = "beforeEnqueuedAt_example"; // String | 
    String afterEnqueuedAt = "afterEnqueuedAt_example"; // String | 
    String beforeStartedAt = "beforeStartedAt_example"; // String | 
    String afterStartedAt = "afterStartedAt_example"; // String | 
    String beforeFinishedAt = "beforeFinishedAt_example"; // String | 
    String afterFinishedAt = "afterFinishedAt_example"; // String | 
    String canceledBy = "canceledBy_example"; // String | 
    String limit = "2"; // String | 
    String from = "10"; // String | 
    try {
      apiInstance.cancelTasks(uids, indexUids, types, statuses, beforeEnqueuedAt, afterEnqueuedAt, beforeStartedAt, afterStartedAt, beforeFinishedAt, afterFinishedAt, canceledBy, limit, from);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#cancelTasks");
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
| **uids** | **String**|  | [optional] |
| **indexUids** | **String**|  | [optional] |
| **types** | **String**|  | [optional] |
| **statuses** | **String**|  | [optional] |
| **beforeEnqueuedAt** | **String**|  | [optional] |
| **afterEnqueuedAt** | **String**|  | [optional] |
| **beforeStartedAt** | **String**|  | [optional] |
| **afterStartedAt** | **String**|  | [optional] |
| **beforeFinishedAt** | **String**|  | [optional] |
| **afterFinishedAt** | **String**|  | [optional] |
| **canceledBy** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |
| **from** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="deleteTasks"></a>
# **deleteTasks**
> deleteTasks(uids, indexUids, types, statuses, beforeEnqueuedAt, afterEnqueuedAt, beforeStartedAt, afterStartedAt, beforeFinishedAt, afterFinishedAt, canceledBy, limit, from)

Delete tasks

Delete tasks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String uids = "uids_example"; // String | 
    String indexUids = "books"; // String | 
    String types = "documentAdditionOrUpdate"; // String | 
    String statuses = "failed"; // String | 
    String beforeEnqueuedAt = "beforeEnqueuedAt_example"; // String | 
    String afterEnqueuedAt = "afterEnqueuedAt_example"; // String | 
    String beforeStartedAt = "beforeStartedAt_example"; // String | 
    String afterStartedAt = "afterStartedAt_example"; // String | 
    String beforeFinishedAt = "beforeFinishedAt_example"; // String | 
    String afterFinishedAt = "afterFinishedAt_example"; // String | 
    String canceledBy = "canceledBy_example"; // String | 
    String limit = "2"; // String | 
    String from = "10"; // String | 
    try {
      apiInstance.deleteTasks(uids, indexUids, types, statuses, beforeEnqueuedAt, afterEnqueuedAt, beforeStartedAt, afterStartedAt, beforeFinishedAt, afterFinishedAt, canceledBy, limit, from);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#deleteTasks");
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
| **uids** | **String**|  | [optional] |
| **indexUids** | **String**|  | [optional] |
| **types** | **String**|  | [optional] |
| **statuses** | **String**|  | [optional] |
| **beforeEnqueuedAt** | **String**|  | [optional] |
| **afterEnqueuedAt** | **String**|  | [optional] |
| **beforeStartedAt** | **String**|  | [optional] |
| **afterStartedAt** | **String**|  | [optional] |
| **beforeFinishedAt** | **String**|  | [optional] |
| **afterFinishedAt** | **String**|  | [optional] |
| **canceledBy** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |
| **from** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="getAllTasks"></a>
# **getAllTasks**
> getAllTasks(uids, indexUids, types, statuses, beforeEnqueuedAt, afterEnqueuedAt, beforeStartedAt, afterStartedAt, beforeFinishedAt, afterFinishedAt, canceledBy, limit, from)

Get all tasks

Get all tasks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String uids = "3"; // String | 
    String indexUids = "books"; // String | 
    String types = "documentAdditionOrUpdate"; // String | 
    String statuses = "failed"; // String | 
    String beforeEnqueuedAt = "beforeEnqueuedAt_example"; // String | 
    String afterEnqueuedAt = "afterEnqueuedAt_example"; // String | 
    String beforeStartedAt = "beforeStartedAt_example"; // String | 
    String afterStartedAt = "afterStartedAt_example"; // String | 
    String beforeFinishedAt = "beforeFinishedAt_example"; // String | 
    String afterFinishedAt = "afterFinishedAt_example"; // String | 
    String canceledBy = "canceledBy_example"; // String | 
    String limit = "2"; // String | 
    String from = "10"; // String | 
    try {
      apiInstance.getAllTasks(uids, indexUids, types, statuses, beforeEnqueuedAt, afterEnqueuedAt, beforeStartedAt, afterStartedAt, beforeFinishedAt, afterFinishedAt, canceledBy, limit, from);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getAllTasks");
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
| **uids** | **String**|  | [optional] |
| **indexUids** | **String**|  | [optional] |
| **types** | **String**|  | [optional] |
| **statuses** | **String**|  | [optional] |
| **beforeEnqueuedAt** | **String**|  | [optional] |
| **afterEnqueuedAt** | **String**|  | [optional] |
| **beforeStartedAt** | **String**|  | [optional] |
| **afterStartedAt** | **String**|  | [optional] |
| **beforeFinishedAt** | **String**|  | [optional] |
| **afterFinishedAt** | **String**|  | [optional] |
| **canceledBy** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |
| **from** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="getOneTask"></a>
# **getOneTask**
> getOneTask()

Get one task

Get one task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    TasksApi apiInstance = new TasksApi(defaultClient);
    try {
      apiInstance.getOneTask();
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getOneTask");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

