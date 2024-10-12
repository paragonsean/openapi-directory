# ProductsCostApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCostStorageV1UpdatePost**](ProductsCostApi.md#catalogCostStorageV1UpdatePost) | **POST** /V1/products/cost | products/cost |


<a id="catalogCostStorageV1UpdatePost"></a>
# **catalogCostStorageV1UpdatePost**
> List&lt;CatalogDataPriceUpdateResultInterface&gt; catalogCostStorageV1UpdatePost(catalogCostStorageV1UpdatePostRequest)

products/cost

Add or update product cost. Input item should correspond to \\Magento\\Catalog\\Api\\Data\\CostInterface. If any items will have invalid cost, store id or sku, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsCostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsCostApi apiInstance = new ProductsCostApi(defaultClient);
    CatalogCostStorageV1UpdatePostRequest catalogCostStorageV1UpdatePostRequest = new CatalogCostStorageV1UpdatePostRequest(); // CatalogCostStorageV1UpdatePostRequest | 
    try {
      List<CatalogDataPriceUpdateResultInterface> result = apiInstance.catalogCostStorageV1UpdatePost(catalogCostStorageV1UpdatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsCostApi#catalogCostStorageV1UpdatePost");
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
| **catalogCostStorageV1UpdatePostRequest** | [**CatalogCostStorageV1UpdatePostRequest**](CatalogCostStorageV1UpdatePostRequest.md)|  | [optional] |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

