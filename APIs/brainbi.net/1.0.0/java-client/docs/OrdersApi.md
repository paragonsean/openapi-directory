# OrdersApi

All URIs are relative to *http://,*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**orders**](OrdersApi.md#orders) | **GET** /api/orders | Orders |
| [**orders1**](OrdersApi.md#orders1) | **DELETE** /api/orders/1137 | Orders |


<a id="orders"></a>
# **orders**
> orders()

Orders

This resource lists all orders that are currently saved in your account.

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
    defaultClient.setBasePath("http://,");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String  = ""; // String | 
    try {
      apiInstance.orders();
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orders");
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
| **** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="orders1"></a>
# **orders1**
> orders1()

Orders

Orders

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
    defaultClient.setBasePath("http://,");

    OrdersApi apiInstance = new OrdersApi(defaultClient);
    String  = ""; // String | 
    try {
      apiInstance.orders1();
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersApi#orders1");
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
| **** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

