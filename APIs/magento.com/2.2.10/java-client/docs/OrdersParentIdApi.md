# OrdersParentIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesOrderAddressRepositoryV1SavePut**](OrdersParentIdApi.md#salesOrderAddressRepositoryV1SavePut) | **PUT** /V1/orders/{parent_id} | orders/{parent_id} |


<a id="salesOrderAddressRepositoryV1SavePut"></a>
# **salesOrderAddressRepositoryV1SavePut**
> SalesDataOrderAddressInterface salesOrderAddressRepositoryV1SavePut(parentId, salesOrderAddressRepositoryV1SavePutRequest)

orders/{parent_id}

Performs persist operations for a specified order address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrdersParentIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    OrdersParentIdApi apiInstance = new OrdersParentIdApi(defaultClient);
    String parentId = "parentId_example"; // String | 
    SalesOrderAddressRepositoryV1SavePutRequest salesOrderAddressRepositoryV1SavePutRequest = new SalesOrderAddressRepositoryV1SavePutRequest(); // SalesOrderAddressRepositoryV1SavePutRequest | 
    try {
      SalesDataOrderAddressInterface result = apiInstance.salesOrderAddressRepositoryV1SavePut(parentId, salesOrderAddressRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrdersParentIdApi#salesOrderAddressRepositoryV1SavePut");
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
| **parentId** | **String**|  | |
| **salesOrderAddressRepositoryV1SavePutRequest** | [**SalesOrderAddressRepositoryV1SavePutRequest**](SalesOrderAddressRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**SalesDataOrderAddressInterface**](SalesDataOrderAddressInterface.md)

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

