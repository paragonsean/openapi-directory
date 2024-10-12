# StockItemsProductSkuApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogInventoryStockRegistryV1GetStockItemBySkuGet**](StockItemsProductSkuApi.md#catalogInventoryStockRegistryV1GetStockItemBySkuGet) | **GET** /V1/stockItems/{productSku} | stockItems/{productSku} |


<a id="catalogInventoryStockRegistryV1GetStockItemBySkuGet"></a>
# **catalogInventoryStockRegistryV1GetStockItemBySkuGet**
> CatalogInventoryDataStockItemInterface catalogInventoryStockRegistryV1GetStockItemBySkuGet(productSku, scopeId)

stockItems/{productSku}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StockItemsProductSkuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    StockItemsProductSkuApi apiInstance = new StockItemsProductSkuApi(defaultClient);
    String productSku = "productSku_example"; // String | 
    Integer scopeId = 56; // Integer | 
    try {
      CatalogInventoryDataStockItemInterface result = apiInstance.catalogInventoryStockRegistryV1GetStockItemBySkuGet(productSku, scopeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StockItemsProductSkuApi#catalogInventoryStockRegistryV1GetStockItemBySkuGet");
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

[**CatalogInventoryDataStockItemInterface**](CatalogInventoryDataStockItemInterface.md)

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

