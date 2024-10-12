# MarketplacesOrdersV3ListApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrderListFullV3**](MarketplacesOrdersV3ListApi.md#getOrderListFullV3) | **POST** /orders/v3/list/full | Get a paginated list of all Orders with all Order and Order Item(s) properties |
| [**getOrderListLightV3**](MarketplacesOrdersV3ListApi.md#getOrderListLightV3) | **POST** /orders/v3/list/light | Get a paginated list of all Orders without details |


<a id="getOrderListFullV3"></a>
# **getOrderListFullV3**
> OrderListFullWithLinks getOrderListFullV3(acceptEncoding, orderListRequest)

Get a paginated list of all Orders with all Order and Order Item(s) properties

The purpose of this operation is to reduce the amount of request to the API.\\ \\ Previous implmentation of this feature only returned a partial (light) version of the Orders. The purpose of this API is to reduce the number of incoming requests by returning the complete (full) Order and Order Item(s) properties. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3ListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3ListApi apiInstance = new MarketplacesOrdersV3ListApi(defaultClient);
    String acceptEncoding = "acceptEncoding_example"; // String | Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size
    OrderListRequest orderListRequest = new OrderListRequest(); // OrderListRequest | 
    try {
      OrderListFullWithLinks result = apiInstance.getOrderListFullV3(acceptEncoding, orderListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3ListApi#getOrderListFullV3");
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
| **acceptEncoding** | **String**| Allows the client to indicate wether it accepts a compressed encoding to reduce traffic size | |
| **orderListRequest** | [**OrderListRequest**](OrderListRequest.md)|  | |

### Return type

[**OrderListFullWithLinks**](OrderListFullWithLinks.md)

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

<a id="getOrderListLightV3"></a>
# **getOrderListLightV3**
> OrderListLightWithLinks getOrderListLightV3(orderListRequest)

Get a paginated list of all Orders without details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3ListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3ListApi apiInstance = new MarketplacesOrdersV3ListApi(defaultClient);
    OrderListRequest orderListRequest = new OrderListRequest(); // OrderListRequest | 
    try {
      OrderListLightWithLinks result = apiInstance.getOrderListLightV3(orderListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3ListApi#getOrderListLightV3");
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

[**OrderListLightWithLinks**](OrderListLightWithLinks.md)

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

