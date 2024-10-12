# ProductsSpecialPriceDeleteApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogSpecialPriceStorageV1DeletePost**](ProductsSpecialPriceDeleteApi.md#catalogSpecialPriceStorageV1DeletePost) | **POST** /V1/products/special-price-delete | products/special-price-delete |


<a id="catalogSpecialPriceStorageV1DeletePost"></a>
# **catalogSpecialPriceStorageV1DeletePost**
> List&lt;CatalogDataPriceUpdateResultInterface&gt; catalogSpecialPriceStorageV1DeletePost(catalogSpecialPriceStorageV1UpdatePostRequest)

products/special-price-delete

Delete product&#39;s special price. If any items will have invalid price, store id, sku or dates, they will be marked as failed and excluded from delete list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the delete exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSpecialPriceDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSpecialPriceDeleteApi apiInstance = new ProductsSpecialPriceDeleteApi(defaultClient);
    CatalogSpecialPriceStorageV1UpdatePostRequest catalogSpecialPriceStorageV1UpdatePostRequest = new CatalogSpecialPriceStorageV1UpdatePostRequest(); // CatalogSpecialPriceStorageV1UpdatePostRequest | 
    try {
      List<CatalogDataPriceUpdateResultInterface> result = apiInstance.catalogSpecialPriceStorageV1DeletePost(catalogSpecialPriceStorageV1UpdatePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSpecialPriceDeleteApi#catalogSpecialPriceStorageV1DeletePost");
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
| **catalogSpecialPriceStorageV1UpdatePostRequest** | [**CatalogSpecialPriceStorageV1UpdatePostRequest**](CatalogSpecialPriceStorageV1UpdatePostRequest.md)|  | [optional] |

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

