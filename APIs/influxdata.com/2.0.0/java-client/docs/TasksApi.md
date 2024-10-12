# TasksApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteTasksID**](TasksApi.md#deleteTasksID) | **DELETE** /tasks/{taskID} | Delete a task |
| [**deleteTasksIDLabelsID**](TasksApi.md#deleteTasksIDLabelsID) | **DELETE** /tasks/{taskID}/labels/{labelID} | Delete a label from a task |
| [**deleteTasksIDMembersID**](TasksApi.md#deleteTasksIDMembersID) | **DELETE** /tasks/{taskID}/members/{userID} | Remove a member from a task |
| [**deleteTasksIDOwnersID**](TasksApi.md#deleteTasksIDOwnersID) | **DELETE** /tasks/{taskID}/owners/{userID} | Remove an owner from a task |
| [**deleteTasksIDRunsID**](TasksApi.md#deleteTasksIDRunsID) | **DELETE** /tasks/{taskID}/runs/{runID} | Cancel a running task |
| [**getTasks**](TasksApi.md#getTasks) | **GET** /tasks | List all tasks |
| [**getTasksID**](TasksApi.md#getTasksID) | **GET** /tasks/{taskID} | Retrieve a task |
| [**getTasksIDLabels**](TasksApi.md#getTasksIDLabels) | **GET** /tasks/{taskID}/labels | List all labels for a task |
| [**getTasksIDLogs**](TasksApi.md#getTasksIDLogs) | **GET** /tasks/{taskID}/logs | Retrieve all logs for a task |
| [**getTasksIDMembers**](TasksApi.md#getTasksIDMembers) | **GET** /tasks/{taskID}/members | List all task members |
| [**getTasksIDOwners**](TasksApi.md#getTasksIDOwners) | **GET** /tasks/{taskID}/owners | List all owners of a task |
| [**getTasksIDRuns**](TasksApi.md#getTasksIDRuns) | **GET** /tasks/{taskID}/runs | List runs for a task |
| [**getTasksIDRunsID**](TasksApi.md#getTasksIDRunsID) | **GET** /tasks/{taskID}/runs/{runID} | Retrieve a single run for a task |
| [**getTasksIDRunsIDLogs**](TasksApi.md#getTasksIDRunsIDLogs) | **GET** /tasks/{taskID}/runs/{runID}/logs | Retrieve all logs for a run |
| [**patchTasksID**](TasksApi.md#patchTasksID) | **PATCH** /tasks/{taskID} | Update a task |
| [**postTasks**](TasksApi.md#postTasks) | **POST** /tasks | Create a new task |
| [**postTasksIDLabels**](TasksApi.md#postTasksIDLabels) | **POST** /tasks/{taskID}/labels | Add a label to a task |
| [**postTasksIDMembers**](TasksApi.md#postTasksIDMembers) | **POST** /tasks/{taskID}/members | Add a member to a task |
| [**postTasksIDOwners**](TasksApi.md#postTasksIDOwners) | **POST** /tasks/{taskID}/owners | Add an owner to a task |
| [**postTasksIDRuns**](TasksApi.md#postTasksIDRuns) | **POST** /tasks/{taskID}/runs | Manually start a task run, overriding the current schedule |
| [**postTasksIDRunsIDRetry**](TasksApi.md#postTasksIDRunsIDRetry) | **POST** /tasks/{taskID}/runs/{runID}/retry | Retry a task run |


<a id="deleteTasksID"></a>
# **deleteTasksID**
> deleteTasksID(taskID, zapTraceSpan)

Delete a task

Deletes a task and all associated records

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The ID of the task to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteTasksID(taskID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#deleteTasksID");
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
| **taskID** | **String**| The ID of the task to delete. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Task deleted |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteTasksIDLabelsID"></a>
# **deleteTasksIDLabelsID**
> deleteTasksIDLabelsID(taskID, labelID, zapTraceSpan)

Delete a label from a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    String labelID = "labelID_example"; // String | The label ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteTasksIDLabelsID(taskID, labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#deleteTasksIDLabelsID");
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
| **taskID** | **String**| The task ID. | |
| **labelID** | **String**| The label ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **404** | Task not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteTasksIDMembersID"></a>
# **deleteTasksIDMembersID**
> deleteTasksIDMembersID(userID, taskID, zapTraceSpan)

Remove a member from a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String userID = "userID_example"; // String | The ID of the member to remove.
    String taskID = "taskID_example"; // String | The task ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteTasksIDMembersID(userID, taskID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#deleteTasksIDMembersID");
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
| **userID** | **String**| The ID of the member to remove. | |
| **taskID** | **String**| The task ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Member removed |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteTasksIDOwnersID"></a>
# **deleteTasksIDOwnersID**
> deleteTasksIDOwnersID(userID, taskID, zapTraceSpan)

Remove an owner from a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String userID = "userID_example"; // String | The ID of the owner to remove.
    String taskID = "taskID_example"; // String | The task ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteTasksIDOwnersID(userID, taskID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#deleteTasksIDOwnersID");
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
| **userID** | **String**| The ID of the owner to remove. | |
| **taskID** | **String**| The task ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Owner removed |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteTasksIDRunsID"></a>
# **deleteTasksIDRunsID**
> deleteTasksIDRunsID(taskID, runID, zapTraceSpan)

Cancel a running task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    String runID = "runID_example"; // String | The run ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteTasksIDRunsID(taskID, runID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#deleteTasksIDRunsID");
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
| **taskID** | **String**| The task ID. | |
| **runID** | **String**| The run ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **0** | Unexpected error |  -  |

<a id="getTasks"></a>
# **getTasks**
> Tasks getTasks(zapTraceSpan, name, after, user, org, orgID, status, limit)

List all tasks

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String name = "name_example"; // String | Returns task with a specific name.
    String after = "after_example"; // String | Return tasks after a specified ID.
    String user = "user_example"; // String | Filter tasks to a specific user ID.
    String org = "org_example"; // String | Filter tasks to a specific organization name.
    String orgID = "orgID_example"; // String | Filter tasks to a specific organization ID.
    String status = "active"; // String | Filter tasks by a status--\"inactive\" or \"active\".
    Integer limit = 100; // Integer | The number of tasks to return
    try {
      Tasks result = apiInstance.getTasks(zapTraceSpan, name, after, user, org, orgID, status, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getTasks");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **name** | **String**| Returns task with a specific name. | [optional] |
| **after** | **String**| Return tasks after a specified ID. | [optional] |
| **user** | **String**| Filter tasks to a specific user ID. | [optional] |
| **org** | **String**| Filter tasks to a specific organization name. | [optional] |
| **orgID** | **String**| Filter tasks to a specific organization ID. | [optional] |
| **status** | **String**| Filter tasks by a status--\&quot;inactive\&quot; or \&quot;active\&quot;. | [optional] [enum: active, inactive] |
| **limit** | **Integer**| The number of tasks to return | [optional] [default to 100] |

### Return type

[**Tasks**](Tasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of tasks |  -  |
| **0** | Unexpected error |  -  |

<a id="getTasksID"></a>
# **getTasksID**
> Task getTasksID(taskID, zapTraceSpan)

Retrieve a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Task result = apiInstance.getTasksID(taskID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getTasksID");
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
| **taskID** | **String**| The task ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Task details |  -  |
| **0** | Unexpected error |  -  |

<a id="getTasksIDLabels"></a>
# **getTasksIDLabels**
> LabelsResponse getTasksIDLabels(taskID, zapTraceSpan)

List all labels for a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelsResponse result = apiInstance.getTasksIDLabels(taskID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getTasksIDLabels");
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
| **taskID** | **String**| The task ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all labels for a task |  -  |
| **0** | Unexpected error |  -  |

<a id="getTasksIDLogs"></a>
# **getTasksIDLogs**
> Logs getTasksIDLogs(taskID, zapTraceSpan)

Retrieve all logs for a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Logs result = apiInstance.getTasksIDLogs(taskID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getTasksIDLogs");
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
| **taskID** | **String**| The task ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Logs**](Logs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All logs for a task |  -  |
| **0** | Unexpected error |  -  |

<a id="getTasksIDMembers"></a>
# **getTasksIDMembers**
> ResourceMembers getTasksIDMembers(taskID, zapTraceSpan)

List all task members

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMembers result = apiInstance.getTasksIDMembers(taskID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getTasksIDMembers");
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
| **taskID** | **String**| The task ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of users who have member privileges for a task |  -  |
| **0** | Unexpected error |  -  |

<a id="getTasksIDOwners"></a>
# **getTasksIDOwners**
> ResourceOwners getTasksIDOwners(taskID, zapTraceSpan)

List all owners of a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwners result = apiInstance.getTasksIDOwners(taskID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getTasksIDOwners");
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
| **taskID** | **String**| The task ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of users who have owner privileges for a task |  -  |
| **0** | Unexpected error |  -  |

<a id="getTasksIDRuns"></a>
# **getTasksIDRuns**
> Runs getTasksIDRuns(taskID, zapTraceSpan, after, limit, afterTime, beforeTime)

List runs for a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The ID of the task to get runs for.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String after = "after_example"; // String | Returns runs after a specific ID.
    Integer limit = 100; // Integer | The number of runs to return
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | Filter runs to those scheduled after this time, RFC3339
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | Filter runs to those scheduled before this time, RFC3339
    try {
      Runs result = apiInstance.getTasksIDRuns(taskID, zapTraceSpan, after, limit, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getTasksIDRuns");
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
| **taskID** | **String**| The ID of the task to get runs for. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **after** | **String**| Returns runs after a specific ID. | [optional] |
| **limit** | **Integer**| The number of runs to return | [optional] [default to 100] |
| **afterTime** | **OffsetDateTime**| Filter runs to those scheduled after this time, RFC3339 | [optional] |
| **beforeTime** | **OffsetDateTime**| Filter runs to those scheduled before this time, RFC3339 | [optional] |

### Return type

[**Runs**](Runs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of task runs |  -  |
| **0** | Unexpected error |  -  |

<a id="getTasksIDRunsID"></a>
# **getTasksIDRunsID**
> Run getTasksIDRunsID(taskID, runID, zapTraceSpan)

Retrieve a single run for a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    String runID = "runID_example"; // String | The run ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Run result = apiInstance.getTasksIDRunsID(taskID, runID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getTasksIDRunsID");
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
| **taskID** | **String**| The task ID. | |
| **runID** | **String**| The run ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The run record |  -  |
| **0** | Unexpected error |  -  |

<a id="getTasksIDRunsIDLogs"></a>
# **getTasksIDRunsIDLogs**
> Logs getTasksIDRunsIDLogs(taskID, runID, zapTraceSpan)

Retrieve all logs for a run

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | ID of task to get logs for.
    String runID = "runID_example"; // String | ID of run to get logs for.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Logs result = apiInstance.getTasksIDRunsIDLogs(taskID, runID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#getTasksIDRunsIDLogs");
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
| **taskID** | **String**| ID of task to get logs for. | |
| **runID** | **String**| ID of run to get logs for. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Logs**](Logs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All logs for a run |  -  |
| **0** | Unexpected error |  -  |

<a id="patchTasksID"></a>
# **patchTasksID**
> Task patchTasksID(taskID, taskUpdateRequest, zapTraceSpan)

Update a task

Update a task. This will cancel all queued runs.

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    TaskUpdateRequest taskUpdateRequest = new TaskUpdateRequest(); // TaskUpdateRequest | Task update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Task result = apiInstance.patchTasksID(taskID, taskUpdateRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#patchTasksID");
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
| **taskID** | **String**| The task ID. | |
| **taskUpdateRequest** | [**TaskUpdateRequest**](TaskUpdateRequest.md)| Task update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Task updated |  -  |
| **0** | Unexpected error |  -  |

<a id="postTasks"></a>
# **postTasks**
> Task postTasks(taskCreateRequest, zapTraceSpan)

Create a new task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    TaskCreateRequest taskCreateRequest = new TaskCreateRequest(); // TaskCreateRequest | Task to create
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Task result = apiInstance.postTasks(taskCreateRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#postTasks");
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
| **taskCreateRequest** | [**TaskCreateRequest**](TaskCreateRequest.md)| Task to create | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Task created |  -  |
| **0** | Unexpected error |  -  |

<a id="postTasksIDLabels"></a>
# **postTasksIDLabels**
> LabelResponse postTasksIDLabels(taskID, labelMapping, zapTraceSpan)

Add a label to a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    LabelMapping labelMapping = new LabelMapping(); // LabelMapping | Label to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.postTasksIDLabels(taskID, labelMapping, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#postTasksIDLabels");
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
| **taskID** | **String**| The task ID. | |
| **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A list of all labels for a task |  -  |
| **0** | Unexpected error |  -  |

<a id="postTasksIDMembers"></a>
# **postTasksIDMembers**
> ResourceMember postTasksIDMembers(taskID, addResourceMemberRequestBody, zapTraceSpan)

Add a member to a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMember result = apiInstance.postTasksIDMembers(taskID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#postTasksIDMembers");
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
| **taskID** | **String**| The task ID. | |
| **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added to task members |  -  |
| **0** | Unexpected error |  -  |

<a id="postTasksIDOwners"></a>
# **postTasksIDOwners**
> ResourceOwner postTasksIDOwners(taskID, addResourceMemberRequestBody, zapTraceSpan)

Add an owner to a task

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwner result = apiInstance.postTasksIDOwners(taskID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#postTasksIDOwners");
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
| **taskID** | **String**| The task ID. | |
| **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added to task owners |  -  |
| **0** | Unexpected error |  -  |

<a id="postTasksIDRuns"></a>
# **postTasksIDRuns**
> Run postTasksIDRuns(taskID, zapTraceSpan, runManually)

Manually start a task run, overriding the current schedule

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | 
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    RunManually runManually = new RunManually(); // RunManually | 
    try {
      Run result = apiInstance.postTasksIDRuns(taskID, zapTraceSpan, runManually);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#postTasksIDRuns");
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
| **taskID** | **String**|  | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **runManually** | [**RunManually**](RunManually.md)|  | [optional] |

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Run scheduled to start |  -  |
| **0** | Unexpected error |  -  |

<a id="postTasksIDRunsIDRetry"></a>
# **postTasksIDRunsIDRetry**
> Run postTasksIDRunsIDRetry(taskID, runID, zapTraceSpan, body)

Retry a task run

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
    defaultClient.setBasePath("/api/v2");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String taskID = "taskID_example"; // String | The task ID.
    String runID = "runID_example"; // String | The run ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    Object body = null; // Object | 
    try {
      Run result = apiInstance.postTasksIDRunsIDRetry(taskID, runID, zapTraceSpan, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#postTasksIDRunsIDRetry");
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
| **taskID** | **String**| The task ID. | |
| **runID** | **String**| The run ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **body** | **Object**|  | [optional] |

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Run that has been queued |  -  |
| **0** | Unexpected error |  -  |

