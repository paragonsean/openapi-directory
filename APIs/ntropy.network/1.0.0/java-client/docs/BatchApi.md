# BatchApi

All URIs are relative to *https://api.ntropy.network*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getABatchOfConsumerTransactionClassificationResults_1**](BatchApi.md#getABatchOfConsumerTransactionClassificationResults_1) | **GET** /classifier/consumer/batch/{id} | Get a batch of consumer transaction classification results. |


<a id="getABatchOfConsumerTransactionClassificationResults_1"></a>
# **getABatchOfConsumerTransactionClassificationResults_1**
> GetABatchOfConsumerTransactionClassificationResults200Response getABatchOfConsumerTransactionClassificationResults_1(id)

Get a batch of consumer transaction classification results.

Get a batch of consumer transaction classification results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BatchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ntropy.network");

    BatchApi apiInstance = new BatchApi(defaultClient);
    String id = "247ee045-3d04-4b3c-872b-a9160b810f33"; // String | (Required) Batch id.
    try {
      GetABatchOfConsumerTransactionClassificationResults200Response result = apiInstance.getABatchOfConsumerTransactionClassificationResults_1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BatchApi#getABatchOfConsumerTransactionClassificationResults_1");
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

[**GetABatchOfConsumerTransactionClassificationResults200Response**](GetABatchOfConsumerTransactionClassificationResults200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned a batch of consumer transaction classification results. |  -  |
| **404** | Not found |  -  |
| **500** | Internal server error |  -  |

