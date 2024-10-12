# MarketplacesOrdersListApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrderListFull**](MarketplacesOrdersListApi.md#getOrderListFull) | **POST** /v2/user/marketplaces/orders/list/full | [DEPRECATED] Get a paginated list of all Orders with all Order and Order Item(s) properties |
| [**getOrderListLight**](MarketplacesOrdersListApi.md#getOrderListLight) | **POST** /v2/user/marketplaces/orders/list/light | [DEPRECATED] Get a paginated list of all Orders without details |


<a id="getOrderListFull"></a>
# **getOrderListFull**
> OrderListFull getOrderListFull(acceptEncoding, orderListRequest)

[DEPRECATED] Get a paginated list of all Orders with all Order and Order Item(s) properties

DEPRECATED - Use /orders/v3 instead The purpose of this operation is to reduce the amount of request to the API.\\ \\ Previous implmentation of this feature only returned a partial (light) version of the Orders. The purpose of this API is to reduce the number of incoming requests by returning the complete (full) Order and Order Item(s) properties. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersListApi apiInstance = new MarketplacesOrdersListApi(defaultClient);
    List<String> acceptEncoding = Arrays.asList(); // List<String> | Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
    OrderListRequest orderListRequest = new OrderListRequest(); // OrderListRequest | 
    try {
      OrderListFull result = apiInstance.getOrderListFull(acceptEncoding, orderListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersListApi#getOrderListFull");
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
| **acceptEncoding** | [**List&lt;String&gt;**](String.md)| Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size | |
| **orderListRequest** | [**OrderListRequest**](OrderListRequest.md)|  | |

### Return type

[**OrderListFull**](OrderListFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched the full list of Orders |  -  |
| **400** | Could not process request for given parameters values. Please check error message for more details. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrderListLight"></a>
# **getOrderListLight**
> OrderListLight getOrderListLight(orderListRequest)

[DEPRECATED] Get a paginated list of all Orders without details

Use /orders/v3 instead

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersListApi apiInstance = new MarketplacesOrdersListApi(defaultClient);
    OrderListRequest orderListRequest = new OrderListRequest(); // OrderListRequest | 
    try {
      OrderListLight result = apiInstance.getOrderListLight(orderListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersListApi#getOrderListLight");
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
| **orderListRequest** | [**OrderListRequest**](OrderListRequest.md)|  | |

### Return type

[**OrderListLight**](OrderListLight.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched the list of Orders |  -  |
| **400** | Could not process request for given parameters values. Please check error message for more details. |  -  |
| **0** | Occurs when something goes wrong |  -  |

