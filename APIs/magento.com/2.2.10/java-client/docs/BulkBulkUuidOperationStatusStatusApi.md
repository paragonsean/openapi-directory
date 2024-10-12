# BulkBulkUuidOperationStatusStatusApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet**](BulkBulkUuidOperationStatusStatusApi.md#asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet) | **GET** /V1/bulk/{bulkUuid}/operation-status/{status} | bulk/{bulkUuid}/operation-status/{status} |


<a id="asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet"></a>
# **asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet**
> Integer asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet(bulkUuid, status)

bulk/{bulkUuid}/operation-status/{status}

Get operations count by bulk uuid and status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkBulkUuidOperationStatusStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    BulkBulkUuidOperationStatusStatusApi apiInstance = new BulkBulkUuidOperationStatusStatusApi(defaultClient);
    String bulkUuid = "bulkUuid_example"; // String | 
    Integer status = 56; // Integer | 
    try {
      Integer result = apiInstance.asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet(bulkUuid, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkBulkUuidOperationStatusStatusApi#asynchronousOperationsBulkStatusV1GetOperationsCountByBulkIdAndStatusGet");
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
| **status** | **Integer**|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

