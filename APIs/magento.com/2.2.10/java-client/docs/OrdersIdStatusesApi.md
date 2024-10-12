# OrdersIdStatusesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrderManagementV1GetStatusGet**](OrdersIdStatusesApi.md#salesOrderManagementV1GetStatusGet) | **GET** /V1/orders/{id}/statuses | orders/{id}/statuses |


<a id="salesOrderManagementV1GetStatusGet"></a>
# **salesOrderManagementV1GetStatusGet**
> String salesOrderManagementV1GetStatusGet(id)

orders/{id}/statuses

Gets the status for a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersIdStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersIdStatusesApi apiInstance = new OrdersIdStatusesApi(defaultClient);
    Integer id = 56; // Integer | The order ID.
    try {
      String result = apiInstance.salesOrderManagementV1GetStatusGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersIdStatusesApi#salesOrderManagementV1GetStatusGet");
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

**String**

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

