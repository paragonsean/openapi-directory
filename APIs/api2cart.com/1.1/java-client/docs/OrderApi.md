# OrderApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**orderAbandonedList**](OrderApi.md#orderAbandonedList) | **GET** /order.abandoned.list.json |  |
| [**orderAdd**](OrderApi.md#orderAdd) | **POST** /order.add.json |  |
| [**orderCount**](OrderApi.md#orderCount) | **GET** /order.count.json |  |
| [**orderFinancialStatusList**](OrderApi.md#orderFinancialStatusList) | **GET** /order.financial_status.list.json |  |
| [**orderFind**](OrderApi.md#orderFind) | **GET** /order.find.json |  |
| [**orderFulfillmentStatusList**](OrderApi.md#orderFulfillmentStatusList) | **GET** /order.fulfillment_status.list.json |  |
| [**orderInfo**](OrderApi.md#orderInfo) | **GET** /order.info.json |  |
| [**orderList**](OrderApi.md#orderList) | **GET** /order.list.json |  |
| [**orderPreestimateShippingList**](OrderApi.md#orderPreestimateShippingList) | **POST** /order.preestimate_shipping.list.json |  |
| [**orderRefundAdd**](OrderApi.md#orderRefundAdd) | **POST** /order.refund.add.json |  |
| [**orderShipmentAdd**](OrderApi.md#orderShipmentAdd) | **POST** /order.shipment.add.json |  |
| [**orderShipmentDelete**](OrderApi.md#orderShipmentDelete) | **DELETE** /order.shipment.delete.json |  |
| [**orderShipmentInfo**](OrderApi.md#orderShipmentInfo) | **GET** /order.shipment.info.json |  |
| [**orderShipmentList**](OrderApi.md#orderShipmentList) | **GET** /order.shipment.list.json |  |
| [**orderShipmentTrackingAdd**](OrderApi.md#orderShipmentTrackingAdd) | **POST** /order.shipment.tracking.add.json |  |
| [**orderShipmentUpdate**](OrderApi.md#orderShipmentUpdate) | **PUT** /order.shipment.update.json |  |
| [**orderStatusList**](OrderApi.md#orderStatusList) | **GET** /order.status.list.json |  |
| [**orderTransactionList**](OrderApi.md#orderTransactionList) | **GET** /order.transaction.list.json |  |
| [**orderUpdate**](OrderApi.md#orderUpdate) | **PUT** /order.update.json |  |


<a id="orderAbandonedList"></a>
# **orderAbandonedList**
> ModelResponseOrderAbandonedList orderAbandonedList(customerId, customerEmail, createdTo, createdFrom, modifiedTo, modifiedFrom, skipEmptyEmail, storeId, pageCursor, count, start, params, responseFields, exclude)



Get list of orders that were left by customers before completing the order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String customerId = "customerId_example"; // String | Retrieves orders specified by customer id
    String customerEmail = "customerEmail_example"; // String | Retrieves orders specified by customer email
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    Boolean skipEmptyEmail = false; // Boolean | Filter empty emails
    String storeId = "storeId_example"; // String | Store Id
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    String params = "customer,totals,items"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    try {
      ModelResponseOrderAbandonedList result = apiInstance.orderAbandonedList(customerId, customerEmail, createdTo, createdFrom, modifiedTo, modifiedFrom, skipEmptyEmail, storeId, pageCursor, count, start, params, responseFields, exclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderAbandonedList");
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
| **customerId** | **String**| Retrieves orders specified by customer id | [optional] |
| **customerEmail** | **String**| Retrieves orders specified by customer email | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **skipEmptyEmail** | **Boolean**| Filter empty emails | [optional] [default to false] |
| **storeId** | **String**| Store Id | [optional] |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to customer,totals,items] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |

### Return type

[**ModelResponseOrderAbandonedList**](ModelResponseOrderAbandonedList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderAdd"></a>
# **orderAdd**
> OrderAdd200Response orderAdd(orderAdd)



Add a new order to the cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    OrderAdd orderAdd = new OrderAdd(); // OrderAdd | 
    try {
      OrderAdd200Response result = apiInstance.orderAdd(orderAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderAdd");
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
| **orderAdd** | [**OrderAdd**](OrderAdd.md)|  | |

### Return type

[**OrderAdd200Response**](OrderAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderCount"></a>
# **orderCount**
> OrderCount200Response orderCount(customerId, customerEmail, orderStatus, orderStatusIds, createdTo, createdFrom, modifiedTo, modifiedFrom, storeId, ids, orderIds, ebayOrderStatus, financialStatus, fulfillmentStatus, shippingMethod, deliveryMethod, shipNodeType)



Count orders in store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String customerId = "customerId_example"; // String | Counts orders quantity specified by customer id
    String customerEmail = "customerEmail_example"; // String | Counts orders quantity specified by customer email
    String orderStatus = "orderStatus_example"; // String | Counts orders quantity specified by order status
    List<String> orderStatusIds = Arrays.asList(); // List<String> | Retrieves orders specified by order statuses
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String storeId = "storeId_example"; // String | Counts orders quantity specified by store id
    String ids = "ids_example"; // String | Counts orders specified by ids
    String orderIds = "orderIds_example"; // String | Counts orders specified by order ids
    String ebayOrderStatus = "ebayOrderStatus_example"; // String | Counts orders quantity specified by order status
    String financialStatus = "financialStatus_example"; // String | Counts orders quantity specified by financial status
    String fulfillmentStatus = "fulfillmentStatus_example"; // String | Create order with fulfillment status
    String shippingMethod = "shippingMethod_example"; // String | Retrieve entities according to shipping method
    String deliveryMethod = "deliveryMethod_example"; // String | Retrieves order with delivery method
    String shipNodeType = "shipNodeType_example"; // String | Retrieves order with ship node type
    try {
      OrderCount200Response result = apiInstance.orderCount(customerId, customerEmail, orderStatus, orderStatusIds, createdTo, createdFrom, modifiedTo, modifiedFrom, storeId, ids, orderIds, ebayOrderStatus, financialStatus, fulfillmentStatus, shippingMethod, deliveryMethod, shipNodeType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderCount");
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
| **customerId** | **String**| Counts orders quantity specified by customer id | [optional] |
| **customerEmail** | **String**| Counts orders quantity specified by customer email | [optional] |
| **orderStatus** | **String**| Counts orders quantity specified by order status | [optional] |
| **orderStatusIds** | [**List&lt;String&gt;**](String.md)| Retrieves orders specified by order statuses | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **storeId** | **String**| Counts orders quantity specified by store id | [optional] |
| **ids** | **String**| Counts orders specified by ids | [optional] |
| **orderIds** | **String**| Counts orders specified by order ids | [optional] |
| **ebayOrderStatus** | **String**| Counts orders quantity specified by order status | [optional] |
| **financialStatus** | **String**| Counts orders quantity specified by financial status | [optional] |
| **fulfillmentStatus** | **String**| Create order with fulfillment status | [optional] |
| **shippingMethod** | **String**| Retrieve entities according to shipping method | [optional] |
| **deliveryMethod** | **String**| Retrieves order with delivery method | [optional] |
| **shipNodeType** | **String**| Retrieves order with ship node type | [optional] |

### Return type

[**OrderCount200Response**](OrderCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderFinancialStatusList"></a>
# **orderFinancialStatusList**
> OrderFinancialStatusList200Response orderFinancialStatusList()



Retrieve list of financial statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    try {
      OrderFinancialStatusList200Response result = apiInstance.orderFinancialStatusList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderFinancialStatusList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrderFinancialStatusList200Response**](OrderFinancialStatusList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderFind"></a>
# **orderFind**
> OrderFind200Response orderFind(customerId, customerEmail, orderStatus, start, count, params, exclude, createdTo, createdFrom, modifiedTo, modifiedFrom, financialStatus)



This method is deprecated and won&#39;t be supported in the future. Please use \&quot;order.list\&quot; instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String customerId = "customerId_example"; // String | Retrieves orders specified by customer id
    String customerEmail = "customerEmail_example"; // String | Retrieves orders specified by customer email
    String orderStatus = "orderStatus_example"; // String | Retrieves orders specified by order status
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String params = "order_id,customer,totals,address,items,bundles,status"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String financialStatus = "financialStatus_example"; // String | Retrieves orders specified by financial status
    try {
      OrderFind200Response result = apiInstance.orderFind(customerId, customerEmail, orderStatus, start, count, params, exclude, createdTo, createdFrom, modifiedTo, modifiedFrom, financialStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderFind");
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
| **customerId** | **String**| Retrieves orders specified by customer id | [optional] |
| **customerEmail** | **String**| Retrieves orders specified by customer email | [optional] |
| **orderStatus** | **String**| Retrieves orders specified by order status | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to order_id,customer,totals,address,items,bundles,status] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **financialStatus** | **String**| Retrieves orders specified by financial status | [optional] |

### Return type

[**OrderFind200Response**](OrderFind200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderFulfillmentStatusList"></a>
# **orderFulfillmentStatusList**
> OrderFulfillmentStatusList200Response orderFulfillmentStatusList()



Retrieve list of fulfillment statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    try {
      OrderFulfillmentStatusList200Response result = apiInstance.orderFulfillmentStatusList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderFulfillmentStatusList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrderFulfillmentStatusList200Response**](OrderFulfillmentStatusList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderInfo"></a>
# **orderInfo**
> OrderInfo200Response orderInfo(orderId, id, params, responseFields, exclude, storeId, enableCache)



Info about a specific order by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String orderId = "orderId_example"; // String | Retrieves order’s info specified by order id
    String id = "id_example"; // String | Retrieves order info specified by id
    String params = "order_id,customer,totals,address,items,bundles,status"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String storeId = "storeId_example"; // String | Defines store id where the order should be found
    Boolean enableCache = false; // Boolean | If the value is 'true' and order exist in our cache, we will return order.info response from cache
    try {
      OrderInfo200Response result = apiInstance.orderInfo(orderId, id, params, responseFields, exclude, storeId, enableCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderInfo");
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
| **orderId** | **String**| Retrieves order’s info specified by order id | [optional] |
| **id** | **String**| Retrieves order info specified by id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to order_id,customer,totals,address,items,bundles,status] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **storeId** | **String**| Defines store id where the order should be found | [optional] |
| **enableCache** | **Boolean**| If the value is &#39;true&#39; and order exist in our cache, we will return order.info response from cache | [optional] [default to false] |

### Return type

[**OrderInfo200Response**](OrderInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderList"></a>
# **orderList**
> ModelResponseOrderList orderList(customerId, customerEmail, phone, orderStatus, orderStatusIds, start, count, pageCursor, sortBy, sortDirection, params, responseFields, exclude, createdTo, createdFrom, modifiedTo, modifiedFrom, storeId, ids, orderIds, ebayOrderStatus, basketId, financialStatus, fulfillmentStatus, shippingMethod, skipOrderIds, sinceId, isDeleted, shippingCountryIso3, enableCache, deliveryMethod, shipNodeType, currencyId)



Get list of orders from store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String customerId = "customerId_example"; // String | Retrieves orders specified by customer id
    String customerEmail = "customerEmail_example"; // String | Retrieves orders specified by customer email
    String phone = "phone_example"; // String | Filter orders by customer's phone number
    String orderStatus = "orderStatus_example"; // String | Retrieves orders specified by order status
    List<String> orderStatusIds = Arrays.asList(); // List<String> | Retrieves orders specified by order statuses
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String pageCursor = "pageCursor_example"; // String | Used to retrieve orders via cursor-based pagination (it can't be used with any other filtering parameter)
    String sortBy = "order_id"; // String | Set field to sort by
    String sortDirection = "asc"; // String | Set sorting direction
    String params = "order_id,customer,totals,address,items,bundles,status"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String storeId = "storeId_example"; // String | Store Id
    String ids = "ids_example"; // String | Retrieves orders specified by ids
    String orderIds = "orderIds_example"; // String | Retrieves orders specified by order ids
    String ebayOrderStatus = "ebayOrderStatus_example"; // String | Retrieves orders specified by order status
    String basketId = "basketId_example"; // String | Retrieves order’s info specified by basket id.
    String financialStatus = "financialStatus_example"; // String | Retrieves orders specified by financial status
    String fulfillmentStatus = "fulfillmentStatus_example"; // String | Create order with fulfillment status
    String shippingMethod = "shippingMethod_example"; // String | Retrieve entities according to shipping method
    String skipOrderIds = "skipOrderIds_example"; // String | Skipped orders by ids
    Integer sinceId = 56; // Integer | Retrieve entities starting from the specified id.
    Boolean isDeleted = true; // Boolean | Filter deleted orders
    String shippingCountryIso3 = "shippingCountryIso3_example"; // String | Retrieve entities according to shipping country
    Boolean enableCache = false; // Boolean | If the value is 'true', we will cache orders for a 15 minutes in order to increase speed and reduce requests throttling for some methods and shoping platforms (for example order.shipment.add)
    String deliveryMethod = "deliveryMethod_example"; // String | Retrieves order with delivery method
    String shipNodeType = "shipNodeType_example"; // String | Retrieves order with ship node type
    String currencyId = "currencyId_example"; // String | Currency Id
    try {
      ModelResponseOrderList result = apiInstance.orderList(customerId, customerEmail, phone, orderStatus, orderStatusIds, start, count, pageCursor, sortBy, sortDirection, params, responseFields, exclude, createdTo, createdFrom, modifiedTo, modifiedFrom, storeId, ids, orderIds, ebayOrderStatus, basketId, financialStatus, fulfillmentStatus, shippingMethod, skipOrderIds, sinceId, isDeleted, shippingCountryIso3, enableCache, deliveryMethod, shipNodeType, currencyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderList");
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
| **customerId** | **String**| Retrieves orders specified by customer id | [optional] |
| **customerEmail** | **String**| Retrieves orders specified by customer email | [optional] |
| **phone** | **String**| Filter orders by customer&#39;s phone number | [optional] |
| **orderStatus** | **String**| Retrieves orders specified by order status | [optional] |
| **orderStatusIds** | [**List&lt;String&gt;**](String.md)| Retrieves orders specified by order statuses | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **pageCursor** | **String**| Used to retrieve orders via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **sortBy** | **String**| Set field to sort by | [optional] [default to order_id] |
| **sortDirection** | **String**| Set sorting direction | [optional] [default to asc] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to order_id,customer,totals,address,items,bundles,status] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **storeId** | **String**| Store Id | [optional] |
| **ids** | **String**| Retrieves orders specified by ids | [optional] |
| **orderIds** | **String**| Retrieves orders specified by order ids | [optional] |
| **ebayOrderStatus** | **String**| Retrieves orders specified by order status | [optional] |
| **basketId** | **String**| Retrieves order’s info specified by basket id. | [optional] |
| **financialStatus** | **String**| Retrieves orders specified by financial status | [optional] |
| **fulfillmentStatus** | **String**| Create order with fulfillment status | [optional] |
| **shippingMethod** | **String**| Retrieve entities according to shipping method | [optional] |
| **skipOrderIds** | **String**| Skipped orders by ids | [optional] |
| **sinceId** | **Integer**| Retrieve entities starting from the specified id. | [optional] |
| **isDeleted** | **Boolean**| Filter deleted orders | [optional] |
| **shippingCountryIso3** | **String**| Retrieve entities according to shipping country | [optional] |
| **enableCache** | **Boolean**| If the value is &#39;true&#39;, we will cache orders for a 15 minutes in order to increase speed and reduce requests throttling for some methods and shoping platforms (for example order.shipment.add) | [optional] [default to false] |
| **deliveryMethod** | **String**| Retrieves order with delivery method | [optional] |
| **shipNodeType** | **String**| Retrieves order with ship node type | [optional] |
| **currencyId** | **String**| Currency Id | [optional] |

### Return type

[**ModelResponseOrderList**](ModelResponseOrderList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderPreestimateShippingList"></a>
# **orderPreestimateShippingList**
> ModelResponseOrderPreestimateShippingList orderPreestimateShippingList(orderPreestimateShippingList)



Retrieve list of order preestimated shipping methods

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    OrderPreestimateShippingList orderPreestimateShippingList = new OrderPreestimateShippingList(); // OrderPreestimateShippingList | 
    try {
      ModelResponseOrderPreestimateShippingList result = apiInstance.orderPreestimateShippingList(orderPreestimateShippingList);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderPreestimateShippingList");
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
| **orderPreestimateShippingList** | [**OrderPreestimateShippingList**](OrderPreestimateShippingList.md)|  | |

### Return type

[**ModelResponseOrderPreestimateShippingList**](ModelResponseOrderPreestimateShippingList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderRefundAdd"></a>
# **orderRefundAdd**
> OrderRefundAdd200Response orderRefundAdd(orderRefundAdd)



Add a refund to the order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    OrderRefundAdd orderRefundAdd = new OrderRefundAdd(); // OrderRefundAdd | 
    try {
      OrderRefundAdd200Response result = apiInstance.orderRefundAdd(orderRefundAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderRefundAdd");
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
| **orderRefundAdd** | [**OrderRefundAdd**](OrderRefundAdd.md)|  | |

### Return type

[**OrderRefundAdd200Response**](OrderRefundAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderShipmentAdd"></a>
# **orderShipmentAdd**
> OrderShipmentAdd200Response orderShipmentAdd(orderShipmentAdd)



Add a shipment to the order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    OrderShipmentAdd orderShipmentAdd = new OrderShipmentAdd(); // OrderShipmentAdd | 
    try {
      OrderShipmentAdd200Response result = apiInstance.orderShipmentAdd(orderShipmentAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderShipmentAdd");
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
| **orderShipmentAdd** | [**OrderShipmentAdd**](OrderShipmentAdd.md)|  | |

### Return type

[**OrderShipmentAdd200Response**](OrderShipmentAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderShipmentDelete"></a>
# **orderShipmentDelete**
> OrderShipmentDelete200Response orderShipmentDelete(shipmentId, orderId, storeId)



Delete order&#39;s shipment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | Shipment id indicates the number of delivery
    String orderId = "orderId_example"; // String | Defines the order for which the shipment will be deleted
    String storeId = "storeId_example"; // String | Store Id
    try {
      OrderShipmentDelete200Response result = apiInstance.orderShipmentDelete(shipmentId, orderId, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderShipmentDelete");
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
| **shipmentId** | **String**| Shipment id indicates the number of delivery | |
| **orderId** | **String**| Defines the order for which the shipment will be deleted | |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**OrderShipmentDelete200Response**](OrderShipmentDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderShipmentInfo"></a>
# **orderShipmentInfo**
> ModelResponseOrderShipmentList orderShipmentInfo(id, orderId, start, params, responseFields, exclude, storeId)



Get information of shipment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String id = "id_example"; // String | Entity id
    String orderId = "orderId_example"; // String | Defines the order id
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    String params = "id,order_id,items,tracking_numbers"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String storeId = "storeId_example"; // String | Store Id
    try {
      ModelResponseOrderShipmentList result = apiInstance.orderShipmentInfo(id, orderId, start, params, responseFields, exclude, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderShipmentInfo");
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
| **id** | **String**| Entity id | |
| **orderId** | **String**| Defines the order id | |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,order_id,items,tracking_numbers] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**ModelResponseOrderShipmentList**](ModelResponseOrderShipmentList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderShipmentList"></a>
# **orderShipmentList**
> ModelResponseOrderShipmentList orderShipmentList(orderId, pageCursor, start, count, params, responseFields, exclude, createdFrom, createdTo, modifiedFrom, modifiedTo, storeId)



Get list of shipments by orders.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String orderId = "orderId_example"; // String | Retrieves shipments specified by order id
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String params = "id,order_id,items,tracking_numbers"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String createdFrom = "createdFrom_example"; // String | Retrieve entities from their creation date
    String createdTo = "createdTo_example"; // String | Retrieve entities to their creation date
    String modifiedFrom = "modifiedFrom_example"; // String | Retrieve entities from their modification date
    String modifiedTo = "modifiedTo_example"; // String | Retrieve entities to their modification date
    String storeId = "storeId_example"; // String | Store Id
    try {
      ModelResponseOrderShipmentList result = apiInstance.orderShipmentList(orderId, pageCursor, start, count, params, responseFields, exclude, createdFrom, createdTo, modifiedFrom, modifiedTo, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderShipmentList");
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
| **orderId** | **String**| Retrieves shipments specified by order id | |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,order_id,items,tracking_numbers] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **createdFrom** | **String**| Retrieve entities from their creation date | [optional] |
| **createdTo** | **String**| Retrieve entities to their creation date | [optional] |
| **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] |
| **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] |
| **storeId** | **String**| Store Id | [optional] |

### Return type

[**ModelResponseOrderShipmentList**](ModelResponseOrderShipmentList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderShipmentTrackingAdd"></a>
# **orderShipmentTrackingAdd**
> OrderShipmentTrackingAdd200Response orderShipmentTrackingAdd(orderShipmentTrackingAdd)



Add order shipment&#39;s tracking info.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    OrderShipmentTrackingAdd orderShipmentTrackingAdd = new OrderShipmentTrackingAdd(); // OrderShipmentTrackingAdd | 
    try {
      OrderShipmentTrackingAdd200Response result = apiInstance.orderShipmentTrackingAdd(orderShipmentTrackingAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderShipmentTrackingAdd");
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
| **orderShipmentTrackingAdd** | [**OrderShipmentTrackingAdd**](OrderShipmentTrackingAdd.md)|  | |

### Return type

[**OrderShipmentTrackingAdd200Response**](OrderShipmentTrackingAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderShipmentUpdate"></a>
# **orderShipmentUpdate**
> AccountConfigUpdate200Response orderShipmentUpdate(orderShipmentUpdate)



Update order&#39;s shipment information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    OrderShipmentUpdate orderShipmentUpdate = new OrderShipmentUpdate(); // OrderShipmentUpdate | 
    try {
      AccountConfigUpdate200Response result = apiInstance.orderShipmentUpdate(orderShipmentUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderShipmentUpdate");
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
| **orderShipmentUpdate** | [**OrderShipmentUpdate**](OrderShipmentUpdate.md)|  | |

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderStatusList"></a>
# **orderStatusList**
> OrderStatusList200Response orderStatusList(storeId, responseFields)



Retrieve list of statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String storeId = "storeId_example"; // String | Store Id
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    try {
      OrderStatusList200Response result = apiInstance.orderStatusList(storeId, responseFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderStatusList");
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
| **storeId** | **String**| Store Id | [optional] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |

### Return type

[**OrderStatusList200Response**](OrderStatusList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderTransactionList"></a>
# **orderTransactionList**
> ModelResponseOrderTransactionList orderTransactionList(orderIds, count, storeId, params, responseFields, exclude, pageCursor)



Retrieve list of order transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String orderIds = "orderIds_example"; // String | Retrieves order transactions specified by order ids
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String storeId = "storeId_example"; // String | Store Id
    String params = "id,order_id,amount,description"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String responseFields = "responseFields_example"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    String exclude = "exclude_example"; // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
    String pageCursor = "pageCursor_example"; // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
    try {
      ModelResponseOrderTransactionList result = apiInstance.orderTransactionList(orderIds, count, storeId, params, responseFields, exclude, pageCursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderTransactionList");
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
| **orderIds** | **String**| Retrieves order transactions specified by order ids | |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **storeId** | **String**| Store Id | [optional] |
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,order_id,amount,description] |
| **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] |
| **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] |
| **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] |

### Return type

[**ModelResponseOrderTransactionList**](ModelResponseOrderTransactionList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="orderUpdate"></a>
# **orderUpdate**
> AccountConfigUpdate200Response orderUpdate(orderId, storeId, orderStatus, comment, adminComment, adminPrivateComment, dateModified, dateFinished, financialStatus, fulfillmentStatus, orderPaymentMethod, sendNotifications)



Update existing order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String orderId = "orderId_example"; // String | Defines the orders specified by order id
    String storeId = "storeId_example"; // String | Defines store id where the order should be found
    String orderStatus = "orderStatus_example"; // String | Defines new order's status
    String comment = "comment_example"; // String | Specifies order comment
    String adminComment = "adminComment_example"; // String | Specifies admin's order comment
    String adminPrivateComment = "adminPrivateComment_example"; // String | Specifies private admin's order comment
    String dateModified = "dateModified_example"; // String | Specifies order's  modification date
    String dateFinished = "dateFinished_example"; // String | Specifies order's  finished date
    String financialStatus = "financialStatus_example"; // String | Update order financial status to specified
    String fulfillmentStatus = "fulfillmentStatus_example"; // String | Create order with fulfillment status
    String orderPaymentMethod = "orderPaymentMethod_example"; // String | Defines order payment method.<br/>Setting order_payment_method on Shopify will also change financial_status field value to 'paid'
    Boolean sendNotifications = false; // Boolean | Send notifications to customer after order was created
    try {
      AccountConfigUpdate200Response result = apiInstance.orderUpdate(orderId, storeId, orderStatus, comment, adminComment, adminPrivateComment, dateModified, dateFinished, financialStatus, fulfillmentStatus, orderPaymentMethod, sendNotifications);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderUpdate");
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
| **orderId** | **String**| Defines the orders specified by order id | |
| **storeId** | **String**| Defines store id where the order should be found | [optional] |
| **orderStatus** | **String**| Defines new order&#39;s status | [optional] |
| **comment** | **String**| Specifies order comment | [optional] |
| **adminComment** | **String**| Specifies admin&#39;s order comment | [optional] |
| **adminPrivateComment** | **String**| Specifies private admin&#39;s order comment | [optional] |
| **dateModified** | **String**| Specifies order&#39;s  modification date | [optional] |
| **dateFinished** | **String**| Specifies order&#39;s  finished date | [optional] |
| **financialStatus** | **String**| Update order financial status to specified | [optional] |
| **fulfillmentStatus** | **String**| Create order with fulfillment status | [optional] |
| **orderPaymentMethod** | **String**| Defines order payment method.&lt;br/&gt;Setting order_payment_method on Shopify will also change financial_status field value to &#39;paid&#39; | [optional] |
| **sendNotifications** | **Boolean**| Send notifications to customer after order was created | [optional] [default to false] |

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

