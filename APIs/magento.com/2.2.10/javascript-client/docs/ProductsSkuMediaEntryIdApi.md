# MagentoB2B.ProductsSkuMediaEntryIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeMediaGalleryManagementV1GetGet**](ProductsSkuMediaEntryIdApi.md#catalogProductAttributeMediaGalleryManagementV1GetGet) | **GET** /V1/products/{sku}/media/{entryId} | products/{sku}/media/{entryId}
[**catalogProductAttributeMediaGalleryManagementV1RemoveDelete**](ProductsSkuMediaEntryIdApi.md#catalogProductAttributeMediaGalleryManagementV1RemoveDelete) | **DELETE** /V1/products/{sku}/media/{entryId} | products/{sku}/media/{entryId}
[**catalogProductAttributeMediaGalleryManagementV1UpdatePut**](ProductsSkuMediaEntryIdApi.md#catalogProductAttributeMediaGalleryManagementV1UpdatePut) | **PUT** /V1/products/{sku}/media/{entryId} | products/{sku}/media/{entryId}



## catalogProductAttributeMediaGalleryManagementV1GetGet

> CatalogDataProductAttributeMediaGalleryEntryInterface catalogProductAttributeMediaGalleryManagementV1GetGet(sku, entryId)

products/{sku}/media/{entryId}

Return information about gallery entry

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuMediaEntryIdApi();
let sku = "sku_example"; // String | 
let entryId = 56; // Number | 
apiInstance.catalogProductAttributeMediaGalleryManagementV1GetGet(sku, entryId, (error, data, response) => {
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
 **entryId** | **Number**|  | 

### Return type

[**CatalogDataProductAttributeMediaGalleryEntryInterface**](CatalogDataProductAttributeMediaGalleryEntryInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogProductAttributeMediaGalleryManagementV1RemoveDelete

> Boolean catalogProductAttributeMediaGalleryManagementV1RemoveDelete(sku, entryId)

products/{sku}/media/{entryId}

Remove gallery entry

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuMediaEntryIdApi();
let sku = "sku_example"; // String | 
let entryId = 56; // Number | 
apiInstance.catalogProductAttributeMediaGalleryManagementV1RemoveDelete(sku, entryId, (error, data, response) => {
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
 **entryId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogProductAttributeMediaGalleryManagementV1UpdatePut

> Boolean catalogProductAttributeMediaGalleryManagementV1UpdatePut(sku, entryId, opts)

products/{sku}/media/{entryId}

Update gallery entry

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuMediaEntryIdApi();
let sku = "sku_example"; // String | 
let entryId = "entryId_example"; // String | 
let opts = {
  'catalogProductAttributeMediaGalleryManagementV1CreatePostRequest': new MagentoB2B.CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest() // CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest | 
};
apiInstance.catalogProductAttributeMediaGalleryManagementV1UpdatePut(sku, entryId, opts, (error, data, response) => {
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
 **entryId** | **String**|  | 
 **catalogProductAttributeMediaGalleryManagementV1CreatePostRequest** | [**CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest**](CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

