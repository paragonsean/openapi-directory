# MagentoB2B.ProductsSkuGroupPricesCustomerGroupIdTiersApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductTierPriceManagementV1GetListGet**](ProductsSkuGroupPricesCustomerGroupIdTiersApi.md#catalogProductTierPriceManagementV1GetListGet) | **GET** /V1/products/{sku}/group-prices/{customerGroupId}/tiers | products/{sku}/group-prices/{customerGroupId}/tiers



## catalogProductTierPriceManagementV1GetListGet

> [CatalogDataProductTierPriceInterface] catalogProductTierPriceManagementV1GetListGet(sku, customerGroupId)

products/{sku}/group-prices/{customerGroupId}/tiers

Get tier price of product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuGroupPricesCustomerGroupIdTiersApi();
let sku = "sku_example"; // String | 
let customerGroupId = "customerGroupId_example"; // String | 'all' can be used to specify 'ALL GROUPS'
apiInstance.catalogProductTierPriceManagementV1GetListGet(sku, customerGroupId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **String**|  | 
 **customerGroupId** | **String**| &#39;all&#39; can be used to specify &#39;ALL GROUPS&#39; | 

### Return type

[**[CatalogDataProductTierPriceInterface]**](CatalogDataProductTierPriceInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

