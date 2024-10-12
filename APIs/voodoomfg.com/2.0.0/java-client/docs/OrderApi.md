# OrderApi

All URIs are relative to */api/2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**orderConfirmPost**](OrderApi.md#orderConfirmPost) | **POST** /order/confirm | Confirms an order from a quote_id and submits it to the Voodoo factory.  |
| [**orderCreatePost**](OrderApi.md#orderCreatePost) | **POST** /order/create | Quotes an order and returns a quote_id that is used to confirm the order.  |
| [**orderGet**](OrderApi.md#orderGet) | **GET** /order | Lists all orders.  |
| [**orderOrderIdGet**](OrderApi.md#orderOrderIdGet) | **GET** /order/{order_id} | Retrieve a previously created model by its id.  |
| [**orderShippingPost**](OrderApi.md#orderShippingPost) | **POST** /order/shipping | List shipping options and prices for a given shipment.  |


<a id="orderConfirmPost"></a>
# **orderConfirmPost**
> OrderConfirmPost200Response orderConfirmPost(body)

Confirms an order from a quote_id and submits it to the Voodoo factory. 

After generating a quote for an order, you can choose to confirm the order for manufacturing by hitting this endpoint with the quote_id returned by the /order/quote endpoint. Returns the order with a unique order_id in place of the quote_id. 

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
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    ConfirmOrderBody body = new ConfirmOrderBody(); // ConfirmOrderBody | 
    try {
      OrderConfirmPost200Response result = apiInstance.orderConfirmPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderConfirmPost");
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
| **body** | [**ConfirmOrderBody**](ConfirmOrderBody.md)|  | |

### Return type

[**OrderConfirmPost200Response**](OrderConfirmPost200Response.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order info with order_id |  -  |

<a id="orderCreatePost"></a>
# **orderCreatePost**
> OrderCreatePost200Response orderCreatePost(body)

Quotes an order and returns a quote_id that is used to confirm the order. 

Creates an order for the requested items, shipping address, and shipping method. This method returns the order along with a quote_id, which needs to be confirmed with /order/confirm prior to the order actually being started. quote_ids are only valid for 15 minutes. 

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
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    CreateOrderBody body = new CreateOrderBody(); // CreateOrderBody | 
    try {
      OrderCreatePost200Response result = apiInstance.orderCreatePost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderCreatePost");
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
| **body** | [**CreateOrderBody**](CreateOrderBody.md)|  | |

### Return type

[**OrderCreatePost200Response**](OrderCreatePost200Response.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Quote and order information. |  -  |

<a id="orderGet"></a>
# **orderGet**
> List&lt;Order&gt; orderGet()

Lists all orders. 

Gets all of orders that you&#39;ve confirmed. 

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
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    try {
      List<Order> result = apiInstance.orderGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderGet");
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

[**List&lt;Order&gt;**](Order.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of orders |  -  |

<a id="orderOrderIdGet"></a>
# **orderOrderIdGet**
> Order orderOrderIdGet(orderId)

Retrieve a previously created model by its id. 

In cases where you&#39;re ordering models you&#39;ve created previously, you can fetch a specific model by its id. 

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
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String orderId = "orderId_example"; // String | 
    try {
      Order result = apiInstance.orderOrderIdGet(orderId);
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
| **orderId** | **String**|  | |

### Return type

[**Order**](Order.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Model object |  -  |

<a id="orderShippingPost"></a>
# **orderShippingPost**
> OrderShippingPost200Response orderShippingPost(body)

List shipping options and prices for a given shipment. 

Get quotes for shipping your order to the given shipping address. Because shipping quotes depend on the items being shipped, you should use the same array of print descriptions here that you do to create the order.  This endpoint should allow you to select the appropriate shipping method using the \&quot;service\&quot; field of the desired shipping method. 

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
    defaultClient.setBasePath("/api/2");
    
    // Configure API key authorization: Voodoo Manufacturing API Key
    ApiKeyAuth Voodoo Manufacturing API Key = (ApiKeyAuth) defaultClient.getAuthentication("Voodoo Manufacturing API Key");
    Voodoo Manufacturing API Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Voodoo Manufacturing API Key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    ShippingOptionsBody body = new ShippingOptionsBody(); // ShippingOptionsBody | 
    try {
      OrderShippingPost200Response result = apiInstance.orderShippingPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderShippingPost");
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
| **body** | [**ShippingOptionsBody**](ShippingOptionsBody.md)|  | |

### Return type

[**OrderShippingPost200Response**](OrderShippingPost200Response.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing an array of shipping rates |  -  |

