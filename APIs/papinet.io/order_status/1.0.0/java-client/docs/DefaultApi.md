# DefaultApi

All URIs are relative to *https://papinet.papinet.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ordersGet**](DefaultApi.md#ordersGet) | **GET** /orders | List &#x60;orders&#x60; |
| [**ordersOrderIdGet**](DefaultApi.md#ordersOrderIdGet) | **GET** /orders/{orderId} | Get an &#x60;order&#x60; |


<a id="ordersGet"></a>
# **ordersGet**
> ListOfOrders ordersGet(orderStatus, offset, limit)

List &#x60;orders&#x60;

Gets a paginated list of all &#x60;orders&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://papinet.papinet.io");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String orderStatus = "Active"; // String | Filter by status
    String offset = "offset_example"; // String | The number of items to skip before starting to collect the result set.
    String limit = "limit_example"; // String | The maximum number of items to return. If the value exceeds the maximum, then the maximum value will be used.
    try {
      ListOfOrders result = apiInstance.ordersGet(orderStatus, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ordersGet");
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
| **orderStatus** | **String**| Filter by status | [optional] [enum: Active, Cancelled, Completed] |
| **offset** | **String**| The number of items to skip before starting to collect the result set. | [optional] |
| **limit** | **String**| The maximum number of items to return. If the value exceeds the maximum, then the maximum value will be used. | [optional] |

### Return type

[**ListOfOrders**](ListOfOrders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="ordersOrderIdGet"></a>
# **ordersOrderIdGet**
> Order ordersOrderIdGet(orderId)

Get an &#x60;order&#x60;

Gets the details of a specific &#x60;order&#x60;, including a paginated list of all its lines.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://papinet.papinet.io");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID orderId = UUID.randomUUID(); // UUID | UUID of the `order` to get
    try {
      Order result = apiInstance.ordersOrderIdGet(orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ordersOrderIdGet");
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
| **orderId** | **UUID**| UUID of the &#x60;order&#x60; to get | |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

