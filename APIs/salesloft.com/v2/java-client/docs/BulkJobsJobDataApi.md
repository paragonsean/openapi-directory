# BulkJobsJobDataApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2BulkJobsBulkJobsIdJobDataGet**](BulkJobsJobDataApi.md#v2BulkJobsBulkJobsIdJobDataGet) | **GET** /v2/bulk_jobs/{bulk_jobs_id}/job_data | List job data for a bulk job |
| [**v2BulkJobsBulkJobsIdJobDataPost**](BulkJobsJobDataApi.md#v2BulkJobsBulkJobsIdJobDataPost) | **POST** /v2/bulk_jobs/{bulk_jobs_id}/job_data | Create job data for a bulk job |


<a id="v2BulkJobsBulkJobsIdJobDataGet"></a>
# **v2BulkJobsBulkJobsIdJobDataGet**
> List&lt;BulkJobResult&gt; v2BulkJobsBulkJobsIdJobDataGet(bulkJobsId, status, id, perPage)

List job data for a bulk job

Fetches multiple job data records for a given bulk job. Pagination is not supported, but cursor based polling is via use of the &#x60;id[gt]&#x60; filter. Pass the last id seen (i.e. &#x60;id[gt]&#x3D;1234&#x60;) in order to get the next batch of records.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkJobsJobDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    BulkJobsJobDataApi apiInstance = new BulkJobsJobDataApi(defaultClient);
    Integer bulkJobsId = 56; // Integer | The id for the bulk job to which the job data relates
    List<String> status = Arrays.asList(); // List<String> | Filter by result status. Accepts multiple statuses. Each status must be one of pending, success, error, retrying
    Object id = null; // Object | Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]=123)
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    try {
      List<BulkJobResult> result = apiInstance.v2BulkJobsBulkJobsIdJobDataGet(bulkJobsId, status, id, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkJobsJobDataApi#v2BulkJobsBulkJobsIdJobDataGet");
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
| **bulkJobsId** | **Integer**| The id for the bulk job to which the job data relates | |
| **status** | [**List&lt;String&gt;**](String.md)| Filter by result status. Accepts multiple statuses. Each status must be one of pending, success, error, retrying | [optional] |
| **id** | [**Object**](.md)| Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]&#x3D;123) | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |

### Return type

[**List&lt;BulkJobResult&gt;**](BulkJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2BulkJobsBulkJobsIdJobDataPost"></a>
# **v2BulkJobsBulkJobsIdJobDataPost**
> JobDataCreationResult v2BulkJobsBulkJobsIdJobDataPost(bulkJobsId, data)

Create job data for a bulk job

Upload job data for the specified bulk job. Upload an array of objects, where element contains the parameters necessary to execute the individual calls. Each call to this endpoint can handle up to 5,000 records at a time. There is no limit to how many times you can create job data for a given bulk job.  For additional information on creating bulk jobs, the types of supported bulk jobs, and examples of the bulk job flow, visit the &lt;a href&#x3D;\&quot;/bulk.html\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;bulk job details page&lt;/a&gt;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkJobsJobDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    BulkJobsJobDataApi apiInstance = new BulkJobsJobDataApi(defaultClient);
    Integer bulkJobsId = 56; // Integer | The id for the bulk job to which the job data relates
    List<String> data = Arrays.asList(); // List<String> | Array of objects containing parameters to be used to execute an instance of each. Array must be 5,000 records or less.
    try {
      JobDataCreationResult result = apiInstance.v2BulkJobsBulkJobsIdJobDataPost(bulkJobsId, data);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkJobsJobDataApi#v2BulkJobsBulkJobsIdJobDataPost");
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
| **bulkJobsId** | **Integer**| The id for the bulk job to which the job data relates | |
| **data** | [**List&lt;String&gt;**](String.md)| Array of objects containing parameters to be used to execute an instance of each. Array must be 5,000 records or less. | |

### Return type

[**JobDataCreationResult**](JobDataCreationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

