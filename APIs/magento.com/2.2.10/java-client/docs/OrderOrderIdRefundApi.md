# OrderOrderIdRefundApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRefundOrderV1ExecutePost**](OrderOrderIdRefundApi.md#salesRefundOrderV1ExecutePost) | **POST** /V1/order/{orderId}/refund | order/{orderId}/refund |


<a id="salesRefundOrderV1ExecutePost"></a>
# **salesRefundOrderV1ExecutePost**
> Integer salesRefundOrderV1ExecutePost(orderId, salesRefundOrderV1ExecutePostRequest)

order/{orderId}/refund

Create offline refund for order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderOrderIdRefundApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrderOrderIdRefundApi apiInstance = new OrderOrderIdRefundApi(defaultClient);
    Integer orderId = 56; // Integer | 
    SalesRefundOrderV1ExecutePostRequest salesRefundOrderV1ExecutePostRequest = new SalesRefundOrderV1ExecutePostRequest(); // SalesRefundOrderV1ExecutePostRequest | 
    try {
      Integer result = apiInstance.salesRefundOrderV1ExecutePost(orderId, salesRefundOrderV1ExecutePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderOrderIdRefundApi#salesRefundOrderV1ExecutePost");
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
| **salesRefundOrderV1ExecutePostRequest** | [**SalesRefundOrderV1ExecutePostRequest**](SalesRefundOrderV1ExecutePostRequest.md)|  | [optional] |

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

