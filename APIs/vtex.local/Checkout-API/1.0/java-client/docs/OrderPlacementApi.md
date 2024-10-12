# OrderPlacementApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**placeOrder**](OrderPlacementApi.md#placeOrder) | **PUT** /api/checkout/pub/orders | Place order |
| [**placeOrderFromExistingOrderForm**](OrderPlacementApi.md#placeOrderFromExistingOrderForm) | **POST** /api/checkout/pub/orderForm/{orderFormId}/transaction | Place order from an existing cart |
| [**processOrder**](OrderPlacementApi.md#processOrder) | **POST** /api/checkout/pub/gatewayCallback/{orderGroup} | Process order |


<a id="placeOrder"></a>
# **placeOrder**
> PlaceOrder200Response placeOrder(contentType, accept, sc, placeOrderRequest)

Place order

Places order without having any prior cart information. This means all information on items, client, payment and shipping must be sent in the body.    &gt;⚠️ The authentication of this endpoint is required if you are creating an order with an item that has an attachment that creates a Subscription. For more information, access [Subscriptions API](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderPlacementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    OrderPlacementApi apiInstance = new OrderPlacementApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer sc = 1; // Integer | Trade Policy (Sales Channel) identification. This query can be used to create an order for a specific sales channel.
    PlaceOrderRequest placeOrderRequest = new PlaceOrderRequest(); // PlaceOrderRequest | 
    try {
      PlaceOrder200Response result = apiInstance.placeOrder(contentType, accept, sc, placeOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderPlacementApi#placeOrder");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sc** | **Integer**| Trade Policy (Sales Channel) identification. This query can be used to create an order for a specific sales channel. | [optional] |
| **placeOrderRequest** | [**PlaceOrderRequest**](PlaceOrderRequest.md)|  | [optional] |

### Return type

[**PlaceOrder200Response**](PlaceOrder200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="placeOrderFromExistingOrderForm"></a>
# **placeOrderFromExistingOrderForm**
> Object placeOrderFromExistingOrderForm(orderFormId, contentType, accept, placeOrderFromExistingOrderFormRequest)

Place order from an existing cart

This endpoint places an order from an existing &#x60;orderForm&#x60; object, meaning an existing cart.    After the creation of an order with this request, you have five minutes to send payment information and then request payment processing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderPlacementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    OrderPlacementApi apiInstance = new OrderPlacementApi(defaultClient);
    String orderFormId = "ede846222cd44046ba6c638442c3505a"; // String | ID of the `orderForm` corresponding to the cart from which to place the order.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    PlaceOrderFromExistingOrderFormRequest placeOrderFromExistingOrderFormRequest = new PlaceOrderFromExistingOrderFormRequest(); // PlaceOrderFromExistingOrderFormRequest | 
    try {
      Object result = apiInstance.placeOrderFromExistingOrderForm(orderFormId, contentType, accept, placeOrderFromExistingOrderFormRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderPlacementApi#placeOrderFromExistingOrderForm");
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
| **orderFormId** | **String**| ID of the &#x60;orderForm&#x60; corresponding to the cart from which to place the order. | [default to ede846222cd44046ba6c638442c3505a] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **placeOrderFromExistingOrderFormRequest** | [**PlaceOrderFromExistingOrderFormRequest**](PlaceOrderFromExistingOrderFormRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="processOrder"></a>
# **processOrder**
> processOrder(orderGroup, contentType, accept, cookie)

Process order

Order processing callback request, which is made after an order&#39;s payment is approved.    &gt; This request has to be made until five minutes after the [Place order](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders) or [Place order from existing cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) request has been made, or else, the order will not be processed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderPlacementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    OrderPlacementApi apiInstance = new OrderPlacementApi(defaultClient);
    String orderGroup = "123456789"; // String | Order group. It is the part of the `orderId` that comes before the `-`. For example, the `orderGroup` of the order `123456789-01` is `123456789`.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String cookie = "Vtex_CHKO_Auth=0e/RpYIEZu19BuwXB4tZ7eIGu9HT8vdUAHWQDHDpxMc=; CheckoutDataAccess=0e/PoiTEZu19BuwXB4tZ7eIGu9HT8vdUAHWQDHDpxMc="; // String | VTEX Chekout cookie associated with a specific order. Use the `Vtex_CHKO_Auth` and the `CheckoutDataAccess` cookies returned by the [Place order](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder) or [Place order from existing cart](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorderfromexistingorderform) API requests, like a browser would.
    try {
      apiInstance.processOrder(orderGroup, contentType, accept, cookie);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderPlacementApi#processOrder");
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
| **orderGroup** | **String**| Order group. It is the part of the &#x60;orderId&#x60; that comes before the &#x60;-&#x60;. For example, the &#x60;orderGroup&#x60; of the order &#x60;123456789-01&#x60; is &#x60;123456789&#x60;. | [default to 123456789] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **cookie** | **String**| VTEX Chekout cookie associated with a specific order. Use the &#x60;Vtex_CHKO_Auth&#x60; and the &#x60;CheckoutDataAccess&#x60; cookies returned by the [Place order](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder) or [Place order from existing cart](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorderfromexistingorderform) API requests, like a browser would. | [default to Vtex_CHKO_Auth&#x3D;0e/RpYIEZu19BuwXB4tZ7eIGu9HT8vdUAHWQDHDpxMc&#x3D;; CheckoutDataAccess&#x3D;0e/PoiTEZu19BuwXB4tZ7eIGu9HT8vdUAHWQDHDpxMc&#x3D;] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

