# JobsApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelJob**](JobsApi.md#cancelJob) | **POST** /v1/jobs/cancel | Cancels a job |
| [**getAttemptNormalizationStatusesForJob**](JobsApi.md#getAttemptNormalizationStatusesForJob) | **POST** /v1/jobs/get_normalization_status | Get normalization status to determine if we can bypass normalization phase |
| [**getJobDebugInfo**](JobsApi.md#getJobDebugInfo) | **POST** /v1/jobs/get_debug_info | Gets all information needed to debug this job |
| [**getJobInfo**](JobsApi.md#getJobInfo) | **POST** /v1/jobs/get | Get information about a job |
| [**getJobInfoLight**](JobsApi.md#getJobInfoLight) | **POST** /v1/jobs/get_light | Get information about a job excluding attempt info and logs |
| [**getLastReplicationJob**](JobsApi.md#getLastReplicationJob) | **POST** /v1/jobs/get_last_replication_job |  |
| [**listJobsFor**](JobsApi.md#listJobsFor) | **POST** /v1/jobs/list | Returns recent jobs for a connection. Jobs are returned in descending order by createdAt. |


<a id="cancelJob"></a>
# **cancelJob**
> JobInfoRead cancelJob(jobIdRequestBody)

Cancels a job

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
    defaultClient.setBasePath("http://airbyte.local");

    JobsApi apiInstance = new JobsApi(defaultClient);
    JobIdRequestBody jobIdRequestBody = new JobIdRequestBody(); // JobIdRequestBody | 
    try {
      JobInfoRead result = apiInstance.cancelJob(jobIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#cancelJob");
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
| **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | |

### Return type

[**JobInfoRead**](JobInfoRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getAttemptNormalizationStatusesForJob"></a>
# **getAttemptNormalizationStatusesForJob**
> AttemptNormalizationStatusReadList getAttemptNormalizationStatusesForJob(jobIdRequestBody)

Get normalization status to determine if we can bypass normalization phase

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
    defaultClient.setBasePath("http://airbyte.local");

    JobsApi apiInstance = new JobsApi(defaultClient);
    JobIdRequestBody jobIdRequestBody = new JobIdRequestBody(); // JobIdRequestBody | 
    try {
      AttemptNormalizationStatusReadList result = apiInstance.getAttemptNormalizationStatusesForJob(jobIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#getAttemptNormalizationStatusesForJob");
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
| **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | [optional] |

### Return type

[**AttemptNormalizationStatusReadList**](AttemptNormalizationStatusReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getJobDebugInfo"></a>
# **getJobDebugInfo**
> JobDebugInfoRead getJobDebugInfo(jobIdRequestBody)

Gets all information needed to debug this job

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
    defaultClient.setBasePath("http://airbyte.local");

    JobsApi apiInstance = new JobsApi(defaultClient);
    JobIdRequestBody jobIdRequestBody = new JobIdRequestBody(); // JobIdRequestBody | 
    try {
      JobDebugInfoRead result = apiInstance.getJobDebugInfo(jobIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#getJobDebugInfo");
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
| **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | |

### Return type

[**JobDebugInfoRead**](JobDebugInfoRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getJobInfo"></a>
# **getJobInfo**
> JobInfoRead getJobInfo(jobIdRequestBody)

Get information about a job

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
    defaultClient.setBasePath("http://airbyte.local");

    JobsApi apiInstance = new JobsApi(defaultClient);
    JobIdRequestBody jobIdRequestBody = new JobIdRequestBody(); // JobIdRequestBody | 
    try {
      JobInfoRead result = apiInstance.getJobInfo(jobIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#getJobInfo");
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
| **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | |

### Return type

[**JobInfoRead**](JobInfoRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getJobInfoLight"></a>
# **getJobInfoLight**
> JobInfoLightRead getJobInfoLight(jobIdRequestBody)

Get information about a job excluding attempt info and logs

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
    defaultClient.setBasePath("http://airbyte.local");

    JobsApi apiInstance = new JobsApi(defaultClient);
    JobIdRequestBody jobIdRequestBody = new JobIdRequestBody(); // JobIdRequestBody | 
    try {
      JobInfoLightRead result = apiInstance.getJobInfoLight(jobIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#getJobInfoLight");
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
| **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | |

### Return type

[**JobInfoLightRead**](JobInfoLightRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getLastReplicationJob"></a>
# **getLastReplicationJob**
> JobOptionalRead getLastReplicationJob(connectionIdRequestBody)



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
    defaultClient.setBasePath("http://airbyte.local");

    JobsApi apiInstance = new JobsApi(defaultClient);
    ConnectionIdRequestBody connectionIdRequestBody = new ConnectionIdRequestBody(); // ConnectionIdRequestBody | 
    try {
      JobOptionalRead result = apiInstance.getLastReplicationJob(connectionIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#getLastReplicationJob");
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
| **connectionIdRequestBody** | [**ConnectionIdRequestBody**](ConnectionIdRequestBody.md)|  | |

### Return type

[**JobOptionalRead**](JobOptionalRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="listJobsFor"></a>
# **listJobsFor**
> JobReadList listJobsFor(jobListRequestBody)

Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.

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
    defaultClient.setBasePath("http://airbyte.local");

    JobsApi apiInstance = new JobsApi(defaultClient);
    JobListRequestBody jobListRequestBody = new JobListRequestBody(); // JobListRequestBody | 
    try {
      JobReadList result = apiInstance.listJobsFor(jobListRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#listJobsFor");
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
| **jobListRequestBody** | [**JobListRequestBody**](JobListRequestBody.md)|  | |

### Return type

[**JobReadList**](JobReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

