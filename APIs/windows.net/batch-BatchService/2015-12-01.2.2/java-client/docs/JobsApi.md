# JobsApi

All URIs are relative to *https://batch.core.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobAdd**](JobsApi.md#jobAdd) | **POST** /jobs |  |
| [**jobDelete**](JobsApi.md#jobDelete) | **DELETE** /jobs/{jobId} |  |
| [**jobDisable**](JobsApi.md#jobDisable) | **POST** /jobs/{jobId}/disable |  |
| [**jobEnable**](JobsApi.md#jobEnable) | **POST** /jobs/{jobId}/enable |  |
| [**jobGet**](JobsApi.md#jobGet) | **GET** /jobs/{jobId} |  |
| [**jobGetAllJobsLifetimeStatistics**](JobsApi.md#jobGetAllJobsLifetimeStatistics) | **GET** /lifetimejobstats |  |
| [**jobList**](JobsApi.md#jobList) | **GET** /jobs |  |
| [**jobListFromJobSchedule**](JobsApi.md#jobListFromJobSchedule) | **GET** /jobschedules/{jobScheduleId}/jobs |  |
| [**jobListPreparationAndReleaseTaskStatus**](JobsApi.md#jobListPreparationAndReleaseTaskStatus) | **GET** /jobs/{jobId}/jobpreparationandreleasetaskstatus |  |
| [**jobPatch**](JobsApi.md#jobPatch) | **PATCH** /jobs/{jobId} |  |
| [**jobTerminate**](JobsApi.md#jobTerminate) | **POST** /jobs/{jobId}/terminate |  |
| [**jobUpdate**](JobsApi.md#jobUpdate) | **PUT** /jobs/{jobId} |  |


<a id="jobAdd"></a>
# **jobAdd**
> jobAdd(apiVersion, jobAddParameter, timeout, clientRequestId, returnClientRequestId, ocpDate)



Adds a job to the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobAddParameter jobAddParameter = new JobAddParameter(); // JobAddParameter | Specifies the job to be added.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.jobAdd(apiVersion, jobAddParameter, timeout, clientRequestId, returnClientRequestId, ocpDate);
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
| **jobAddParameter** | [**JobAddParameter**](JobAddParameter.md)| Specifies the job to be added. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
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
| **201** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobDelete"></a>
# **jobDelete**
> jobDelete(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Deletes a job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job to delete.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
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
| **jobId** | **String**| The id of the job to delete. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
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
| **202** |  |  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobDisable"></a>
# **jobDisable**
> jobDisable(jobId, apiVersion, jobDisableParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Disables the specified job, preventing new tasks from running.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job to disable.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobDisableParameter jobDisableParameter = new JobDisableParameter(); // JobDisableParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
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
| **jobId** | **String**| The id of the job to disable. | |
| **apiVersion** | **String**| Client API Version. | |
| **jobDisableParameter** | [**JobDisableParameter**](JobDisableParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
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
| **202** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobEnable"></a>
# **jobEnable**
> jobEnable(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Enables the specified job, allowing new tasks to run.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job to enable.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
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
| **jobId** | **String**| The id of the job to enable. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
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
| **202** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobGet"></a>
# **jobGet**
> CloudJob jobGet(jobId, apiVersion, $select, $expand, timeout, clientRequestId, returnClientRequestId, ocpDate)



Gets information about the specified job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $select = "$select_example"; // String | Sets an OData $select clause.
    String $expand = "$expand_example"; // String | Sets an OData $expand clause.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      CloudJob result = apiInstance.jobGet(jobId, apiVersion, $select, $expand, timeout, clientRequestId, returnClientRequestId, ocpDate);
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
| **jobId** | **String**| The id of the job. | |
| **apiVersion** | **String**| Client API Version. | |
| **$select** | **String**| Sets an OData $select clause. | [optional] |
| **$expand** | **String**| Sets an OData $expand clause. | [optional] |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**CloudJob**](CloudJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobGetAllJobsLifetimeStatistics"></a>
# **jobGetAllJobsLifetimeStatistics**
> JobStatistics jobGetAllJobsLifetimeStatistics(apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate)



Gets lifetime summary statistics for all of the jobs in the specified account. Statistics are aggregated across all jobs that have ever existed in the account, from account creation to the last update time of the statistics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      JobStatistics result = apiInstance.jobGetAllJobsLifetimeStatistics(apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobGetAllJobsLifetimeStatistics");
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
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**JobStatistics**](JobStatistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobList"></a>
# **jobList**
> CloudJobListResult jobList(apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists all of the jobs in the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | Sets an OData $filter clause.
    String $select = "$select_example"; // String | Sets an OData $select clause.
    String $expand = "$expand_example"; // String | Sets an OData $expand clause.
    Integer maxresults = 56; // Integer | Sets the maximum number of items to return in the response.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
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
| **$filter** | **String**| Sets an OData $filter clause. | [optional] |
| **$select** | **String**| Sets an OData $select clause. | [optional] |
| **$expand** | **String**| Sets an OData $expand clause. | [optional] |
| **maxresults** | **Integer**| Sets the maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**CloudJobListResult**](CloudJobListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobListFromJobSchedule"></a>
# **jobListFromJobSchedule**
> CloudJobListResult jobListFromJobSchedule(jobScheduleId, apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists the jobs that have been created under the specified job schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule from which you want to get a list of jobs.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | Sets an OData $filter clause.
    String $select = "$select_example"; // String | Sets an OData $select clause.
    String $expand = "$expand_example"; // String | Sets an OData $expand clause.
    Integer maxresults = 56; // Integer | Sets the maximum number of items to return in the response.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
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
| **jobScheduleId** | **String**| The id of the job schedule from which you want to get a list of jobs. | |
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| Sets an OData $filter clause. | [optional] |
| **$select** | **String**| Sets an OData $select clause. | [optional] |
| **$expand** | **String**| Sets an OData $expand clause. | [optional] |
| **maxresults** | **Integer**| Sets the maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**CloudJobListResult**](CloudJobListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobListPreparationAndReleaseTaskStatus"></a>
# **jobListPreparationAndReleaseTaskStatus**
> CloudJobListPreparationAndReleaseTaskStatusResult jobListPreparationAndReleaseTaskStatus(jobId, apiVersion, $filter, $select, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists the execution status of the Job Preparation and Job Release task for the specified job across the compute nodes where the job has run.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $filter = "$filter_example"; // String | Sets an OData $filter clause.
    String $select = "$select_example"; // String | Sets an OData $select clause.
    Integer maxresults = 56; // Integer | Sets the maximum number of items to return in the response.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
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
| **jobId** | **String**| The id of the job. | |
| **apiVersion** | **String**| Client API Version. | |
| **$filter** | **String**| Sets an OData $filter clause. | [optional] |
| **$select** | **String**| Sets an OData $select clause. | [optional] |
| **maxresults** | **Integer**| Sets the maximum number of items to return in the response. | [optional] |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |

### Return type

[**CloudJobListPreparationAndReleaseTaskStatusResult**](CloudJobListPreparationAndReleaseTaskStatusResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobPatch"></a>
# **jobPatch**
> jobPatch(jobId, apiVersion, jobPatchParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Updates the properties of a job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job whose properties you want to update.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobPatchParameter jobPatchParameter = new JobPatchParameter(); // JobPatchParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
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
| **jobId** | **String**| The id of the job whose properties you want to update. | |
| **apiVersion** | **String**| Client API Version. | |
| **jobPatchParameter** | [**JobPatchParameter**](JobPatchParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
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
| **200** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobTerminate"></a>
# **jobTerminate**
> jobTerminate(jobId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince, jobTerminateParameter)



Terminates the specified job, marking it as completed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job to terminate.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
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
| **jobId** | **String**| The id of the job to terminate. | |
| **apiVersion** | **String**| Client API Version. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |
| **jobTerminateParameter** | [**JobTerminateParameter**](JobTerminateParameter.md)| The parameters for the request. | [optional] |

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
| **202** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobUpdate"></a>
# **jobUpdate**
> jobUpdate(jobId, apiVersion, jobUpdateParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Updates the properties of a job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String jobId = "jobId_example"; // String | The id of the job whose properties you want to update.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobUpdateParameter jobUpdateParameter = new JobUpdateParameter(); // JobUpdateParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
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
| **jobId** | **String**| The id of the job whose properties you want to update. | |
| **apiVersion** | **String**| Client API Version. | |
| **jobUpdateParameter** | [**JobUpdateParameter**](JobUpdateParameter.md)| The parameters for the request. | |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
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
| **200** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

