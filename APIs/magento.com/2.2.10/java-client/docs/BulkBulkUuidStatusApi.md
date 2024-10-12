# BulkBulkUuidStatusApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**asynchronousOperationsBulkStatusV1GetBulkShortStatusGet**](BulkBulkUuidStatusApi.md#asynchronousOperationsBulkStatusV1GetBulkShortStatusGet) | **GET** /V1/bulk/{bulkUuid}/status | bulk/{bulkUuid}/status |


<a id="asynchronousOperationsBulkStatusV1GetBulkShortStatusGet"></a>
# **asynchronousOperationsBulkStatusV1GetBulkShortStatusGet**
> AsynchronousOperationsDataBulkOperationsStatusInterface asynchronousOperationsBulkStatusV1GetBulkShortStatusGet(bulkUuid)

bulk/{bulkUuid}/status

Get Bulk summary data with list of operations items short data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkBulkUuidStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BulkBulkUuidStatusApi apiInstance = new BulkBulkUuidStatusApi(defaultClient);
    String bulkUuid = "bulkUuid_example"; // String | 
    try {
      AsynchronousOperationsDataBulkOperationsStatusInterface result = apiInstance.asynchronousOperationsBulkStatusV1GetBulkShortStatusGet(bulkUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkBulkUuidStatusApi#asynchronousOperationsBulkStatusV1GetBulkShortStatusGet");
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

[**AsynchronousOperationsDataBulkOperationsStatusInterface**](AsynchronousOperationsDataBulkOperationsStatusInterface.md)

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

