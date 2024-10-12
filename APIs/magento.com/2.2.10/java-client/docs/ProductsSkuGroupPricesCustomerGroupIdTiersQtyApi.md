# ProductsSkuGroupPricesCustomerGroupIdTiersQtyApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductTierPriceManagementV1RemoveDelete**](ProductsSkuGroupPricesCustomerGroupIdTiersQtyApi.md#catalogProductTierPriceManagementV1RemoveDelete) | **DELETE** /V1/products/{sku}/group-prices/{customerGroupId}/tiers/{qty} | products/{sku}/group-prices/{customerGroupId}/tiers/{qty} |


<a id="catalogProductTierPriceManagementV1RemoveDelete"></a>
# **catalogProductTierPriceManagementV1RemoveDelete**
> Boolean catalogProductTierPriceManagementV1RemoveDelete(sku, customerGroupId, qty)

products/{sku}/group-prices/{customerGroupId}/tiers/{qty}

Remove tier price from product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuGroupPricesCustomerGroupIdTiersQtyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuGroupPricesCustomerGroupIdTiersQtyApi apiInstance = new ProductsSkuGroupPricesCustomerGroupIdTiersQtyApi(defaultClient);
    String sku = "sku_example"; // String | 
    String customerGroupId = "customerGroupId_example"; // String | 'all' can be used to specify 'ALL GROUPS'
    BigDecimal qty = new BigDecimal(78); // BigDecimal | 
    try {
      Boolean result = apiInstance.catalogProductTierPriceManagementV1RemoveDelete(sku, customerGroupId, qty);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuGroupPricesCustomerGroupIdTiersQtyApi#catalogProductTierPriceManagementV1RemoveDelete");
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

