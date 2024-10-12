# JobsClassicApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignFileToJobOutput**](JobsClassicApi.md#assignFileToJobOutput) | **POST** /jobs/{jobId}/files/output |  |
| [**assignVendor**](JobsClassicApi.md#assignVendor) | **PUT** /jobs/{jobId}/vendor | Assigns vendor to a job in a project. |
| [**changeStatus**](JobsClassicApi.md#changeStatus) | **PUT** /jobs/{jobId}/status | Changes job status if possible (400 Bad Request is returned otherwise). |
| [**getJobDetails**](JobsClassicApi.md#getJobDetails) | **GET** /jobs/{jobId} | Returns job details by jobId. |
| [**getJobFiles**](JobsClassicApi.md#getJobFiles) | **GET** /jobs/{jobId}/files | Returns list of input and output files of a job. |
| [**getJobFiles1**](JobsClassicApi.md#getJobFiles1) | **GET** /jobs/{jobId}/files/{fileId} | Returns file metadata. |
| [**updateDates**](JobsClassicApi.md#updateDates) | **PUT** /jobs/{jobId}/dates | Updates dates of a given job. |
| [**updateInstructions**](JobsClassicApi.md#updateInstructions) | **PUT** /jobs/{jobId}/instructions | Updates instructions for a job. |


<a id="assignFileToJobOutput"></a>
# **assignFileToJobOutput**
> assignFileToJobOutput(jobId, taskFileDTO)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsClassicApi apiInstance = new JobsClassicApi(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    TaskFileDTO taskFileDTO = new TaskFileDTO(); // TaskFileDTO | Assigns file to job output files.
    try {
      apiInstance.assignFileToJobOutput(jobId, taskFileDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsClassicApi#assignFileToJobOutput");
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
| **jobId** | **String**| job&#39;s internal identifier | |
| **taskFileDTO** | [**TaskFileDTO**](TaskFileDTO.md)| Assigns file to job output files. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | default response |  -  |

<a id="assignVendor"></a>
# **assignVendor**
> assignVendor(jobId, assignVendorDTO)

Assigns vendor to a job in a project.

Assigns vendor to a job in a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsClassicApi apiInstance = new JobsClassicApi(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    AssignVendorDTO assignVendorDTO = new AssignVendorDTO(); // AssignVendorDTO | Assigned vendor to a job in a project.
    try {
      apiInstance.assignVendor(jobId, assignVendorDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsClassicApi#assignVendor");
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
| **jobId** | **String**| job&#39;s internal identifier | |
| **assignVendorDTO** | [**AssignVendorDTO**](AssignVendorDTO.md)| Assigned vendor to a job in a project. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="changeStatus"></a>
# **changeStatus**
> changeStatus(jobId, jobStatusDTO)

Changes job status if possible (400 Bad Request is returned otherwise).

Changes job status if possible (400 Bad Request is returned otherwise). The status has to be specified using one of the following keys:&lt;ul&gt;&lt;li&gt;OPEN – available when the job has one of the following statuses: ACCEPTED, CANCELED&lt;/li&gt;&lt;li&gt;ACCEPTED – available when the job has one of the following statuses: OPEN (Vendor and dates have to be set before calling the operation), STARTED&lt;/li&gt;&lt;li&gt;STARTED – available when the job has one of the following statuses: ACCEPTED, READY&lt;/li&gt;&lt;li&gt;READY – available when the job has one of the following statuses: STARTED&lt;/li&gt;&lt;li&gt;CANCELLED – available when the job has one of the following statuses: OPEN, ACCEPTED, STARTED, OFFERS_SENT&lt;/li&gt;&lt;li&gt;OFFERS_SENT – not available as a target status for this operation&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsClassicApi apiInstance = new JobsClassicApi(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    JobStatusDTO jobStatusDTO = new JobStatusDTO(); // JobStatusDTO | Changed job status.
    try {
      apiInstance.changeStatus(jobId, jobStatusDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsClassicApi#changeStatus");
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
| **jobId** | **String**| job&#39;s internal identifier | |
| **jobStatusDTO** | [**JobStatusDTO**](JobStatusDTO.md)| Changed job status. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="getJobDetails"></a>
# **getJobDetails**
> JobDto getJobDetails(jobId)

Returns job details by jobId.

Returns job details by jobId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsClassicApi apiInstance = new JobsClassicApi(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    try {
      JobDto result = apiInstance.getJobDetails(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsClassicApi#getJobDetails");
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
| **jobId** | **String**| job&#39;s internal identifier | |

### Return type

[**JobDto**](JobDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getJobFiles"></a>
# **getJobFiles**
> JobFilesDTO getJobFiles(jobId)

Returns list of input and output files of a job.

Returns list of input and output files of a job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsClassicApi apiInstance = new JobsClassicApi(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    try {
      JobFilesDTO result = apiInstance.getJobFiles(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsClassicApi#getJobFiles");
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
| **jobId** | **String**| job&#39;s internal identifier | |

### Return type

[**JobFilesDTO**](JobFilesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getJobFiles1"></a>
# **getJobFiles1**
> FileMetadataDTO getJobFiles1(jobId, fileId)

Returns file metadata.

Returns file metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsClassicApi apiInstance = new JobsClassicApi(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    Long fileId = 56L; // Long | file's internal identifier
    try {
      FileMetadataDTO result = apiInstance.getJobFiles1(jobId, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsClassicApi#getJobFiles1");
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
| **jobId** | **String**| job&#39;s internal identifier | |
| **fileId** | **Long**| file&#39;s internal identifier | |

### Return type

[**FileMetadataDTO**](FileMetadataDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateDates"></a>
# **updateDates**
> updateDates(jobId, jobDatesDto)

Updates dates of a given job.

Updates dates of a given job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsClassicApi apiInstance = new JobsClassicApi(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    JobDatesDto jobDatesDto = new JobDatesDto(); // JobDatesDto | New job dates.
    try {
      apiInstance.updateDates(jobId, jobDatesDto);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsClassicApi#updateDates");
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
| **jobId** | **String**| job&#39;s internal identifier | |
| **jobDatesDto** | [**JobDatesDto**](JobDatesDto.md)| New job dates. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateInstructions"></a>
# **updateInstructions**
> updateInstructions(jobId, instructionsDTO)

Updates instructions for a job.

Updates instructions for a job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsClassicApi apiInstance = new JobsClassicApi(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    InstructionsDTO instructionsDTO = new InstructionsDTO(); // InstructionsDTO | Updated instructions for a job.
    try {
      apiInstance.updateInstructions(jobId, instructionsDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsClassicApi#updateInstructions");
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
| **jobId** | **String**| job&#39;s internal identifier | |
| **instructionsDTO** | [**InstructionsDTO**](InstructionsDTO.md)| Updated instructions for a job. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

