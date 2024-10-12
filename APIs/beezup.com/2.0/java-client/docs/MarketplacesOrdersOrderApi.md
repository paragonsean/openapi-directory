# MarketplacesOrdersOrderApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeOrder**](MarketplacesOrdersOrderApi.md#changeOrder) | **POST** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/{changeOrderType} | [DEPRECATED] Change your marketplace Order Information (accept, ship, etc.) |
| [**clearMerchantOrderInfo**](MarketplacesOrdersOrderApi.md#clearMerchantOrderInfo) | **POST** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/clearMerchantOrderInfo | [DEPRECATED] Clear an Order&#39;s merchant information |
| [**getOrder**](MarketplacesOrdersOrderApi.md#getOrder) | **GET** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId} | [DEPRECATED] DEPRECATED - Get full Order and Order Item(s) properties |
| [**getOrderHistory**](MarketplacesOrdersOrderApi.md#getOrderHistory) | **GET** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/history | [DEPRECATED] Get an Order&#39;s harvest and change history |
| [**harvestOrder**](MarketplacesOrdersOrderApi.md#harvestOrder) | **POST** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/harvest | [DEPRECATED] Send harvest request for a single Order |
| [**headOrder**](MarketplacesOrdersOrderApi.md#headOrder) | **HEAD** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId} | [DEPRECATED] DEPRECATED - Get the meta information about the order (ETag, Last-Modified) |
| [**setMerchantOrderInfo**](MarketplacesOrdersOrderApi.md#setMerchantOrderInfo) | **POST** /v2/user/marketplaces/orders/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/setMerchantOrderInfo | [DEPRECATED] Set an Order&#39;s merchant information |


<a id="changeOrder"></a>
# **changeOrder**
> changeOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, changeOrderType, userName, ifMatch, testMode, requestBody)

[DEPRECATED] Change your marketplace Order Information (accept, ship, etc.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersOrderApi apiInstance = new MarketplacesOrdersOrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    String changeOrderType = "changeOrderType_example"; // String | The Order change type
    String userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
    String ifMatch = "ifMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To ensure that you are making a change on the lastest version of the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    Boolean testMode = false; // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    Map<String, String> requestBody = new HashMap(); // Map<String, String> | 
    try {
      apiInstance.changeOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, changeOrderType, userName, ifMatch, testMode, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersOrderApi#changeOrder");
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
| **marketplaceTechnicalCode** | **String**| The marketplace technical code | |
| **accountId** | **Integer**|  | |
| **beezUPOrderId** | **UUID**| The BeezUP Order identifier | |
| **changeOrderType** | **String**| The Order change type | |
| **userName** | **String**| Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login. | |
| **ifMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To ensure that you are making a change on the lastest version of the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | |
| **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false] |
| **requestBody** | [**Map&lt;String, String&gt;**](String.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Order change request accepted |  -  |
| **400** | Invalid order change request, could not be send to the marketplace. Please check the body of this request. |  -  |
| **404** | Requested Order could not be found |  -  |
| **409** | Already processing a change request for this Order.\\ Please refresh your clients Order information and retry later.  |  * Retry-After - Indicates the duration in seconds to wait to be able to make this request again <br>  |
| **412** | The ETag sent in the http header If-Match did not match with the current version. Please refresh the information related to this resource. |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="clearMerchantOrderInfo"></a>
# **clearMerchantOrderInfo**
> clearMerchantOrderInfo(marketplaceTechnicalCode, accountId, beezUPOrderId)

[DEPRECATED] Clear an Order&#39;s merchant information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersOrderApi apiInstance = new MarketplacesOrdersOrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    try {
      apiInstance.clearMerchantOrderInfo(marketplaceTechnicalCode, accountId, beezUPOrderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersOrderApi#clearMerchantOrderInfo");
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
| **marketplaceTechnicalCode** | **String**| The marketplace technical code | |
| **accountId** | **Integer**|  | |
| **beezUPOrderId** | **UUID**| The BeezUP Order identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully cleared Order merchant order info set |  -  |
| **400** | Could not update Order merchant information. Please see body for more information. |  -  |
| **404** | Requested Order could not be found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrder"></a>
# **getOrder**
> Order getOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, ifNoneMatch)

[DEPRECATED] DEPRECATED - Get full Order and Order Item(s) properties

DEPRECATED - Use /orders/v3 instead

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersOrderApi apiInstance = new MarketplacesOrdersOrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      Order result = apiInstance.getOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersOrderApi#getOrder");
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
| **marketplaceTechnicalCode** | **String**| The marketplace technical code | |
| **accountId** | **Integer**|  | |
| **beezUPOrderId** | **UUID**| The BeezUP Order identifier | |
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched Order and Order Item(s) properties |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **404** | Requested Order could not be found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrderHistory"></a>
# **getOrderHistory**
> OrderHistory getOrderHistory(marketplaceTechnicalCode, accountId, beezUPOrderId, ifNoneMatch)

[DEPRECATED] Get an Order&#39;s harvest and change history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersOrderApi apiInstance = new MarketplacesOrdersOrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      OrderHistory result = apiInstance.getOrderHistory(marketplaceTechnicalCode, accountId, beezUPOrderId, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersOrderApi#getOrderHistory");
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
| **marketplaceTechnicalCode** | **String**| The marketplace technical code | |
| **accountId** | **Integer**|  | |
| **beezUPOrderId** | **UUID**| The BeezUP Order identifier | |
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**OrderHistory**](OrderHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched Order history |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **404** | Requested Order could not be found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="harvestOrder"></a>
# **harvestOrder**
> harvestOrder(marketplaceTechnicalCode, accountId, beezUPOrderId)

[DEPRECATED] Send harvest request for a single Order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersOrderApi apiInstance = new MarketplacesOrdersOrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    try {
      apiInstance.harvestOrder(marketplaceTechnicalCode, accountId, beezUPOrderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersOrderApi#harvestOrder");
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
| **marketplaceTechnicalCode** | **String**| The marketplace technical code | |
| **accountId** | **Integer**|  | |
| **beezUPOrderId** | **UUID**| The BeezUP Order identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successfully sent Order harvest request |  * Retry-After - Indicates the duration in seconds to wait to be able to make this request again <br>  |
| **404** | Requested Order could not be found |  -  |
| **409** | Failed to send harvest request because allowed rate limits have been exceeded |  * Retry-After - Indicates the duration in seconds to wait to be able to make this request again <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="headOrder"></a>
# **headOrder**
> headOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, ifNoneMatch)

[DEPRECATED] DEPRECATED - Get the meta information about the order (ETag, Last-Modified)

DEPRECATED - Use /orders/v3 instead The purpose of this operation is to reduce the bandwith usage by getting just the meta information about the order (ETag, Last-Modified) with the body. This could be useful 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersOrderApi apiInstance = new MarketplacesOrdersOrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      apiInstance.headOrder(marketplaceTechnicalCode, accountId, beezUPOrderId, ifNoneMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersOrderApi#headOrder");
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
| **marketplaceTechnicalCode** | **String**| The marketplace technical code | |
| **accountId** | **Integer**|  | |
| **beezUPOrderId** | **UUID**| The BeezUP Order identifier | |
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched Order and Order Item(s) properties |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **404** | Requested Order could not be found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="setMerchantOrderInfo"></a>
# **setMerchantOrderInfo**
> setMerchantOrderInfo(marketplaceTechnicalCode, accountId, beezUPOrderId, setMerchantOrderInfoRequest)

[DEPRECATED] Set an Order&#39;s merchant information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersOrderApi apiInstance = new MarketplacesOrdersOrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    SetMerchantOrderInfoRequest setMerchantOrderInfoRequest = new SetMerchantOrderInfoRequest(); // SetMerchantOrderInfoRequest | 
    try {
      apiInstance.setMerchantOrderInfo(marketplaceTechnicalCode, accountId, beezUPOrderId, setMerchantOrderInfoRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersOrderApi#setMerchantOrderInfo");
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
| **marketplaceTechnicalCode** | **String**| The marketplace technical code | |
| **accountId** | **Integer**|  | |
| **beezUPOrderId** | **UUID**| The BeezUP Order identifier | |
| **setMerchantOrderInfoRequest** | [**SetMerchantOrderInfoRequest**](SetMerchantOrderInfoRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully set Order merchant order info set |  -  |
| **400** | Could not update Order merchant information. Please see body for more information. |  -  |
| **404** | Requested Order could not be found |  -  |
| **0** | Occurs when something goes wrong |  -  |

