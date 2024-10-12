# OrderApi

All URIs are relative to *https://www.envoice.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**orderApiAll**](OrderApi.md#orderApiAll) | **GET** /api/order/all | Return all orders for the account |
| [**orderApiChangeShippingDetails**](OrderApi.md#orderApiChangeShippingDetails) | **POST** /api/order/changeshippingdetails | Change order shipping details |
| [**orderApiChangeStatus**](OrderApi.md#orderApiChangeStatus) | **POST** /api/order/changestatus | Change order status |
| [**orderApiDelete**](OrderApi.md#orderApiDelete) | **POST** /api/order/delete | Delete an existing order |
| [**orderApiDetails**](OrderApi.md#orderApiDetails) | **GET** /api/order/details | Return order details |
| [**orderApiNew**](OrderApi.md#orderApiNew) | **POST** /api/order/new | Create an order |


<a id="orderApiAll"></a>
# **orderApiAll**
> ListResultOrderDetailsApiModel orderApiAll(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize)

Return all orders for the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    Integer queryOptionsPage = 56; // Integer | 
    Integer queryOptionsPageSize = 56; // Integer | 
    try {
      ListResultOrderDetailsApiModel result = apiInstance.orderApiAll(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderApiAll");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **queryOptionsPage** | **Integer**|  | [optional] |
| **queryOptionsPageSize** | **Integer**|  | [optional] |

### Return type

[**ListResultOrderDetailsApiModel**](ListResultOrderDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiChangeShippingDetails"></a>
# **orderApiChangeShippingDetails**
> orderApiChangeShippingDetails(orderId, xAuthKey, xAuthSecret, orderShippingDetailsApiModel)

Change order shipping details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    OrderApi apiInstance = new OrderApi(defaultClient);
    Integer orderId = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    OrderShippingDetailsApiModel orderShippingDetailsApiModel = new OrderShippingDetailsApiModel(); // OrderShippingDetailsApiModel | 
    try {
      apiInstance.orderApiChangeShippingDetails(orderId, xAuthKey, xAuthSecret, orderShippingDetailsApiModel);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderApiChangeShippingDetails");
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
| **orderId** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **orderShippingDetailsApiModel** | [**OrderShippingDetailsApiModel**](OrderShippingDetailsApiModel.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="orderApiChangeStatus"></a>
# **orderApiChangeStatus**
> orderApiChangeStatus(xAuthKey, xAuthSecret, changeOrderStatusApiModel)

Change order status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    ChangeOrderStatusApiModel changeOrderStatusApiModel = new ChangeOrderStatusApiModel(); // ChangeOrderStatusApiModel | 
    try {
      apiInstance.orderApiChangeStatus(xAuthKey, xAuthSecret, changeOrderStatusApiModel);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderApiChangeStatus");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **changeOrderStatusApiModel** | [**ChangeOrderStatusApiModel**](ChangeOrderStatusApiModel.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="orderApiDelete"></a>
# **orderApiDelete**
> Integer orderApiDelete(xAuthKey, xAuthSecret, orderDeleteApiModel)

Delete an existing order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    OrderDeleteApiModel orderDeleteApiModel = new OrderDeleteApiModel(); // OrderDeleteApiModel | 
    try {
      Integer result = apiInstance.orderApiDelete(xAuthKey, xAuthSecret, orderDeleteApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderApiDelete");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **orderDeleteApiModel** | [**OrderDeleteApiModel**](OrderDeleteApiModel.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiDetails"></a>
# **orderApiDetails**
> OrderFullDetailsApiModel orderApiDetails(id, xAuthKey, xAuthSecret)

Return order details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    OrderApi apiInstance = new OrderApi(defaultClient);
    Integer id = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      OrderFullDetailsApiModel result = apiInstance.orderApiDetails(id, xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderApiDetails");
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
| **id** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**OrderFullDetailsApiModel**](OrderFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="orderApiNew"></a>
# **orderApiNew**
> Integer orderApiNew(xAuthKey, xAuthSecret, orderCreateApiModel)

Create an order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    OrderCreateApiModel orderCreateApiModel = new OrderCreateApiModel(); // OrderCreateApiModel | 
    try {
      Integer result = apiInstance.orderApiNew(xAuthKey, xAuthSecret, orderCreateApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#orderApiNew");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **orderCreateApiModel** | [**OrderCreateApiModel**](OrderCreateApiModel.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

