# BulkBulkUuidDetailedStatusApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet**](BulkBulkUuidDetailedStatusApi.md#asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet) | **GET** /V1/bulk/{bulkUuid}/detailed-status | bulk/{bulkUuid}/detailed-status |


<a id="asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet"></a>
# **asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet**
> AsynchronousOperationsDataDetailedBulkOperationsStatusInterface asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet(bulkUuid)

bulk/{bulkUuid}/detailed-status

Get Bulk summary data with list of operations items full data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkBulkUuidDetailedStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BulkBulkUuidDetailedStatusApi apiInstance = new BulkBulkUuidDetailedStatusApi(defaultClient);
    String bulkUuid = "bulkUuid_example"; // String | 
    try {
      AsynchronousOperationsDataDetailedBulkOperationsStatusInterface result = apiInstance.asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet(bulkUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkBulkUuidDetailedStatusApi#asynchronousOperationsBulkStatusV1GetBulkDetailedStatusGet");
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
| **bulkUuid** | **String**|  | |

### Return type

[**AsynchronousOperationsDataDetailedBulkOperationsStatusInterface**](AsynchronousOperationsDataDetailedBulkOperationsStatusInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

