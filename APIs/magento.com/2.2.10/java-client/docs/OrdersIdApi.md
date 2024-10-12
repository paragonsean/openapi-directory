# OrdersIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrderRepositoryV1GetGet**](OrdersIdApi.md#salesOrderRepositoryV1GetGet) | **GET** /V1/orders/{id} | orders/{id} |


<a id="salesOrderRepositoryV1GetGet"></a>
# **salesOrderRepositoryV1GetGet**
> SalesDataOrderInterface salesOrderRepositoryV1GetGet(id)

orders/{id}

Loads a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersIdApi apiInstance = new OrdersIdApi(defaultClient);
    Integer id = 56; // Integer | The order ID.
    try {
      SalesDataOrderInterface result = apiInstance.salesOrderRepositoryV1GetGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersIdApi#salesOrderRepositoryV1GetGet");
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
| **id** | **Integer**| The order ID. | |

### Return type

[**SalesDataOrderInterface**](SalesDataOrderInterface.md)

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

