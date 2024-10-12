# OrdersIdEmailsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrderManagementV1NotifyPost**](OrdersIdEmailsApi.md#salesOrderManagementV1NotifyPost) | **POST** /V1/orders/{id}/emails | orders/{id}/emails |


<a id="salesOrderManagementV1NotifyPost"></a>
# **salesOrderManagementV1NotifyPost**
> Boolean salesOrderManagementV1NotifyPost(id)

orders/{id}/emails

Emails a user a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersIdEmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersIdEmailsApi apiInstance = new OrdersIdEmailsApi(defaultClient);
    Integer id = 56; // Integer | The order ID.
    try {
      Boolean result = apiInstance.salesOrderManagementV1NotifyPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersIdEmailsApi#salesOrderManagementV1NotifyPost");
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

