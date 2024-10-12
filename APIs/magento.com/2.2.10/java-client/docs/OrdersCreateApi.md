# OrdersCreateApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrderRepositoryV1SavePut**](OrdersCreateApi.md#salesOrderRepositoryV1SavePut) | **PUT** /V1/orders/create | orders/create |


<a id="salesOrderRepositoryV1SavePut"></a>
# **salesOrderRepositoryV1SavePut**
> SalesDataOrderInterface salesOrderRepositoryV1SavePut(salesOrderRepositoryV1SavePostRequest)

orders/create

Performs persist operations for a specified order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersCreateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersCreateApi apiInstance = new OrdersCreateApi(defaultClient);
    SalesOrderRepositoryV1SavePostRequest salesOrderRepositoryV1SavePostRequest = new SalesOrderRepositoryV1SavePostRequest(); // SalesOrderRepositoryV1SavePostRequest | 
    try {
      SalesDataOrderInterface result = apiInstance.salesOrderRepositoryV1SavePut(salesOrderRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersCreateApi#salesOrderRepositoryV1SavePut");
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
| **salesOrderRepositoryV1SavePostRequest** | [**SalesOrderRepositoryV1SavePostRequest**](SalesOrderRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**SalesDataOrderInterface**](SalesDataOrderInterface.md)

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

