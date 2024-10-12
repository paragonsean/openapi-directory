# BusinessApi

All URIs are relative to *https://api.ntropy.network*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getABatchOfBusinessTransactionClassificationResults_0**](BusinessApi.md#getABatchOfBusinessTransactionClassificationResults_0) | **GET** /classifier/business/batch/{id} | Get a batch of business transaction classification results. |


<a id="getABatchOfBusinessTransactionClassificationResults_0"></a>
# **getABatchOfBusinessTransactionClassificationResults_0**
> GetABatchOfBusinessTransactionClassificationResults200Response getABatchOfBusinessTransactionClassificationResults_0(id)

Get a batch of business transaction classification results.

Get a batch of business transaction classification results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ntropy.network");

    BusinessApi apiInstance = new BusinessApi(defaultClient);
    String id = "247ee045-3d04-4b3c-872b-a9160b810f33"; // String | (Required) Batch id.
    try {
      GetABatchOfBusinessTransactionClassificationResults200Response result = apiInstance.getABatchOfBusinessTransactionClassificationResults_0(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessApi#getABatchOfBusinessTransactionClassificationResults_0");
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
| **id** | **String**| (Required) Batch id. | |

### Return type

[**GetABatchOfBusinessTransactionClassificationResults200Response**](GetABatchOfBusinessTransactionClassificationResults200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned a batch of business transaction classification results. |  -  |
| **404** | Not found. |  -  |
| **500** | Internal server error. |  -  |

