# JobSchedulesApi

All URIs are relative to *https://batch.core.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobScheduleAdd**](JobSchedulesApi.md#jobScheduleAdd) | **POST** /jobschedules |  |
| [**jobScheduleDelete**](JobSchedulesApi.md#jobScheduleDelete) | **DELETE** /jobschedules/{jobScheduleId} |  |
| [**jobScheduleDisable**](JobSchedulesApi.md#jobScheduleDisable) | **POST** /jobschedules/{jobScheduleId}/disable |  |
| [**jobScheduleEnable**](JobSchedulesApi.md#jobScheduleEnable) | **POST** /jobschedules/{jobScheduleId}/enable |  |
| [**jobScheduleExists**](JobSchedulesApi.md#jobScheduleExists) | **HEAD** /jobschedules/{jobScheduleId} |  |
| [**jobScheduleGet**](JobSchedulesApi.md#jobScheduleGet) | **GET** /jobschedules/{jobScheduleId} |  |
| [**jobScheduleList**](JobSchedulesApi.md#jobScheduleList) | **GET** /jobschedules |  |
| [**jobSchedulePatch**](JobSchedulesApi.md#jobSchedulePatch) | **PATCH** /jobschedules/{jobScheduleId} |  |
| [**jobScheduleTerminate**](JobSchedulesApi.md#jobScheduleTerminate) | **POST** /jobschedules/{jobScheduleId}/terminate |  |
| [**jobScheduleUpdate**](JobSchedulesApi.md#jobScheduleUpdate) | **PUT** /jobschedules/{jobScheduleId} |  |


<a id="jobScheduleAdd"></a>
# **jobScheduleAdd**
> jobScheduleAdd(apiVersion, jobScheduleAddParameter, timeout, clientRequestId, returnClientRequestId, ocpDate)



Adds a job schedule to the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobSchedulesApi apiInstance = new JobSchedulesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobScheduleAddParameter jobScheduleAddParameter = new JobScheduleAddParameter(); // JobScheduleAddParameter | Specifies the job schedule to be added.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    try {
      apiInstance.jobScheduleAdd(apiVersion, jobScheduleAddParameter, timeout, clientRequestId, returnClientRequestId, ocpDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobSchedulesApi#jobScheduleAdd");
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
| **jobScheduleAddParameter** | [**JobScheduleAddParameter**](JobScheduleAddParameter.md)| Specifies the job schedule to be added. | |
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

<a id="jobScheduleDelete"></a>
# **jobScheduleDelete**
> jobScheduleDelete(jobScheduleId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Deletes a job schedule from the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobSchedulesApi apiInstance = new JobSchedulesApi(defaultClient);
    String jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to delete.
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
      apiInstance.jobScheduleDelete(jobScheduleId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobSchedulesApi#jobScheduleDelete");
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
| **jobScheduleId** | **String**| The id of the job schedule to delete. | |
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

<a id="jobScheduleDisable"></a>
# **jobScheduleDisable**
> jobScheduleDisable(jobScheduleId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Disables a job schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobSchedulesApi apiInstance = new JobSchedulesApi(defaultClient);
    String jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to disable.
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
      apiInstance.jobScheduleDisable(jobScheduleId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobSchedulesApi#jobScheduleDisable");
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
| **jobScheduleId** | **String**| The id of the job schedule to disable. | |
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
| **204** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobScheduleEnable"></a>
# **jobScheduleEnable**
> jobScheduleEnable(jobScheduleId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Enables a job schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobSchedulesApi apiInstance = new JobSchedulesApi(defaultClient);
    String jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to enable.
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
      apiInstance.jobScheduleEnable(jobScheduleId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobSchedulesApi#jobScheduleEnable");
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
| **jobScheduleId** | **String**| The id of the job schedule to enable. | |
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
| **204** |  |  * DataServiceId - Gets the OData id of the resource to which the request applied. <br>  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **0** | Error from the Batch service |  -  |

<a id="jobScheduleExists"></a>
# **jobScheduleExists**
> jobScheduleExists(jobScheduleId, apiVersion, $select, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Checks the specified job schedule exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobSchedulesApi apiInstance = new JobSchedulesApi(defaultClient);
    String jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule which you want to check.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $select = "$select_example"; // String | Sets an OData $select clause.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.jobScheduleExists(jobScheduleId, apiVersion, $select, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobSchedulesApi#jobScheduleExists");
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
| **jobScheduleId** | **String**| The id of the job schedule which you want to check. | |
| **apiVersion** | **String**| Client API Version. | |
| **$select** | **String**| Sets an OData $select clause. | [optional] |
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
| **200** | Found the jobschedule. |  * ETag - Gets the content of the ETag HTTP response header. <br>  * Last-Modified - Gets the content of the Last-Modified HTTP response header. <br>  * client-request-id - Gets the ClientRequestId provided by the client during the request, if present and requested to be returned. <br>  * request-id - Gets the value that uniquely identifies a request. <br>  |
| **404** | JobSchedules not found |  -  |
| **0** | Error from the Batch service |  -  |

<a id="jobScheduleGet"></a>
# **jobScheduleGet**
> CloudJobSchedule jobScheduleGet(jobScheduleId, apiVersion, $select, $expand, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Gets information about the specified job schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobSchedulesApi apiInstance = new JobSchedulesApi(defaultClient);
    String jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to get.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String $select = "$select_example"; // String | Sets an OData $select clause.
    String $expand = "$expand_example"; // String | Sets an OData $expand clause.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      CloudJobSchedule result = apiInstance.jobScheduleGet(jobScheduleId, apiVersion, $select, $expand, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobSchedulesApi#jobScheduleGet");
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
| **jobScheduleId** | **String**| The id of the job schedule to get. | |
| **apiVersion** | **String**| Client API Version. | |
| **$select** | **String**| Sets an OData $select clause. | [optional] |
| **$expand** | **String**| Sets an OData $expand clause. | [optional] |
| **timeout** | **Integer**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30] |
| **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] |
| **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] |
| **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] |
| **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] |
| **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] |
| **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] |
| **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] |

### Return type

[**CloudJobSchedule**](CloudJobSchedule.md)

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

<a id="jobScheduleList"></a>
# **jobScheduleList**
> CloudJobScheduleListResult jobScheduleList(apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate)



Lists all of the job schedules in the specified account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobSchedulesApi apiInstance = new JobSchedulesApi(defaultClient);
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
      CloudJobScheduleListResult result = apiInstance.jobScheduleList(apiVersion, $filter, $select, $expand, maxresults, timeout, clientRequestId, returnClientRequestId, ocpDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobSchedulesApi#jobScheduleList");
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

[**CloudJobScheduleListResult**](CloudJobScheduleListResult.md)

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

<a id="jobSchedulePatch"></a>
# **jobSchedulePatch**
> jobSchedulePatch(jobScheduleId, apiVersion, jobSchedulePatchParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Updates the properties of the specified job schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobSchedulesApi apiInstance = new JobSchedulesApi(defaultClient);
    String jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to update.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobSchedulePatchParameter jobSchedulePatchParameter = new JobSchedulePatchParameter(); // JobSchedulePatchParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.jobSchedulePatch(jobScheduleId, apiVersion, jobSchedulePatchParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobSchedulesApi#jobSchedulePatch");
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
| **jobScheduleId** | **String**| The id of the job schedule to update. | |
| **apiVersion** | **String**| Client API Version. | |
| **jobSchedulePatchParameter** | [**JobSchedulePatchParameter**](JobSchedulePatchParameter.md)| The parameters for the request. | |
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

<a id="jobScheduleTerminate"></a>
# **jobScheduleTerminate**
> jobScheduleTerminate(jobScheduleId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Terminates a job schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobSchedulesApi apiInstance = new JobSchedulesApi(defaultClient);
    String jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to terminates.
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
      apiInstance.jobScheduleTerminate(jobScheduleId, apiVersion, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobSchedulesApi#jobScheduleTerminate");
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
| **jobScheduleId** | **String**| The id of the job schedule to terminates. | |
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

<a id="jobScheduleUpdate"></a>
# **jobScheduleUpdate**
> jobScheduleUpdate(jobScheduleId, apiVersion, jobScheduleUpdateParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince)



Updates the properties of the specified job schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://batch.core.windows.net");

    JobSchedulesApi apiInstance = new JobSchedulesApi(defaultClient);
    String jobScheduleId = "jobScheduleId_example"; // String | The id of the job schedule to update.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    JobScheduleUpdateParameter jobScheduleUpdateParameter = new JobScheduleUpdateParameter(); // JobScheduleUpdateParameter | The parameters for the request.
    Integer timeout = 30; // Integer | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    String clientRequestId = "clientRequestId_example"; // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    Boolean returnClientRequestId = true; // Boolean | Specifies if the server should return the client-request-id identifier in the response.
    String ocpDate = "ocpDate_example"; // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    String ifMatch = "ifMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
    String ifNoneMatch = "ifNoneMatch_example"; // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
    String ifModifiedSince = "ifModifiedSince_example"; // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    String ifUnmodifiedSince = "ifUnmodifiedSince_example"; // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    try {
      apiInstance.jobScheduleUpdate(jobScheduleId, apiVersion, jobScheduleUpdateParameter, timeout, clientRequestId, returnClientRequestId, ocpDate, ifMatch, ifNoneMatch, ifModifiedSince, ifUnmodifiedSince);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobSchedulesApi#jobScheduleUpdate");
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
| **jobScheduleId** | **String**| The id of the job schedule to update. | |
| **apiVersion** | **String**| Client API Version. | |
| **jobScheduleUpdateParameter** | [**JobScheduleUpdateParameter**](JobScheduleUpdateParameter.md)| The parameters for the request. | |
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

