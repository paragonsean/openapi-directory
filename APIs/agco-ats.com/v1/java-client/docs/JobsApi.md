# JobsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobsDeleteJob**](JobsApi.md#jobsDeleteJob) | **DELETE** /api/v2/jobs/{jobID} | Mark the delete flag for the Job |
| [**jobsGetJob**](JobsApi.md#jobsGetJob) | **GET** /api/v2/jobs/{jobID} | Get a Job by ID |
| [**jobsGetJobs**](JobsApi.md#jobsGetJobs) | **GET** /api/v2/jobs | Get Jobs |
| [**jobsPostJob**](JobsApi.md#jobsPostJob) | **POST** /api/v2/jobs | Create a Job |
| [**jobsPutJob**](JobsApi.md#jobsPutJob) | **PUT** /api/v2/jobs/{jobID} | Update a Job |


<a id="jobsDeleteJob"></a>
# **jobsDeleteJob**
> jobsDeleteJob(jobID)

Mark the delete flag for the Job

Deletes a Job. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    JobsApi apiInstance = new JobsApi(defaultClient);
    Integer jobID = 56; // Integer | The id of the job to delete
    try {
      apiInstance.jobsDeleteJob(jobID);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsDeleteJob");
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
| **jobID** | **Integer**| The id of the job to delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="jobsGetJob"></a>
# **jobsGetJob**
> BuildSystemSharedDTOJob jobsGetJob(jobID, isIncludeDeleted)

Get a Job by ID

Gets a Job by ID. When successful, the response is the requested Job.              If unsuccessful, an appropriate ApiError is returned.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    JobsApi apiInstance = new JobsApi(defaultClient);
    Integer jobID = 56; // Integer | The ID of the Job to get.
    Boolean isIncludeDeleted = true; // Boolean | Does it include deleted job, or not
    try {
      BuildSystemSharedDTOJob result = apiInstance.jobsGetJob(jobID, isIncludeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsGetJob");
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
| **jobID** | **Integer**| The ID of the Job to get. | |
| **isIncludeDeleted** | **Boolean**| Does it include deleted job, or not | [optional] |

### Return type

[**BuildSystemSharedDTOJob**](BuildSystemSharedDTOJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="jobsGetJobs"></a>
# **jobsGetJobs**
> APIPagedResponseBuildSystemSharedDTOJob jobsGetJobs(limit, offset, isIncludeDeleted)

Get Jobs

Gets a collection of Jobs. When successful, the response is a PagedResponse of Jobs.              If unsuccessful, an appropriate ApiError is returned.               ///

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    JobsApi apiInstance = new JobsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    Boolean isIncludeDeleted = true; // Boolean | Does it include deleted job, or not
    try {
      APIPagedResponseBuildSystemSharedDTOJob result = apiInstance.jobsGetJobs(limit, offset, isIncludeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsGetJobs");
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
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **isIncludeDeleted** | **Boolean**| Does it include deleted job, or not | [optional] |

### Return type

[**APIPagedResponseBuildSystemSharedDTOJob**](APIPagedResponseBuildSystemSharedDTOJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="jobsPostJob"></a>
# **jobsPostJob**
> Integer jobsPostJob(buildSystemSharedDTOJob)

Create a Job

Creates a Job.  The body of the POST is the Job to create.  The JobID will be assigned on              creation of the Job.  When successful, the response is the JobID.  If unsuccessful, an               appropriate ApiError is returned.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    JobsApi apiInstance = new JobsApi(defaultClient);
    BuildSystemSharedDTOJob buildSystemSharedDTOJob = new BuildSystemSharedDTOJob(); // BuildSystemSharedDTOJob | The job to create.  The JobID will be assigned on creation of the Job.
    try {
      Integer result = apiInstance.jobsPostJob(buildSystemSharedDTOJob);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsPostJob");
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
| **buildSystemSharedDTOJob** | [**BuildSystemSharedDTOJob**](BuildSystemSharedDTOJob.md)| The job to create.  The JobID will be assigned on creation of the Job. | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="jobsPutJob"></a>
# **jobsPutJob**
> jobsPutJob(jobID, buildSystemSharedDTOJob)

Update a Job

Updates a Job.  The body of the PUT is the updated Job.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    JobsApi apiInstance = new JobsApi(defaultClient);
    Integer jobID = 56; // Integer | The id of the job to update
    BuildSystemSharedDTOJob buildSystemSharedDTOJob = new BuildSystemSharedDTOJob(); // BuildSystemSharedDTOJob | The updated job
    try {
      apiInstance.jobsPutJob(jobID, buildSystemSharedDTOJob);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsPutJob");
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
| **jobID** | **Integer**| The id of the job to update | |
| **buildSystemSharedDTOJob** | [**BuildSystemSharedDTOJob**](BuildSystemSharedDTOJob.md)| The updated job | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

