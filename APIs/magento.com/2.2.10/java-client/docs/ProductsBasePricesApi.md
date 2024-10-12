# ProductsBasePricesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogBasePriceStorageV1UpdatePost**](ProductsBasePricesApi.md#catalogBasePriceStorageV1UpdatePost) | **POST** /V1/products/base-prices | products/base-prices |


<a id="catalogBasePriceStorageV1UpdatePost"></a>
# **catalogBasePriceStorageV1UpdatePost**
> List&lt;CatalogDataPriceUpdateResultInterface&gt; catalogBasePriceStorageV1UpdatePost(catalogBasePriceStorageV1UpdatePostRequest)

products/base-prices

Add or update product prices. Input item should correspond \\Magento\\Catalog\\Api\\Data\\CostInterface. If any items will have invalid price, store id or sku, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsBasePricesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsBasePricesApi apiInstance = new ProductsBasePricesApi(defaultClient);
    CatalogBasePriceStorageV1UpdatePostRequest catalogBasePriceStorageV1UpdatePostRequest = new CatalogBasePriceStorageV1UpdatePostRequest(); // CatalogBasePriceStorageV1UpdatePostRequest | 
    try {
      List<CatalogDataPriceUpdateResultInterface> result = apiInstance.catalogBasePriceStorageV1UpdatePost(catalogBasePriceStorageV1UpdatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsBasePricesApi#catalogBasePriceStorageV1UpdatePost");
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
| **catalogBasePriceStorageV1UpdatePostRequest** | [**CatalogBasePriceStorageV1UpdatePostRequest**](CatalogBasePriceStorageV1UpdatePostRequest.md)|  | [optional] |

### Return type

[**List&lt;CatalogDataPriceUpdateResultInterface&gt;**](CatalogDataPriceUpdateResultInterface.md)

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

