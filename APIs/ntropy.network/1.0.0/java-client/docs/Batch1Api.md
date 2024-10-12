# Batch1Api

All URIs are relative to *https://api.ntropy.network*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getABatchOfBusinessTransactionClassificationResults_1**](Batch1Api.md#getABatchOfBusinessTransactionClassificationResults_1) | **GET** /classifier/business/batch/{id} | Get a batch of business transaction classification results. |


<a id="getABatchOfBusinessTransactionClassificationResults_1"></a>
# **getABatchOfBusinessTransactionClassificationResults_1**
> GetABatchOfBusinessTransactionClassificationResults200Response getABatchOfBusinessTransactionClassificationResults_1(id)

Get a batch of business transaction classification results.

Get a batch of business transaction classification results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Batch1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ntropy.network");

    Batch1Api apiInstance = new Batch1Api(defaultClient);
    String id = "247ee045-3d04-4b3c-872b-a9160b810f33"; // String | (Required) Batch id.
    try {
      GetABatchOfBusinessTransactionClassificationResults200Response result = apiInstance.getABatchOfBusinessTransactionClassificationResults_1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Batch1Api#getABatchOfBusinessTransactionClassificationResults_1");
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

