# MagentoB2B.ProductsSkuMediaApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeMediaGalleryManagementV1CreatePost**](ProductsSkuMediaApi.md#catalogProductAttributeMediaGalleryManagementV1CreatePost) | **POST** /V1/products/{sku}/media | products/{sku}/media
[**catalogProductAttributeMediaGalleryManagementV1GetListGet**](ProductsSkuMediaApi.md#catalogProductAttributeMediaGalleryManagementV1GetListGet) | **GET** /V1/products/{sku}/media | products/{sku}/media



## catalogProductAttributeMediaGalleryManagementV1CreatePost

> Number catalogProductAttributeMediaGalleryManagementV1CreatePost(sku, opts)

products/{sku}/media

Create new gallery entry

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuMediaApi();
let sku = "sku_example"; // String | 
let opts = {
  'catalogProductAttributeMediaGalleryManagementV1CreatePostRequest': new MagentoB2B.CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest() // CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest | 
};
apiInstance.catalogProductAttributeMediaGalleryManagementV1CreatePost(sku, opts, (error, data, response) => {
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
 **catalogProductAttributeMediaGalleryManagementV1CreatePostRequest** | [**CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest**](CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## catalogProductAttributeMediaGalleryManagementV1GetListGet

> [CatalogDataProductAttributeMediaGalleryEntryInterface] catalogProductAttributeMediaGalleryManagementV1GetListGet(sku)

products/{sku}/media

Retrieve the list of gallery entries associated with given product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuMediaApi();
let sku = "sku_example"; // String | 
apiInstance.catalogProductAttributeMediaGalleryManagementV1GetListGet(sku, (error, data, response) => {
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

### Return type

[**[CatalogDataProductAttributeMediaGalleryEntryInterface]**](CatalogDataProductAttributeMediaGalleryEntryInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

