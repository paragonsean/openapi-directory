# MarketplacesOrdersV3OrderApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeOrderV3**](MarketplacesOrdersV3OrderApi.md#changeOrderV3) | **POST** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/{changeOrderType} | Change your marketplace Order Information (accept, ship, etc.) |
| [**clearMerchantOrderInfoV3**](MarketplacesOrdersV3OrderApi.md#clearMerchantOrderInfoV3) | **POST** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/clearMerchantOrderInfo | Clear an Order&#39;s merchant information |
| [**getOrderChangeReportingV3**](MarketplacesOrdersV3OrderApi.md#getOrderChangeReportingV3) | **GET** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/history/{orderChangeExecutionUUID} | Get the order change reporting |
| [**getOrderHistoryV3**](MarketplacesOrdersV3OrderApi.md#getOrderHistoryV3) | **GET** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/history | Get an Order&#39;s harvest and change history |
| [**getOrderV3**](MarketplacesOrdersV3OrderApi.md#getOrderV3) | **GET** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId} | Get full Order and Order Item(s) properties |
| [**harvestAccount**](MarketplacesOrdersV3OrderApi.md#harvestAccount) | **POST** /orders/v3/{marketplaceTechnicalCode}/{accountId}/harvest | Send harvest request for an Account |
| [**harvestOrderV3**](MarketplacesOrdersV3OrderApi.md#harvestOrderV3) | **POST** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/harvest | Send harvest request for a single Order |
| [**headOrderV3**](MarketplacesOrdersV3OrderApi.md#headOrderV3) | **HEAD** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId} | Get the meta information about the order (ETag, Last-Modified) |
| [**setMerchantOrderInfoV3**](MarketplacesOrdersV3OrderApi.md#setMerchantOrderInfoV3) | **POST** /orders/v3/{marketplaceTechnicalCode}/{accountId}/{beezUPOrderId}/setMerchantOrderInfo | Set an Order&#39;s merchant information |


<a id="changeOrderV3"></a>
# **changeOrderV3**
> changeOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, changeOrderType, userName, testMode, requestBody)

Change your marketplace Order Information (accept, ship, etc.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3OrderApi apiInstance = new MarketplacesOrdersV3OrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    String changeOrderType = "changeOrderType_example"; // String | The Order change type
    String userName = "userName_example"; // String | Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application's user login.
    Boolean testMode = false; // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    Map<String, String> requestBody = new HashMap(); // Map<String, String> | 
    try {
      apiInstance.changeOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, changeOrderType, userName, testMode, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3OrderApi#changeOrderV3");
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
| **202** | Order change request accepted |  * Location - The location of the generated invoice. Might take a few seconds to be available <br>  |
| **400** | Invalid order change request, could not be send to the marketplace. Please check the body of this request. |  -  |
| **404** | Requested Order could not be found |  -  |
| **409** | Already processing a change request for this Order.\\ Please refresh your clients Order information and retry later.  |  * Location - The location of the generated invoice. Might take a few seconds to be available <br>  * Retry-After - Indicates the duration in seconds to wait to be able to make this request again <br>  |
| **412** | The ETag sent in the http header If-Match did not match with the current version. Please refresh the information related to this resource. |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="clearMerchantOrderInfoV3"></a>
# **clearMerchantOrderInfoV3**
> clearMerchantOrderInfoV3(marketplaceTechnicalCode, accountId, beezUPOrderId, testMode)

Clear an Order&#39;s merchant information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3OrderApi apiInstance = new MarketplacesOrdersV3OrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    Boolean testMode = false; // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    try {
      apiInstance.clearMerchantOrderInfoV3(marketplaceTechnicalCode, accountId, beezUPOrderId, testMode);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3OrderApi#clearMerchantOrderInfoV3");
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
| **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false] |

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
| **202** | Clear Order merchant order info accepted |  -  |
| **400** | Could not update Order merchant information. Please see body for more information. |  -  |
| **404** | Requested Order could not be found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrderChangeReportingV3"></a>
# **getOrderChangeReportingV3**
> ChangeOrderReporting getOrderChangeReportingV3(marketplaceTechnicalCode, accountId, beezUPOrderId, orderChangeExecutionUUID)

Get the order change reporting

This operation will help you to know the status of your order change operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3OrderApi apiInstance = new MarketplacesOrdersV3OrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    String orderChangeExecutionUUID = "orderChangeExecutionUUID_example"; // String | The order change execution id
    try {
      ChangeOrderReporting result = apiInstance.getOrderChangeReportingV3(marketplaceTechnicalCode, accountId, beezUPOrderId, orderChangeExecutionUUID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3OrderApi#getOrderChangeReportingV3");
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
| **orderChangeExecutionUUID** | **String**| The order change execution id | |

### Return type

[**ChangeOrderReporting**](ChangeOrderReporting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched Order change reporting |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **404** | Requested Order could not be found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getOrderHistoryV3"></a>
# **getOrderHistoryV3**
> OrderHistory getOrderHistoryV3(marketplaceTechnicalCode, accountId, beezUPOrderId)

Get an Order&#39;s harvest and change history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3OrderApi apiInstance = new MarketplacesOrdersV3OrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    try {
      OrderHistory result = apiInstance.getOrderHistoryV3(marketplaceTechnicalCode, accountId, beezUPOrderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3OrderApi#getOrderHistoryV3");
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

<a id="getOrderV3"></a>
# **getOrderV3**
> OrderWithLinks getOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, ifNoneMatch)

Get full Order and Order Item(s) properties

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3OrderApi apiInstance = new MarketplacesOrdersV3OrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      OrderWithLinks result = apiInstance.getOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3OrderApi#getOrderV3");
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

[**OrderWithLinks**](OrderWithLinks.md)

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

<a id="harvestAccount"></a>
# **harvestAccount**
> harvestAccount(marketplaceTechnicalCode, accountId, marketplaceOrderId, beezUPOrderId)

Send harvest request for an Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3OrderApi apiInstance = new MarketplacesOrdersV3OrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    String marketplaceOrderId = "marketplaceOrderId_example"; // String | 
    String beezUPOrderId = "beezUPOrderId_example"; // String | 
    try {
      apiInstance.harvestAccount(marketplaceTechnicalCode, accountId, marketplaceOrderId, beezUPOrderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3OrderApi#harvestAccount");
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
| **marketplaceOrderId** | **String**|  | [optional] |
| **beezUPOrderId** | **String**|  | [optional] |

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
| **404** | Requested Account Or beezUPOrderId could not be found |  -  |
| **409** | Failed to send harvest request because allowed rate limits have been exceeded |  * Retry-After - Indicates the duration in seconds to wait to be able to make this request again <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="harvestOrderV3"></a>
# **harvestOrderV3**
> harvestOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId)

Send harvest request for a single Order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3OrderApi apiInstance = new MarketplacesOrdersV3OrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    try {
      apiInstance.harvestOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3OrderApi#harvestOrderV3");
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

<a id="headOrderV3"></a>
# **headOrderV3**
> headOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, ifNoneMatch)

Get the meta information about the order (ETag, Last-Modified)

The purpose of this operation is to reduce the bandwith usage by getting just the meta information about the order (ETag, Last-Modified) with the body. This could be useful 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3OrderApi apiInstance = new MarketplacesOrdersV3OrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      apiInstance.headOrderV3(marketplaceTechnicalCode, accountId, beezUPOrderId, ifNoneMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3OrderApi#headOrderV3");
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

<a id="setMerchantOrderInfoV3"></a>
# **setMerchantOrderInfoV3**
> setMerchantOrderInfoV3(marketplaceTechnicalCode, accountId, beezUPOrderId, setMerchantOrderInfoRequest, testMode)

Set an Order&#39;s merchant information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesOrdersV3OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesOrdersV3OrderApi apiInstance = new MarketplacesOrdersV3OrderApi(defaultClient);
    String marketplaceTechnicalCode = "Amazon"; // String | The marketplace technical code
    Integer accountId = 1001; // Integer | 
    UUID beezUPOrderId = UUID.fromString("00000000000000000000000000000000000000000000000"); // UUID | The BeezUP Order identifier
    SetMerchantOrderInfoRequest setMerchantOrderInfoRequest = new SetMerchantOrderInfoRequest(); // SetMerchantOrderInfoRequest | 
    Boolean testMode = false; // Boolean | If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    try {
      apiInstance.setMerchantOrderInfoV3(marketplaceTechnicalCode, accountId, beezUPOrderId, setMerchantOrderInfoRequest, testMode);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesOrdersV3OrderApi#setMerchantOrderInfoV3");
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
| **testMode** | **Boolean**| If true, the operation will be not be sent to marketplace. But the validation will be taken in account. | [optional] [default to false] |

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
| **202** | Set Order merchant order info accepted |  -  |
| **400** | Could not update Order merchant information. Please see body for more information. |  -  |
| **404** | Requested Order could not be found |  -  |
| **0** | Occurs when something goes wrong |  -  |

