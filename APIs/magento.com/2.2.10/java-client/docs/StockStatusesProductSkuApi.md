# StockStatusesProductSkuApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogInventoryStockRegistryV1GetStockStatusBySkuGet**](StockStatusesProductSkuApi.md#catalogInventoryStockRegistryV1GetStockStatusBySkuGet) | **GET** /V1/stockStatuses/{productSku} | stockStatuses/{productSku} |


<a id="catalogInventoryStockRegistryV1GetStockStatusBySkuGet"></a>
# **catalogInventoryStockRegistryV1GetStockStatusBySkuGet**
> CatalogInventoryDataStockStatusInterface catalogInventoryStockRegistryV1GetStockStatusBySkuGet(productSku, scopeId)

stockStatuses/{productSku}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StockStatusesProductSkuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    StockStatusesProductSkuApi apiInstance = new StockStatusesProductSkuApi(defaultClient);
    String productSku = "productSku_example"; // String | 
    Integer scopeId = 56; // Integer | 
    try {
      CatalogInventoryDataStockStatusInterface result = apiInstance.catalogInventoryStockRegistryV1GetStockStatusBySkuGet(productSku, scopeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StockStatusesProductSkuApi#catalogInventoryStockRegistryV1GetStockStatusBySkuGet");
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
| **productSku** | **String**|  | |
| **scopeId** | **Integer**|  | [optional] |

### Return type

[**CatalogInventoryDataStockStatusInterface**](CatalogInventoryDataStockStatusInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

