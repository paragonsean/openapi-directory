# JobsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobAdd**](JobsApi.md#jobAdd) | **POST** /jobs | Adds a Job to the specified Account. |
| [**jobDelete**](JobsApi.md#jobDelete) | **DELETE** /jobs/{jobId} | Deletes a Job. |
| [**jobDisable**](JobsApi.md#jobDisable) | **POST** /jobs/{jobId}/disable | Disables the specified Job, preventing new Tasks from running. |
| [**jobEnable**](JobsApi.md#jobEnable) | **POST** /jobs/{jobId}/enable | Enables the specified Job, allowing new Tasks to run. |
| [**jobGet**](JobsApi.md#jobGet) | **GET** /jobs/{jobId} | Gets information about the specified Job. |
| [**jobGetAllLifetimeStatistics**](JobsApi.md#jobGetAllLifetimeStatistics) | **GET** /lifetimejobstats | Gets lifetime summary statistics for all of the Jobs in the specified Account. |
| [**jobGetTaskCounts**](JobsApi.md#jobGetTaskCounts) | **GET** /jobs/{jobId}/taskcounts | Gets the Task counts for the specified Job. |
| [**jobList**](JobsApi.md#jobList) | **GET** /jobs | Lists all of the Jobs in the specified Account. |
| [**jobListFromJobSchedule**](JobsApi.md#jobListFromJobSchedule) | **GET** /jobschedules/{jobScheduleId}/jobs | Lists the Jobs that have been created under the specified Job Schedule. |
| [**jobListPreparationAndReleaseTaskStatus**](JobsApi.md#jobListPreparationAndReleaseTaskStatus) | **GET** /jobs/{jobId}/jobpreparationandreleasetaskstatus | Lists the execution status of the Job Preparation and Job Release Task for the specified Job across the Compute Nodes where the Job has run. |
| [**jobPatch**](JobsApi.md#jobPatch) | **PATCH** /jobs/{jobId} | Updates the properties of the specified Job. |
| [**jobTerminate**](JobsApi.md#jobTerminate) | **POST** /jobs/{jobId}/terminate | Terminates the specified Job, marking it as completed. |
| [**jobUpdate**](JobsApi.md#jobUpdate) | **PUT** /jobs/{jobId} | Updates the properties of the specified Job. |


<a id="jobAdd"></a>
# **jobAdd**
> jobAdd(apiVersion, job, timeout, clientRequestId, returnClientRequestId, ocpDate)

Adds a Job to the specified Account.

The Batch service supports two ways to control the work done as part of a Job. In the first approach, the user specifies a Job Manager Task. The Batch service launches this Task when it is ready to start the Job. The Job Manager Task controls all other Tasks that run under this Job, by using the Task APIs. In the second approach, the user directly controls the execution of Tasks under an active Job, by using the Task APIs. Also note: when naming Jobs, avoid including sensitive information such as user names or secret project names. This information may appear in telemetry logs accessible to Microsoft Support engineers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobAddParameter job = new JobAddParameter(); // JobAddParameter | The Job to be added.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      apiInstance.jobAdd(apiVersion, job, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobAdd");
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
| **apiVersion** | **String**| Client API Version. | |
| **job** | [**JobAddParameter**](JobAddParameter.md)| The Job to be added. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobDelete"></a>
# **jobDelete**
> jobDelete(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)

Deletes a Job.

Deleting a Job also deletes all Tasks that are part of that Job, and all Job statistics. This also overrides the retention period for Task data; that is, if the Job contains Tasks which are still retained on Compute Nodes, the Batch services deletes those Tasks&#39; working directories and all their contents.  When a Delete Job request is received, the Batch service sets the Job to the deleting state. All update operations on a Job that is in deleting state will fail with status code 409 (Conflict), with additional information indicating that the Job is being deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The ID of the Job to delete.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    String ifMatch = "ifMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    String ifModifiedSince = "ifModifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    try {
      apiInstance.jobDelete(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobDelete");
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
| **jobId** | **String**| The ID of the Job to delete. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] |
| **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] |
| **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] |
| **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request to the Batch service was successful. |  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobDisable"></a>
# **jobDisable**
> jobDisable(jobId, apiVersion, jobDisableParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)

Disables the specified Job, preventing new Tasks from running.

The Batch Service immediately moves the Job to the disabling state. Batch then uses the disableTasks parameter to determine what to do with the currently running Tasks of the Job. The Job remains in the disabling state until the disable operation is completed and all Tasks have been dealt with according to the disableTasks option; the Job then moves to the disabled state. No new Tasks are started under the Job until it moves back to active state. If you try to disable a Job that is in any state other than active, disabling, or disabled, the request fails with status code 409.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The ID of the Job to disable.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobDisableParameter jobDisableParameter = new JobDisableParameter(); // JobDisableParameter | The parameters for the request.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    String ifMatch = "ifMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    String ifModifiedSince = "ifModifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    try {
      apiInstance.jobDisable(jobId, apiVersion, jobDisableParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobDisable");
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
| **jobId** | **String**| The ID of the Job to disable. | |
| **apiVersion** | **String**| Client API Version. | |
| **jobDisableParameter** | [**JobDisableParameter**](JobDisableParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] |
| **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] |
| **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] |
| **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobEnable"></a>
# **jobEnable**
> jobEnable(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)

Enables the specified Job, allowing new Tasks to run.

When you call this API, the Batch service sets a disabled Job to the enabling state. After the this operation is completed, the Job moves to the active state, and scheduling of new Tasks under the Job resumes. The Batch service does not allow a Task to remain in the active state for more than 180 days. Therefore, if you enable a Job containing active Tasks which were added more than 180 days ago, those Tasks will not run.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The ID of the Job to enable.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    String ifMatch = "ifMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    String ifModifiedSince = "ifModifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    try {
      apiInstance.jobEnable(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobEnable");
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
| **jobId** | **String**| The ID of the Job to enable. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] |
| **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] |
| **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] |
| **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobGet"></a>
# **jobGet**
> CloudJob jobGet(jobId, apiVersion, $select, $expand, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)

Gets information about the specified Job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The ID of the Job.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $select = "$select_example"; // String | An OData $select clause.
    String $expand = "$expand_example"; // String | An OData $expand clause.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    String ifMatch = "ifMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    String ifModifiedSince = "ifModifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    try {
      CloudJob result = apiInstance.jobGet(jobId, apiVersion, $select, $expand, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobGet");
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
| **jobId** | **String**| The ID of the Job. | |
| **apiVersion** | **String**| Client API Version. | |
| **$select** | **String**| An OData $select clause. | [optional] |
| **$expand** | **String**| An OData $expand clause. | [optional] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] |
| **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] |
| **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] |
| **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] |

### Return type

[**CloudJob**](CloudJob.md)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the Job. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobGetAllLifetimeStatistics"></a>
# **jobGetAllLifetimeStatistics**
> JobStatistics jobGetAllLifetimeStatistics(apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)

Gets lifetime summary statistics for all of the Jobs in the specified Account.

Statistics are aggregated across all Jobs that have ever existed in the Account, from Account creation to the last update time of the statistics. The statistics may not be immediately available. The Batch service performs periodic roll-up of statistics. The typical delay is about 30 minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      JobStatistics result = apiInstance.jobGetAllLifetimeStatistics(apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobGetAllLifetimeStatistics");
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
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

[**JobStatistics**](JobStatistics.md)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the Job statistics for the lifetime of the Batch Account. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobGetTaskCounts"></a>
# **jobGetTaskCounts**
> TaskCounts jobGetTaskCounts(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)

Gets the Task counts for the specified Job.

Task counts provide a count of the Tasks by active, running or completed Task state, and a count of Tasks which succeeded or failed. Tasks in the preparing state are counted as running.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The ID of the Job.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      TaskCounts result = apiInstance.jobGetTaskCounts(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobGetTaskCounts");
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
| **jobId** | **String**| The ID of the Job. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

[**TaskCounts**](TaskCounts.md)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the Task counts for the specified Job. |  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobList"></a>
# **jobList**
> CloudJobListResult jobList(apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)

Lists all of the Jobs in the specified Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-jobs.
    String $select = "$select_example"; // String | An OData $select clause.
    String $expand = "$expand_example"; // String | An OData $expand clause.
    Integer maxresults = 1000; // Integer | The maximum number of items to return in the response. A maximum of 1000 Jobs can be returned.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      CloudJobListResult result = apiInstance.jobList(apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobList");
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
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-jobs. | [optional] |
| **$select** | **String**| An OData $select clause. | [optional] |
| **$expand** | **String**| An OData $expand clause. | [optional] |
| **maxresults** | **Integer**| The maximum number of items to return in the response. A maximum of 1000 Jobs can be returned. | [optional] [default to 1000] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

[**CloudJobListResult**](CloudJobListResult.md)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the list of Jobs. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobListFromJobSchedule"></a>
# **jobListFromJobSchedule**
> CloudJobListResult jobListFromJobSchedule(jobScheduleId, apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)

Lists the Jobs that have been created under the specified Job Schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobScheduleId = "jobScheduleId_example"; // String | The ID of the Job Schedule from which you want to get a list of Jobs.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-jobs-in-a-job-schedule.
    String $select = "$select_example"; // String | An OData $select clause.
    String $expand = "$expand_example"; // String | An OData $expand clause.
    Integer maxresults = 1000; // Integer | The maximum number of items to return in the response. A maximum of 1000 Jobs can be returned.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      CloudJobListResult result = apiInstance.jobListFromJobSchedule(jobScheduleId, apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobListFromJobSchedule");
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
| **jobScheduleId** | **String**| The ID of the Job Schedule from which you want to get a list of Jobs. | |
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-jobs-in-a-job-schedule. | [optional] |
| **$select** | **String**| An OData $select clause. | [optional] |
| **$expand** | **String**| An OData $expand clause. | [optional] |
| **maxresults** | **Integer**| The maximum number of items to return in the response. A maximum of 1000 Jobs can be returned. | [optional] [default to 1000] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

[**CloudJobListResult**](CloudJobListResult.md)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing the list of Jobs. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobListPreparationAndReleaseTaskStatus"></a>
# **jobListPreparationAndReleaseTaskStatus**
> CloudJobListPreparationAndReleaseTaskStatusResult jobListPreparationAndReleaseTaskStatus(jobId, apiVersion, $filter, $select, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)

Lists the execution status of the Job Preparation and Job Release Task for the specified Job across the Compute Nodes where the Job has run.

This API returns the Job Preparation and Job Release Task status on all Compute Nodes that have run the Job Preparation or Job Release Task. This includes Compute Nodes which have since been removed from the Pool. If this API is invoked on a Job which has no Job Preparation or Job Release Task, the Batch service returns HTTP status code 409 (Conflict) with an error code of JobPreparationTaskNotSpecified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The ID of the Job.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-job-preparation-and-release-status.
    String $select = "$select_example"; // String | An OData $select clause.
    Integer maxresults = 1000; // Integer | The maximum number of items to return in the response. A maximum of 1000 Tasks can be returned.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    try {
      CloudJobListPreparationAndReleaseTaskStatusResult result = apiInstance.jobListPreparationAndReleaseTaskStatus(jobId, apiVersion, $filter, $select, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobListPreparationAndReleaseTaskStatus");
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
| **jobId** | **String**| The ID of the Job. | |
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-job-preparation-and-release-status. | [optional] |
| **$select** | **String**| An OData $select clause. | [optional] |
| **maxresults** | **Integer**| The maximum number of items to return in the response. A maximum of 1000 Tasks can be returned. | [optional] [default to 1000] |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |

### Return type

[**CloudJobListPreparationAndReleaseTaskStatusResult**](CloudJobListPreparationAndReleaseTaskStatusResult.md)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response containing a list of Job Preparation and Job Release Task statuses. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. If this API is invoked on a Job which has no Job Preparation or Job Release Task, the Batch service returns HTTP status code 409. |  -  |

<a id="jobPatch"></a>
# **jobPatch**
> jobPatch(jobId, apiVersion, jobPatchParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)

Updates the properties of the specified Job.

This replaces only the Job properties specified in the request. For example, if the Job has constraints, and a request does not specify the constraints element, then the Job keeps the existing constraints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The ID of the Job whose properties you want to update.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobPatchParameter jobPatchParameter = new JobPatchParameter(); // JobPatchParameter | The parameters for the request.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    String ifMatch = "ifMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    String ifModifiedSince = "ifModifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    try {
      apiInstance.jobPatch(jobId, apiVersion, jobPatchParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobPatch");
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
| **jobId** | **String**| The ID of the Job whose properties you want to update. | |
| **apiVersion** | **String**| Client API Version. | |
| **jobPatchParameter** | [**JobPatchParameter**](JobPatchParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] |
| **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] |
| **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] |
| **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobTerminate"></a>
# **jobTerminate**
> jobTerminate(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince, jobTerminateParameter)

Terminates the specified Job, marking it as completed.

When a Terminate Job request is received, the Batch service sets the Job to the terminating state. The Batch service then terminates any running Tasks associated with the Job and runs any required Job release Tasks. Then the Job moves into the completed state. If there are any Tasks in the Job in the active state, they will remain in the active state. Once a Job is terminated, new Tasks cannot be added and any remaining active Tasks will not be scheduled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The ID of the Job to terminate.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    String ifMatch = "ifMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    String ifModifiedSince = "ifModifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    JobTerminateParameter jobTerminateParameter = new JobTerminateParameter(); // JobTerminateParameter | The parameters for the request.
    try {
      apiInstance.jobTerminate(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince, jobTerminateParameter);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobTerminate");
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
| **jobId** | **String**| The ID of the Job to terminate. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] |
| **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] |
| **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] |
| **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] |
| **jobTerminateParameter** | [**JobTerminateParameter**](JobTerminateParameter.md)| The parameters for the request. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

<a id="jobUpdate"></a>
# **jobUpdate**
> jobUpdate(jobId, apiVersion, jobUpdateParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)

Updates the properties of the specified Job.

This fully replaces all the updatable properties of the Job. For example, if the Job has constraints associated with it and if constraints is not specified with this request, then the Batch service will remove the existing constraints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The ID of the Job whose properties you want to update.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobUpdateParameter jobUpdateParameter = new JobUpdateParameter(); // JobUpdateParameter | The parameters for the request.
    Integer timeout = 30; // Integer | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    UUID clientRequestId = UUID.randomUUID(); // UUID | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = false; // Boolean | Whether the server should return the client-request-id in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    String ifMatch = "ifMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    String ifModifiedSince = "ifModifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    try {
      apiInstance.jobUpdate(jobId, apiVersion, jobUpdateParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobUpdate");
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
| **jobId** | **String**| The ID of the Job whose properties you want to update. | |
| **apiVersion** | **String**| Client API Version. | |
| **jobUpdateParameter** | [**JobUpdateParameter**](JobUpdateParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **UUID**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false] |
| **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] |
| **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] |
| **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] |
| **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] |
| **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json; odata=minimalmetadata
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request to the Batch service was successful. |  * ETag - The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers. <br>  * client-request-id - The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true. <br>  * DataServiceId - The OData ID of the resource to which the request applied. <br>  * Last-Modified - The time at which the resource was last modified. <br>  * request-id - A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in. <br>  |
| **0** | The error from the Batch service. |  -  |

