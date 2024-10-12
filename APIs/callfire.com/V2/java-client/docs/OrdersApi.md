# OrdersApi

All URIs are relative to *https://api.callfire.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findOrders**](OrdersApi.md#findOrders) | **GET** /orders | Find orders |
| [**getOrder**](OrdersApi.md#getOrder) | **GET** /orders/{id} | Find a specific order |
| [**orderKeywords**](OrdersApi.md#orderKeywords) | **POST** /orders/keywords | Purchase keywords |
| [**orderNumbers**](OrdersApi.md#orderNumbers) | **POST** /orders/numbers | Purchase numbers |


<a id="findOrders"></a>
# **findOrders**
> PageNumberOrder findOrders(limit, offset, fields, status, intervalBegin, intervalEnd)

Find orders

Searches for account orders

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Integer limit = 20; // Integer | To set the maximum number of records to return in a paged list response. The default is 100
    Integer offset = 0; // Integer | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    List<String> status = Arrays.asList(); // List<String> | Filter by order status, accepts multiple values in comma separated string, available values: [PROCESSING, FINISHED, PAYMENT_ERROR, VOID, WAIT_FOR_PAYMENT, PARTIALLY_ADJUSTED, ADJUSTED]
    Long intervalBegin = 56L; // Long | Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
    Long intervalEnd = 56L; // Long | End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
    try {
      PageNumberOrder result = apiInstance.findOrders(limit, offset, fields, status, intervalBegin, intervalEnd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#findOrders");
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
| **limit** | **Integer**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 20] |
| **offset** | **Integer**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0] |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **status** | [**List&lt;String&gt;**](String.md)| Filter by order status, accepts multiple values in comma separated string, available values: [PROCESSING, FINISHED, PAYMENT_ERROR, VOID, WAIT_FOR_PAYMENT, PARTIALLY_ADJUSTED, ADJUSTED] | [optional] |
| **intervalBegin** | **Long**| Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 | [optional] |
| **intervalEnd** | **Long**| End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 | [optional] |

### Return type

[**PageNumberOrder**](PageNumberOrder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getOrder"></a>
# **getOrder**
> NumberOrder getOrder(id, fields)

Find a specific order

Returns a single NumberOrder instance for a given order id. Order contains information about purchased keywords, local, toll-free numbers

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    Long id = 56L; // Long | An id of an order
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    try {
      NumberOrder result = apiInstance.getOrder(id, fields);
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
| **id** | **Long**| An id of an order | |
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |

### Return type

[**NumberOrder**](NumberOrder.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="orderKeywords"></a>
# **orderKeywords**
> ResourceId orderKeywords(fields, keywordPurchaseRequest)

Purchase keywords

Purchase keywords. Send a list of available keywords into this API to purchase them using CallFire credits. Make sure the account has enough credits before trying to purchase the keywords. Keyword should only consist of uppercase and lowercase letters and numbers. Number of characters must be greater than 2, but less than 65.

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    KeywordPurchaseRequest keywordPurchaseRequest = new KeywordPurchaseRequest(); // KeywordPurchaseRequest | Request object which contains a list of keywords to buy
    try {
      ResourceId result = apiInstance.orderKeywords(fields, keywordPurchaseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderKeywords");
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
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **keywordPurchaseRequest** | [**KeywordPurchaseRequest**](KeywordPurchaseRequest.md)| Request object which contains a list of keywords to buy | [optional] |

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="orderNumbers"></a>
# **orderNumbers**
> ResourceId orderNumbers(fields, numberPurchaseRequest)

Purchase numbers

Purchase numbers. There are many ways to purchase a number. Set either &#39;tollFreeCount&#39; or &#39;localCount&#39; along with some querying fields to purchase numbers by bulk query. Set the list of numbers to purchase by list. Available numbers will be purchased using CallFire credits owned by the user. Make sure the account has enough credits before trying to purchase

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
    defaultClient.setBasePath("https://api.callfire.com/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String fields = "fields_example"; // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    NumberPurchaseRequest numberPurchaseRequest = new NumberPurchaseRequest(); // NumberPurchaseRequest | Request object contains a list of numbers to buy, you can filter the numbers by their region information: city, state, zipcode, etc
    try {
      ResourceId result = apiInstance.orderNumbers(fields, numberPurchaseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orderNumbers");
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
| **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] |
| **numberPurchaseRequest** | [**NumberPurchaseRequest**](NumberPurchaseRequest.md)| Request object contains a list of numbers to buy, you can filter the numbers by their region information: city, state, zipcode, etc | [optional] |

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **500** | Internal Server Error |  -  |

