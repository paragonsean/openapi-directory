# V1Api

All URIs are relative to *http://api.ote-godaddy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**callList**](V1Api.md#callList) | **GET** /v1/orders | Retrieve a list of orders for the authenticated shopper. Only one filter may be used at a time |
| [**get**](V1Api.md#get) | **GET** /v1/orders/{orderId} | Retrieve details for specified order |


<a id="callList"></a>
# **callList**
> OrderList callList(periodStart, periodEnd, domain, productGroupId, paymentProfileId, parentOrderId, offset, limit, sort, xShopperId, xMarketId)

Retrieve a list of orders for the authenticated shopper. Only one filter may be used at a time

&lt;strong&gt;API Resellers&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;This endpoint does not support subaccounts and therefore API Resellers should not supply an X-Shopper-Id header&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String periodStart = "periodStart_example"; // String | Start of range indicating what time-frame should be returned. Inclusive
    String periodEnd = "periodEnd_example"; // String | End of range indicating what time-frame should be returned. Inclusive
    String domain = "domain_example"; // String | Domain name to use as the filter of results
    Integer productGroupId = 56; // Integer | Product group id to use as the filter of results
    Integer paymentProfileId = 56; // Integer | Payment profile id to use as the filter of results
    String parentOrderId = "parentOrderId_example"; // String | Parent order id to use as the filter of results
    Integer offset = 0; // Integer | Number of results to skip for pagination
    Integer limit = 25; // Integer | Maximum number of items to return
    String sort = "createdAt"; // String | Property name that will be used to sort results. '-' indicates descending
    String xShopperId = "xShopperId_example"; // String | Shopper ID to be operated on, if different from JWT<br/><b>Reseller subaccounts are not supported</b>
    String xMarketId = "en-US"; // String | Unique identifier of the Market in which the request is happening
    try {
      OrderList result = apiInstance.callList(periodStart, periodEnd, domain, productGroupId, paymentProfileId, parentOrderId, offset, limit, sort, xShopperId, xMarketId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#callList");
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
| **periodStart** | **String**| Start of range indicating what time-frame should be returned. Inclusive | [optional] |
| **periodEnd** | **String**| End of range indicating what time-frame should be returned. Inclusive | [optional] |
| **domain** | **String**| Domain name to use as the filter of results | [optional] |
| **productGroupId** | **Integer**| Product group id to use as the filter of results | [optional] |
| **paymentProfileId** | **Integer**| Payment profile id to use as the filter of results | [optional] |
| **parentOrderId** | **String**| Parent order id to use as the filter of results | [optional] |
| **offset** | **Integer**| Number of results to skip for pagination | [optional] [default to 0] |
| **limit** | **Integer**| Maximum number of items to return | [optional] [default to 25] |
| **sort** | **String**| Property name that will be used to sort results. &#39;-&#39; indicates descending | [optional] [default to -createdAt] [enum: createdAt, -createdAt, orderId, -orderId, pricing.total, -pricing.total] |
| **xShopperId** | **String**| Shopper ID to be operated on, if different from JWT&lt;br/&gt;&lt;b&gt;Reseller subaccounts are not supported&lt;/b&gt; | [optional] |
| **xMarketId** | **String**| Unique identifier of the Market in which the request is happening | [optional] [default to en-US] |

### Return type

[**OrderList**](OrderList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="get"></a>
# **get**
> Order get(orderId, xShopperId, xMarketId)

Retrieve details for specified order

&lt;strong&gt;API Resellers&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;This endpoint does not support subaccounts and therefore API Resellers should not supply an X-Shopper-Id header&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    String orderId = "orderId_example"; // String | Order id whose details are to be retrieved
    String xShopperId = "xShopperId_example"; // String | Shopper ID to be operated on, if different from JWT<br/><b>Reseller subaccounts are not supported</b>
    String xMarketId = "en-US"; // String | Unique identifier of the Market in which the request is happening
    try {
      Order result = apiInstance.get(orderId, xShopperId, xMarketId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#get");
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
| **orderId** | **String**| Order id whose details are to be retrieved | |
| **xShopperId** | **String**| Shopper ID to be operated on, if different from JWT&lt;br/&gt;&lt;b&gt;Reseller subaccounts are not supported&lt;/b&gt; | [optional] |
| **xMarketId** | **String**| Unique identifier of the Market in which the request is happening | [optional] [default to en-US] |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

