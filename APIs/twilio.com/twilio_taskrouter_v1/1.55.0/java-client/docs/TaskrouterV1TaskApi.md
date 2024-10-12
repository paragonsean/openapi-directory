# TaskrouterV1TaskApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTask**](TaskrouterV1TaskApi.md#createTask) | **POST** /v1/Workspaces/{WorkspaceSid}/Tasks |  |
| [**deleteTask**](TaskrouterV1TaskApi.md#deleteTask) | **DELETE** /v1/Workspaces/{WorkspaceSid}/Tasks/{Sid} |  |
| [**fetchTask**](TaskrouterV1TaskApi.md#fetchTask) | **GET** /v1/Workspaces/{WorkspaceSid}/Tasks/{Sid} |  |
| [**listTask**](TaskrouterV1TaskApi.md#listTask) | **GET** /v1/Workspaces/{WorkspaceSid}/Tasks |  |
| [**updateTask**](TaskrouterV1TaskApi.md#updateTask) | **POST** /v1/Workspaces/{WorkspaceSid}/Tasks/{Sid} |  |


<a id="createTask"></a>
# **createTask**
> TaskrouterV1WorkspaceTask createTask(workspaceSid, attributes, priority, taskChannel, timeout, virtualStartTime, workflowSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskApi apiInstance = new TaskrouterV1TaskApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new Task belongs to.
    String attributes = "attributes_example"; // String | A URL-encoded JSON string with the attributes of the new task. This value is passed to the Workflow's `assignment_callback_url` when the Task is assigned to a Worker. For example: `{ \\\"task_type\\\": \\\"call\\\", \\\"twilio_call_sid\\\": \\\"CAxxx\\\", \\\"customer_ticket_number\\\": \\\"12345\\\" }`.
    Integer priority = 56; // Integer | The priority to assign the new task and override the default. When supplied, the new Task will have this priority unless it matches a Workflow Target with a Priority set. When not supplied, the new Task will have the priority of the matching Workflow Target. Value can be 0 to 2^31^ (2,147,483,647).
    String taskChannel = "taskChannel_example"; // String | When MultiTasking is enabled, specify the TaskChannel by passing either its `unique_name` or `sid`. Default value is `default`.
    Integer timeout = 56; // Integer | The amount of time in seconds the new task can live before being assigned. Can be up to a maximum of 2 weeks (1,209,600 seconds). The default value is 24 hours (86,400 seconds). On timeout, the `task.canceled` event will fire with description `Task TTL Exceeded`.
    OffsetDateTime virtualStartTime = OffsetDateTime.now(); // OffsetDateTime | The virtual start time to assign the new task and override the default. When supplied, the new task will have this virtual start time. When not supplied, the new task will have the virtual start time equal to `date_created`. Value can't be in the future.
    String workflowSid = "workflowSid_example"; // String | The SID of the Workflow that you would like to handle routing for the new Task. If there is only one Workflow defined for the Workspace that you are posting the new task to, this parameter is optional.
    try {
      TaskrouterV1WorkspaceTask result = apiInstance.createTask(workspaceSid, attributes, priority, taskChannel, timeout, virtualStartTime, workflowSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskApi#createTask");
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
| **workspaceSid** | **String**| The SID of the Workspace that the new Task belongs to. | |
| **attributes** | **String**| A URL-encoded JSON string with the attributes of the new task. This value is passed to the Workflow&#39;s &#x60;assignment_callback_url&#x60; when the Task is assigned to a Worker. For example: &#x60;{ \\\&quot;task_type\\\&quot;: \\\&quot;call\\\&quot;, \\\&quot;twilio_call_sid\\\&quot;: \\\&quot;CAxxx\\\&quot;, \\\&quot;customer_ticket_number\\\&quot;: \\\&quot;12345\\\&quot; }&#x60;. | [optional] |
| **priority** | **Integer**| The priority to assign the new task and override the default. When supplied, the new Task will have this priority unless it matches a Workflow Target with a Priority set. When not supplied, the new Task will have the priority of the matching Workflow Target. Value can be 0 to 2^31^ (2,147,483,647). | [optional] |
| **taskChannel** | **String**| When MultiTasking is enabled, specify the TaskChannel by passing either its &#x60;unique_name&#x60; or &#x60;sid&#x60;. Default value is &#x60;default&#x60;. | [optional] |
| **timeout** | **Integer**| The amount of time in seconds the new task can live before being assigned. Can be up to a maximum of 2 weeks (1,209,600 seconds). The default value is 24 hours (86,400 seconds). On timeout, the &#x60;task.canceled&#x60; event will fire with description &#x60;Task TTL Exceeded&#x60;. | [optional] |
| **virtualStartTime** | **OffsetDateTime**| The virtual start time to assign the new task and override the default. When supplied, the new task will have this virtual start time. When not supplied, the new task will have the virtual start time equal to &#x60;date_created&#x60;. Value can&#39;t be in the future. | [optional] |
| **workflowSid** | **String**| The SID of the Workflow that you would like to handle routing for the new Task. If there is only one Workflow defined for the Workspace that you are posting the new task to, this parameter is optional. | [optional] |

### Return type

[**TaskrouterV1WorkspaceTask**](TaskrouterV1WorkspaceTask.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteTask"></a>
# **deleteTask**
> deleteTask(workspaceSid, sid, ifMatch)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskApi apiInstance = new TaskrouterV1TaskApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task to delete.
    String sid = "sid_example"; // String | The SID of the Task resource to delete.
    String ifMatch = "ifMatch_example"; // String | If provided, deletes this Task if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    try {
      apiInstance.deleteTask(workspaceSid, sid, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskApi#deleteTask");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Task to delete. | |
| **sid** | **String**| The SID of the Task resource to delete. | |
| **ifMatch** | **String**| If provided, deletes this Task if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] |

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

<a id="fetchTask"></a>
# **fetchTask**
> TaskrouterV1WorkspaceTask fetchTask(workspaceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskApi apiInstance = new TaskrouterV1TaskApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task to fetch.
    String sid = "sid_example"; // String | The SID of the Task resource to fetch.
    try {
      TaskrouterV1WorkspaceTask result = apiInstance.fetchTask(workspaceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskApi#fetchTask");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Task to fetch. | |
| **sid** | **String**| The SID of the Task resource to fetch. | |

### Return type

[**TaskrouterV1WorkspaceTask**](TaskrouterV1WorkspaceTask.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTask"></a>
# **listTask**
> ListTaskResponse listTask(workspaceSid, priority, assignmentStatus, workflowSid, workflowName, taskQueueSid, taskQueueName, evaluateTaskAttributes, ordering, hasAddons, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskApi apiInstance = new TaskrouterV1TaskApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Tasks to read.
    Integer priority = 56; // Integer | The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the specified priority.
    List<String> assignmentStatus = Arrays.asList(); // List<String> | The `assignment_status` of the Tasks you want to read. Can be: `pending`, `reserved`, `assigned`, `canceled`, `wrapping`, or `completed`. Returns all Tasks in the Workspace with the specified `assignment_status`.
    String workflowSid = "workflowSid_example"; // String | The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this SID.
    String workflowName = "workflowName_example"; // String | The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this friendly name.
    String taskQueueSid = "taskQueueSid_example"; // String | The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this SID.
    String taskQueueName = "taskQueueName_example"; // String | The `friendly_name` of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this friendly name.
    String evaluateTaskAttributes = "evaluateTaskAttributes_example"; // String | The attributes of the Tasks to read. Returns the Tasks that match the attributes specified in this parameter.
    String ordering = "ordering_example"; // String | How to order the returned Task resources. By default, Tasks are sorted by ascending DateCreated. This value is specified as: `Attribute:Order`, where `Attribute` can be either `DateCreated`, `Priority`, or `VirtualStartTime` and `Order` can be either `asc` or `desc`. For example, `Priority:desc` returns Tasks ordered in descending order of their Priority. Pairings of sort orders can be specified in a comma-separated list such as `Priority:desc,DateCreated:asc`, which returns the Tasks in descending Priority order and ascending DateCreated Order. The only ordering pairing not allowed is DateCreated and VirtualStartTime.
    Boolean hasAddons = true; // Boolean | Whether to read Tasks with Add-ons. If `true`, returns only Tasks with Add-ons. If `false`, returns only Tasks without Add-ons.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTaskResponse result = apiInstance.listTask(workspaceSid, priority, assignmentStatus, workflowSid, workflowName, taskQueueSid, taskQueueName, evaluateTaskAttributes, ordering, hasAddons, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskApi#listTask");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Tasks to read. | |
| **priority** | **Integer**| The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the specified priority. | [optional] |
| **assignmentStatus** | [**List&lt;String&gt;**](String.md)| The &#x60;assignment_status&#x60; of the Tasks you want to read. Can be: &#x60;pending&#x60;, &#x60;reserved&#x60;, &#x60;assigned&#x60;, &#x60;canceled&#x60;, &#x60;wrapping&#x60;, or &#x60;completed&#x60;. Returns all Tasks in the Workspace with the specified &#x60;assignment_status&#x60;. | [optional] |
| **workflowSid** | **String**| The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this SID. | [optional] |
| **workflowName** | **String**| The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this friendly name. | [optional] |
| **taskQueueSid** | **String**| The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this SID. | [optional] |
| **taskQueueName** | **String**| The &#x60;friendly_name&#x60; of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this friendly name. | [optional] |
| **evaluateTaskAttributes** | **String**| The attributes of the Tasks to read. Returns the Tasks that match the attributes specified in this parameter. | [optional] |
| **ordering** | **String**| How to order the returned Task resources. By default, Tasks are sorted by ascending DateCreated. This value is specified as: &#x60;Attribute:Order&#x60;, where &#x60;Attribute&#x60; can be either &#x60;DateCreated&#x60;, &#x60;Priority&#x60;, or &#x60;VirtualStartTime&#x60; and &#x60;Order&#x60; can be either &#x60;asc&#x60; or &#x60;desc&#x60;. For example, &#x60;Priority:desc&#x60; returns Tasks ordered in descending order of their Priority. Pairings of sort orders can be specified in a comma-separated list such as &#x60;Priority:desc,DateCreated:asc&#x60;, which returns the Tasks in descending Priority order and ascending DateCreated Order. The only ordering pairing not allowed is DateCreated and VirtualStartTime. | [optional] |
| **hasAddons** | **Boolean**| Whether to read Tasks with Add-ons. If &#x60;true&#x60;, returns only Tasks with Add-ons. If &#x60;false&#x60;, returns only Tasks without Add-ons. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTaskResponse**](ListTaskResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTask"></a>
# **updateTask**
> TaskrouterV1WorkspaceTask updateTask(workspaceSid, sid, ifMatch, assignmentStatus, attributes, priority, reason, taskChannel, virtualStartTime)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskApi apiInstance = new TaskrouterV1TaskApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task to update.
    String sid = "sid_example"; // String | The SID of the Task resource to update.
    String ifMatch = "ifMatch_example"; // String | If provided, applies this mutation if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
    TaskEnumStatus assignmentStatus = TaskEnumStatus.fromValue("pending"); // TaskEnumStatus | 
    String attributes = "attributes_example"; // String | The JSON string that describes the custom attributes of the task.
    Integer priority = 56; // Integer | The Task's new priority value. When supplied, the Task takes on the specified priority unless it matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647).
    String reason = "reason_example"; // String | The reason that the Task was canceled or completed. This parameter is required only if the Task is canceled or completed. Setting this value queues the task for deletion and logs the reason.
    String taskChannel = "taskChannel_example"; // String | When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
    OffsetDateTime virtualStartTime = OffsetDateTime.now(); // OffsetDateTime | The task's new virtual start time value. When supplied, the Task takes on the specified virtual start time. Value can't be in the future.
    try {
      TaskrouterV1WorkspaceTask result = apiInstance.updateTask(workspaceSid, sid, ifMatch, assignmentStatus, attributes, priority, reason, taskChannel, virtualStartTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskApi#updateTask");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Task to update. | |
| **sid** | **String**| The SID of the Task resource to update. | |
| **ifMatch** | **String**| If provided, applies this mutation if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] |
| **assignmentStatus** | **TaskEnumStatus**|  | [optional] [enum: pending, reserved, assigned, canceled, completed, wrapping] |
| **attributes** | **String**| The JSON string that describes the custom attributes of the task. | [optional] |
| **priority** | **Integer**| The Task&#39;s new priority value. When supplied, the Task takes on the specified priority unless it matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647). | [optional] |
| **reason** | **String**| The reason that the Task was canceled or completed. This parameter is required only if the Task is canceled or completed. Setting this value queues the task for deletion and logs the reason. | [optional] |
| **taskChannel** | **String**| When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] |
| **virtualStartTime** | **OffsetDateTime**| The task&#39;s new virtual start time value. When supplied, the Task takes on the specified virtual start time. Value can&#39;t be in the future. | [optional] |

### Return type

[**TaskrouterV1WorkspaceTask**](TaskrouterV1WorkspaceTask.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

