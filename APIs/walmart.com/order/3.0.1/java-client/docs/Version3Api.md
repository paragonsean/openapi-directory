# Version3Api

All URIs are relative to *https://developer.walmart.com/orderProxy/order-api-doc-app/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acknowledgeOrders**](Version3Api.md#acknowledgeOrders) | **POST** /v3/orders/{purchaseOrderId}/acknowledge | Acknowledge orders |
| [**cancelOrder**](Version3Api.md#cancelOrder) | **POST** /v3/orders/{purchaseOrderId}/cancel | Cancel order lines |
| [**getAllOrders**](Version3Api.md#getAllOrders) | **GET** /v3/orders | Get all orders |
| [**getAllOrdersNext**](Version3Api.md#getAllOrdersNext) | **GET** /v3/orders{nextCursor} | Get orders for next page |
| [**getNextCursorReleasedOrders**](Version3Api.md#getNextCursorReleasedOrders) | **GET** /v3/orders/released{nextCursor} | Get released orders for next page |
| [**getOrderByPurchaseOrderId**](Version3Api.md#getOrderByPurchaseOrderId) | **GET** /v3/orders/{purchaseOrderId} | Get an order |
| [**getReleasedOrders**](Version3Api.md#getReleasedOrders) | **GET** /v3/orders/released | Get all released orders |
| [**refundOrder**](Version3Api.md#refundOrder) | **POST** /v3/orders/{purchaseOrderId}/refund | Refund order lines |
| [**shippingOrder**](Version3Api.md#shippingOrder) | **POST** /v3/orders/{purchaseOrderId}/shipping | Shipping updates |


<a id="acknowledgeOrders"></a>
# **acknowledgeOrders**
> acknowledgeOrders(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, shipNode)

Acknowledge orders

You can acknowledge an entire order, including all of its order lines. Walmart business rules require to acknowledge orders within four hour of receipt of the order, except in extenuating circumstances.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/orderProxy/order-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String purchaseOrderId = "purchaseOrderId_example"; // String | Purchase Order ID
    String contentType = "application/xml"; // String | application/xml, application/json
    String accept = "application/xml"; // String | application/xml, application/json
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    String shipNode = "shipNode_example"; // String | Ship Node
    try {
      apiInstance.acknowledgeOrders(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, shipNode);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#acknowledgeOrders");
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
| **purchaseOrderId** | **String**| Purchase Order ID | |
| **contentType** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **accept** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |
| **shipNode** | **String**| Ship Node | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="cancelOrder"></a>
# **cancelOrder**
> cancelOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, shipNode)

Cancel order lines

You can cancel one or more order lines. You must include a purchaseOrderLineNumber when cancelling an order. After cancelling your order, update the inventory for the cancelled order and send it in the next inventory feed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/orderProxy/order-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String purchaseOrderId = "purchaseOrderId_example"; // String | Purchase Order ID
    String contentType = "application/xml"; // String | application/xml, application/json
    String accept = "application/xml"; // String | application/xml, application/json
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    String requestBody = "requestBody_example"; // String | Request body
    String shipNode = "shipNode_example"; // String | Ship Node
    try {
      apiInstance.cancelOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, shipNode);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#cancelOrder");
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
| **purchaseOrderId** | **String**| Purchase Order ID | |
| **contentType** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **accept** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |
| **requestBody** | **String**| Request body | |
| **shipNode** | **String**| Ship Node | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="getAllOrders"></a>
# **getAllOrders**
> getAllOrders(contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, shipNode, sku, customerOrderId, purchaseOrderId, status, createdStartDate, createdEndDate, fromExpectedShipDate, toExpectedShipDate, limit)

Get all orders

You can display a list of all orders with the query parameter filter criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/orderProxy/order-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String contentType = "application/xml"; // String | application/xml, application/json
    String accept = "application/xml"; // String | application/xml, application/json
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    String shipNode = "shipNode_example"; // String | Ship Node
    String sku = "sku_example"; // String | Retrieves all orders with the specified SKU.
    String customerOrderId = "customerOrderId_example"; // String | Retrives the details of the specified customerOrderId.
    String purchaseOrderId = "purchaseOrderId_example"; // String | The purchase order ID associated with the order to retrieve. One customer order can have multiple purchase orders associated with it.
    String status = "status_example"; // String | The list of orders corresponding to the requested status.
    String createdStartDate = "createdStartDate_example"; // String | Limit orders to those created after this date or a timestamp.
    String createdEndDate = "createdEndDate_example"; // String | Limit orders to those created before this date or timestamp.
    String fromExpectedShipDate = "fromExpectedShipDate_example"; // String | Limit orders to those that have order lines with an expected ship date after this date.
    String toExpectedShipDate = "toExpectedShipDate_example"; // String | Limit orders to those that have order lines with an expected ship date before this date. 
    Integer limit = 10; // Integer | The number of orders to be returned. Do not set this parameter to over 200 orders.
    try {
      apiInstance.getAllOrders(contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, shipNode, sku, customerOrderId, purchaseOrderId, status, createdStartDate, createdEndDate, fromExpectedShipDate, toExpectedShipDate, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#getAllOrders");
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
| **contentType** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **accept** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |
| **shipNode** | **String**| Ship Node | [optional] |
| **sku** | **String**| Retrieves all orders with the specified SKU. | [optional] |
| **customerOrderId** | **String**| Retrives the details of the specified customerOrderId. | [optional] |
| **purchaseOrderId** | **String**| The purchase order ID associated with the order to retrieve. One customer order can have multiple purchase orders associated with it. | [optional] |
| **status** | **String**| The list of orders corresponding to the requested status. | [optional] |
| **createdStartDate** | **String**| Limit orders to those created after this date or a timestamp. | [optional] |
| **createdEndDate** | **String**| Limit orders to those created before this date or timestamp. | [optional] |
| **fromExpectedShipDate** | **String**| Limit orders to those that have order lines with an expected ship date after this date. | [optional] |
| **toExpectedShipDate** | **String**| Limit orders to those that have order lines with an expected ship date before this date.  | [optional] |
| **limit** | **Integer**| The number of orders to be returned. Do not set this parameter to over 200 orders. | [optional] [default to 10] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="getAllOrdersNext"></a>
# **getAllOrdersNext**
> getAllOrdersNext(nextCursor, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID)

Get orders for next page

You can display a list of all orders with nextCursor path parameter pagination criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/orderProxy/order-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String nextCursor = "nextCursor_example"; // String | Used for pagination when there are more than 200 orders to retrieve. The nextCursor value of the returned response includes a link to another GET call to retrieve the next page. Copy the link and paste it in the next call.
    String contentType = "application/xml"; // String | application/xml, application/json
    String accept = "application/xml"; // String | application/xml, application/json
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    try {
      apiInstance.getAllOrdersNext(nextCursor, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#getAllOrdersNext");
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
| **nextCursor** | **String**| Used for pagination when there are more than 200 orders to retrieve. The nextCursor value of the returned response includes a link to another GET call to retrieve the next page. Copy the link and paste it in the next call. | |
| **contentType** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **accept** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="getNextCursorReleasedOrders"></a>
# **getNextCursorReleasedOrders**
> getNextCursorReleasedOrders(nextCursor, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID)

Get released orders for next page

You can display all released orders that have been created and are ready for fulfilment with nextCursor path parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/orderProxy/order-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String nextCursor = "nextCursor_example"; // String | Used for pagination when there are more than 200 orders to retrieve. The nextCursor value of the returned response includes a link to another GET call to retrieve the next page. Copy the link and paste it in the next call.
    String contentType = "application/xml"; // String | application/xml, application/json
    String accept = "application/xml"; // String | application/xml, application/json
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    try {
      apiInstance.getNextCursorReleasedOrders(nextCursor, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#getNextCursorReleasedOrders");
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
| **nextCursor** | **String**| Used for pagination when there are more than 200 orders to retrieve. The nextCursor value of the returned response includes a link to another GET call to retrieve the next page. Copy the link and paste it in the next call. | |
| **contentType** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **accept** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="getOrderByPurchaseOrderId"></a>
# **getOrderByPurchaseOrderId**
> getOrderByPurchaseOrderId(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, shipNode)

Get an order

You can display details of a specific order based on the purchaseOrderId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/orderProxy/order-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String purchaseOrderId = "purchaseOrderId_example"; // String | Purchase Order ID
    String contentType = "application/xml"; // String | application/xml, application/json
    String accept = "application/xml"; // String | application/xml, application/json
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    String shipNode = "shipNode_example"; // String | Ship Node
    try {
      apiInstance.getOrderByPurchaseOrderId(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, shipNode);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#getOrderByPurchaseOrderId");
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
| **purchaseOrderId** | **String**| Purchase Order ID | |
| **contentType** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **accept** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |
| **shipNode** | **String**| Ship Node | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="getReleasedOrders"></a>
# **getReleasedOrders**
> getReleasedOrders(createdStartDate, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, shipNode, limit)

Get all released orders

You can display all released orders that have been created and are ready for fulfilment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/orderProxy/order-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String createdStartDate = "createdStartDate_example"; // String | Limit orders to those created after this date or a timestamp.
    String contentType = "application/xml"; // String | application/xml, application/json
    String accept = "application/xml"; // String | application/xml, application/json
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    String shipNode = "shipNode_example"; // String | Ship Node
    Integer limit = 56; // Integer | The number of orders to be returned. Do not set this parameter to over 200 orders.
    try {
      apiInstance.getReleasedOrders(createdStartDate, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, shipNode, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#getReleasedOrders");
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
| **createdStartDate** | **String**| Limit orders to those created after this date or a timestamp. | |
| **contentType** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **accept** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |
| **shipNode** | **String**| Ship Node | [optional] |
| **limit** | **Integer**| The number of orders to be returned. Do not set this parameter to over 200 orders. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="refundOrder"></a>
# **refundOrder**
> refundOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, shipNode)

Refund order lines

You can refund one or more order lines that have been shipped. The response to a successful call contains the order with the refunded line item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/orderProxy/order-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String purchaseOrderId = "purchaseOrderId_example"; // String | Purchase Order ID
    String contentType = "application/xml"; // String | application/xml, application/json
    String accept = "application/xml"; // String | application/xml, application/json
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    String requestBody = "requestBody_example"; // String | Request body
    String shipNode = "shipNode_example"; // String | Ship Node
    try {
      apiInstance.refundOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, shipNode);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#refundOrder");
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
| **purchaseOrderId** | **String**| Purchase Order ID | |
| **contentType** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **accept** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |
| **requestBody** | **String**| Request body | |
| **shipNode** | **String**| Ship Node | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

<a id="shippingOrder"></a>
# **shippingOrder**
> shippingOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, shipNode)

Shipping updates

You can change the status of order lines to \&quot;Shipped\&quot; and trigger the charge to a customer. You must acknowledge your orders before sending a shipping update to avoid underselling. An order line, once marked as shipped, cannot be updated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Version3Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.walmart.com/orderProxy/order-api-doc-app/rest");

    Version3Api apiInstance = new Version3Api(defaultClient);
    String purchaseOrderId = "purchaseOrderId_example"; // String | Purchase Order ID
    String contentType = "application/xml"; // String | application/xml, application/json
    String accept = "application/xml"; // String | application/xml, application/json
    String WM_CONSUMER_CHANNEL_TYPE = "SWAGGER_CHANNEL_TYPE"; // String | Channel Type
    String WM_CONSUMER_ID = "WM_CONSUMER_ID_example"; // String | Your Consumer ID
    String WM_SEC_TIMESTAMP = "Auto populated"; // String | Epoch timestamp
    String WM_SEC_AUTH_SIGNATURE = "Auto populated"; // String | Authentication signature
    String WM_SVC_NAME = "Walmart Marketplace"; // String | The Service name
    String WM_QOS_CORRELATION_ID = "123456abcdef"; // String | A Transaction ID
    String requestBody = "requestBody_example"; // String | Request body
    String shipNode = "shipNode_example"; // String | Ship Node
    try {
      apiInstance.shippingOrder(purchaseOrderId, contentType, accept, WM_CONSUMER_CHANNEL_TYPE, WM_CONSUMER_ID, WM_SEC_TIMESTAMP, WM_SEC_AUTH_SIGNATURE, WM_SVC_NAME, WM_QOS_CORRELATION_ID, requestBody, shipNode);
    } catch (ApiException e) {
      System.err.println("Exception when calling Version3Api#shippingOrder");
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
| **purchaseOrderId** | **String**| Purchase Order ID | |
| **contentType** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **accept** | **String**| application/xml, application/json | [default to application/xml] [enum: application/xml, application/json] |
| **WM_CONSUMER_CHANNEL_TYPE** | **String**| Channel Type | [default to SWAGGER_CHANNEL_TYPE] [enum: SWAGGER_CHANNEL_TYPE] |
| **WM_CONSUMER_ID** | **String**| Your Consumer ID | |
| **WM_SEC_TIMESTAMP** | **String**| Epoch timestamp | [default to Auto populated] |
| **WM_SEC_AUTH_SIGNATURE** | **String**| Authentication signature | [default to Auto populated] |
| **WM_SVC_NAME** | **String**| The Service name | [default to Walmart Marketplace] |
| **WM_QOS_CORRELATION_ID** | **String**| A Transaction ID | [default to 123456abcdef] |
| **requestBody** | **String**| Request body | |
| **shipNode** | **String**| Ship Node | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | successful operation |  -  |

