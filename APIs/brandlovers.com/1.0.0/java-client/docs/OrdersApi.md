# OrdersApi

All URIs are relative to *https://api.brandlovers.com/marketplace/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ordersGet**](OrdersApi.md#ordersGet) | **GET** /orders | Returns orders details |
| [**ordersShipmentsDeliveredGet**](OrdersApi.md#ordersShipmentsDeliveredGet) | **GET** /orders/shipments/delivered | Returns list of shipments |
| [**ordersShipmentsDeliveredPost**](OrdersApi.md#ordersShipmentsDeliveredPost) | **POST** /orders/shipments/delivered | Bulk update of order shipments |
| [**ordersShipmentsShippedGet**](OrdersApi.md#ordersShipmentsShippedGet) | **GET** /orders/shipments/shipped | Returns a list of shipments shipped |
| [**ordersShipmentsShippedPost**](OrdersApi.md#ordersShipmentsShippedPost) | **POST** /orders/shipments/shipped | Bulk update of order shipments |
| [**ordersStatusApprovedGet**](OrdersApi.md#ordersStatusApprovedGet) | **GET** /orders/status/approved | Return list of approved orders |
| [**ordersStatusCanceledGet**](OrdersApi.md#ordersStatusCanceledGet) | **GET** /orders/status/canceled | Returns lists of canceled orders |
| [**ordersStatusDeliveredGet**](OrdersApi.md#ordersStatusDeliveredGet) | **GET** /orders/status/delivered | Returns a list of orders successfully delivered associated with this seller. |
| [**ordersStatusNewGet**](OrdersApi.md#ordersStatusNewGet) | **GET** /orders/status/new | Returns a list of orders flagged as new. |
| [**ordersStatusPartiallyDeliveredGet**](OrdersApi.md#ordersStatusPartiallyDeliveredGet) | **GET** /orders/status/partiallyDelivered | Returns a list of partially deliverd orders |
| [**ordersStatusPartiallySentGet**](OrdersApi.md#ordersStatusPartiallySentGet) | **GET** /orders/status/partiallySent | Returns a list of orders partially fullfiled |
| [**ordersStatusSentGet**](OrdersApi.md#ordersStatusSentGet) | **GET** /orders/status/sent | Returns a list with orders fully sent |


<a id="ordersGet"></a>
# **ordersGet**
> GetOrders ordersGet(authorization, offset, limit)

Returns orders details

Retuns a list of orders associated with this seller. The list is ordered by dateCreated.

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
    try {
      GetOrders result = apiInstance.ordersGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersGet");
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
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetOrders**](GetOrders.md)

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

<a id="ordersShipmentsDeliveredGet"></a>
# **ordersShipmentsDeliveredGet**
> GetOrdersShipments ordersShipmentsDeliveredGet(authorization, status, offset, limit)

Returns list of shipments

Returns list of shipments. By default this will return list of the last shipments ordered by dateCreated, folowed by last update date.

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String status = "status_example"; // String | Query by shippment status.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
    try {
      GetOrdersShipments result = apiInstance.ordersShipmentsDeliveredGet(authorization, status, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersShipmentsDeliveredGet");
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
| **status** | **String**| Query by shippment status. | [optional] |
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetOrdersShipments**](GetOrdersShipments.md)

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

<a id="ordersShipmentsDeliveredPost"></a>
# **ordersShipmentsDeliveredPost**
> ordersShipmentsDeliveredPost(authorization, ordersshipments)

Bulk update of order shipments

Bulk update of order shipments status. This alows to inform multiple shipments status

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    OrdersShipments ordersshipments = new OrdersShipments(); // OrdersShipments | JSON body with list of shipments to be updated.
    try {
      apiInstance.ordersShipmentsDeliveredPost(authorization, ordersshipments);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersShipmentsDeliveredPost");
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
| **ordersshipments** | [**OrdersShipments**](OrdersShipments.md)| JSON body with list of shipments to be updated. | |

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
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **403** | Server refused to process your request. Please check the API SLA and reduce number of requests per second. |  -  |

<a id="ordersShipmentsShippedGet"></a>
# **ordersShipmentsShippedGet**
> GetOrdersShipments ordersShipmentsShippedGet(authorization, status, offset, limit)

Returns a list of shipments shipped

Returns a list of shipments shipped. By Default returns items ordered by dateCreated folowed by last update

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    String status = "NEW"; // String | Product status.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
    try {
      GetOrdersShipments result = apiInstance.ordersShipmentsShippedGet(authorization, status, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersShipmentsShippedGet");
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
| **status** | **String**| Product status. | [optional] [enum: NEW, APPROVED, DECLINED, PENDING] |
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetOrdersShipments**](GetOrdersShipments.md)

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

<a id="ordersShipmentsShippedPost"></a>
# **ordersShipmentsShippedPost**
> ordersShipmentsShippedPost(ordersshipments)

Bulk update of order shipments

Allows bulk updates of orders shippments.

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    OrdersShipments ordersshipments = new OrdersShipments(); // OrdersShipments | JSON payload with list of shippments of orders.
    try {
      apiInstance.ordersShipmentsShippedPost(ordersshipments);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersShipmentsShippedPost");
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
| **ordersshipments** | [**OrdersShipments**](OrdersShipments.md)| JSON payload with list of shippments of orders. | |

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
| **200** | Success! |  -  |
| **400** | Bad request. |  -  |
| **401** | Access denied. You&#39;re not authenticated or token expired. Check your request header the &#x60;authorization&#x60; field is required. |  -  |
| **403** | Server refused to process your request. Please check the API SLA and reduce number of requests per second. |  -  |

<a id="ordersStatusApprovedGet"></a>
# **ordersStatusApprovedGet**
> GetOrders ordersStatusApprovedGet(authorization, offset, limit)

Return list of approved orders

Returns a list of approved orders. Orders in the &#x60;approved&#x60; state must be fullfiled imediadetelly.

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number or items to return when executing query. Defaults to 100, max 200. Use this in conjuction with `offset` to paginate across the results.
    try {
      GetOrders result = apiInstance.ordersStatusApprovedGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersStatusApprovedGet");
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
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 100, max 200. Use this in conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetOrders**](GetOrders.md)

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

<a id="ordersStatusCanceledGet"></a>
# **ordersStatusCanceledGet**
> GetOrders ordersStatusCanceledGet(authorization, offset, limit)

Returns lists of canceled orders

Returns a list with canceled orders. Canceled orders should not be fullfiled.

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 100; // Integer | Number or items to return when executing query. Default 100, max 250. Use this conjuction with `offset` to paginate across the results.
    try {
      GetOrders result = apiInstance.ordersStatusCanceledGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersStatusCanceledGet");
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
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Default 100, max 250. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] [default to 100] |

### Return type

[**GetOrders**](GetOrders.md)

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

<a id="ordersStatusDeliveredGet"></a>
# **ordersStatusDeliveredGet**
> GetOrders ordersStatusDeliveredGet(authorization, offset, limit)

Returns a list of orders successfully delivered associated with this seller.

Returns a list of orders successfully delivered associated with this seller.

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
    try {
      GetOrders result = apiInstance.ordersStatusDeliveredGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersStatusDeliveredGet");
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
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetOrders**](GetOrders.md)

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

<a id="ordersStatusNewGet"></a>
# **ordersStatusNewGet**
> GetOrders ordersStatusNewGet(authorization, offset, limit)

Returns a list of orders flagged as new.

Returns a list of orders flagged as new. New orders should not be fullfiled until marketplace flags them as approved.

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 100; // Integer | Number or items to return when executing query. Defaults to 100. Max 250. Use this conjuction with `offset` to paginate across the results.
    try {
      GetOrders result = apiInstance.ordersStatusNewGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersStatusNewGet");
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
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 100. Max 250. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] [default to 100] |

### Return type

[**GetOrders**](GetOrders.md)

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

<a id="ordersStatusPartiallyDeliveredGet"></a>
# **ordersStatusPartiallyDeliveredGet**
> GetOrders ordersStatusPartiallyDeliveredGet(authorization, offset, limit)

Returns a list of partially deliverd orders

Returns a list of partially deliverd orders. This is a list of orders with items shipped but with not all items ackwlodged as deliverd

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 100; // Integer | Number or items to return when executing query. Defaults to 100. Max 250. Use this conjuction with `offset` to paginate across the results.
    try {
      GetOrders result = apiInstance.ordersStatusPartiallyDeliveredGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersStatusPartiallyDeliveredGet");
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
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 100. Max 250. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] [default to 100] |

### Return type

[**GetOrders**](GetOrders.md)

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

<a id="ordersStatusPartiallySentGet"></a>
# **ordersStatusPartiallySentGet**
> GetOrders ordersStatusPartiallySentGet(authorization, offset, limit)

Returns a list of orders partially fullfiled

Returns a list of orders that contain one (or more) items that where not shipped. This will list the entire order as well the items with peding shipment. Use this service to track orders that need to be fullfiled.

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number or items to return when executing query. Defaults to 100. Use this conjuction with `offset` to paginate across the results.
    try {
      GetOrders result = apiInstance.ordersStatusPartiallySentGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersStatusPartiallySentGet");
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
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 100. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetOrders**](GetOrders.md)

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

<a id="ordersStatusSentGet"></a>
# **ordersStatusSentGet**
> GetOrders ordersStatusSentGet(authorization, offset, limit)

Returns a list with orders fully sent

Returns a list with orders completely fullfiled, this means orders with all items sent. Orders will ordered by dateCreated fowllowed by last update

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
    defaultClient.setBasePath("https://api.brandlovers.com/marketplace/v1");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
    Integer offset = 56; // Integer | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
    Integer limit = 56; // Integer | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
    try {
      GetOrders result = apiInstance.ordersStatusSentGet(authorization, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersStatusSentGet");
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
| **offset** | **Integer**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] |
| **limit** | **Integer**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] |

### Return type

[**GetOrders**](GetOrders.md)

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

