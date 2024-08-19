# OrdersApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrder**](OrdersApi.md#createOrder) | **POST** /orders | Create an order in the eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Order&#39; model are those required to create a new order.The paymentStatus can only be AWAITING_PAYMENT or INCOMPLETE.The fulfillmentStatus can only be AWAITING_PROCESSING |
| [**deleteOrderById**](OrdersApi.md#deleteOrderById) | **DELETE** /orders/{id} | Delete an order associated with a given ID from your eCommerce system. Specifying an order associated with a given ID that does not exist will result in an error message |
| [**getOrderById**](OrdersApi.md#getOrderById) | **GET** /orders/{id} | Retrieve an order associated with a given ID from the eCommerce system. Specifying an order with an ID that does not exist will result in an error response |
| [**getOrders**](OrdersApi.md#getOrders) | **GET** /orders | Find orders in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved |
| [**getOrdersPayments**](OrdersApi.md#getOrdersPayments) | **GET** /orders/{orderId}/payments | Retrieve the payments in the eCommerce system for the specified order |
| [**getOrdersRefunds**](OrdersApi.md#getOrdersRefunds) | **GET** /orders/{orderId}/refunds | Retrieve the refunds in the eCommerce system for the specified order |
| [**updateOrderById**](OrdersApi.md#updateOrderById) | **PATCH** /orders/{id} | Update an order associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the order object will be updated, and those fields not provided will be left alone. Updating an order with a specified ID that does not exist will result in an error response&lt;/strong&gt; |


<a id="createOrder"></a>
# **createOrder**
> Order createOrder(authorization, order)

Create an order in the eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Order&#39; model are those required to create a new order.The paymentStatus can only be AWAITING_PAYMENT or INCOMPLETE.The fulfillmentStatus can only be AWAITING_PROCESSING

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    OrderPost order = new OrderPost(); // OrderPost | The order object to be created
    try {
      Order result = apiInstance.createOrder(authorization, order);
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **order** | [**OrderPost**](OrderPost.md)| The order object to be created | |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="deleteOrderById"></a>
# **deleteOrderById**
> deleteOrderById(authorization, id)

Delete an order associated with a given ID from your eCommerce system. Specifying an order associated with a given ID that does not exist will result in an error message

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the order to delete from the eCommerce system
    try {
      apiInstance.deleteOrderById(authorization, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#deleteOrderById");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the order to delete from the eCommerce system | |

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
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getOrderById"></a>
# **getOrderById**
> Order getOrderById(authorization, id)

Retrieve an order associated with a given ID from the eCommerce system. Specifying an order with an ID that does not exist will result in an error response

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the order to retrieve from the eCommerce system
    try {
      Order result = apiInstance.getOrderById(authorization, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getOrderById");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the order to retrieve from the eCommerce system | |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getOrders"></a>
# **getOrders**
> List&lt;Order&gt; getOrders(authorization, where, pageSize, nextPage, fields)

Find orders in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String where = "where_example"; // String | The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field='value'). <p>Supported search terms: date, from_date, to_date, from_update_date, to_update_date, order, from_order, to_order, customer_id, customer_email and statuses. All other search criteria are ignored
    Long pageSize = 56L; // Long | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    String nextPage = "nextPage_example"; // String | The next page cursor, taken from the response header: `elements-next-page-token`
    String fields = "fields_example"; // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
    try {
      List<Order> result = apiInstance.getOrders(authorization, where, pageSize, nextPage, fields);
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **where** | **String**| The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field&#x3D;&#39;value&#39;). &lt;p&gt;Supported search terms: date, from_date, to_date, from_update_date, to_update_date, order, from_order, to_order, customer_id, customer_email and statuses. All other search criteria are ignored | [optional] |
| **pageSize** | **Long**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] |
| **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] |
| **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] |

### Return type

[**List&lt;Order&gt;**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getOrdersPayments"></a>
# **getOrdersPayments**
> List&lt;Payment&gt; getOrdersPayments(authorization, orderId, pageSize, nextPage, fields)

Retrieve the payments in the eCommerce system for the specified order

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String orderId = "orderId_example"; // String | The ID of the order to retrieve payments from in the eCommerce system
    Long pageSize = 56L; // Long | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    String nextPage = "nextPage_example"; // String | The next page cursor, taken from the response header: `elements-next-page-token`
    String fields = "fields_example"; // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
    try {
      List<Payment> result = apiInstance.getOrdersPayments(authorization, orderId, pageSize, nextPage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getOrdersPayments");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **orderId** | **String**| The ID of the order to retrieve payments from in the eCommerce system | |
| **pageSize** | **Long**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] |
| **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] |
| **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] |

### Return type

[**List&lt;Payment&gt;**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="getOrdersRefunds"></a>
# **getOrdersRefunds**
> List&lt;Payment&gt; getOrdersRefunds(authorization, orderId, pageSize, nextPage, fields)

Retrieve the refunds in the eCommerce system for the specified order

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String orderId = "orderId_example"; // String | The ID of the order to retrieve refunds from in the eCommerce system
    Long pageSize = 56L; // Long | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
    String nextPage = "nextPage_example"; // String | The next page cursor, taken from the response header: `elements-next-page-token`
    String fields = "fields_example"; // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
    try {
      List<Payment> result = apiInstance.getOrdersRefunds(authorization, orderId, pageSize, nextPage, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#getOrdersRefunds");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **orderId** | **String**| The ID of the order to retrieve refunds from in the eCommerce system | |
| **pageSize** | **Long**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] |
| **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] |
| **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] |

### Return type

[**List&lt;Payment&gt;**](Payment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

<a id="updateOrderById"></a>
# **updateOrderById**
> Order updateOrderById(authorization, id, order, action)

Update an order associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the order object will be updated, and those fields not provided will be left alone. Updating an order with a specified ID that does not exist will result in an error response&lt;/strong&gt;

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
    defaultClient.setBasePath("https://api.cloud-elements.com/elements/api-v2");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
    String id = "id_example"; // String | The ID of the order to update in the eCommerce system
    OrderPatch order = new OrderPatch(); // OrderPatch | The order object, with those fields that are to be updated
    String action = "action_example"; // String | An action to perform on the order: cancel, reopen or close. If left blank then the order is updated but no action is taken
    try {
      Order result = apiInstance.updateOrderById(authorization, id, order, action);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#updateOrderById");
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
| **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | |
| **id** | **String**| The ID of the order to update in the eCommerce system | |
| **order** | [**OrderPatch**](OrderPatch.md)| The order object, with those fields that are to be updated | |
| **action** | **String**| An action to perform on the order: cancel, reopen or close. If left blank then the order is updated but no action is taken | [optional] |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Everything worked as expected |  -  |
| **400** | Bad Request - Often due to a missing request parameter |  -  |
| **401** | Unauthorized - An invalid element token, user secret and/or org secret provided |  -  |
| **403** | Forbidden - Access to the resource by the provider is forbidden |  -  |
| **404** | Not found - The requested resource is not found |  -  |
| **405** | Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected |  -  |
| **406** | Not acceptable - The response content type does not match the &#39;Accept&#39; header value |  -  |
| **409** | Conflict - If a resource being created already exists |  -  |
| **415** | Unsupported media type - The server cannot handle the requested Content-Type |  -  |
| **500** | Server error - Something went wrong on the Cloud Elements server |  -  |
| **502** | Provider server error - Something went wrong on the Provider or Endpoint&#39;s server |  -  |

