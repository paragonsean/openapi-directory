# OrdersIdCancelApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrderManagementV1CancelPost**](OrdersIdCancelApi.md#salesOrderManagementV1CancelPost) | **POST** /V1/orders/{id}/cancel | orders/{id}/cancel |


<a id="salesOrderManagementV1CancelPost"></a>
# **salesOrderManagementV1CancelPost**
> Boolean salesOrderManagementV1CancelPost(id)

orders/{id}/cancel

Cancels a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersIdCancelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersIdCancelApi apiInstance = new OrdersIdCancelApi(defaultClient);
    Integer id = 56; // Integer | The order ID.
    try {
      Boolean result = apiInstance.salesOrderManagementV1CancelPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersIdCancelApi#salesOrderManagementV1CancelPost");
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

**Boolean**

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

