# ClassifierApi

All URIs are relative to *https://api.ntropy.network*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getABatchOfBusinessTransactionClassificationResults**](ClassifierApi.md#getABatchOfBusinessTransactionClassificationResults) | **GET** /classifier/business/batch/{id} | Get a batch of business transaction classification results. |
| [**getABatchOfConsumerTransactionClassificationResults**](ClassifierApi.md#getABatchOfConsumerTransactionClassificationResults) | **GET** /classifier/consumer/batch/{id} | Get a batch of consumer transaction classification results. |


<a id="getABatchOfBusinessTransactionClassificationResults"></a>
# **getABatchOfBusinessTransactionClassificationResults**
> GetABatchOfBusinessTransactionClassificationResults200Response getABatchOfBusinessTransactionClassificationResults(id)

Get a batch of business transaction classification results.

Get a batch of business transaction classification results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassifierApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ntropy.network");

    ClassifierApi apiInstance = new ClassifierApi(defaultClient);
    String id = "247ee045-3d04-4b3c-872b-a9160b810f33"; // String | (Required) Batch id.
    try {
      GetABatchOfBusinessTransactionClassificationResults200Response result = apiInstance.getABatchOfBusinessTransactionClassificationResults(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassifierApi#getABatchOfBusinessTransactionClassificationResults");
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

<a id="getABatchOfConsumerTransactionClassificationResults"></a>
# **getABatchOfConsumerTransactionClassificationResults**
> GetABatchOfConsumerTransactionClassificationResults200Response getABatchOfConsumerTransactionClassificationResults(id)

Get a batch of consumer transaction classification results.

Get a batch of consumer transaction classification results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassifierApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ntropy.network");

    ClassifierApi apiInstance = new ClassifierApi(defaultClient);
    String id = "247ee045-3d04-4b3c-872b-a9160b810f33"; // String | (Required) Batch id.
    try {
      GetABatchOfConsumerTransactionClassificationResults200Response result = apiInstance.getABatchOfConsumerTransactionClassificationResults(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassifierApi#getABatchOfConsumerTransactionClassificationResults");
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

