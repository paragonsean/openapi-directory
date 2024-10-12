# TransactionsIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesTransactionRepositoryV1GetGet**](TransactionsIdApi.md#salesTransactionRepositoryV1GetGet) | **GET** /V1/transactions/{id} | transactions/{id} |


<a id="salesTransactionRepositoryV1GetGet"></a>
# **salesTransactionRepositoryV1GetGet**
> SalesDataTransactionInterface salesTransactionRepositoryV1GetGet(id)

transactions/{id}

Loads a specified transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransactionsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    TransactionsIdApi apiInstance = new TransactionsIdApi(defaultClient);
    Integer id = 56; // Integer | The transaction ID.
    try {
      SalesDataTransactionInterface result = apiInstance.salesTransactionRepositoryV1GetGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransactionsIdApi#salesTransactionRepositoryV1GetGet");
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
| **id** | **Integer**| The transaction ID. | |

### Return type

[**SalesDataTransactionInterface**](SalesDataTransactionInterface.md)

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

