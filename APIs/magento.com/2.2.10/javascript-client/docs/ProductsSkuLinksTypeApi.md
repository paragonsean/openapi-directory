# MagentoB2B.ProductsSkuLinksTypeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductLinkManagementV1GetLinkedItemsByTypeGet**](ProductsSkuLinksTypeApi.md#catalogProductLinkManagementV1GetLinkedItemsByTypeGet) | **GET** /V1/products/{sku}/links/{type} | products/{sku}/links/{type}



## catalogProductLinkManagementV1GetLinkedItemsByTypeGet

> [CatalogDataProductLinkInterface] catalogProductLinkManagementV1GetLinkedItemsByTypeGet(sku, type)

products/{sku}/links/{type}

Provide the list of links for a specific product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuLinksTypeApi();
let sku = "sku_example"; // String | 
let type = "type_example"; // String | 
apiInstance.catalogProductLinkManagementV1GetLinkedItemsByTypeGet(sku, type, (error, data, response) => {
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
 **type** | **String**|  | 

### Return type

[**[CatalogDataProductLinkInterface]**](CatalogDataProductLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

