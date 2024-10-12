# ProductsSkuGroupPricesCustomerGroupIdTiersApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductTierPriceManagementV1GetListGet**](ProductsSkuGroupPricesCustomerGroupIdTiersApi.md#catalogProductTierPriceManagementV1GetListGet) | **GET** /V1/products/{sku}/group-prices/{customerGroupId}/tiers | products/{sku}/group-prices/{customerGroupId}/tiers |


<a id="catalogProductTierPriceManagementV1GetListGet"></a>
# **catalogProductTierPriceManagementV1GetListGet**
> List&lt;CatalogDataProductTierPriceInterface&gt; catalogProductTierPriceManagementV1GetListGet(sku, customerGroupId)

products/{sku}/group-prices/{customerGroupId}/tiers

Get tier price of product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuGroupPricesCustomerGroupIdTiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuGroupPricesCustomerGroupIdTiersApi apiInstance = new ProductsSkuGroupPricesCustomerGroupIdTiersApi(defaultClient);
    String sku = "sku_example"; // String | 
    String customerGroupId = "customerGroupId_example"; // String | 'all' can be used to specify 'ALL GROUPS'
    try {
      List<CatalogDataProductTierPriceInterface> result = apiInstance.catalogProductTierPriceManagementV1GetListGet(sku, customerGroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuGroupPricesCustomerGroupIdTiersApi#catalogProductTierPriceManagementV1GetListGet");
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

### Return type

[**List&lt;CatalogDataProductTierPriceInterface&gt;**](CatalogDataProductTierPriceInterface.md)

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

