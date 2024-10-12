# TaskrouterV1TaskQueueApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTaskQueue**](TaskrouterV1TaskQueueApi.md#createTaskQueue) | **POST** /v1/Workspaces/{WorkspaceSid}/TaskQueues |  |
| [**deleteTaskQueue**](TaskrouterV1TaskQueueApi.md#deleteTaskQueue) | **DELETE** /v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid} |  |
| [**fetchTaskQueue**](TaskrouterV1TaskQueueApi.md#fetchTaskQueue) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid} |  |
| [**listTaskQueue**](TaskrouterV1TaskQueueApi.md#listTaskQueue) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskQueues |  |
| [**updateTaskQueue**](TaskrouterV1TaskQueueApi.md#updateTaskQueue) | **POST** /v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid} |  |


<a id="createTaskQueue"></a>
# **createTaskQueue**
> TaskrouterV1WorkspaceTaskQueue createTaskQueue(workspaceSid, friendlyName, assignmentActivitySid, maxReservedWorkers, reservationActivitySid, targetWorkers, taskOrder)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskQueueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskQueueApi apiInstance = new TaskrouterV1TaskQueueApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new TaskQueue belongs to.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the TaskQueue. For example `Support-Tier 1`, `Sales`, or `Escalation`.
    String assignmentActivitySid = "assignmentActivitySid_example"; // String | The SID of the Activity to assign Workers when a task is assigned to them.
    Integer maxReservedWorkers = 56; // Integer | The maximum number of Workers to reserve for the assignment of a Task in the queue. Can be an integer between 1 and 50, inclusive and defaults to 1.
    String reservationActivitySid = "reservationActivitySid_example"; // String | The SID of the Activity to assign Workers when a task is reserved for them.
    String targetWorkers = "targetWorkers_example"; // String | A string that describes the Worker selection criteria for any Tasks that enter the TaskQueue. For example, `'\\\"language\\\" == \\\"spanish\\\"'`. The default value is `1==1`. If this value is empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more information about Worker selection, see [Describing Worker selection criteria](https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers).
    TaskQueueEnumTaskOrder taskOrder = TaskQueueEnumTaskOrder.fromValue("FIFO"); // TaskQueueEnumTaskOrder | 
    try {
      TaskrouterV1WorkspaceTaskQueue result = apiInstance.createTaskQueue(workspaceSid, friendlyName, assignmentActivitySid, maxReservedWorkers, reservationActivitySid, targetWorkers, taskOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskQueueApi#createTaskQueue");
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
| **workspaceSid** | **String**| The SID of the Workspace that the new TaskQueue belongs to. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the TaskQueue. For example &#x60;Support-Tier 1&#x60;, &#x60;Sales&#x60;, or &#x60;Escalation&#x60;. | |
| **assignmentActivitySid** | **String**| The SID of the Activity to assign Workers when a task is assigned to them. | [optional] |
| **maxReservedWorkers** | **Integer**| The maximum number of Workers to reserve for the assignment of a Task in the queue. Can be an integer between 1 and 50, inclusive and defaults to 1. | [optional] |
| **reservationActivitySid** | **String**| The SID of the Activity to assign Workers when a task is reserved for them. | [optional] |
| **targetWorkers** | **String**| A string that describes the Worker selection criteria for any Tasks that enter the TaskQueue. For example, &#x60;&#39;\\\&quot;language\\\&quot; &#x3D;&#x3D; \\\&quot;spanish\\\&quot;&#39;&#x60;. The default value is &#x60;1&#x3D;&#x3D;1&#x60;. If this value is empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more information about Worker selection, see [Describing Worker selection criteria](https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers). | [optional] |
| **taskOrder** | **TaskQueueEnumTaskOrder**|  | [optional] [enum: FIFO, LIFO] |

### Return type

[**TaskrouterV1WorkspaceTaskQueue**](TaskrouterV1WorkspaceTaskQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteTaskQueue"></a>
# **deleteTaskQueue**
> deleteTaskQueue(workspaceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskQueueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskQueueApi apiInstance = new TaskrouterV1TaskQueueApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to delete.
    String sid = "sid_example"; // String | The SID of the TaskQueue resource to delete.
    try {
      apiInstance.deleteTaskQueue(workspaceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskQueueApi#deleteTaskQueue");
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
| **workspaceSid** | **String**| The SID of the Workspace with the TaskQueue to delete. | |
| **sid** | **String**| The SID of the TaskQueue resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchTaskQueue"></a>
# **fetchTaskQueue**
> TaskrouterV1WorkspaceTaskQueue fetchTaskQueue(workspaceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskQueueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskQueueApi apiInstance = new TaskrouterV1TaskQueueApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to fetch.
    String sid = "sid_example"; // String | The SID of the TaskQueue resource to fetch.
    try {
      TaskrouterV1WorkspaceTaskQueue result = apiInstance.fetchTaskQueue(workspaceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskQueueApi#fetchTaskQueue");
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
| **workspaceSid** | **String**| The SID of the Workspace with the TaskQueue to fetch. | |
| **sid** | **String**| The SID of the TaskQueue resource to fetch. | |

### Return type

[**TaskrouterV1WorkspaceTaskQueue**](TaskrouterV1WorkspaceTaskQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTaskQueue"></a>
# **listTaskQueue**
> ListTaskQueueResponse listTaskQueue(workspaceSid, friendlyName, evaluateWorkerAttributes, workerSid, ordering, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskQueueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskQueueApi apiInstance = new TaskrouterV1TaskQueueApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to read.
    String friendlyName = "friendlyName_example"; // String | The `friendly_name` of the TaskQueue resources to read.
    String evaluateWorkerAttributes = "evaluateWorkerAttributes_example"; // String | The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter.
    String workerSid = "workerSid_example"; // String | The SID of the Worker with the TaskQueue resources to read.
    String ordering = "ordering_example"; // String | Sorting parameter for TaskQueues
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTaskQueueResponse result = apiInstance.listTaskQueue(workspaceSid, friendlyName, evaluateWorkerAttributes, workerSid, ordering, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskQueueApi#listTaskQueue");
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
| **workspaceSid** | **String**| The SID of the Workspace with the TaskQueue to read. | |
| **friendlyName** | **String**| The &#x60;friendly_name&#x60; of the TaskQueue resources to read. | [optional] |
| **evaluateWorkerAttributes** | **String**| The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter. | [optional] |
| **workerSid** | **String**| The SID of the Worker with the TaskQueue resources to read. | [optional] |
| **ordering** | **String**| Sorting parameter for TaskQueues | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTaskQueueResponse**](ListTaskQueueResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTaskQueue"></a>
# **updateTaskQueue**
> TaskrouterV1WorkspaceTaskQueue updateTaskQueue(workspaceSid, sid, assignmentActivitySid, friendlyName, maxReservedWorkers, reservationActivitySid, targetWorkers, taskOrder)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskQueueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskQueueApi apiInstance = new TaskrouterV1TaskQueueApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to update.
    String sid = "sid_example"; // String | The SID of the TaskQueue resource to update.
    String assignmentActivitySid = "assignmentActivitySid_example"; // String | The SID of the Activity to assign Workers when a task is assigned for them.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the TaskQueue. For example `Support-Tier 1`, `Sales`, or `Escalation`.
    Integer maxReservedWorkers = 56; // Integer | The maximum number of Workers to create reservations for the assignment of a task while in the queue. Maximum of 50.
    String reservationActivitySid = "reservationActivitySid_example"; // String | The SID of the Activity to assign Workers when a task is reserved for them.
    String targetWorkers = "targetWorkers_example"; // String | A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example '\\\"language\\\" == \\\"spanish\\\"' If no TargetWorkers parameter is provided, Tasks will wait in the queue until they are either deleted or moved to another queue. Additional examples on how to describing Worker selection criteria below.
    TaskQueueEnumTaskOrder taskOrder = TaskQueueEnumTaskOrder.fromValue("FIFO"); // TaskQueueEnumTaskOrder | 
    try {
      TaskrouterV1WorkspaceTaskQueue result = apiInstance.updateTaskQueue(workspaceSid, sid, assignmentActivitySid, friendlyName, maxReservedWorkers, reservationActivitySid, targetWorkers, taskOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskQueueApi#updateTaskQueue");
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
| **workspaceSid** | **String**| The SID of the Workspace with the TaskQueue to update. | |
| **sid** | **String**| The SID of the TaskQueue resource to update. | |
| **assignmentActivitySid** | **String**| The SID of the Activity to assign Workers when a task is assigned for them. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the TaskQueue. For example &#x60;Support-Tier 1&#x60;, &#x60;Sales&#x60;, or &#x60;Escalation&#x60;. | [optional] |
| **maxReservedWorkers** | **Integer**| The maximum number of Workers to create reservations for the assignment of a task while in the queue. Maximum of 50. | [optional] |
| **reservationActivitySid** | **String**| The SID of the Activity to assign Workers when a task is reserved for them. | [optional] |
| **targetWorkers** | **String**| A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example &#39;\\\&quot;language\\\&quot; &#x3D;&#x3D; \\\&quot;spanish\\\&quot;&#39; If no TargetWorkers parameter is provided, Tasks will wait in the queue until they are either deleted or moved to another queue. Additional examples on how to describing Worker selection criteria below. | [optional] |
| **taskOrder** | **TaskQueueEnumTaskOrder**|  | [optional] [enum: FIFO, LIFO] |

### Return type

[**TaskrouterV1WorkspaceTaskQueue**](TaskrouterV1WorkspaceTaskQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

