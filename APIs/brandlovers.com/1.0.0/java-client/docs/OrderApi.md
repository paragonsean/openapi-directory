# OrderApi

All URIs are relative to *https://api.brandlovers.com/marketplace/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**orderOrderIdGet**](OrderApi.md#orderOrderIdGet) | **GET** /order/{orderId} | Returns all details of a order |
| [**orderOrderIdShipmentCancelPost**](OrderApi.md#orderOrderIdShipmentCancelPost) | **POST** /order/{orderId}/shipment/cancel | Confirm shipment canceletion (when requested by the customer) or failure to deliver |
| [**orderOrderIdShipmentDeliveredPost**](OrderApi.md#orderOrderIdShipmentDeliveredPost) | **POST** /order/{orderId}/shipment/delivered | Confirms that a shipment was delivered |
| [**orderOrderIdShipmentExchangePost**](OrderApi.md#orderOrderIdShipmentExchangePost) | **POST** /order/{orderId}/shipment/exchange | Confirm item exchange |
| [**orderOrderIdShipmentReturnPost**](OrderApi.md#orderOrderIdShipmentReturnPost) | **POST** /order/{orderId}/shipment/return | Confirm order item return and refund |
| [**orderOrderIdShipmentSentPost**](OrderApi.md#orderOrderIdShipmentSentPost) | **POST** /order/{orderId}/shipment/sent | Update new order to include shipment information |


<a id="orderOrderIdGet"></a>
# **orderOrderIdGet**
> Order orderOrderIdGet(authorization, orderId)

Returns all details of a order

Returns all details of a single order, including last status, items shipped or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String orderId = "orderId_example"; // String | Unique Id of this order.
    try {
      Order result = apiInstance.orderOrderIdGet(authorization, orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderOrderIdGet");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **orderId** | **String**| Unique Id of this order. | |

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
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **403** | Server refused to process your request. Please check the API SLA and reduce number of requests per second. |  -  |
| **404** | Object not found. Was not able to find orderId |  -  |

<a id="orderOrderIdShipmentCancelPost"></a>
# **orderOrderIdShipmentCancelPost**
> orderOrderIdShipmentCancelPost(authorization, orderId, body)

Confirm shipment canceletion (when requested by the customer) or failure to deliver

Confirm shipment canceletion (when requested by the customer) or failure to deliver one shipment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String orderId = "orderId_example"; // String | Unique Order Id
    NewTrackingRefund body = new NewTrackingRefund(); // NewTrackingRefund | 
    try {
      apiInstance.orderOrderIdShipmentCancelPost(authorization, orderId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderOrderIdShipmentCancelPost");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **orderId** | **String**| Unique Order Id | |
| **body** | [**NewTrackingRefund**](NewTrackingRefund.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success. |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **404** | Object not found. Was not able to find orderId |  -  |

<a id="orderOrderIdShipmentDeliveredPost"></a>
# **orderOrderIdShipmentDeliveredPost**
> orderOrderIdShipmentDeliveredPost(authorization, orderId, body)

Confirms that a shipment was delivered

Confirms that a shipment was delivered. Must inform quantity of successfully deliverd items even if items deliverd was less than the original order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String orderId = "orderId_example"; // String | Unique Order Id
    Newshipmentstatus body = new Newshipmentstatus(); // Newshipmentstatus | 
    try {
      apiInstance.orderOrderIdShipmentDeliveredPost(authorization, orderId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderOrderIdShipmentDeliveredPost");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **orderId** | **String**| Unique Order Id | |
| **body** | [**Newshipmentstatus**](Newshipmentstatus.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucess! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **404** | Object not found. Was not able to find orderId |  -  |

<a id="orderOrderIdShipmentExchangePost"></a>
# **orderOrderIdShipmentExchangePost**
> orderOrderIdShipmentExchangePost(authorization, orderId, body)

Confirm item exchange

This enpoint to confirm item exchange when failure to deliver or requested by the customer. All customer requests are tracket via trouble tickets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String orderId = "orderId_example"; // String | Unique Order Id
    NewTrackingRefund body = new NewTrackingRefund(); // NewTrackingRefund | 
    try {
      apiInstance.orderOrderIdShipmentExchangePost(authorization, orderId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderOrderIdShipmentExchangePost");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **orderId** | **String**| Unique Order Id | |
| **body** | [**NewTrackingRefund**](NewTrackingRefund.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucess! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **404** | Object not found. Was not able to find orderId |  -  |

<a id="orderOrderIdShipmentReturnPost"></a>
# **orderOrderIdShipmentReturnPost**
> orderOrderIdShipmentReturnPost(authorization, orderId, body)

Confirm order item return and refund

Use this endpoint to return and refund items froma a order. In order to fully return an order list all items and applicate quantity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String orderId = "orderId_example"; // String | Order unique Id
    NewTrackingRefund body = new NewTrackingRefund(); // NewTrackingRefund | 
    try {
      apiInstance.orderOrderIdShipmentReturnPost(authorization, orderId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderOrderIdShipmentReturnPost");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **orderId** | **String**| Order unique Id | |
| **body** | [**NewTrackingRefund**](NewTrackingRefund.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucess! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **404** | Object not found. Was not able to find orderId |  -  |

<a id="orderOrderIdShipmentSentPost"></a>
# **orderOrderIdShipmentSentPost**
> orderOrderIdShipmentSentPost(authorization, orderId, body)

Update new order to include shipment information

Updates order to include shipment shiped information. This endpoint can be used to include a single or multiple shipments for any give order. In order to inform that all items of a order where shipped list all of them, including applicable quantities in the payload.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String orderId = "orderId_example"; // String | Unique Order Id
    Newshipmentstatus body = new Newshipmentstatus(); // Newshipmentstatus | 
    try {
      apiInstance.orderOrderIdShipmentSentPost(authorization, orderId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderOrderIdShipmentSentPost");
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
| **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | |
| **orderId** | **String**| Unique Order Id | |
| **body** | [**Newshipmentstatus**](Newshipmentstatus.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucess! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **404** | Object not found. Was not able to find orderId |  -  |

