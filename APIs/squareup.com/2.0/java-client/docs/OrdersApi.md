# OrdersApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchRetrieveOrders**](OrdersApi.md#batchRetrieveOrders) | **POST** /v2/orders/batch-retrieve | BatchRetrieveOrders |
| [**calculateOrder**](OrdersApi.md#calculateOrder) | **POST** /v2/orders/calculate | CalculateOrder |
| [**createOrder**](OrdersApi.md#createOrder) | **POST** /v2/orders | CreateOrder |
| [**payOrder**](OrdersApi.md#payOrder) | **POST** /v2/orders/{order_id}/pay | PayOrder |
| [**searchOrders**](OrdersApi.md#searchOrders) | **POST** /v2/orders/search | SearchOrders |
| [**v2OrdersOrderIdGet**](OrdersApi.md#v2OrdersOrderIdGet) | **GET** /v2/orders/{order_id} | RetrieveOrder |
| [**v2OrdersOrderIdPut**](OrdersApi.md#v2OrdersOrderIdPut) | **PUT** /v2/orders/{order_id} | UpdateOrder |


<a id="batchRetrieveOrders"></a>
# **batchRetrieveOrders**
> BatchRetrieveOrdersResponse batchRetrieveOrders(batchRetrieveOrdersRequest)

BatchRetrieveOrders

Retrieves a set of [orders](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by their IDs.  If a given order ID does not exist, the ID is ignored instead of generating an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    BatchRetrieveOrdersRequest batchRetrieveOrdersRequest = new BatchRetrieveOrdersRequest(); // BatchRetrieveOrdersRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      BatchRetrieveOrdersResponse result = apiInstance.batchRetrieveOrders(batchRetrieveOrdersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#batchRetrieveOrders");
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
| **batchRetrieveOrdersRequest** | [**BatchRetrieveOrdersRequest**](BatchRetrieveOrdersRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**BatchRetrieveOrdersResponse**](BatchRetrieveOrdersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="calculateOrder"></a>
# **calculateOrder**
> CalculateOrderResponse calculateOrder(calculateOrderRequest)

CalculateOrder

Enables applications to preview order pricing without creating an order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    CalculateOrderRequest calculateOrderRequest = new CalculateOrderRequest(); // CalculateOrderRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CalculateOrderResponse result = apiInstance.calculateOrder(calculateOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#calculateOrder");
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
| **calculateOrderRequest** | [**CalculateOrderRequest**](CalculateOrderRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CalculateOrderResponse**](CalculateOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="createOrder"></a>
# **createOrder**
> CreateOrderResponse createOrder(createOrderRequest)

CreateOrder

Creates a new [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) that can include information about products for purchase and settings to apply to the purchase.  To pay for a created order, see  [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).  You can modify open orders using the [UpdateOrder](https://developer.squareup.com/reference/square_2021-08-18/orders-api/update-order) endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    CreateOrderRequest createOrderRequest = new CreateOrderRequest(); // CreateOrderRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateOrderResponse result = apiInstance.createOrder(createOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#createOrder");
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
| **createOrderRequest** | [**CreateOrderRequest**](CreateOrderRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateOrderResponse**](CreateOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="payOrder"></a>
# **payOrder**
> PayOrderResponse payOrder(orderId, payOrderRequest)

PayOrder

Pay for an [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) using one or more approved [payments](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment) or settle an order with a total of &#x60;0&#x60;.  The total of the &#x60;payment_ids&#x60; listed in the request must be equal to the order total. Orders with a total amount of &#x60;0&#x60; can be marked as paid by specifying an empty array of &#x60;payment_ids&#x60; in the request.  To be used with &#x60;PayOrder&#x60;, a payment must:  - Reference the order by specifying the &#x60;order_id&#x60; when [creating the payment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/create-payment). Any approved payments that reference the same &#x60;order_id&#x60; not specified in the &#x60;payment_ids&#x60; is canceled. - Be approved with [delayed capture](https://developer.squareup.com/docs/payments-api/take-payments#delayed-capture). Using a delayed capture payment with &#x60;PayOrder&#x60; completes the approved payment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String orderId = "orderId_example"; // String | The ID of the order being paid.
    PayOrderRequest payOrderRequest = new PayOrderRequest(); // PayOrderRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      PayOrderResponse result = apiInstance.payOrder(orderId, payOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#payOrder");
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
| **orderId** | **String**| The ID of the order being paid. | |
| **payOrderRequest** | [**PayOrderRequest**](PayOrderRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**PayOrderResponse**](PayOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="searchOrders"></a>
# **searchOrders**
> SearchOrdersResponse searchOrders(searchOrdersRequest)

SearchOrders

Search all orders for one or more locations. Orders include all sales, returns, and exchanges regardless of how or when they entered the Square ecosystem (such as Point of Sale, Invoices, and Connect APIs).  &#x60;SearchOrders&#x60; requests need to specify which locations to search and define a [SearchOrdersQuery](https://developer.squareup.com/reference/square_2021-08-18/objects/SearchOrdersQuery) object that controls how to sort or filter the results. Your &#x60;SearchOrdersQuery&#x60; can:    Set filter criteria.   Set the sort order.   Determine whether to return results as complete &#x60;Order&#x60; objects or as [OrderEntry](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) objects.  Note that details for orders processed with Square Point of Sale while in offline mode might not be transmitted to Square for up to 72 hours. Offline orders have a &#x60;created_at&#x60; value that reflects the time the order was created, not the time it was subsequently transmitted to Square.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    SearchOrdersRequest searchOrdersRequest = new SearchOrdersRequest(); // SearchOrdersRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      SearchOrdersResponse result = apiInstance.searchOrders(searchOrdersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#searchOrders");
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
| **searchOrdersRequest** | [**SearchOrdersRequest**](SearchOrdersRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**SearchOrdersResponse**](SearchOrdersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2OrdersOrderIdGet"></a>
# **v2OrdersOrderIdGet**
> RetrieveOrderResponse v2OrdersOrderIdGet(orderId)

RetrieveOrder

Retrieves an [Order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String orderId = "orderId_example"; // String | The ID of the order to retrieve.
    try {
      RetrieveOrderResponse result = apiInstance.v2OrdersOrderIdGet(orderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#v2OrdersOrderIdGet");
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
| **orderId** | **String**| The ID of the order to retrieve. | |

### Return type

[**RetrieveOrderResponse**](RetrieveOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2OrdersOrderIdPut"></a>
# **v2OrdersOrderIdPut**
> UpdateOrderResponse v2OrdersOrderIdPut(orderId, updateOrderRequest)

UpdateOrder

Updates an open [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by adding, replacing, or deleting fields. Orders with a &#x60;COMPLETED&#x60; or &#x60;CANCELED&#x60; state cannot be updated.  An &#x60;UpdateOrder&#x60; request requires the following:  - The &#x60;order_id&#x60; in the endpoint path, identifying the order to update. - The latest &#x60;version&#x60; of the order to update. - The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders#sparse-order-objects) containing only the fields to update and the version to which the update is being applied. - If deleting fields, the [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation) identifying the fields to clear.  To pay for an order, see  [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String orderId = "orderId_example"; // String | The ID of the order to update.
    UpdateOrderRequest updateOrderRequest = new UpdateOrderRequest(); // UpdateOrderRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      UpdateOrderResponse result = apiInstance.v2OrdersOrderIdPut(orderId, updateOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#v2OrdersOrderIdPut");
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
| **orderId** | **String**| The ID of the order to update. | |
| **updateOrderRequest** | [**UpdateOrderRequest**](UpdateOrderRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**UpdateOrderResponse**](UpdateOrderResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

