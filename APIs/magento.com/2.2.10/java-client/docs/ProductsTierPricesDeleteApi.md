# ProductsTierPricesDeleteApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogTierPriceStorageV1DeletePost**](ProductsTierPricesDeleteApi.md#catalogTierPriceStorageV1DeletePost) | **POST** /V1/products/tier-prices-delete | products/tier-prices-delete |


<a id="catalogTierPriceStorageV1DeletePost"></a>
# **catalogTierPriceStorageV1DeletePost**
> List&lt;CatalogDataPriceUpdateResultInterface&gt; catalogTierPriceStorageV1DeletePost(catalogTierPriceStorageV1ReplacePutRequest)

products/tier-prices-delete

Delete product tier prices. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from delete list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsTierPricesDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsTierPricesDeleteApi apiInstance = new ProductsTierPricesDeleteApi(defaultClient);
    CatalogTierPriceStorageV1ReplacePutRequest catalogTierPriceStorageV1ReplacePutRequest = new CatalogTierPriceStorageV1ReplacePutRequest(); // CatalogTierPriceStorageV1ReplacePutRequest | 
    try {
      List<CatalogDataPriceUpdateResultInterface> result = apiInstance.catalogTierPriceStorageV1DeletePost(catalogTierPriceStorageV1ReplacePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsTierPricesDeleteApi#catalogTierPriceStorageV1DeletePost");
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
| **catalogTierPriceStorageV1ReplacePutRequest** | [**CatalogTierPriceStorageV1ReplacePutRequest**](CatalogTierPriceStorageV1ReplacePutRequest.md)|  | [optional] |

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

