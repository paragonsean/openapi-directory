# OrdersIdHoldApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrderManagementV1HoldPost**](OrdersIdHoldApi.md#salesOrderManagementV1HoldPost) | **POST** /V1/orders/{id}/hold | orders/{id}/hold |


<a id="salesOrderManagementV1HoldPost"></a>
# **salesOrderManagementV1HoldPost**
> Boolean salesOrderManagementV1HoldPost(id)

orders/{id}/hold

Holds a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersIdHoldApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersIdHoldApi apiInstance = new OrdersIdHoldApi(defaultClient);
    Integer id = 56; // Integer | The order ID.
    try {
      Boolean result = apiInstance.salesOrderManagementV1HoldPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersIdHoldApi#salesOrderManagementV1HoldPost");
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

