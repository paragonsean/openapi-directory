# ProductsProductSkuStockItemsItemIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogInventoryStockRegistryV1UpdateStockItemBySkuPut**](ProductsProductSkuStockItemsItemIdApi.md#catalogInventoryStockRegistryV1UpdateStockItemBySkuPut) | **PUT** /V1/products/{productSku}/stockItems/{itemId} | products/{productSku}/stockItems/{itemId} |


<a id="catalogInventoryStockRegistryV1UpdateStockItemBySkuPut"></a>
# **catalogInventoryStockRegistryV1UpdateStockItemBySkuPut**
> Integer catalogInventoryStockRegistryV1UpdateStockItemBySkuPut(productSku, itemId, catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest)

products/{productSku}/stockItems/{itemId}



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsProductSkuStockItemsItemIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsProductSkuStockItemsItemIdApi apiInstance = new ProductsProductSkuStockItemsItemIdApi(defaultClient);
    String productSku = "productSku_example"; // String | 
    String itemId = "itemId_example"; // String | 
    CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest = new CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest(); // CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest | 
    try {
      Integer result = apiInstance.catalogInventoryStockRegistryV1UpdateStockItemBySkuPut(productSku, itemId, catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsProductSkuStockItemsItemIdApi#catalogInventoryStockRegistryV1UpdateStockItemBySkuPut");
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
| **itemId** | **String**|  | |
| **catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest** | [**CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest**](CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest.md)|  | [optional] |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

