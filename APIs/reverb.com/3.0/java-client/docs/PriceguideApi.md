# PriceguideApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**priceguideIdTransactionsSummaryGet**](PriceguideApi.md#priceguideIdTransactionsSummaryGet) | **GET** /priceguide/{id}/transactions/summary | Get a summary of transactions for a given price guide |


<a id="priceguideIdTransactionsSummaryGet"></a>
# **priceguideIdTransactionsSummaryGet**
> priceguideIdTransactionsSummaryGet(id, numberOfMonths, condition)

Get a summary of transactions for a given price guide

Get a summary of transactions for a given price guide

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceguideApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    PriceguideApi apiInstance = new PriceguideApi(defaultClient);
    String id = "id_example"; // String | 
    Integer numberOfMonths = 3; // Integer | 
    String condition = "used"; // String | 
    try {
      apiInstance.priceguideIdTransactionsSummaryGet(id, numberOfMonths, condition);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceguideApi#priceguideIdTransactionsSummaryGet");
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
| **id** | **String**|  | |
| **numberOfMonths** | **Integer**|  | [optional] [default to 3] |
| **condition** | **String**|  | [optional] [default to used] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

