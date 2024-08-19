# OrdersApi

All URIs are relative to *https://api.fulfillment.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteOrdersId**](OrdersApi.md#deleteOrdersId) | **DELETE** /orders/{id} | Cancel an Order |
| [**getOrder**](OrdersApi.md#getOrder) | **GET** /orders/{id} | Order Details |
| [**getOrders**](OrdersApi.md#getOrders) | **GET** /orders | List of Orders |
| [**postOrders**](OrdersApi.md#postOrders) | **POST** /orders | New Order |


<a id="deleteOrdersId"></a>
# **deleteOrdersId**
> Object deleteOrdersId(id)

Cancel an Order

Request an order is canceled to prevent shipment.

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
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Integer id = 56; // Integer | ID of order that needs to be canceled
    try {
      Object result = apiInstance.deleteOrdersId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#deleteOrdersId");
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
| **id** | **Integer**| ID of order that needs to be canceled | |

### Return type

**Object**

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your order was successfully canceled |  -  |
| **404** | Order not found |  -  |
| **405** | Could not cancel your order, perhaps it already shipped |  -  |

<a id="getOrder"></a>
# **getOrder**
> Object getOrder(id, merchantId, hydrate)

Order Details

For the fastest results use the FDC provided &#x60;id&#x60; however you can use your &#x60;merchantOrderId&#x60; as the &#x60;id&#x60;.

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
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String id = "id_example"; // String | The FDC order Id
    Integer merchantId = 56; // Integer | Providing your `merchantId` indicates the `id` is your `merchantOrderId`. Although it is not necessary to provide this it will speed up your results when using your `merchantOrderId` however it will slow your results when using the FDC provided `id`
    List<String> hydrate = Arrays.asList(); // List<String> | Adds additional information to the response, uses a CSV format for multiple values.'
    try {
      Object result = apiInstance.getOrder(id, merchantId, hydrate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getOrder");
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
| **id** | **String**| The FDC order Id | |
| **merchantId** | **Integer**| Providing your &#x60;merchantId&#x60; indicates the &#x60;id&#x60; is your &#x60;merchantOrderId&#x60;. Although it is not necessary to provide this it will speed up your results when using your &#x60;merchantOrderId&#x60; however it will slow your results when using the FDC provided &#x60;id&#x60; | [optional] |
| **hydrate** | [**List&lt;String&gt;**](String.md)| Adds additional information to the response, uses a CSV format for multiple values.&#39; | [optional] [enum: integrator, lineItems, trackingNumbers.carrier] |

### Return type

**Object**

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order Found |  -  |
| **404** | Order not found |  -  |

<a id="getOrders"></a>
# **getOrders**
> OrderResponseOneOfV2 getOrders(fromDate, toDate, merchantIds, warehouseIds, page, limit, hydrate)

List of Orders

Retrieve many orders at once

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
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String fromDate = "fromDate_example"; // String | Date-time in ISO 8601 format for selecting orders after, or at, the specified time
    String toDate = "toDate_example"; // String | Date-time in ISO 8601 format for selecting orders before, or at, the specified time
    List<Integer> merchantIds = Arrays.asList(); // List<Integer> | A CSV of merchant id, '123' or '1,2,3'
    List<Integer> warehouseIds = Arrays.asList(); // List<Integer> | A CSV of warehouse id, '123' or '1,2,3'
    Integer page = 1; // Integer | A multiplier of the number of items (limit parameter) to skip before returning results
    Integer limit = 80; // Integer | The numbers of items to return
    List<String> hydrate = Arrays.asList(); // List<String> | Adds additional information to the response, uses a CSV format for multiple values.'
    try {
      OrderResponseOneOfV2 result = apiInstance.getOrders(fromDate, toDate, merchantIds, warehouseIds, page, limit, hydrate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getOrders");
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
| **fromDate** | **String**| Date-time in ISO 8601 format for selecting orders after, or at, the specified time | |
| **toDate** | **String**| Date-time in ISO 8601 format for selecting orders before, or at, the specified time | |
| **merchantIds** | [**List&lt;Integer&gt;**](Integer.md)| A CSV of merchant id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] |
| **warehouseIds** | [**List&lt;Integer&gt;**](Integer.md)| A CSV of warehouse id, &#39;123&#39; or &#39;1,2,3&#39; | [optional] |
| **page** | **Integer**| A multiplier of the number of items (limit parameter) to skip before returning results | [optional] [default to 1] |
| **limit** | **Integer**| The numbers of items to return | [optional] [default to 80] |
| **hydrate** | [**List&lt;String&gt;**](String.md)| Adds additional information to the response, uses a CSV format for multiple values.&#39; | [optional] [enum: integrator, lineItems, trackingNumbers.carrier] |

### Return type

[**OrderResponseOneOfV2**](OrderResponseOneOfV2.md)

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | No Orders Found |  -  |

<a id="postOrders"></a>
# **postOrders**
> OrderResponseV2 postOrders(body)

New Order

Error Notes&amp;#58; * When &#x60;409 Conflict&#x60; is a &#39;Duplicate Order&#39; the &#x60;context&#x60; will include the FDC &#x60;id&#x60;, see samples. 

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
    defaultClient.setBasePath("https://api.fulfillment.com/v2");
    
    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: fdcAuth
    OAuth fdcAuth = (OAuth) defaultClient.getAuthentication("fdcAuth");
    fdcAuth.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    OrderRequestV2 body = new OrderRequestV2(); // OrderRequestV2 | The order to create
    try {
      OrderResponseV2 result = apiInstance.postOrders(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#postOrders");
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
| **body** | [**OrderRequestV2**](OrderRequestV2.md)| The order to create | |

### Return type

[**OrderResponseV2**](OrderResponseV2.md)

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Order Created |  -  |
| **400** | Invalid order object |  -  |
| **401** | You do not have permission to create orders |  -  |
| **403** | Forbidden |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Failure |  -  |

