# MagentoB2B.ProductsLinksTypeAttributesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductLinkTypeListV1GetItemAttributesGet**](ProductsLinksTypeAttributesApi.md#catalogProductLinkTypeListV1GetItemAttributesGet) | **GET** /V1/products/links/{type}/attributes | products/links/{type}/attributes



## catalogProductLinkTypeListV1GetItemAttributesGet

> [CatalogDataProductLinkAttributeInterface] catalogProductLinkTypeListV1GetItemAttributesGet(type)

products/links/{type}/attributes

Provide a list of the product link type attributes

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsLinksTypeAttributesApi();
let type = "type_example"; // String | 
apiInstance.catalogProductLinkTypeListV1GetItemAttributesGet(type, (error, data, response) => {
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
 **type** | **String**|  | 

### Return type

[**[CatalogDataProductLinkAttributeInterface]**](CatalogDataProductLinkAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

