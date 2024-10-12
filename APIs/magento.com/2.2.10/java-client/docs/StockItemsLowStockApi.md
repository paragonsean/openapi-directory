# StockItemsLowStockApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogInventoryStockRegistryV1GetLowStockItemsGet**](StockItemsLowStockApi.md#catalogInventoryStockRegistryV1GetLowStockItemsGet) | **GET** /V1/stockItems/lowStock/ | stockItems/lowStock/ |


<a id="catalogInventoryStockRegistryV1GetLowStockItemsGet"></a>
# **catalogInventoryStockRegistryV1GetLowStockItemsGet**
> CatalogInventoryDataStockItemCollectionInterface catalogInventoryStockRegistryV1GetLowStockItemsGet(scopeId, qty, currentPage, pageSize)

stockItems/lowStock/

Retrieves a list of SKU&#39;s with low inventory qty

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StockItemsLowStockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    StockItemsLowStockApi apiInstance = new StockItemsLowStockApi(defaultClient);
    Integer scopeId = 56; // Integer | 
    BigDecimal qty = new BigDecimal(78); // BigDecimal | 
    Integer currentPage = 56; // Integer | 
    Integer pageSize = 56; // Integer | 
    try {
      CatalogInventoryDataStockItemCollectionInterface result = apiInstance.catalogInventoryStockRegistryV1GetLowStockItemsGet(scopeId, qty, currentPage, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StockItemsLowStockApi#catalogInventoryStockRegistryV1GetLowStockItemsGet");
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
| **scopeId** | **Integer**|  | |
| **qty** | **BigDecimal**|  | |
| **currentPage** | **Integer**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |

### Return type

[**CatalogInventoryDataStockItemCollectionInterface**](CatalogInventoryDataStockItemCollectionInterface.md)

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

