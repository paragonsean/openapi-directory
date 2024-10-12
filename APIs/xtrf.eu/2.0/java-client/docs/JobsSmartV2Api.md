# JobsSmartV2Api

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addExternalFileLink**](JobsSmartV2Api.md#addExternalFileLink) | **POST** /v2/jobs/{jobId}/files/addExternalLink |  |
| [**addFileLinks**](JobsSmartV2Api.md#addFileLinks) | **POST** /v2/jobs/{jobId}/files/delivered/addLink | Adds file link to the project as a link delivered in the job. |
| [**addFiles**](JobsSmartV2Api.md#addFiles) | **PUT** /v2/jobs/{jobId}/files/delivered/add | Adds files to the project as delivered in the job. |
| [**assignVendor1**](JobsSmartV2Api.md#assignVendor1) | **PUT** /v2/jobs/{jobId}/vendor | Assigns vendor to a job in a project. |
| [**changeDates**](JobsSmartV2Api.md#changeDates) | **PUT** /v2/jobs/{jobId}/dates | Updates dates of a given job. |
| [**changeStatus1**](JobsSmartV2Api.md#changeStatus1) | **PUT** /v2/jobs/{jobId}/status | Changes job status if possible (400 Bad Request is returned otherwise). |
| [**getByExternalId**](JobsSmartV2Api.md#getByExternalId) | **GET** /v2/jobs/for-external-id |  |
| [**getDeliveredFiles**](JobsSmartV2Api.md#getDeliveredFiles) | **GET** /v2/jobs/{jobId}/files/delivered | Returns list of files delivered in the job. |
| [**getFileById1**](JobsSmartV2Api.md#getFileById1) | **GET** /v2/jobs/{jobId} | Returns details for a job. |
| [**getSharedReferenceFiles**](JobsSmartV2Api.md#getSharedReferenceFiles) | **GET** /v2/jobs/{jobId}/files/sharedReferenceFiles | Returns list of files shared with the job as Reference Files. |
| [**getSharedWorkFiles**](JobsSmartV2Api.md#getSharedWorkFiles) | **GET** /v2/jobs/{jobId}/files/sharedWorkFiles | Returns list of files shared with the job as Work Files. |
| [**shareAsReferenceFiles**](JobsSmartV2Api.md#shareAsReferenceFiles) | **PUT** /v2/jobs/{jobId}/files/sharedReferenceFiles/share | Shares selected files as Reference Files with a job in a project. |
| [**shareAsWorkFiles**](JobsSmartV2Api.md#shareAsWorkFiles) | **PUT** /v2/jobs/{jobId}/files/sharedWorkFiles/share | Shares selected files as Work Files with a job in a project. |
| [**stopSharing**](JobsSmartV2Api.md#stopSharing) | **PUT** /v2/jobs/{jobId}/files/stopSharing | Stops sharing selected files with a job in a project. |
| [**updateInstructions4**](JobsSmartV2Api.md#updateInstructions4) | **PUT** /v2/jobs/{jobId}/instructions | Updates instructions for a job. |
| [**uploadFile1**](JobsSmartV2Api.md#uploadFile1) | **POST** /v2/jobs/{jobId}/files/delivered/upload | Uploads file to the project as a file delivered in the job. |


<a id="addExternalFileLink"></a>
# **addExternalFileLink**
> addExternalFileLink(jobId, externalFileDto)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    ExternalFileDto externalFileDto = new ExternalFileDto(); // ExternalFileDto | Added file links to the project as added by PM.
    try {
      apiInstance.addExternalFileLink(jobId, externalFileDto);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#addExternalFileLink");
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
| **externalFileDto** | [**ExternalFileDto**](ExternalFileDto.md)| Added file links to the project as added by PM. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | default response |  -  |

<a id="addFileLinks"></a>
# **addFileLinks**
> FilesDto addFileLinks(jobId, fileLinkCategorizationsDto)

Adds file link to the project as a link delivered in the job.

Adds file link to the project as a link delivered in the job. The following properties can be specified for each file link:&lt;ul&gt;&lt;li&gt;url (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    FileLinkCategorizationsDto fileLinkCategorizationsDto = new FileLinkCategorizationsDto(); // FileLinkCategorizationsDto | Adds file link to the project as a link delivered in the job.
    try {
      FilesDto result = apiInstance.addFileLinks(jobId, fileLinkCategorizationsDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#addFileLinks");
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
| **fileLinkCategorizationsDto** | [**FileLinkCategorizationsDto**](FileLinkCategorizationsDto.md)| Adds file link to the project as a link delivered in the job. | |

### Return type

[**FilesDto**](FilesDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="addFiles"></a>
# **addFiles**
> addFiles(jobId, fileCategorizationsDto)

Adds files to the project as delivered in the job.

Adds files to the project as delivered in the job. The files have to be uploaded beforehand (see \&quot;POST /jobs/{jobId}/files/upload\&quot; operation). The following properties can be specified for each file:&lt;ul&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    FileCategorizationsDto fileCategorizationsDto = new FileCategorizationsDto(); // FileCategorizationsDto | Added files to the project as delivered in the job.
    try {
      apiInstance.addFiles(jobId, fileCategorizationsDto);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#addFiles");
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
| **fileCategorizationsDto** | [**FileCategorizationsDto**](FileCategorizationsDto.md)| Added files to the project as delivered in the job. | |

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

<a id="assignVendor1"></a>
# **assignVendor1**
> assignVendor1(jobId, vendorPriceProfileDTO)

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
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    VendorPriceProfileDTO vendorPriceProfileDTO = new VendorPriceProfileDTO(); // VendorPriceProfileDTO | Assigned vendor to a job in a project.
    try {
      apiInstance.assignVendor1(jobId, vendorPriceProfileDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#assignVendor1");
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
| **vendorPriceProfileDTO** | [**VendorPriceProfileDTO**](VendorPriceProfileDTO.md)| Assigned vendor to a job in a project. | |

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

<a id="changeDates"></a>
# **changeDates**
> changeDates(jobId, jobDatesDto)

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
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    JobDatesDto jobDatesDto = new JobDatesDto(); // JobDatesDto | New job dates.
    try {
      apiInstance.changeDates(jobId, jobDatesDto);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#changeDates");
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

<a id="changeStatus1"></a>
# **changeStatus1**
> changeStatus1(jobId, jobStatusDTO)

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
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    JobStatusDTO jobStatusDTO = new JobStatusDTO(); // JobStatusDTO | Changed job status.
    try {
      apiInstance.changeStatus1(jobId, jobStatusDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#changeStatus1");
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

<a id="getByExternalId"></a>
# **getByExternalId**
> getByExternalId(externalProjectId, externalId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String externalProjectId = "externalProjectId_example"; // String | job's externalProjectId
    String externalId = "externalId_example"; // String | job's external identifier
    try {
      apiInstance.getByExternalId(externalProjectId, externalId);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#getByExternalId");
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
| **externalProjectId** | **String**| job&#39;s externalProjectId | [optional] |
| **externalId** | **String**| job&#39;s external identifier | [optional] |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | default response |  -  |

<a id="getDeliveredFiles"></a>
# **getDeliveredFiles**
> List&lt;ProjectFileDto&gt; getDeliveredFiles(jobId)

Returns list of files delivered in the job.

Returns list of files delivered in the job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    try {
      List<ProjectFileDto> result = apiInstance.getDeliveredFiles(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#getDeliveredFiles");
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

[**List&lt;ProjectFileDto&gt;**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getFileById1"></a>
# **getFileById1**
> ProjectFileDto getFileById1(jobId)

Returns details for a job.

Returns details for a job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    try {
      ProjectFileDto result = apiInstance.getFileById1(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#getFileById1");
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

[**ProjectFileDto**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getSharedReferenceFiles"></a>
# **getSharedReferenceFiles**
> List&lt;ProjectFileDto&gt; getSharedReferenceFiles(jobId)

Returns list of files shared with the job as Reference Files.

Returns list of files shared with the job as Reference Files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    try {
      List<ProjectFileDto> result = apiInstance.getSharedReferenceFiles(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#getSharedReferenceFiles");
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

[**List&lt;ProjectFileDto&gt;**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getSharedWorkFiles"></a>
# **getSharedWorkFiles**
> List&lt;ProjectFileDto&gt; getSharedWorkFiles(jobId)

Returns list of files shared with the job as Work Files.

Returns list of files shared with the job as Work Files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    try {
      List<ProjectFileDto> result = apiInstance.getSharedWorkFiles(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#getSharedWorkFiles");
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

[**List&lt;ProjectFileDto&gt;**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="shareAsReferenceFiles"></a>
# **shareAsReferenceFiles**
> FilesShareStatusDto shareAsReferenceFiles(jobId, filesDto)

Shares selected files as Reference Files with a job in a project.

Shares selected files as Reference Files with a job in a project. The files and the job have to be part of the same project. The operation is finished successfully even if some of the selected files were already shared with the job. If a file was shared with the job as Work File, it will now be shared as Reference File (and not as Work File).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    FilesDto filesDto = new FilesDto(); // FilesDto | Shared selected files as Reference Files with a job in a project.
    try {
      FilesShareStatusDto result = apiInstance.shareAsReferenceFiles(jobId, filesDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#shareAsReferenceFiles");
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
| **filesDto** | [**FilesDto**](FilesDto.md)| Shared selected files as Reference Files with a job in a project. | |

### Return type

[**FilesShareStatusDto**](FilesShareStatusDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="shareAsWorkFiles"></a>
# **shareAsWorkFiles**
> FilesShareStatusDto shareAsWorkFiles(jobId, filesDto)

Shares selected files as Work Files with a job in a project.

Shares selected files as Work Files with a job in a project. The files and the job have to be part of the same project. The operation is finished successfully even if some of the selected files were already shared with the job. If a file was shared with the job as Reference File, it will now be shared as Work File (and not as Reference File).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    FilesDto filesDto = new FilesDto(); // FilesDto | Shared selected files as Work Files with a job in a project.
    try {
      FilesShareStatusDto result = apiInstance.shareAsWorkFiles(jobId, filesDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#shareAsWorkFiles");
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
| **filesDto** | [**FilesDto**](FilesDto.md)| Shared selected files as Work Files with a job in a project. | |

### Return type

[**FilesShareStatusDto**](FilesShareStatusDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="stopSharing"></a>
# **stopSharing**
> FilesShareStatusDto stopSharing(jobId, filesDto)

Stops sharing selected files with a job in a project.

Stops sharing selected files with a job in a project. The files and the job have to be part of the same project. The operation is finished successfully even if some of the selected files were not shared with the job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    FilesDto filesDto = new FilesDto(); // FilesDto | File sharing stopped for a project task.
    try {
      FilesShareStatusDto result = apiInstance.stopSharing(jobId, filesDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#stopSharing");
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
| **filesDto** | [**FilesDto**](FilesDto.md)| File sharing stopped for a project task. | |

### Return type

[**FilesShareStatusDto**](FilesShareStatusDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateInstructions4"></a>
# **updateInstructions4**
> updateInstructions4(jobId, stringDTO)

Updates instructions for a job.

Updates instructions for a job. See also \&quot;PUT /projects/{projectId}/vendorInstructions\&quot; and \&quot;PUT /quotes/{quoteId}/vendorInstructions\&quot; for updating instructions for all jobs in a project or quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | Updated instructions for a job.
    try {
      apiInstance.updateInstructions4(jobId, stringDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#updateInstructions4");
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
| **stringDTO** | [**StringDTO**](StringDTO.md)| Updated instructions for a job. | |

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

<a id="uploadFile1"></a>
# **uploadFile1**
> FileDto uploadFile1(jobId, _file)

Uploads file to the project as a file delivered in the job.

Uploads file to the project as a file delivered in the job. Only one file can be uploaded at once. When the upload is finished the file has to be added by specifying its category and languages (see \&quot;PUT /jobs/{jobId}/files/add\&quot; operation).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    JobsSmartV2Api apiInstance = new JobsSmartV2Api(defaultClient);
    String jobId = "jobId_example"; // String | job's internal identifier
    File _file = new File("/path/to/file"); // File | 
    try {
      FileDto result = apiInstance.uploadFile1(jobId, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsSmartV2Api#uploadFile1");
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
| **_file** | **File**|  | [optional] |

### Return type

[**FileDto**](FileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

