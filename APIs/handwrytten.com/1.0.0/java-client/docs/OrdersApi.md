# OrdersApi

All URIs are relative to *https://api.handwrytten.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**singleStepOrder**](OrdersApi.md#singleStepOrder) | **POST** /orders/singleStepOrder | sends an order in a single step.  This is much easier than using other order commands |


<a id="singleStepOrder"></a>
# **singleStepOrder**
> SingleStepOrder200Response singleStepOrder(body)

sends an order in a single step.  This is much easier than using other order commands

Sends an order in one step.  No need to create then process order.  Optionally include a gift card.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    SingleStepOrderRequest body = new SingleStepOrderRequest(); // SingleStepOrderRequest | additional parameters
    try {
      SingleStepOrder200Response result = apiInstance.singleStepOrder(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#singleStepOrder");
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
| **body** | [**SingleStepOrderRequest**](SingleStepOrderRequest.md)| additional parameters | |

### Return type

[**SingleStepOrder200Response**](SingleStepOrder200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful order placement |  -  |

