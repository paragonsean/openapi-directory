# OrdersIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrderManagementV1AddCommentPost**](OrdersIdCommentsApi.md#salesOrderManagementV1AddCommentPost) | **POST** /V1/orders/{id}/comments | orders/{id}/comments |
| [**salesOrderManagementV1GetCommentsListGet**](OrdersIdCommentsApi.md#salesOrderManagementV1GetCommentsListGet) | **GET** /V1/orders/{id}/comments | orders/{id}/comments |


<a id="salesOrderManagementV1AddCommentPost"></a>
# **salesOrderManagementV1AddCommentPost**
> Boolean salesOrderManagementV1AddCommentPost(id, salesOrderManagementV1AddCommentPostRequest)

orders/{id}/comments

Adds a comment to a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersIdCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersIdCommentsApi apiInstance = new OrdersIdCommentsApi(defaultClient);
    Integer id = 56; // Integer | The order ID.
    SalesOrderManagementV1AddCommentPostRequest salesOrderManagementV1AddCommentPostRequest = new SalesOrderManagementV1AddCommentPostRequest(); // SalesOrderManagementV1AddCommentPostRequest | 
    try {
      Boolean result = apiInstance.salesOrderManagementV1AddCommentPost(id, salesOrderManagementV1AddCommentPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersIdCommentsApi#salesOrderManagementV1AddCommentPost");
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
| **id** | **Integer**| The order ID. | |
| **salesOrderManagementV1AddCommentPostRequest** | [**SalesOrderManagementV1AddCommentPostRequest**](SalesOrderManagementV1AddCommentPostRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="salesOrderManagementV1GetCommentsListGet"></a>
# **salesOrderManagementV1GetCommentsListGet**
> SalesDataOrderStatusHistorySearchResultInterface salesOrderManagementV1GetCommentsListGet(id)

orders/{id}/comments

Lists comments for a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersIdCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersIdCommentsApi apiInstance = new OrdersIdCommentsApi(defaultClient);
    Integer id = 56; // Integer | The order ID.
    try {
      SalesDataOrderStatusHistorySearchResultInterface result = apiInstance.salesOrderManagementV1GetCommentsListGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersIdCommentsApi#salesOrderManagementV1GetCommentsListGet");
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
| **id** | **Integer**| The order ID. | |

### Return type

[**SalesDataOrderStatusHistorySearchResultInterface**](SalesDataOrderStatusHistorySearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

