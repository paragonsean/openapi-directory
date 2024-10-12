# MagentoB2B.ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductTierPriceManagementV1AddPost**](ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi.md#catalogProductTierPriceManagementV1AddPost) | **POST** /V1/products/{sku}/group-prices/{customerGroupId}/tiers/{qty}/price/{price} | products/{sku}/group-prices/{customerGroupId}/tiers/{qty}/price/{price}



## catalogProductTierPriceManagementV1AddPost

> Boolean catalogProductTierPriceManagementV1AddPost(sku, customerGroupId, price, qty)

products/{sku}/group-prices/{customerGroupId}/tiers/{qty}/price/{price}

Create tier price for product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuGroupPricesCustomerGroupIdTiersQtyPricePriceApi();
let sku = "sku_example"; // String | 
let customerGroupId = "customerGroupId_example"; // String | 'all' can be used to specify 'ALL GROUPS'
let price = 3.4; // Number | 
let qty = 3.4; // Number | 
apiInstance.catalogProductTierPriceManagementV1AddPost(sku, customerGroupId, price, qty, (error, data, response) => {
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
 **price** | **Number**|  | 
 **qty** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

