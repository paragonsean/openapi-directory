# TasksApi

All URIs are relative to *https://batch.core.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taskAdd**](TasksApi.md#taskAdd) | **POST** /jobs/{jobId}/tasks |  |
| [**taskAddCollection**](TasksApi.md#taskAddCollection) | **POST** /jobs/{jobId}/addtaskcollection |  |
| [**taskDelete**](TasksApi.md#taskDelete) | **DELETE** /jobs/{jobId}/tasks/{taskId} |  |
| [**taskGet**](TasksApi.md#taskGet) | **GET** /jobs/{jobId}/tasks/{taskId} |  |
| [**taskList**](TasksApi.md#taskList) | **GET** /jobs/{jobId}/tasks |  |
| [**taskListSubtasks**](TasksApi.md#taskListSubtasks) | **GET** /jobs/{jobId}/tasks/{taskId}/subtasksinfo |  |
| [**taskTerminate**](TasksApi.md#taskTerminate) | **POST** /jobs/{jobId}/tasks/{taskId}/terminate |  |
| [**taskUpdate**](TasksApi.md#taskUpdate) | **PUT** /jobs/{jobId}/tasks/{taskId} |  |


<a id="taskAdd"></a>
# **taskAdd**
> taskAdd(jobId, apiVersion, taskAddParameter, timeout, clientRequestId, returnClientRequestId, ocpDate)



Adds a task to the specified job.

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
    defaultClient.setBasePath("https://batch.core.windows.net");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job to which the task is to be added.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    TaskAddParameter taskAddParameter = new TaskAddParameter(); // TaskAddParameter | The task to be added.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.taskAdd(jobId, apiVersion, taskAddParameter, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#taskAdd");
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
| **jobId** | **String**| The id of the job to which the task is to be added. | |
| **apiVersion** | **String**| Client API Version. | |
| **taskAddParameter** | [**TaskAddParameter**](TaskAddParameter.md)| The task to be added. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  * DataServiceId - The OData id of the resource to which the request applied. <br>  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="taskAddCollection"></a>
# **taskAddCollection**
> TaskAddCollectionResult taskAddCollection(jobId, apiVersion, taskAddCollectionParameter, timeout, clientRequestId, returnClientRequestId, ocpDate)



Adds a collection of tasks to the specified job.

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
    defaultClient.setBasePath("https://batch.core.windows.net");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job to which the task collection is to be added.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    TaskAddCollectionParameter taskAddCollectionParameter = new TaskAddCollectionParameter(); // TaskAddCollectionParameter | The tasks to be added.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      TaskAddCollectionResult result = apiInstance.taskAddCollection(jobId, apiVersion, taskAddCollectionParameter, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#taskAddCollection");
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
| **jobId** | **String**| The id of the job to which the task collection is to be added. | |
| **apiVersion** | **String**| Client API Version. | |
| **taskAddCollectionParameter** | [**TaskAddCollectionParameter**](TaskAddCollectionParameter.md)| The tasks to be added. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**TaskAddCollectionResult**](TaskAddCollectionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | Unexpected error |  -  |

<a id="taskDelete"></a>
# **taskDelete**
> taskDelete(jobId, taskId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Deletes a task from the specified job.

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
    defaultClient.setBasePath("https://batch.core.windows.net");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job from which to delete the task.
    String taskId = "taskId_example"; // String | The id of the task to delete.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.taskDelete(jobId, taskId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#taskDelete");
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
| **jobId** | **String**| The id of the job from which to delete the task. | |
| **taskId** | **String**| The id of the task to delete. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

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
| **200** |  |  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="taskGet"></a>
# **taskGet**
> CloudTask taskGet(jobId, taskId, apiVersion, $select, $expand, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Gets information about the specified task.

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
    defaultClient.setBasePath("https://batch.core.windows.net");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job that contains the task.
    String taskId = "taskId_example"; // String | The id of the task to get information about.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $select = "$select_example"; // String | An OData $select clause.
    String $expand = "$expand_example"; // String | An OData $expand clause.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      CloudTask result = apiInstance.taskGet(jobId, taskId, apiVersion, $select, $expand, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#taskGet");
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
| **jobId** | **String**| The id of the job that contains the task. | |
| **taskId** | **String**| The id of the task to get information about. | |
| **apiVersion** | **String**| Client API Version. | |
| **$select** | **String**| An OData $select clause. | [optional] |
| **$expand** | **String**| An OData $expand clause. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

[**CloudTask**](CloudTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * DataServiceId - The OData id of the resource to which the request applied. <br>  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="taskList"></a>
# **taskList**
> CloudTaskListResult taskList(jobId, apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists all of the tasks that are associated with the specified job.

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
    defaultClient.setBasePath("https://batch.core.windows.net");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | An OData $filter clause.
    String $select = "$select_example"; // String | An OData $select clause.
    String $expand = "$expand_example"; // String | An OData $expand clause.
    Integer maxresults = 56; // Integer | The maximum number of items to return in the response.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      CloudTaskListResult result = apiInstance.taskList(jobId, apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#taskList");
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
| **jobId** | **String**| The id of the job. | |
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| An OData $filter clause. | [optional] |
| **$select** | **String**| An OData $select clause. | [optional] |
| **$expand** | **String**| An OData $expand clause. | [optional] |
| **maxresults** | **Integer**| The maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**CloudTaskListResult**](CloudTaskListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="taskListSubtasks"></a>
# **taskListSubtasks**
> CloudTaskListSubtasksResult taskListSubtasks(jobId, taskId, apiVersion, $select, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists all of the subtasks that are associated with the specified multi-instance task.

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
    defaultClient.setBasePath("https://batch.core.windows.net");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job.
    String taskId = "taskId_example"; // String | The id of the task.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $select = "$select_example"; // String | An OData $select clause.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      CloudTaskListSubtasksResult result = apiInstance.taskListSubtasks(jobId, taskId, apiVersion, $select, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#taskListSubtasks");
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
| **jobId** | **String**| The id of the job. | |
| **taskId** | **String**| The id of the task. | |
| **apiVersion** | **String**| Client API Version. | |
| **$select** | **String**| An OData $select clause. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**CloudTaskListSubtasksResult**](CloudTaskListSubtasksResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="taskTerminate"></a>
# **taskTerminate**
> taskTerminate(jobId, taskId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Terminates the specified task.

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
    defaultClient.setBasePath("https://batch.core.windows.net");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job containing the task.
    String taskId = "taskId_example"; // String | The id of the task to terminate.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.taskTerminate(jobId, taskId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#taskTerminate");
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
| **jobId** | **String**| The id of the job containing the task. | |
| **taskId** | **String**| The id of the task to terminate. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

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
| **204** |  |  * DataServiceId - The OData id of the resource to which the request applied. <br>  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="taskUpdate"></a>
# **taskUpdate**
> taskUpdate(jobId, taskId, apiVersion, taskUpdateParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Updates the properties of the specified task.

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
    defaultClient.setBasePath("https://batch.core.windows.net");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job containing the task.
    String taskId = "taskId_example"; // String | The id of the task to update.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    TaskUpdateParameter taskUpdateParameter = new TaskUpdateParameter(); // TaskUpdateParameter | The parameters for the request.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.taskUpdate(jobId, taskId, apiVersion, taskUpdateParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#taskUpdate");
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
| **jobId** | **String**| The id of the job containing the task. | |
| **taskId** | **String**| The id of the task to update. | |
| **apiVersion** | **String**| Client API Version. | |
| **taskUpdateParameter** | [**TaskUpdateParameter**](TaskUpdateParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * DataServiceId - The OData id of the resource to which the request applied. <br>  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

