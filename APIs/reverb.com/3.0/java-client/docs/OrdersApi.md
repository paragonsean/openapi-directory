# OrdersApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ordersOrderIdFeedbackBuyerGet**](OrdersApi.md#ordersOrderIdFeedbackBuyerGet) | **GET** /orders/{order_id}/feedback/buyer | Feedback details for an order&#39;s buyer |
| [**ordersOrderIdFeedbackBuyerPost**](OrdersApi.md#ordersOrderIdFeedbackBuyerPost) | **POST** /orders/{order_id}/feedback/buyer | Add feedback about an order&#39;s buyer |
| [**ordersOrderIdFeedbackSellerGet**](OrdersApi.md#ordersOrderIdFeedbackSellerGet) | **GET** /orders/{order_id}/feedback/seller | Feedback details for an order&#39;s seller |
| [**ordersOrderIdFeedbackSellerPost**](OrdersApi.md#ordersOrderIdFeedbackSellerPost) | **POST** /orders/{order_id}/feedback/seller | Add feedback about an order&#39;s seller |


<a id="ordersOrderIdFeedbackBuyerGet"></a>
# **ordersOrderIdFeedbackBuyerGet**
> ordersOrderIdFeedbackBuyerGet(orderId)

Feedback details for an order&#39;s buyer

Feedback details for an order&#39;s buyer

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
    defaultClient.setBasePath("https://api.reverb.com/api");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String orderId = "orderId_example"; // String | 
    try {
      apiInstance.ordersOrderIdFeedbackBuyerGet(orderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersOrderIdFeedbackBuyerGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="ordersOrderIdFeedbackBuyerPost"></a>
# **ordersOrderIdFeedbackBuyerPost**
> ordersOrderIdFeedbackBuyerPost(orderId)

Add feedback about an order&#39;s buyer

Add feedback about an order&#39;s buyer

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
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String orderId = "orderId_example"; // String | 
    try {
      apiInstance.ordersOrderIdFeedbackBuyerPost(orderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersOrderIdFeedbackBuyerPost");
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

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="ordersOrderIdFeedbackSellerGet"></a>
# **ordersOrderIdFeedbackSellerGet**
> ordersOrderIdFeedbackSellerGet(orderId)

Feedback details for an order&#39;s seller

Feedback details for an order&#39;s seller

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
    defaultClient.setBasePath("https://api.reverb.com/api");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String orderId = "orderId_example"; // String | 
    try {
      apiInstance.ordersOrderIdFeedbackSellerGet(orderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersOrderIdFeedbackSellerGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="ordersOrderIdFeedbackSellerPost"></a>
# **ordersOrderIdFeedbackSellerPost**
> ordersOrderIdFeedbackSellerPost(orderId)

Add feedback about an order&#39;s seller

Add feedback about an order&#39;s seller

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
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String orderId = "orderId_example"; // String | 
    try {
      apiInstance.ordersOrderIdFeedbackSellerPost(orderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#ordersOrderIdFeedbackSellerPost");
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

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

