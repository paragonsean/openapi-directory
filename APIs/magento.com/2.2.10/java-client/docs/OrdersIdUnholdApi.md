# OrdersIdUnholdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrderManagementV1UnHoldPost**](OrdersIdUnholdApi.md#salesOrderManagementV1UnHoldPost) | **POST** /V1/orders/{id}/unhold | orders/{id}/unhold |


<a id="salesOrderManagementV1UnHoldPost"></a>
# **salesOrderManagementV1UnHoldPost**
> Boolean salesOrderManagementV1UnHoldPost(id)

orders/{id}/unhold

Releases a specified order from hold status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersIdUnholdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersIdUnholdApi apiInstance = new OrdersIdUnholdApi(defaultClient);
    Integer id = 56; // Integer | The order ID.
    try {
      Boolean result = apiInstance.salesOrderManagementV1UnHoldPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersIdUnholdApi#salesOrderManagementV1UnHoldPost");
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

