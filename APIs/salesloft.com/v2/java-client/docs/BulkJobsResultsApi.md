# BulkJobsResultsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2BulkJobsBulkJobsIdResultsGet**](BulkJobsResultsApi.md#v2BulkJobsBulkJobsIdResultsGet) | **GET** /v2/bulk_jobs/{bulk_jobs_id}/results | List job data for a completed bulk job. |


<a id="v2BulkJobsBulkJobsIdResultsGet"></a>
# **v2BulkJobsBulkJobsIdResultsGet**
> List&lt;BulkJobResult&gt; v2BulkJobsBulkJobsIdResultsGet(bulkJobsId, status, id, perPage)

List job data for a completed bulk job.

Fetches multiple job data records for a completed bulk job. Note that until a bulk job&#39;s state is set to &#x60;done&#x60; the returned &#x60;data&#x60; will be an empty array. Pagination is not supported, but cursor based polling is via use of the &#x60;id[gt]&#x60; filter. Pass the last id seen (i.e. &#x60;id[gt]&#x3D;1234&#x60;) in order to get the next batch of records.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkJobsResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    BulkJobsResultsApi apiInstance = new BulkJobsResultsApi(defaultClient);
    Integer bulkJobsId = 56; // Integer | The id for the Bulk Job
    List<String> status = Arrays.asList(); // List<String> | Filter by result status. Accepts multiple statuses. Each status must be one of pending, success, error, retrying
    Object id = null; // Object | Filter by id using comparison operators. Only supports greater than (gt) comparison (i.e. id[gt]=123)
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    try {
      List<BulkJobResult> result = apiInstance.v2BulkJobsBulkJobsIdResultsGet(bulkJobsId, status, id, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkJobsResultsApi#v2BulkJobsBulkJobsIdResultsGet");
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
| **bulkJobsId** | **Integer**| The id for the Bulk Job | |
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

