# OrderOrderIdInvoiceApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesInvoiceOrderV1ExecutePost**](OrderOrderIdInvoiceApi.md#salesInvoiceOrderV1ExecutePost) | **POST** /V1/order/{orderId}/invoice | order/{orderId}/invoice |


<a id="salesInvoiceOrderV1ExecutePost"></a>
# **salesInvoiceOrderV1ExecutePost**
> Integer salesInvoiceOrderV1ExecutePost(orderId, salesInvoiceOrderV1ExecutePostRequest)

order/{orderId}/invoice



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderOrderIdInvoiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrderOrderIdInvoiceApi apiInstance = new OrderOrderIdInvoiceApi(defaultClient);
    Integer orderId = 56; // Integer | 
    SalesInvoiceOrderV1ExecutePostRequest salesInvoiceOrderV1ExecutePostRequest = new SalesInvoiceOrderV1ExecutePostRequest(); // SalesInvoiceOrderV1ExecutePostRequest | 
    try {
      Integer result = apiInstance.salesInvoiceOrderV1ExecutePost(orderId, salesInvoiceOrderV1ExecutePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderOrderIdInvoiceApi#salesInvoiceOrderV1ExecutePost");
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
| **orderId** | **Integer**|  | |
| **salesInvoiceOrderV1ExecutePostRequest** | [**SalesInvoiceOrderV1ExecutePostRequest**](SalesInvoiceOrderV1ExecutePostRequest.md)|  | [optional] |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

