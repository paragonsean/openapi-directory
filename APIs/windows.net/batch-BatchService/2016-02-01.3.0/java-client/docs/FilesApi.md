# FilesApi

All URIs are relative to *https://batch.core.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fileDeleteFromComputeNode**](FilesApi.md#fileDeleteFromComputeNode) | **DELETE** /pools/{poolId}/nodes/{nodeId}/files/{fileName} |  |
| [**fileDeleteFromTask**](FilesApi.md#fileDeleteFromTask) | **DELETE** /jobs/{jobId}/tasks/{taskId}/files/{fileName} |  |
| [**fileGetFromComputeNode**](FilesApi.md#fileGetFromComputeNode) | **GET** /pools/{poolId}/nodes/{nodeId}/files/{fileName} |  |
| [**fileGetFromTask**](FilesApi.md#fileGetFromTask) | **GET** /jobs/{jobId}/tasks/{taskId}/files/{fileName} |  |
| [**fileGetNodeFilePropertiesFromComputeNode**](FilesApi.md#fileGetNodeFilePropertiesFromComputeNode) | **HEAD** /pools/{poolId}/nodes/{nodeId}/files/{fileName} |  |
| [**fileGetNodeFilePropertiesFromTask**](FilesApi.md#fileGetNodeFilePropertiesFromTask) | **HEAD** /jobs/{jobId}/tasks/{taskId}/files/{fileName} |  |
| [**fileListFromComputeNode**](FilesApi.md#fileListFromComputeNode) | **GET** /pools/{poolId}/nodes/{nodeId}/files |  |
| [**fileListFromTask**](FilesApi.md#fileListFromTask) | **GET** /jobs/{jobId}/tasks/{taskId}/files |  |


<a id="fileDeleteFromComputeNode"></a>
# **fileDeleteFromComputeNode**
> fileDeleteFromComputeNode(poolId, nodeId, fileName, apiVersion, recursive, timeout, clientRequestId, returnClientRequestId, ocpDate)



Deletes the specified task file from the compute node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool that contains the compute node.
    String nodeId = "nodeId_example"; // String | The id of the compute node from which you want to delete the file.
    String fileName = "fileName_example"; // String | The path to the file that you want to delete.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Boolean recursive = true; // Boolean | Whether to delete children of a directory. If the fileName parameter represents a directory instead of a file, you can set Recursive to true to delete the directory and all of the files and subdirectories in it. If Recursive is false then the directory must be empty or deletion will fail.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.fileDeleteFromComputeNode(poolId, nodeId, fileName, apiVersion, recursive, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#fileDeleteFromComputeNode");
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
| **poolId** | **String**| The id of the pool that contains the compute node. | |
| **nodeId** | **String**| The id of the compute node from which you want to delete the file. | |
| **fileName** | **String**| The path to the file that you want to delete. | |
| **apiVersion** | **String**| Client API Version. | |
| **recursive** | **Boolean**| Whether to delete children of a directory. If the fileName parameter represents a directory instead of a file, you can set Recursive to true to delete the directory and all of the files and subdirectories in it. If Recursive is false then the directory must be empty or deletion will fail. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

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

<a id="fileDeleteFromTask"></a>
# **fileDeleteFromTask**
> fileDeleteFromTask(jobId, taskId, fileName, apiVersion, recursive, timeout, clientRequestId, returnClientRequestId, ocpDate)



Deletes the specified task file from the compute node where the task ran.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job that contains the task.
    String taskId = "taskId_example"; // String | The id of the task whose file you want to delete.
    String fileName = "fileName_example"; // String | The path to the task file that you want to delete.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Boolean recursive = true; // Boolean | Whether to delete children of a directory. If the fileName parameter represents a directory instead of a file, you can set Recursive to true to delete the directory and all of the files and subdirectories in it. If Recursive is false then the directory must be empty or deletion will fail.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.fileDeleteFromTask(jobId, taskId, fileName, apiVersion, recursive, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#fileDeleteFromTask");
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
| **taskId** | **String**| The id of the task whose file you want to delete. | |
| **fileName** | **String**| The path to the task file that you want to delete. | |
| **apiVersion** | **String**| Client API Version. | |
| **recursive** | **Boolean**| Whether to delete children of a directory. If the fileName parameter represents a directory instead of a file, you can set Recursive to true to delete the directory and all of the files and subdirectories in it. If Recursive is false then the directory must be empty or deletion will fail. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

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

<a id="fileGetFromComputeNode"></a>
# **fileGetFromComputeNode**
> File fileGetFromComputeNode(poolId, nodeId, fileName, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ocpRange, ifModifiedSince, ifUnmodifiedSince)



Returns the content of the specified task file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool that contains the compute node.
    String nodeId = "nodeId_example"; // String | The id of the compute node that contains the file.
    String fileName = "fileName_example"; // String | The path to the task file that you want to get the content of.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ocpRange = "ocpRange_example"; // String | The byte range to be retrieved. The default is to retrieve the entire file. The format is startRange-endRange.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      File result = apiInstance.fileGetFromComputeNode(poolId, nodeId, fileName, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ocpRange, ifModifiedSince, ifUnmodifiedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#fileGetFromComputeNode");
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
| **poolId** | **String**| The id of the pool that contains the compute node. | |
| **nodeId** | **String**| The id of the compute node that contains the file. | |
| **fileName** | **String**| The path to the task file that you want to get the content of. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ocpRange** | **String**| The byte range to be retrieved. The default is to retrieve the entire file. The format is startRange-endRange. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Content-Length - The length of the file. <br>  * Content-Type - The content type of the file. <br>  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * ocp-batch-file-isdirectory - Whether the object represents a directory. <br>  * ocp-batch-file-mode - The file mode attribute in octal format. <br>  * ocp-batch-file-url - The URL of the file. <br>  * ocp-creation-time - The file creation time. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="fileGetFromTask"></a>
# **fileGetFromTask**
> File fileGetFromTask(jobId, taskId, fileName, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ocpRange, ifModifiedSince, ifUnmodifiedSince)



Returns the content of the specified task file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job that contains the task.
    String taskId = "taskId_example"; // String | The id of the task whose file you want to retrieve.
    String fileName = "fileName_example"; // String | The path to the task file that you want to get the content of.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ocpRange = "ocpRange_example"; // String | The byte range to be retrieved. The default is to retrieve the entire file. The format is startRange-endRange.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      File result = apiInstance.fileGetFromTask(jobId, taskId, fileName, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ocpRange, ifModifiedSince, ifUnmodifiedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#fileGetFromTask");
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
| **taskId** | **String**| The id of the task whose file you want to retrieve. | |
| **fileName** | **String**| The path to the task file that you want to get the content of. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ocpRange** | **String**| The byte range to be retrieved. The default is to retrieve the entire file. The format is startRange-endRange. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Content-Length - The length of the file. <br>  * Content-Type - The content type of the file. <br>  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * ocp-batch-file-isdirectory - Whether the object represents a directory. <br>  * ocp-batch-file-mode - The file mode attribute in octal format. <br>  * ocp-batch-file-url - The URL of the file. <br>  * ocp-creation-time - The file creation time. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="fileGetNodeFilePropertiesFromComputeNode"></a>
# **fileGetNodeFilePropertiesFromComputeNode**
> fileGetNodeFilePropertiesFromComputeNode(poolId, nodeId, fileName, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifModifiedSince, ifUnmodifiedSince)



Gets the properties of the specified compute node file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool that contains the compute node.
    String nodeId = "nodeId_example"; // String | The id of the compute node that contains the file.
    String fileName = "fileName_example"; // String | The path to the compute node file that you want to get the properties of.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.fileGetNodeFilePropertiesFromComputeNode(poolId, nodeId, fileName, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#fileGetNodeFilePropertiesFromComputeNode");
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
| **poolId** | **String**| The id of the pool that contains the compute node. | |
| **nodeId** | **String**| The id of the compute node that contains the file. | |
| **fileName** | **String**| The path to the compute node file that you want to get the properties of. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
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
| **200** | Found the file |  * Content-Length - The length of the file. <br>  * Content-Type - The content type of the file. <br>  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * ocp-batch-file-isdirectory - Whether the object represents a directory. <br>  * ocp-batch-file-mode - The file mode attribute in octal format. <br>  * ocp-batch-file-url - The URL of the file. <br>  * ocp-creation-time - The file creation time. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="fileGetNodeFilePropertiesFromTask"></a>
# **fileGetNodeFilePropertiesFromTask**
> fileGetNodeFilePropertiesFromTask(jobId, taskId, fileName, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifModifiedSince, ifUnmodifiedSince)



Gets the properties of the specified task file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job that contains the task.
    String taskId = "taskId_example"; // String | The id of the task whose file you want to get the properties of.
    String fileName = "fileName_example"; // String | The path to the task file that you want to get the properties of.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.fileGetNodeFilePropertiesFromTask(jobId, taskId, fileName, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#fileGetNodeFilePropertiesFromTask");
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
| **taskId** | **String**| The id of the task whose file you want to get the properties of. | |
| **fileName** | **String**| The path to the task file that you want to get the properties of. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
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
| **200** | Found the file |  * Content-Length - The length of the file. <br>  * Content-Type - The content type of the file. <br>  * ETag - The content of the ETag HTTP response header. <br>  * Last-Modified - The content of the Last-Modified HTTP response header. <br>  * client-request-id - The ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * ocp-batch-file-isdirectory - Whether the object represents a directory. <br>  * ocp-batch-file-mode - The file mode attribute in octal format. <br>  * ocp-batch-file-url - The URL of the file. <br>  * ocp-creation-time - The file creation time. <br>  * request-id - The value that uniquely identifies a request. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="fileListFromComputeNode"></a>
# **fileListFromComputeNode**
> NodeFileListResult fileListFromComputeNode(poolId, nodeId, apiVersion, $filter, recursive, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists all of the files in task directories on the specified compute node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String poolId = "poolId_example"; // String | The id of the pool that contains the compute node.
    String nodeId = "nodeId_example"; // String | The id of the compute node whose files you want to list.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | An OData $filter clause.
    Boolean recursive = true; // Boolean | Whether to list children of a directory.
    Integer maxresults = 56; // Integer | The maximum number of items to return in the response.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      NodeFileListResult result = apiInstance.fileListFromComputeNode(poolId, nodeId, apiVersion, $filter, recursive, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#fileListFromComputeNode");
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
| **poolId** | **String**| The id of the pool that contains the compute node. | |
| **nodeId** | **String**| The id of the compute node whose files you want to list. | |
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| An OData $filter clause. | [optional] |
| **recursive** | **Boolean**| Whether to list children of a directory. | [optional] |
| **maxresults** | **Integer**| The maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**NodeFileListResult**](NodeFileListResult.md)

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

<a id="fileListFromTask"></a>
# **fileListFromTask**
> NodeFileListResult fileListFromTask(jobId, taskId, apiVersion, $filter, recursive, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists the files in a task&#39;s directory on its compute node.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    FilesApi apiInstance = new FilesApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job that contains the task.
    String taskId = "taskId_example"; // String | The id of the task whose files you want to list.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | An OData $filter clause.
    Boolean recursive = true; // Boolean | Whether to list children of a directory.
    Integer maxresults = 56; // Integer | The maximum number of items to return in the response.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Whether the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      NodeFileListResult result = apiInstance.fileListFromTask(jobId, taskId, apiVersion, $filter, recursive, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesApi#fileListFromTask");
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
| **taskId** | **String**| The id of the task whose files you want to list. | |
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| An OData $filter clause. | [optional] |
| **recursive** | **Boolean**| Whether to list children of a directory. | [optional] |
| **maxresults** | **Integer**| The maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**NodeFileListResult**](NodeFileListResult.md)

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

