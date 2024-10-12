# TaskApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCustomTaskTypesOfWg**](TaskApi.md#getCustomTaskTypesOfWg) | **GET** /v1/workgroups/{workgroup_id}/customTaskTypes | Get custom task types of workgroup level |
| [**getDefaultTaskStatusList**](TaskApi.md#getDefaultTaskStatusList) | **GET** /v1/workgroups/{workgroup_id}/defaultTaskStatus | Get default task status list |
| [**getTaskListOfProject**](TaskApi.md#getTaskListOfProject) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/tasks | Get task list of project level |
| [**getTaskListOfWorkgroup**](TaskApi.md#getTaskListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/tasks | Get task list of workgroup level |
| [**getTaskOfProject**](TaskApi.md#getTaskOfProject) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/tasks/{task_id} | Get a sepcific task of project level |
| [**getTaskOfWorkgroup**](TaskApi.md#getTaskOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/tasks/{task_id} | Get a sepcific task of workgroup level |
| [**getTaskTypesOfWorkgroup**](TaskApi.md#getTaskTypesOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/taskTypes | Get task types of workgroup level |
| [**getWgTaskStatusListOfWorkgroup**](TaskApi.md#getWgTaskStatusListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/customTaskStatus | Get custom task status of workgroup level |
| [**postTaskForProject**](TaskApi.md#postTaskForProject) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/tasks | Create a new task |
| [**taskPriorityList**](TaskApi.md#taskPriorityList) | **GET** /v1/workgroups/{workgroup_id}/defaultTaskPriority | Get default task priority list |


<a id="getCustomTaskTypesOfWg"></a>
# **getCustomTaskTypesOfWg**
> TaskTypeListVO getCustomTaskTypesOfWg(workgroupId)

Get custom task types of workgroup level

Get custom task types of workgroup level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      TaskTypeListVO result = apiInstance.getCustomTaskTypesOfWg(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#getCustomTaskTypesOfWg");
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
| **workgroupId** | **String**|  | |

### Return type

[**TaskTypeListVO**](TaskTypeListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getDefaultTaskStatusList"></a>
# **getDefaultTaskStatusList**
> TaskStatusListVO getDefaultTaskStatusList(workgroupId)

Get default task status list

Get default task status list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      TaskStatusListVO result = apiInstance.getDefaultTaskStatusList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#getDefaultTaskStatusList");
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
| **workgroupId** | **String**|  | |

### Return type

[**TaskStatusListVO**](TaskStatusListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **500** | Internal server error |  -  |

<a id="getTaskListOfProject"></a>
# **getTaskListOfProject**
> TaskListVO getTaskListOfProject(workgroupId, projectId)

Get task list of project level

Get task list of project level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      TaskListVO result = apiInstance.getTaskListOfProject(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#getTaskListOfProject");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |

### Return type

[**TaskListVO**](TaskListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getTaskListOfWorkgroup"></a>
# **getTaskListOfWorkgroup**
> TaskWorkgroupLevelListVO getTaskListOfWorkgroup(workgroupId)

Get task list of workgroup level

Get task list of workgroup level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      TaskWorkgroupLevelListVO result = apiInstance.getTaskListOfWorkgroup(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#getTaskListOfWorkgroup");
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
| **workgroupId** | **String**|  | |

### Return type

[**TaskWorkgroupLevelListVO**](TaskWorkgroupLevelListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getTaskOfProject"></a>
# **getTaskOfProject**
> TaskExpandVO getTaskOfProject(workgroupId, projectId, taskId)

Get a sepcific task of project level

Get a sepcific task of project level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String taskId = "taskId_example"; // String | 
    try {
      TaskExpandVO result = apiInstance.getTaskOfProject(workgroupId, projectId, taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#getTaskOfProject");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **taskId** | **String**|  | |

### Return type

[**TaskExpandVO**](TaskExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getTaskOfWorkgroup"></a>
# **getTaskOfWorkgroup**
> TaskExpandWorkgroupLevelVO getTaskOfWorkgroup(workgroupId, taskId)

Get a sepcific task of workgroup level

Get a sepcific task of workgroup level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String taskId = "taskId_example"; // String | 
    try {
      TaskExpandWorkgroupLevelVO result = apiInstance.getTaskOfWorkgroup(workgroupId, taskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#getTaskOfWorkgroup");
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
| **workgroupId** | **String**|  | |
| **taskId** | **String**|  | |

### Return type

[**TaskExpandWorkgroupLevelVO**](TaskExpandWorkgroupLevelVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getTaskTypesOfWorkgroup"></a>
# **getTaskTypesOfWorkgroup**
> TaskTypeListVO getTaskTypesOfWorkgroup(workgroupId)

Get task types of workgroup level

Get task types of workgroup level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      TaskTypeListVO result = apiInstance.getTaskTypesOfWorkgroup(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#getTaskTypesOfWorkgroup");
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
| **workgroupId** | **String**|  | |

### Return type

[**TaskTypeListVO**](TaskTypeListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getWgTaskStatusListOfWorkgroup"></a>
# **getWgTaskStatusListOfWorkgroup**
> WgTaskStatusListVO getWgTaskStatusListOfWorkgroup(workgroupId)

Get custom task status of workgroup level

Get custom task status of workgroup level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      WgTaskStatusListVO result = apiInstance.getWgTaskStatusListOfWorkgroup(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#getWgTaskStatusListOfWorkgroup");
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
| **workgroupId** | **String**|  | |

### Return type

[**WgTaskStatusListVO**](WgTaskStatusListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="postTaskForProject"></a>
# **postTaskForProject**
> TaskCreatedVO postTaskForProject(workgroupId, projectId, taskPersistVO)

Create a new task

Create a new task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    TaskPersistVO taskPersistVO = new TaskPersistVO(); // TaskPersistVO | 
    try {
      TaskCreatedVO result = apiInstance.postTaskForProject(workgroupId, projectId, taskPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#postTaskForProject");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **taskPersistVO** | [**TaskPersistVO**](TaskPersistVO.md)|  | [optional] |

### Return type

[**TaskCreatedVO**](TaskCreatedVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful created |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

<a id="taskPriorityList"></a>
# **taskPriorityList**
> TaskPriorityListVO taskPriorityList(workgroupId)

Get default task priority list

Get default task priority list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TaskApi apiInstance = new TaskApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      TaskPriorityListVO result = apiInstance.taskPriorityList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskApi#taskPriorityList");
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
| **workgroupId** | **String**|  | |

### Return type

[**TaskPriorityListVO**](TaskPriorityListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **500** | Internal server error |  -  |

