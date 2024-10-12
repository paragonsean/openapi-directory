# OrdersItemsIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrderItemRepositoryV1GetGet**](OrdersItemsIdApi.md#salesOrderItemRepositoryV1GetGet) | **GET** /V1/orders/items/{id} | orders/items/{id} |


<a id="salesOrderItemRepositoryV1GetGet"></a>
# **salesOrderItemRepositoryV1GetGet**
> SalesDataOrderItemInterface salesOrderItemRepositoryV1GetGet(id)

orders/items/{id}

Loads a specified order item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersItemsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersItemsIdApi apiInstance = new OrdersItemsIdApi(defaultClient);
    Integer id = 56; // Integer | The order item ID.
    try {
      SalesDataOrderItemInterface result = apiInstance.salesOrderItemRepositoryV1GetGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersItemsIdApi#salesOrderItemRepositoryV1GetGet");
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
| **id** | **Integer**| The order item ID. | |

### Return type

[**SalesDataOrderItemInterface**](SalesDataOrderItemInterface.md)

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

