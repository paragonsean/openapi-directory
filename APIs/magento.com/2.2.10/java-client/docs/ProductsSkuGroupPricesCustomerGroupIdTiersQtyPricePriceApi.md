# ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductTierPriceManagementV1AddPost**](ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi.md#catalogProductTierPriceManagementV1AddPost) | **POST** /V1/products/{sku}/group-prices/{customerGroupId}/tiers/{qty}/price/{price} | products/{sku}/group-prices/{customerGroupId}/tiers/{qty}/price/{price} |


<a id="catalogProductTierPriceManagementV1AddPost"></a>
# **catalogProductTierPriceManagementV1AddPost**
> Boolean catalogProductTierPriceManagementV1AddPost(sku, customerGroupId, price, qty)

products/{sku}/group-prices/{customerGroupId}/tiers/{qty}/price/{price}

Create tier price for product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi apiInstance = new ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi(defaultClient);
    String sku = "sku_example"; // String | 
    String customerGroupId = "customerGroupId_example"; // String | 'all' can be used to specify 'ALL GROUPS'
    BigDecimal price = new BigDecimal(78); // BigDecimal | 
    BigDecimal qty = new BigDecimal(78); // BigDecimal | 
    try {
      Boolean result = apiInstance.catalogProductTierPriceManagementV1AddPost(sku, customerGroupId, price, qty);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi#catalogProductTierPriceManagementV1AddPost");
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
| **sku** | **String**|  | |
| **customerGroupId** | **String**| &#39;all&#39; can be used to specify &#39;ALL GROUPS&#39; | |
| **price** | **BigDecimal**|  | |
| **qty** | **BigDecimal**|  | |

### Return type

**Boolean**

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

