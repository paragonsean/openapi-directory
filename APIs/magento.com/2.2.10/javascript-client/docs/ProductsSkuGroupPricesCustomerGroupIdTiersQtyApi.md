# MagentoB2B.ProductsSkuGroupPricesCustomerGroupIdTiersQtyApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductTierPriceManagementV1RemoveDelete**](ProductsSkuGroupPricesCustomerGroupIdTiersQtyApi.md#catalogProductTierPriceManagementV1RemoveDelete) | **DELETE** /V1/products/{sku}/group-prices/{customerGroupId}/tiers/{qty} | products/{sku}/group-prices/{customerGroupId}/tiers/{qty}



## catalogProductTierPriceManagementV1RemoveDelete

> Boolean catalogProductTierPriceManagementV1RemoveDelete(sku, customerGroupId, qty)

products/{sku}/group-prices/{customerGroupId}/tiers/{qty}

Remove tier price from product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuGroupPricesCustomerGroupIdTiersQtyApi();
let sku = "sku_example"; // String | 
let customerGroupId = "customerGroupId_example"; // String | 'all' can be used to specify 'ALL GROUPS'
let qty = 3.4; // Number | 
apiInstance.catalogProductTierPriceManagementV1RemoveDelete(sku, customerGroupId, qty, (error, data, response) => {
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
 **qty** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

