# OrderOrderIdShipApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesShipOrderV1ExecutePost**](OrderOrderIdShipApi.md#salesShipOrderV1ExecutePost) | **POST** /V1/order/{orderId}/ship | order/{orderId}/ship |


<a id="salesShipOrderV1ExecutePost"></a>
# **salesShipOrderV1ExecutePost**
> Integer salesShipOrderV1ExecutePost(orderId, salesShipOrderV1ExecutePostRequest)

order/{orderId}/ship

Creates new Shipment for given Order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderOrderIdShipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrderOrderIdShipApi apiInstance = new OrderOrderIdShipApi(defaultClient);
    Integer orderId = 56; // Integer | 
    SalesShipOrderV1ExecutePostRequest salesShipOrderV1ExecutePostRequest = new SalesShipOrderV1ExecutePostRequest(); // SalesShipOrderV1ExecutePostRequest | 
    try {
      Integer result = apiInstance.salesShipOrderV1ExecutePost(orderId, salesShipOrderV1ExecutePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderOrderIdShipApi#salesShipOrderV1ExecutePost");
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
| **salesShipOrderV1ExecutePostRequest** | [**SalesShipOrderV1ExecutePostRequest**](SalesShipOrderV1ExecutePostRequest.md)|  | [optional] |

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

