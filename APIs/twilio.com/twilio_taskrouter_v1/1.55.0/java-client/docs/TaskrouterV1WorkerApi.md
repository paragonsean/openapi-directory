# TaskrouterV1WorkerApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWorker**](TaskrouterV1WorkerApi.md#createWorker) | **POST** /v1/Workspaces/{WorkspaceSid}/Workers |  |
| [**deleteWorker**](TaskrouterV1WorkerApi.md#deleteWorker) | **DELETE** /v1/Workspaces/{WorkspaceSid}/Workers/{Sid} |  |
| [**fetchWorker**](TaskrouterV1WorkerApi.md#fetchWorker) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{Sid} |  |
| [**listWorker**](TaskrouterV1WorkerApi.md#listWorker) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers |  |
| [**updateWorker**](TaskrouterV1WorkerApi.md#updateWorker) | **POST** /v1/Workspaces/{WorkspaceSid}/Workers/{Sid} |  |


<a id="createWorker"></a>
# **createWorker**
> TaskrouterV1WorkspaceWorker createWorker(workspaceSid, friendlyName, activitySid, attributes)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkerApi apiInstance = new TaskrouterV1WorkerApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new Worker belongs to.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new Worker. It can be up to 64 characters long.
    String activitySid = "activitySid_example"; // String | The SID of a valid Activity that will describe the new Worker's initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information. If not provided, the new Worker's initial state is the `default_activity_sid` configured on the Workspace.
    String attributes = "attributes_example"; // String | A valid JSON string that describes the new Worker. For example: `{ \\\"email\\\": \\\"Bob@example.com\\\", \\\"phone\\\": \\\"+5095551234\\\" }`. This data is passed to the `assignment_callback_url` when TaskRouter assigns a Task to the Worker. Defaults to {}.
    try {
      TaskrouterV1WorkspaceWorker result = apiInstance.createWorker(workspaceSid, friendlyName, activitySid, attributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkerApi#createWorker");
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
| **workspaceSid** | **String**| The SID of the Workspace that the new Worker belongs to. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the new Worker. It can be up to 64 characters long. | |
| **activitySid** | **String**| The SID of a valid Activity that will describe the new Worker&#39;s initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information. If not provided, the new Worker&#39;s initial state is the &#x60;default_activity_sid&#x60; configured on the Workspace. | [optional] |
| **attributes** | **String**| A valid JSON string that describes the new Worker. For example: &#x60;{ \\\&quot;email\\\&quot;: \\\&quot;Bob@example.com\\\&quot;, \\\&quot;phone\\\&quot;: \\\&quot;+5095551234\\\&quot; }&#x60;. This data is passed to the &#x60;assignment_callback_url&#x60; when TaskRouter assigns a Task to the Worker. Defaults to {}. | [optional] |

### Return type

[**TaskrouterV1WorkspaceWorker**](TaskrouterV1WorkspaceWorker.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteWorker"></a>
# **deleteWorker**
> deleteWorker(workspaceSid, sid, ifMatch)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkerApi apiInstance = new TaskrouterV1WorkerApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Worker to delete.
    String sid = "sid_example"; // String | The SID of the Worker resource to delete.
    String ifMatch = "ifMatch_example"; // String | The If-Match HTTP request header
    try {
      apiInstance.deleteWorker(workspaceSid, sid, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkerApi#deleteWorker");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Worker to delete. | |
| **sid** | **String**| The SID of the Worker resource to delete. | |
| **ifMatch** | **String**| The If-Match HTTP request header | [optional] |

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

<a id="fetchWorker"></a>
# **fetchWorker**
> TaskrouterV1WorkspaceWorker fetchWorker(workspaceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkerApi apiInstance = new TaskrouterV1WorkerApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Worker to fetch.
    String sid = "sid_example"; // String | The SID of the Worker resource to fetch.
    try {
      TaskrouterV1WorkspaceWorker result = apiInstance.fetchWorker(workspaceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkerApi#fetchWorker");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Worker to fetch. | |
| **sid** | **String**| The SID of the Worker resource to fetch. | |

### Return type

[**TaskrouterV1WorkspaceWorker**](TaskrouterV1WorkspaceWorker.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listWorker"></a>
# **listWorker**
> ListWorkerResponse listWorker(workspaceSid, activityName, activitySid, available, friendlyName, targetWorkersExpression, taskQueueName, taskQueueSid, ordering, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkerApi apiInstance = new TaskrouterV1WorkerApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workers to read.
    String activityName = "activityName_example"; // String | The `activity_name` of the Worker resources to read.
    String activitySid = "activitySid_example"; // String | The `activity_sid` of the Worker resources to read.
    String available = "available_example"; // String | Whether to return only Worker resources that are available or unavailable. Can be `true`, `1`, or `yes` to return Worker resources that are available, and `false`, or any value returns the Worker resources that are not available.
    String friendlyName = "friendlyName_example"; // String | The `friendly_name` of the Worker resources to read.
    String targetWorkersExpression = "targetWorkersExpression_example"; // String | Filter by Workers that would match an expression. In addition to fields in the workers' attributes, the expression can include the following worker fields: `sid`, `friendly_name`, `activity_sid`, or `activity_name`
    String taskQueueName = "taskQueueName_example"; // String | The `friendly_name` of the TaskQueue that the Workers to read are eligible for.
    String taskQueueSid = "taskQueueSid_example"; // String | The SID of the TaskQueue that the Workers to read are eligible for.
    String ordering = "ordering_example"; // String | Sorting parameter for Workers
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListWorkerResponse result = apiInstance.listWorker(workspaceSid, activityName, activitySid, available, friendlyName, targetWorkersExpression, taskQueueName, taskQueueSid, ordering, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkerApi#listWorker");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Workers to read. | |
| **activityName** | **String**| The &#x60;activity_name&#x60; of the Worker resources to read. | [optional] |
| **activitySid** | **String**| The &#x60;activity_sid&#x60; of the Worker resources to read. | [optional] |
| **available** | **String**| Whether to return only Worker resources that are available or unavailable. Can be &#x60;true&#x60;, &#x60;1&#x60;, or &#x60;yes&#x60; to return Worker resources that are available, and &#x60;false&#x60;, or any value returns the Worker resources that are not available. | [optional] |
| **friendlyName** | **String**| The &#x60;friendly_name&#x60; of the Worker resources to read. | [optional] |
| **targetWorkersExpression** | **String**| Filter by Workers that would match an expression. In addition to fields in the workers&#39; attributes, the expression can include the following worker fields: &#x60;sid&#x60;, &#x60;friendly_name&#x60;, &#x60;activity_sid&#x60;, or &#x60;activity_name&#x60; | [optional] |
| **taskQueueName** | **String**| The &#x60;friendly_name&#x60; of the TaskQueue that the Workers to read are eligible for. | [optional] |
| **taskQueueSid** | **String**| The SID of the TaskQueue that the Workers to read are eligible for. | [optional] |
| **ordering** | **String**| Sorting parameter for Workers | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListWorkerResponse**](ListWorkerResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateWorker"></a>
# **updateWorker**
> TaskrouterV1WorkspaceWorker updateWorker(workspaceSid, sid, ifMatch, activitySid, attributes, friendlyName, rejectPendingReservations)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkerApi apiInstance = new TaskrouterV1WorkerApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Worker to update.
    String sid = "sid_example"; // String | The SID of the Worker resource to update.
    String ifMatch = "ifMatch_example"; // String | The If-Match HTTP request header
    String activitySid = "activitySid_example"; // String | The SID of a valid Activity that will describe the Worker's initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information.
    String attributes = "attributes_example"; // String | The JSON string that describes the Worker. For example: `{ \\\"email\\\": \\\"Bob@example.com\\\", \\\"phone\\\": \\\"+5095551234\\\" }`. This data is passed to the `assignment_callback_url` when TaskRouter assigns a Task to the Worker. Defaults to {}.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Worker. It can be up to 64 characters long.
    Boolean rejectPendingReservations = true; // Boolean | Whether to reject the Worker's pending reservations. This option is only valid if the Worker's new [Activity](https://www.twilio.com/docs/taskrouter/api/activity) resource has its `availability` property set to `False`.
    try {
      TaskrouterV1WorkspaceWorker result = apiInstance.updateWorker(workspaceSid, sid, ifMatch, activitySid, attributes, friendlyName, rejectPendingReservations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkerApi#updateWorker");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Worker to update. | |
| **sid** | **String**| The SID of the Worker resource to update. | |
| **ifMatch** | **String**| The If-Match HTTP request header | [optional] |
| **activitySid** | **String**| The SID of a valid Activity that will describe the Worker&#39;s initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information. | [optional] |
| **attributes** | **String**| The JSON string that describes the Worker. For example: &#x60;{ \\\&quot;email\\\&quot;: \\\&quot;Bob@example.com\\\&quot;, \\\&quot;phone\\\&quot;: \\\&quot;+5095551234\\\&quot; }&#x60;. This data is passed to the &#x60;assignment_callback_url&#x60; when TaskRouter assigns a Task to the Worker. Defaults to {}. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the Worker. It can be up to 64 characters long. | [optional] |
| **rejectPendingReservations** | **Boolean**| Whether to reject the Worker&#39;s pending reservations. This option is only valid if the Worker&#39;s new [Activity](https://www.twilio.com/docs/taskrouter/api/activity) resource has its &#x60;availability&#x60; property set to &#x60;False&#x60;. | [optional] |

### Return type

[**TaskrouterV1WorkspaceWorker**](TaskrouterV1WorkspaceWorker.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

